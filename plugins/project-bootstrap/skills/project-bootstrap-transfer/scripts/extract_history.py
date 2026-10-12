#!/usr/bin/env python3
"""Bounded public/local extraction. Never executes page JavaScript or history commands."""
from __future__ import annotations
import argparse
import datetime
import hashlib
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

MAX_BYTES = 64 * 1024 * 1024
MAX_MESSAGES = 100000
VERSION = "1"

def validate_shared_url(url):
    p = urllib.parse.urlsplit(url)
    if (p.scheme != "https" or p.hostname != "chatgpt.com" or p.username or p.password
            or p.port not in (None, 443) or p.query or p.fragment
            or not re.fullmatch(r"/share/[0-9a-fA-F-]{36}", p.path)):
        raise ValueError("Use a user-provided public https://chatgpt.com/share/<id> URL without credentials")
    return url

class PublicRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        validate_shared_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)

def load_source(source):
    if source.startswith("https://"):
        validate_shared_url(source)
        opener = urllib.request.build_opener(PublicRedirect())
        with opener.open(urllib.request.Request(source, headers={"User-Agent": "Mozilla/5.0"}), timeout=25) as response:
            raw = response.read(MAX_BYTES + 1)
    else:
        path = Path(source)
        if path.stat().st_size > MAX_BYTES:
            raise ValueError("Source exceeds 64 MiB; supply a smaller explicit conversation export")
        raw = path.read_bytes()
    if len(raw) > MAX_BYTES:
        raise ValueError("Source exceeds 64 MiB; no partial archive was written")
    text = raw.decode("utf-8-sig")
    data = parse_html(text) if text.lstrip().startswith("<") else json.loads(text)
    return data, hashlib.sha256(raw).hexdigest()

def parse_html(text):
    # This is published page data, not a private API. Format changes fail closed.
    chunks = re.findall(r'streamController\.enqueue\(("(?:[^"\\]|\\.)*")\)', text)
    for chunk in chunks:
        try:
            table = json.loads(json.loads(chunk))
        except (ValueError, TypeError):
            continue
        if not isinstance(table, list):
            continue
        memo, active = {}, set()
        def decode(index, depth=0):
            if depth > 300 or not isinstance(index, int):
                raise ValueError("Unsupported/deep published page data")
            if index < 0:
                if index in (-1, -5): return None
                raise ValueError("Unsupported numeric sentinel in conversation data")
            if index >= len(table) or index in active:
                raise ValueError("Invalid or cyclic published data reference")
            if index in memo: return memo[index]
            value = table[index]; active.add(index)
            if isinstance(value, dict):
                result = {}
                for k, v in value.items():
                    if not re.fullmatch(r"_\d+", k): raise ValueError("Unknown published object encoding")
                    result[decode(int(k[1:]), depth+1)] = decode(v, depth+1)
            elif isinstance(value, list):
                if value and isinstance(value[0], str): raise ValueError("Unknown published typed encoding")
                result = [decode(v, depth+1) for v in value]
            else: result = value
            active.remove(index); memo[index] = result; return result
        for value in table:
            if not isinstance(value, dict): continue
            for key, ref in value.items():
                if re.fullmatch(r"_\d+", key) and int(key[1:]) < len(table) and table[int(key[1:])] == "serverResponse":
                    response = decode(ref)
                    data = response.get("data") if isinstance(response, dict) else None
                    if isinstance(data, dict) and ("linear_conversation" in data or "mapping" in data): return data
    raise ValueError("No supported public conversation data; use a user-provided JSON export")

def ordered_nodes(data):
    losses = []
    if isinstance(data.get("linear_conversation"), list):
        nodes = data["linear_conversation"]
        if any(not isinstance(n, dict) for n in nodes): raise ValueError("Invalid conversation node")
        if nodes and nodes[0].get("parent"): losses.append("Published chain starts with a missing ancestor")
        mapping = data.get("mapping")
        if isinstance(mapping, dict):
            if any(n.get("id") not in mapping for n in nodes): losses.append("Published linear nodes missing from mapping")
        for i, node in enumerate(nodes):
            if i and node.get("parent") != nodes[i-1].get("id"):
                losses.append("Published linear parent chain has a gap")
        if nodes and data.get("current_node") and nodes[-1].get("id") != data["current_node"]:
            losses.append("Published chain does not reach current_node")
        return nodes, losses
    mapping = data.get("mapping")
    if not isinstance(mapping, dict) or not data.get("current_node"):
        raise ValueError("No explicit message order; do not infer order from JSON object keys")
    nodes, seen, current = [], set(), data["current_node"]
    message_count = 0
    while current:
        if current in seen: raise ValueError("Cyclic conversation parent chain")
        seen.add(current)
        if current not in mapping:
            losses.append("Missing parent node in selected conversation chain"); break
        node = mapping[current]; nodes.append(node); current = node.get("parent")
        if node.get("message") is not None: message_count += 1
        if message_count > MAX_MESSAGES: raise ValueError("Too many messages in selected chain")
    return list(reversed(nodes)), losses

def visible_text(content):
    if not isinstance(content, dict): return None
    parts = content.get("parts")
    if isinstance(parts, list):
        strings = [p for p in parts if isinstance(p, str)]
        return "\n".join(strings) if strings else None
    return content.get("text") if isinstance(content.get("text"), str) else None

def attachment_records(message):
    found = []
    def visit(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if key == "attachments" and isinstance(item, list):
                    for a in item: found.append({"metadata": a, "availability": "NOT_FETCHED", "reason": "Attachment bytes are not in the extracted message; no download or reconstruction attempted"})
                elif key in ("asset_pointer", "image_url", "audio_url"):
                    found.append({"metadata": {key: item}, "availability": "NOT_FETCHED", "reason": "Referenced media is not archived as bytes"})
                else: visit(item)
        elif isinstance(value, list):
            for item in value: visit(item)
    visit(message)
    return found


def control_comparison(data, messages, baseline):
    """Project identity is not proof that two snapshots share conversation lineage."""
    def identities(value):
        backing = conversation = None
        for _ in range(8):
            if not isinstance(value, dict): break
            backing = backing or value.get("backing_conversation_id")
            source = value.get("source") or {}
            conversation = conversation or value.get("conversation_id") or value.get("id") or source.get("conversation_id")
            value = (value.get("provenance") or {}).get("source_metadata")
        return backing, conversation
    current_backing, current_id = identities(data)
    control_backing, control_id = identities(baseline)
    if current_backing and control_backing:
        if current_backing == control_backing:
            return {"status": "CONFIRMED", "reason": "Matching source backing_conversation_id", "conversation_id": current_backing}
        return {"status": "UNVERIFIED", "reason": "Conflicting backing conversation identities; control not applied"}
    if current_id and current_id == control_id:
        return {"status": "CONFIRMED", "reason": "Matching source conversation identity", "conversation_id": current_id}
    # Different share IDs may represent one original conversation. A common ordered,
    # content-matching prefix with a user message establishes observed lineage only.
    prefix, has_user = 0, False
    for current, control in zip(messages, baseline.get("messages") or []):
        if (not current.get("id") or current.get("id") != control.get("id")
                or not current.get("role") or current.get("role") != control.get("role")
                or not current.get("text") or current.get("text") != control.get("text")):
            break
        current_content = (current.get("raw_message") or {}).get("content")
        control_content = (control.get("raw_message") or {}).get("content")
        if current_content is not None and control_content is not None and current_content != control_content: break
        prefix += 1; has_user = has_user or current["role"] == "user"
    if prefix >= 2 and has_user:
        return {"status": "CONFIRMED", "reason": "Common ordered message-ID/content prefix including a user message", "matching_prefix_records": prefix}
    return {"status": "UNVERIFIED", "reason": "Common conversation lineage is not established; control not applied"}


def attachment_summary(messages, unselected, previous):
    """Recompute raw-record markers once, retaining known upstream availability."""
    records, aliases = {}, {}
    for message in messages:
        if message.get("id") and message.get("node_id"): aliases[message["id"]] = message["node_id"]
    for key, node in unselected.items():
        raw = node.get("message")
        if isinstance(raw, dict) and raw.get("id"): aliases[raw["id"]] = key
    def add(record):
        anchor = record.get("node_id") or record.get("message_id")
        anchor = aliases.get(anchor, anchor)
        key = (anchor, json.dumps(record.get("metadata"), sort_keys=True, ensure_ascii=False))
        records[key] = record
    for message in messages:
        for record in attachment_records(message["raw_message"]):
            record["message_id"] = message.get("id")
            if message.get("node_id"): record["node_id"] = message["node_id"]
            add(record)
    for key, node in unselected.items():
        for record in attachment_records(node.get("message")):
            record["node_id"] = key
            if isinstance(node.get("message"), dict): record["message_id"] = node["message"].get("id")
            add(record)
    # Previous markers are evidence; do not replace an established availability with
    # a new generic NOT_FETCHED label or reconstruct missing attachment content.
    for record in previous or []:
        if not isinstance(record, dict): raise ValueError("Invalid inherited attachment marker")
        add(dict(record))
    return list(records.values())

def build_history(data, source, project_id, baseline=None, source_sha256=None, conversation_id=None):
    if not project_id.strip(): raise ValueError("A confirmed project identifier is required")
    if isinstance(data, list):
        matches = [c for c in data if isinstance(c, dict) and (c.get("id") == conversation_id or c.get("conversation_id") == conversation_id)] if conversation_id else []
        if len(matches) != 1: raise ValueError("Multi-conversation export requires an exact --conversation-id")
        data = matches[0]
    if not isinstance(data, dict): raise ValueError("Unsupported source format")
    if data.get("project_id") and data["project_id"] != project_id:
        raise ValueError("Source archive belongs to a different confirmed project")
    if baseline and baseline.get("project_id") != project_id:
        raise ValueError("Control archive belongs to a different or unconfirmed project")
    losses, messages, attachments = [], [], []
    unselected = data.get("unselected_source_nodes") or {}
    if not isinstance(unselected, dict): raise ValueError("Invalid inherited branch records")
    upstream = {k: data[k] for k in ("source_completeness", "extraction_completeness", "status", "limitations") if k in data}
    if "linear_conversation" in data or "mapping" in data:
        nodes, losses = ordered_nodes(data)
        selected_ids = {n.get("id") for n in nodes}
        unselected = {k: v for k, v in (data.get("mapping") or {}).items() if k not in selected_ids}
        for position, node in enumerate(nodes):
            message = node.get("message")
            if message is None: continue
            if not isinstance(message, dict): raise ValueError("Invalid source message")
            author = message.get("author") or {}
            content = message.get("content")
            messages.append({"index": len(messages), "source_index": position, "id": message.get("id"), "node_id": node.get("id"), "role": author.get("role"), "text": visible_text(content), "raw_message": message})
    elif isinstance(data.get("messages"), list):
        for position, message in enumerate(data["messages"]):
            if not isinstance(message, dict): raise ValueError("Invalid exported message")
            messages.append({"index": position, "source_index": message.get("source_index", message.get("source_linear_index", position)), "id": message.get("id", message.get("message_id")), "node_id": message.get("node_id"), "role": message.get("role"), "text": message.get("text"), "raw_message": message.get("raw_message", message)})
        losses.append("Normalized local export: completeness of its original extraction is unverified")
    else: raise ValueError("Unsupported export; provide structured JSON or supported public-page HTML")
    if not messages: raise ValueError("No messages extracted; no HISTORY created")
    if any(not isinstance(node, dict) for node in unselected.values()):
        raise ValueError("Invalid unselected branch node")
    total_messages = len(messages) + sum(node.get("message") is not None for node in unselected.values())
    if total_messages > MAX_MESSAGES:
        raise ValueError("Too many messages across selected chain and additional branches")
    attachments = attachment_summary(messages, unselected, data.get("inaccessible_attachments"))
    ids = [m["id"] for m in messages if m["id"]]
    if len(ids) != len(set(ids)): raise ValueError("Duplicate message IDs; ambiguous source")
    missing = []
    comparison = control_comparison(data, messages, baseline) if baseline else None
    available_ids = set(ids) | {node["message"].get("id") for node in unselected.values() if isinstance(node.get("message"), dict)}
    if comparison and comparison["status"] == "CONFIRMED":
        missing = [m["id"] for m in baseline["messages"] if m.get("id") and m["id"] not in available_ids]
    limitations = list(data.get("limitations") or [])
    if comparison and comparison["status"] == "UNVERIFIED": limitations.append(comparison["reason"])
    if unselected: limitations.append("Additional accessible branch nodes are preserved separately without inventing cross-branch chronology")
    limitations += ["A public snapshot/export does not prove completeness of the original private conversation", "Alternative branches, UI rendering and private attachment bytes are not verified"]
    if attachments: limitations.append("Referenced attachments/media are unavailable in this archive")
    redacted = any((m["raw_message"].get("metadata") or {}).get("is_redacted") or m["raw_message"].get("is_redacted") for m in messages)
    if redacted: limitations.append("Published redacted messages are preserved as supplied; private content unavailable")
    source_partial = (upstream.get("source_completeness") or {}).get("status") == "PARTIAL" or upstream.get("status") == "PARTIAL"
    extraction_partial = (upstream.get("extraction_completeness") or {}).get("status") == "PARTIAL"
    source_status = "PARTIAL" if missing or attachments or redacted or source_partial or extraction_partial else "UNVERIFIED"
    concrete_losses = [x for x in losses if not x.startswith("Normalized local export")]
    if extraction_partial: losses.append("Upstream extraction remains PARTIAL: " + str(upstream["extraction_completeness"].get("reason", "Known upstream loss")))
    extraction_status = "PARTIAL" if concrete_losses or extraction_partial else ("UNVERIFIED" if losses else "COMPLETE")
    source_reasons = ["Original private conversation completeness is not independently attested"]
    if attachments: source_reasons.append("Some referenced attachment contents are unavailable")
    if redacted: source_reasons.append("Redacted source content is unavailable")
    if missing: source_reasons.append("Confirmed same-lineage control contains messages absent from this source")
    if source_partial or extraction_partial: source_reasons.append("Known upstream loss/completeness limitations are retained")
    if comparison and comparison["status"] == "UNVERIFIED": source_reasons.append(comparison["reason"])
    return {"schema_version": VERSION, "project_id": project_id, "source": {"location": source, "sha256": source_sha256, "conversation_id": data.get("conversation_id", data.get("id")), "title": data.get("title")}, "extracted_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "provenance": {"extractor_version": VERSION, "method": "Public page data or user-provided local export; no JavaScript execution/private API", "source_metadata": {k: v for k, v in data.items() if k not in ("mapping", "linear_conversation", "messages")}}, "upstream_completeness": upstream, "unselected_source_nodes": unselected, "source_completeness": {"status": source_status, "scope": "Original conversation versus supplied snapshot", "reason": "; ".join(source_reasons), "missing_control_message_ids": missing, "control_comparison": comparison, "control_provenance": {"project_id": baseline.get("project_id"), "source": baseline.get("source"), "extracted_at_utc": baseline.get("extracted_at_utc")} if baseline else None}, "extraction_completeness": {"status": extraction_status, "scope": "Selected ordered records and separately preserved accessible branch nodes; excludes inaccessible media bytes", "reason": "; ".join(losses) if losses else "Available structured messages extracted without detected gaps; some attachment contents may be unavailable; original private conversation completeness is not confirmed"}, "status": "PARTIAL" if source_status == "PARTIAL" or extraction_status == "PARTIAL" else "UNVERIFIED", "limitations": limitations + losses, "inaccessible_attachments": attachments, "messages": messages}

def write_snapshot(destination, history):
    encoded = json.dumps(history, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if len(encoded.encode("utf-8")) > MAX_BYTES:
        raise ValueError("Archive exceeds 64 MiB; no oversized snapshot written")
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    with (destination / "HISTORY.json").open("x", encoding="utf-8", newline="\n") as handle: handle.write(encoded)

def message_window(history, start, count):
    if start < 0 or count < 1 or count > 1000: raise ValueError("Use a nonnegative start and count 1..1000")
    return history["messages"][start:start+count]

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    extract = sub.add_parser("extract")
    extract.add_argument("--source", required=True); extract.add_argument("--project-id", required=True)
    extract.add_argument("--output", required=True); extract.add_argument("--conversation-id"); extract.add_argument("--control-history")
    read = sub.add_parser("read")
    read.add_argument("history"); read.add_argument("--start", type=int, default=0); read.add_argument("--count", type=int, default=20)
    args = parser.parse_args(argv)
    try:
        if args.command == "read":
            path = Path(args.history)
            if path.stat().st_size > MAX_BYTES: raise ValueError("History exceeds bounded reader size")
            history = json.loads(path.read_text(encoding="utf-8"))
            print(json.dumps(message_window(history, args.start, args.count), ensure_ascii=False, allow_nan=False)); return 0
        data, sha = load_source(args.source)
        baseline = None
        if args.control_history:
            path = Path(args.control_history)
            if path.stat().st_size > MAX_BYTES: raise ValueError("Control history exceeds bounded reader size")
            baseline = json.loads(path.read_text(encoding="utf-8"))
        history = build_history(data, args.source, args.project_id, baseline, sha, args.conversation_id)
        write_snapshot(args.output, history)
        print(json.dumps({"status": history["status"], "messages": len(history["messages"]), "source_completeness": history["source_completeness"], "extraction_completeness": history["extraction_completeness"]}, ensure_ascii=False)); return 0
    except (ValueError, OSError, KeyError, TypeError, AttributeError, RecursionError) as error:
        print("BLOCKED: " + str(error) + ". Use an available user-provided local JSON export if appropriate.", file=sys.stderr); return 2

if __name__ == "__main__":
    raise SystemExit(main())
