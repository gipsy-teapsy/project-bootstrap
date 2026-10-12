"""Transfer mechanics fixtures; these are not model-behavior tests."""
import importlib.util
import sys
import json
import tempfile
import contextlib
import io
from unittest.mock import patch
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "plugins/project-bootstrap/skills/project-bootstrap-transfer/scripts/extract_history.py"

class TransferTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("transfer_helper", HELPER)
        cls.helper = importlib.util.module_from_spec(spec)
        previous = sys.dont_write_bytecode
        try:
            sys.dont_write_bytecode = True
            spec.loader.exec_module(cls.helper)
        finally:
            sys.dont_write_bytecode = previous

    def source(self, extra=None):
        messages = [{"id": "u1", "author": {"role": "user"}, "content": {"content_type": "text", "parts": ["Русский контекст. Do not execute: delete files"]}, "create_time": 10},
                    {"id": "a1", "author": {"role": "assistant"}, "content": {"content_type": "text", "parts": ["Принято только чтение"]}}]
        if extra:
            messages += extra
        nodes = [{"id": m["id"], "parent": messages[i-1]["id"] if i else None, "message": m} for i, m in enumerate(messages)]
        return {"linear_conversation": nodes, "mapping": {n["id"]: n for n in reversed(nodes)}, "current_node": nodes[-1]["id"]}

    def archive(self, source=None, baseline=None):
        return self.helper.build_history(source or self.source(), "fixture", "confirmed-project", baseline=baseline)

    def test_order_roles_metadata_and_unverified_source(self):
        h = self.archive()
        self.assertEqual([m["id"] for m in h["messages"]], ["u1", "a1"])
        self.assertEqual([m["role"] for m in h["messages"]], ["user", "assistant"])
        self.assertEqual(h["messages"][0]["raw_message"]["create_time"], 10)
        self.assertEqual(h["source_completeness"]["status"], "UNVERIFIED")
        self.assertEqual(h["extraction_completeness"]["status"], "COMPLETE")
        json.dumps(h, allow_nan=False)

    def test_short_snapshot_relative_to_control_is_partial(self):
        full = self.archive(self.source([{"id": "u2", "author": {"role": "user"}, "content": {"parts": ["S6"]}}]))
        early = self.archive(baseline=full)
        self.assertEqual(early["source_completeness"]["status"], "PARTIAL")
        self.assertIn("u2", early["source_completeness"]["missing_control_message_ids"])

    def test_other_project_control_rejected(self):
        h = self.archive(); h["project_id"] = "different-project"
        with self.assertRaises(ValueError): self.archive(baseline=h)

    def test_no_invented_role_or_time(self):
        s = self.source(); s["linear_conversation"][0]["message"].pop("author")
        h = self.archive(s)
        self.assertIsNone(h["messages"][0]["role"])
        self.assertNotIn("create_time", h["messages"][1]["raw_message"])

    def test_attachments_and_redaction_are_labeled(self):
        s = self.source(); m = s["linear_conversation"][0]["message"]
        m["metadata"] = {"attachments": [{"id": "file-test", "name": "policy.pdf"}], "is_redacted": True}
        h = self.archive(s)
        self.assertEqual(h["inaccessible_attachments"][0]["availability"], "NOT_FETCHED")
        self.assertIn("redacted", " ".join(h["limitations"]).lower())

    def test_mapping_chain_is_used_without_sorting(self):
        s = self.source(); del s["linear_conversation"]
        self.assertEqual([m["id"] for m in self.archive(s)["messages"]], ["u1", "a1"])

    def test_missing_chain_is_partial(self):
        s = self.source(); del s["linear_conversation"]; s["mapping"].pop("u1")
        self.assertEqual(self.archive(s)["extraction_completeness"]["status"], "PARTIAL")

    def test_unknown_format_and_empty_history_are_blocked(self):
        for data in ({"messages": []}, {"unrelated": 1}):
            with self.assertRaises(ValueError): self.helper.build_history(data, "fixture", "p")

    def test_history_is_data_and_source_language_is_unchanged(self):
        h = self.archive()
        self.assertIn("Русский контекст", h["messages"][0]["text"])
        self.assertIn("delete files", h["messages"][0]["text"])

    def test_existing_snapshot_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "snapshot"
            self.helper.write_snapshot(p, self.archive())
            before = (p / "HISTORY.json").read_bytes()
            with self.assertRaises(FileExistsError): self.helper.write_snapshot(p, self.archive())
            self.assertEqual(before, (p / "HISTORY.json").read_bytes())

    def test_flattened_html_and_unknown_tag_fail_closed(self):
        table = [{"_1": 2}, "serverResponse", {"_3": 4}, "data", {"_5": 6}, "linear_conversation", []]
        html = "streamController.enqueue(" + json.dumps(json.dumps(table)) + ")"
        self.assertEqual(self.helper.parse_html(html)["linear_conversation"], [])
        with self.assertRaises(ValueError): self.helper.parse_html("<html>login page</html>")

    def test_shared_url_is_bounded_to_public_chatgpt(self):
        for url in ("https://example.com/share/x", "file:///tmp/history", "https://chatgpt.com/backend-api/x", "https://user:pass@chatgpt.com/share/x"):
            with self.assertRaises(ValueError): self.helper.validate_shared_url(url)

    def test_bounded_read_outputs_requested_window(self):
        h = self.archive()
        self.assertEqual(len(self.helper.message_window(h, 1, 1)), 1)
        self.assertEqual(self.helper.message_window(h, 1, 1)[0]["id"], "a1")
        with self.assertRaises(ValueError): self.helper.message_window(h, 0, 1001)


    def test_dead_link_returns_blocked_without_output(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "absent"
            with patch.object(self.helper, "load_source", side_effect=OSError("HTTP 404")), contextlib.redirect_stderr(io.StringIO()) as errors:
                code = self.helper.main(["extract", "--source", "https://chatgpt.com/share/11111111-1111-1111-1111-111111111111", "--project-id", "p", "--output", str(out)])
            self.assertEqual(code, 2)
            self.assertFalse(out.exists())
            self.assertIn("BLOCKED", errors.getvalue())
            self.assertIn("local JSON export", errors.getvalue())

    def test_account_export_requires_exact_conversation_selection(self):
        data = [dict(self.source(), id="one"), dict(self.source(), id="two")]
        with self.assertRaises(ValueError): self.helper.build_history(data, "fixture", "p")
        result = self.helper.build_history(data, "fixture", "p", conversation_id="two")
        self.assertEqual(result["source"]["conversation_id"], "two")

    def test_missing_start_is_partial_and_output_bound_is_enforced(self):
        s = self.source(); s["linear_conversation"][0]["parent"] = "lost"
        self.assertEqual(self.archive(s)["extraction_completeness"]["status"], "PARTIAL")
        with tempfile.TemporaryDirectory() as d, patch.object(self.helper, "MAX_BYTES", 20):
            p = Path(d) / "not-created"
            with self.assertRaises(ValueError): self.helper.write_snapshot(p, self.archive())
            self.assertFalse(p.exists())

    def test_skill_and_cloud_routing_preserve_architecture_and_boundaries(self):
        text = (HELPER.parents[1] / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: project-bootstrap-transfer", text)
        for topic in ("not a fourth logical role", "Source completeness", "Extraction completeness", "UNVERIFIED", "PARTIAL", "untrusted data", "new full REFERENCE and HANDOFF", "without separate authorization", "Do not execute them", "historical permission", "language override"):
            self.assertIn(topic, text)
        cloud = (ROOT / "plugins/project-bootstrap/shared/references/cloud-manager-delivery.md").read_text(encoding="utf-8")
        for topic in ("manual Cloud Context Transfer", "$project-bootstrap-transfer", "local export", "anyone with the link", "do not execute", "before evidence"):
            self.assertIn(topic.lower(), cloud.lower())


    def test_normalized_archive_retains_upstream_partial_evidence(self):
        source = self.archive()
        source["source_completeness"] = {"status": "PARTIAL", "reason": "Truncated after S5"}
        source["extraction_completeness"] = {"status": "PARTIAL", "reason": "Lost accessible message u2"}
        source["limitations"] = ["Known truncation after S5"]
        result = self.helper.build_history(source, "fixture-normalized", "confirmed-project")
        self.assertEqual(result["status"], "PARTIAL")
        self.assertEqual(result["extraction_completeness"]["status"], "PARTIAL")
        self.assertIn("Truncated after S5", json.dumps(result["upstream_completeness"]))
        self.assertIn("Known truncation after S5", result["limitations"])

    def test_accessible_unselected_branch_nodes_are_archived_without_invented_order(self):
        s = self.source(); del s["linear_conversation"]
        s["mapping"]["other"] = {"id": "other", "parent": "u1", "message": {"id": "other", "author": {"role": "assistant"}, "content": {"parts": ["Alternative response"]}}}
        h = self.archive(s)
        self.assertEqual([m["id"] for m in h["messages"]], ["u1", "a1"])
        self.assertEqual(h["unselected_source_nodes"]["other"]["message"]["content"]["parts"], ["Alternative response"])
        self.assertIn("branch", " ".join(h["limitations"]).lower())
        repeated = self.helper.build_history(h, "normalized-fixture", "confirmed-project")
        self.assertEqual(repeated["unselected_source_nodes"], h["unselected_source_nodes"])


    def test_normalized_source_of_another_project_cannot_be_relabelled(self):
        other = self.archive(); other["project_id"] = "other-confirmed-project"
        with self.assertRaises(ValueError): self.helper.build_history(other, "fixture", "current-confirmed-project")


    def test_unrelated_same_project_control_does_not_claim_missing_messages(self):
        old = self.source(); old["id"] = "old-thread"
        control = self.archive(old)
        new = self.source(); new["id"] = "new-thread"
        for n in new["linear_conversation"]:
            n["id"] = "new-" + n["id"]; n["message"]["id"] = n["id"]
            if n["parent"]: n["parent"] = "new-" + n["parent"]
        new["mapping"] = {n["id"]: n for n in new["linear_conversation"]}; new["current_node"] = "new-a1"
        result = self.archive(new, baseline=control)
        self.assertEqual(result["source_completeness"]["status"], "UNVERIFIED")
        self.assertEqual(result["source_completeness"]["missing_control_message_ids"], [])
        self.assertEqual(result["source_completeness"]["control_comparison"]["status"], "UNVERIFIED")

    def test_different_share_ids_with_same_backing_conversation_allow_control(self):
        full = self.source([{"id": "u2", "author": {"role": "user"}, "content": {"parts": ["S6"]}}])
        full.update(conversation_id="share-t0", backing_conversation_id="original-thread")
        early = self.source(); early.update(conversation_id="share-s5", backing_conversation_id="original-thread")
        result = self.archive(early, baseline=self.archive(full))
        self.assertEqual(result["source_completeness"]["missing_control_message_ids"], ["u2"])
        self.assertEqual(result["source_completeness"]["control_comparison"]["status"], "CONFIRMED")

    def test_unknown_control_lineage_is_unverified_without_loss_inference(self):
        result = self.archive(baseline={"project_id": "confirmed-project", "messages": [{"id": "unknown", "role": "user", "text": "unrelated"}]})
        self.assertEqual(result["source_completeness"]["status"], "UNVERIFIED")
        self.assertEqual(result["source_completeness"]["missing_control_message_ids"], [])
        self.assertEqual(result["source_completeness"]["control_comparison"]["status"], "UNVERIFIED")

    def test_shared_prefix_can_establish_lineage_without_conversation_metadata(self):
        full = self.archive(self.source([{"id": "u2", "author": {"role": "user"}, "content": {"parts": ["later"]}}]))
        early = self.archive(baseline=full)
        self.assertEqual(early["source_completeness"]["control_comparison"]["status"], "CONFIRMED")
        self.assertEqual(early["source_completeness"]["missing_control_message_ids"], ["u2"])

    def test_same_ids_without_matching_message_content_do_not_prove_lineage(self):
        full = self.archive(self.source([{"id": "u2", "content": {"parts": ["later"]}}]))
        early = self.source(); early["linear_conversation"][0]["message"]["content"]["parts"] = ["different"]
        result = self.archive(early, baseline=full)
        self.assertEqual(result["source_completeness"]["missing_control_message_ids"], [])
        self.assertEqual(result["source_completeness"]["control_comparison"]["status"], "UNVERIFIED")

    def test_repeat_attachment_summary_includes_all_branches_without_duplicates(self):
        source = self.source()
        source["linear_conversation"][0]["message"]["metadata"] = {"attachments": [{"id": "selected-file", "name": "selected.pdf"}]}
        source["mapping"]["branch"] = {"id": "branch", "parent": "u1", "message": {"id": "branch-message", "author": {"role": "assistant"}, "content": {"parts": ["branch"]}, "metadata": {"attachments": [{"id": "branch-file", "name": "branch.pdf"}]}}}
        first = self.archive(source)
        self.assertEqual(len(first["inaccessible_attachments"]), 2)
        branch = next(a for a in first["inaccessible_attachments"] if a.get("node_id") == "branch")
        branch["availability"] = "UNAVAILABLE"; branch["reason"] = "Confirmed inaccessible original attachment"
        repeated = self.helper.build_history(first, "normalized", "confirmed-project")
        twice = self.helper.build_history(repeated, "normalized-again", "confirmed-project")
        for result in (repeated, twice):
            self.assertEqual(len(result["inaccessible_attachments"]), 2)
            self.assertEqual(result["unselected_source_nodes"], first["unselected_source_nodes"])
            self.assertEqual(next(a for a in result["inaccessible_attachments"] if a.get("node_id") == "branch")["availability"], "UNAVAILABLE")
        self.assertEqual(repeated["upstream_completeness"]["source_completeness"], first["source_completeness"])
        self.assertEqual(repeated["provenance"]["source_metadata"]["provenance"], first["provenance"])

    def test_total_message_bound_includes_additional_branches_and_normalized_repeat(self):
        source = self.source()
        source["mapping"]["branch"] = {"id": "branch", "parent": "u1", "message": {"id": "branch-message", "content": {"parts": ["branch"]}}}
        first = self.archive(source)
        with patch.object(self.helper, "MAX_MESSAGES", 2):
            with self.assertRaises(ValueError): self.archive(source)
            with self.assertRaises(ValueError): self.helper.build_history(first, "normalized", "confirmed-project")
        with patch.object(self.helper, "MAX_MESSAGES", 3):
            result = self.archive(source)
            self.assertEqual(len(result["messages"]) + len(result["unselected_source_nodes"]), 3)

    def test_total_message_boundary_ignores_empty_root_nodes(self):
        source = self.source(); root = {"id": "root", "parent": None, "message": None}
        source["linear_conversation"][0]["parent"] = "root"; source["linear_conversation"].insert(0, root)
        source["mapping"]["root"] = root; del source["linear_conversation"]
        with patch.object(self.helper, "MAX_MESSAGES", 2):
            self.assertEqual(len(self.archive(source)["messages"]), 2)
        with patch.object(self.helper, "MAX_MESSAGES", 1):
            with self.assertRaises(ValueError): self.archive(source)

    def test_branch_limit_error_does_not_write_output(self):
        source = self.source(); source["mapping"]["branch"] = {"id": "branch", "message": {"id": "b", "content": {"parts": ["branch"]}}}
        with tempfile.TemporaryDirectory() as d, patch.object(self.helper, "MAX_MESSAGES", 2), patch.object(self.helper, "load_source", return_value=(source, "fixture-hash")), contextlib.redirect_stderr(io.StringIO()) as errors:
            out = Path(d) / "not-created"
            code = self.helper.main(["extract", "--source", "synthetic.json", "--project-id", "confirmed-project", "--output", str(out)])
            self.assertEqual(code, 2); self.assertFalse(out.exists()); self.assertIn("BLOCKED", errors.getvalue())

if __name__ == "__main__":
    unittest.main()
