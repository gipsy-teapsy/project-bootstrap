import hashlib
import json
import re
import struct
import unittest
import zlib
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "project-bootstrap"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
SKILLS = (
    "project-bootstrap-manager",
    "project-bootstrap-master",
    "project-bootstrap-task",
)
SHARED_REFERENCES = (
    "cloud-manager-delivery.md",
    "control-model.md",
    "evidence-and-authority.md",
    "recovery-and-continuity.md",
    "environments-git-portable-migration.md",
    "execution-profiles.md",
)
SHARED_TEMPLATES = (
    "cloud-to-codex-fallback.md",
    "manager-to-master.md",
    "master-to-task.md",
    "task-state.md",
    "task-checkpoint.md",
    "task-handoff.md",
)
BRAND_ASSETS = {
    "icon-master-1024.png": (1024, 1024),
    "icon-512.png": (512, 512),
    "icon-128.png": (128, 128),
    "icon-64.png": (64, 64),
    "icon-32.png": (32, 32),
    "icon-16.png": (16, 16),
    "icon-small-32.png": (32, 32),
    "icon-small-24.png": (24, 24),
    "icon-small-16.png": (16, 16),
}
SEMVER = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SCHEMA = ROOT / "tests" / "fixtures" / "plugin.schema-1.0.0.json"
SCHEMA_SHA256 = "0a4aad95ce337878ad38802ebf0daa3fde76abe3f65400c86bcbb1ec0b3ab883"
SECRET = re.compile(
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|"
    r"\b(?:(?:ghp|github_pat)_|sk-proj-)[A-Za-z0-9_-]{16,}\b"
)


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise AssertionError(f"{path} has no opening frontmatter delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise AssertionError(f"{path} has no closing frontmatter delimiter") from exc
    fields = {}
    for line in lines[1:end]:
        if ":" not in line:
            raise AssertionError(f"{path} has invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, text


def product_text_files():
    roots = [ROOT / "README.md", ROOT / "docs", ROOT / ".agents", PLUGIN]
    for item in roots:
        if item.is_file():
            yield item
        elif item.is_dir():
            yield from (path for path in item.rglob("*") if path.is_file())


def read_png_rgba_alpha(path: Path):
    data = path.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise AssertionError(f"{path} is not a PNG")
    offset = 8
    header = None
    compressed = bytearray()
    while offset < len(data):
        length = struct.unpack(">I", data[offset : offset + 4])[0]
        chunk_type = data[offset + 4 : offset + 8]
        payload = data[offset + 8 : offset + 8 + length]
        crc = struct.unpack(">I", data[offset + 8 + length : offset + 12 + length])[0]
        if zlib.crc32(chunk_type + payload) & 0xFFFFFFFF != crc:
            raise AssertionError(f"{path} has an invalid PNG chunk CRC")
        offset += 12 + length
        if chunk_type == b"IHDR":
            header = struct.unpack(">IIBBBBB", payload)
        elif chunk_type == b"IDAT":
            compressed.extend(payload)
        elif chunk_type == b"IEND":
            break
    if header is None:
        raise AssertionError(f"{path} has no PNG IHDR")
    width, height, depth, color_type, compression, filtering, interlace = header
    if (depth, color_type, compression, filtering, interlace) != (8, 6, 0, 0, 0):
        raise AssertionError(f"{path} must be non-interlaced 8-bit RGBA PNG")
    stride = width * 4
    raw = zlib.decompress(bytes(compressed))
    if len(raw) != height * (stride + 1):
        raise AssertionError(f"{path} has an unexpected decompressed size")
    rows = []
    previous = bytearray(stride)
    cursor = 0
    for _ in range(height):
        filter_type = raw[cursor]
        current = bytearray(raw[cursor + 1 : cursor + 1 + stride])
        cursor += stride + 1
        for index in range(stride):
            left = current[index - 4] if index >= 4 else 0
            above = previous[index]
            upper_left = previous[index - 4] if index >= 4 else 0
            if filter_type == 1:
                current[index] = (current[index] + left) & 0xFF
            elif filter_type == 2:
                current[index] = (current[index] + above) & 0xFF
            elif filter_type == 3:
                current[index] = (current[index] + ((left + above) // 2)) & 0xFF
            elif filter_type == 4:
                estimate = left + above - upper_left
                distances = (
                    abs(estimate - left),
                    abs(estimate - above),
                    abs(estimate - upper_left),
                )
                predictor = (left, above, upper_left)[distances.index(min(distances))]
                current[index] = (current[index] + predictor) & 0xFF
            elif filter_type != 0:
                raise AssertionError(f"{path} uses unknown PNG filter {filter_type}")
        rows.append(current)
        previous = current
    alpha = [row[index] for row in rows for index in range(3, stride, 4)]
    return (width, height), rows, alpha


class SecretDetectorTests(unittest.TestCase):
    def test_github_pat_underscore_prefixes_are_detected(self):
        for prefix in ("ghp_", "github_pat_"):
            with self.subTest(prefix=prefix):
                token = prefix + "A" * 36
                self.assertIsNotNone(SECRET.search("token=" + token))

    def test_github_hyphen_prefixes_are_not_pats(self):
        for prefix in ("ghp-", "github_pat-"):
            with self.subTest(prefix=prefix):
                self.assertIsNone(SECRET.search(prefix + "A" * 36))

    def test_other_supported_secret_families_are_detected(self):
        samples = ["sk-proj-" + "A" * 36]
        samples.extend(
            "-----BEGIN " + kind + "PRIVATE KEY-----"
            for kind in ("", "RSA ", "EC ", "OPENSSH ")
        )
        for sample in samples:
            with self.subTest(sample=sample):
                self.assertIsNotNone(SECRET.search(sample))


class PackageContractTests(unittest.TestCase):
    def test_portable_manifest_validates_against_declared_official_schema(self):
        # Git may materialize the public JSON fixture with CRLF on Windows.
        schema_bytes = SCHEMA.read_bytes().replace(b"\r\n", b"\n")
        self.assertEqual(SCHEMA_SHA256, hashlib.sha256(schema_bytes).hexdigest())
        schema = load_json(SCHEMA)
        manifest = load_json(PLUGIN / "plugin.json")
        self.assertEqual(schema["$id"], manifest["$schema"])
        Draft202012Validator.check_schema(schema)
        errors = list(Draft202012Validator(schema).iter_errors(manifest))
        self.assertEqual([], [error.message for error in errors])

    def test_schema_rejects_return_of_top_level_interface(self):
        manifest = load_json(PLUGIN / "plugin.json")
        manifest["interface"] = load_json(PLUGIN / ".codex-plugin" / "plugin.json")["interface"]
        errors = list(Draft202012Validator(load_json(SCHEMA)).iter_errors(manifest))
        self.assertTrue(any(
            error.validator == "additionalProperties" and "interface" in error.message
            for error in errors
        ), "the original forbidden top-level interface must fail schema validation")

    def test_expected_layout_exists(self):
        expected = [
            MARKETPLACE,
            PLUGIN / "plugin.json",
            PLUGIN / ".codex-plugin" / "plugin.json",
            PLUGIN / "README.md",
            PLUGIN / "CHANGELOG.md",
            PLUGIN / "docs" / "QUICK_START_RU.md",
            PLUGIN / "docs" / "USER_GUIDE_RU.md",
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md",
            ROOT / "README.md",
            ROOT / "docs" / "TESTING.md",
            ROOT / "docs" / "MARKETPLACE_INSTALL_RU.md",
        ]
        expected.extend(PLUGIN / "skills" / name / "SKILL.md" for name in SKILLS)
        expected.extend(
            PLUGIN / "shared" / "references" / name for name in SHARED_REFERENCES
        )
        expected.extend(
            PLUGIN / "shared" / "templates" / name for name in SHARED_TEMPLATES
        )
        expected.extend(PLUGIN / "assets" / name for name in BRAND_ASSETS)
        missing = [str(path.relative_to(ROOT)) for path in expected if not path.is_file()]
        self.assertEqual([], missing, f"missing required files: {missing}")

    def test_marketplace_contract(self):
        data = load_json(MARKETPLACE)
        self.assertEqual("gipsy-project-bootstrap", data["name"])
        self.assertEqual("Project Bootstrap", data["interface"]["displayName"])
        self.assertEqual(1, len(data["plugins"]))
        entry = data["plugins"][0]
        self.assertEqual("project-bootstrap", entry["name"])
        self.assertEqual(
            {"source": "local", "path": "./plugins/project-bootstrap"},
            entry["source"],
        )
        self.assertEqual(
            {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            entry["policy"],
        )
        self.assertNotIn("products", entry["policy"])
        self.assertEqual("Developer Tools", entry["category"])
        source = (ROOT / entry["source"]["path"]).resolve()
        self.assertTrue(source.is_dir())
        self.assertEqual(PLUGIN.resolve(), source)

    def test_portable_and_compatibility_manifests_are_consistent(self):
        portable = load_json(PLUGIN / "plugin.json")
        compat = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
        self.assertEqual(
            "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            portable["$schema"],
        )
        for manifest in (portable, compat):
            self.assertEqual("project-bootstrap", manifest["name"])
            self.assertEqual("0.1.8", manifest["version"])
            self.assertRegex(manifest["version"], SEMVER)
            self.assertTrue(manifest["description"].strip())
            self.assertEqual("Gipsy", manifest["author"]["name"])
            self.assertEqual(
                "https://github.com/gipsy-teapsy/project-bootstrap",
                manifest["repository"],
            )
            self.assertNotIn("license", manifest)
            self.assertNotIn("apps", manifest)
            self.assertNotIn("mcpServers", manifest)
        self.assertEqual("./skills/", compat["skills"])
        self.assertEqual(portable["extensions"]["com.openai"]["interface"], compat["interface"])
        interface = compat["interface"]
        self.assertEqual("Project Bootstrap", interface["displayName"])
        self.assertEqual("Gipsy", interface["developerName"])
        self.assertEqual("Developer Tools", interface["category"])
        self.assertIsInstance(interface["capabilities"], list)
        self.assertGreater(len(interface["capabilities"]), 0)
        self.assertIsInstance(interface["defaultPrompt"], list)
        self.assertGreater(len(interface["defaultPrompt"]), 0)
        self.assertLessEqual(len(interface["defaultPrompt"]), 3)
        self.assertTrue(all(len(item) <= 128 for item in interface["defaultPrompt"]))
        self.assertEqual("./assets/icon-master-1024.png", interface["logo"])
        self.assertEqual("./assets/icon-64.png", interface["composerIcon"])
        for field in ("logo", "composerIcon"):
            self.assertTrue((PLUGIN / interface[field]).resolve().is_file())

    def test_brand_assets_are_exact_rgba_png_set(self):
        assets = PLUGIN / "assets"
        self.assertEqual(sorted(BRAND_ASSETS), sorted(path.name for path in assets.iterdir()))
        for name, expected_size in BRAND_ASSETS.items():
            with self.subTest(name=name):
                size, rows, alpha = read_png_rgba_alpha(assets / name)
                self.assertEqual(expected_size, size)
                self.assertEqual(0, min(alpha), "transparent pixels are required")
                self.assertEqual(255, max(alpha), "opaque symbol pixels are required")
                self.assertTrue(any(0 < value < 255 for value in alpha))
                width, height = size
                corner_indexes = (0, width - 1, (height - 1) * width, width * height - 1)
                self.assertTrue(all(alpha[index] == 0 for index in corner_indexes))
                edge_alpha = (
                    [rows[0][index] for index in range(3, width * 4, 4)]
                    + [rows[-1][index] for index in range(3, width * 4, 4)]
                    + [row[3] for row in rows[1:-1]]
                    + [row[-1] for row in rows[1:-1]]
                )
                self.assertFalse(any(value == 255 for value in edge_alpha))

    def test_manager_skill_frontmatter_and_links(self):
        self._assert_skill("project-bootstrap-manager")
        manager = (
            PLUGIN / "skills" / "project-bootstrap-manager" / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("USER-FACING → user's language", manager)
        self.assertIn(
            "AGENT-FACING → English by default where appropriate", manager
        )

    def test_manager_owns_prompt_first_handoff_presentation_contract(self):
        manager = (
            PLUGIN / "skills" / "project-bootstrap-manager" / "SKILL.md"
        ).read_text(encoding="utf-8")
        cloud = (
            PLUGIN / "shared" / "references" / "cloud-manager-delivery.md"
        ).read_text(encoding="utf-8")
        native = (
            PLUGIN / "shared" / "templates" / "manager-to-master.md"
        ).read_text(encoding="utf-8")
        fallback = (
            PLUGIN / "shared" / "templates" / "cloud-to-codex-fallback.md"
        ).read_text(encoding="utf-8")
        artifact = (
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md"
        ).read_text(encoding="utf-8")

        presentation = manager.split("### Codex handoff presentation", 1)[1]
        presentation = presentation.split("\n## ", 1)[0]
        order_marker = "PROMPT → RECOMMENDATION → REASON → COMMENTARY"
        self.assertEqual(1, manager.count(order_marker))
        self.assertEqual(1, artifact.count(order_marker))
        self.assertNotIn(order_marker, cloud)

        ordered_slots = (
            "1. Make the complete plain fenced copy-ready Codex prompt the first visible content",
            "2. Immediately present the recommended model and reasoning effort.",
            "3. Immediately give one short reason",
            "4. Only then provide any remaining user-facing commentary",
        )
        positions = [presentation.index(slot) for slot in ordered_slots]
        self.assertEqual(sorted(positions), positions)
        self.assertIn("user's current language", presentation)
        self.assertIn("English by default where appropriate", presentation)
        self.assertIn("before declaring the handoff copy-ready", presentation)
        self.assertIn("no ordinary preamble or label", presentation)
        self.assertIn("Only a material decision, safety issue, authority boundary", presentation)

        self.assertIn("both native and fallback routes", cloud)
        self.assertIn("canonical Manager handoff presentation contract", cloud)
        self.assertIn("prompt, recommendation, reason, and remaining commentary", cloud)
        for template in (native, fallback):
            self.assertNotIn("Recommended execution profile:", template)
            self.assertNotIn("PROMPT FIRST", template)
            self.assertNotIn(order_marker, template)

    def test_explanation_request_does_not_implicitly_create_a_handoff(self):
        manager = (PLUGIN / "skills" / "project-bootstrap-manager" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        artifact = (PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md").read_text(
            encoding="utf-8"
        )
        for text in (manager, artifact):
            self.assertIn("EXPLANATION REQUEST ≠ HANDOFF REQUEST", text, "missing intent distinction")
            self.assertIn("answer the explanation/advice completely first", text, "explanation precedence missing")
            self.assertIn("whether it is critical or work was lost", text, "recovery questions missing")
            self.assertIn("user asks for a handoff, prompt, or transfer", text, "explicit handoff trigger missing")
            self.assertIn("necessary to satisfy the requested action", text, "necessary-action trigger missing")
            self.assertIn("offer a handoff afterwards", text, "optional next step missing")
            self.assertIn("prompt-first applies only to an actual ready-to-copy handoff", text, "prompt-first scope missing")

    def test_model_presentation_has_exact_tokens_and_evidence_safe_fallback(self):
        labels = {"LOW": "Низкое", "MEDIUM": "Среднее", "HIGH": "Высокое", "XHIGH": "Очень высокое", "MAX": "Максимальное"}
        for path in (
            PLUGIN / "shared" / "references" / "execution-profiles.md",
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md",
        ):
            text = path.read_text(encoding="utf-8")
            for syntax, reason in (
                ("<Exact Model Name>", "one short task-specific reason"),
                ("Конкретная модель не подтверждена", "one short uncertainty explanation"),
            ):
                pattern = rf"```text\s*\*\*{re.escape(syntax)} — <Exact Localized Reasoning Label>\*\*\n\n<{reason}[^>]*>\s*```"
                self.assertTrue(re.search(pattern, text), "recommendation/reason syntax changed")
            actual_labels = dict(re.findall(r"(?m)^\| (LOW|MEDIUM|HIGH|XHIGH|MAX) \| ([^|]+?) \|$", text))
            self.assertEqual(labels, actual_labels)
            for semantic, pattern in {
                "localized exact token": r"(?i)labels.*?exact localized tokens.*?not free-form prose",
                "no decorated reasoning": r"(?i)no synonyms.*?English/internal duplicate.*?parenthetical level.*?explanation on the recommendation line",
                "prompt first, guidance outside": r"(?i)immediately after.*?copy-ready prompt.*?outside the durable.*?handoff body",
                "explanations do not trigger advice": r"(?i)explanation-only response does not need model advice",
                "unknown is evidence, not installation": r"(?i)unknown.*?insufficient.*?evidence.*?not uninstalled",
                "no invented model": r"(?i)never substitute.*?capability-class pseudo-model.*?invent.*?concrete name.*?stale examples/memory",
                "non-normative syntax": r"(?i)placeholders define syntax.*?not current models or defaults",
            }.items():
                with self.subTest(path=path.name, semantic=semantic):
                    self.assertTrue(re.search(pattern, text, re.S), f"missing static presentation invariant: {semantic}")

    def test_model_reason_applies_shared_plain_language_disclosure(self):
        # Static delivery guard only; consuming-agent behavior remains a manual gate.
        requirements = {
            "existing disclosure owner": r"apply.*?Shared Core user-facing disclosure contract.*?short reason.*?related commentary",
            "practical work in user language": r"reason.*?actual task work.*?ordinary.*?user.*?language",
            "classification is not an explanation": r"internal.*?classification.*?inputs.*?not.*?user-facing explanation",
            "translate before rendering": r"translate.*?practical.*?before.*?render",
            "standalone meaning": r"remove.*?internal.*?terms.*?reason.*?understandable",
            "no parallel policy or blacklist": r"no.*?blacklist.*?language-policy subsystem",
            "user terminology remains valid": r"technical terms.*?user independently.*?useful",
        }
        for path in (
            PLUGIN / "shared" / "references" / "execution-profiles.md",
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md",
        ):
            text = path.read_text(encoding="utf-8").split("## Presentation\n", 1)[1]
            for semantic, pattern in requirements.items():
                with self.subTest(path=path.name, semantic=semantic):
                    self.assertTrue(re.search(pattern, text, re.I | re.S),
                                    f"missing model-reason delivery guard: {semantic}")

    def test_manager_onboarding_offers_optional_cloud_first_path(self):
        manager = (
            PLUGIN / "skills" / "project-bootstrap-manager" / "SKILL.md"
        ).read_text(encoding="utf-8")
        for marker in (
            "## Onboarding paths",
            "CHATGPT_CLOUD_MANAGER.md",
            "Cloud-first",
            "Codex-first",
            "not mandatory",
            "established project work",
        ):
            self.assertIn(marker, manager)

    def test_coordination_compression_has_one_shared_core_owner(self):
        control = (
            PLUGIN / "shared" / "references" / "control-model.md"
        ).read_text(encoding="utf-8")
        artifact = (
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md"
        ).read_text(encoding="utf-8")
        other_contracts = (
            PLUGIN / "skills" / "project-bootstrap-manager" / "SKILL.md",
            PLUGIN / "skills" / "project-bootstrap-master" / "SKILL.md",
            PLUGIN / "skills" / "project-bootstrap-task" / "SKILL.md",
            PLUGIN / "shared" / "references" / "cloud-manager-delivery.md",
        )
        markers = (
            "ONE OWNER → ONE EVIDENCE PACKET → ONE REVIEW",
            "NO NEW EVIDENCE → NO NEW HANDOFF",
            "CORRECTNESS > COORDINATION COMPRESSION",
            "CAPABILITY AVAILABLE ≠ CAPABILITY MUST CONTROL THE WORKFLOW",
        )
        for marker in markers:
            with self.subTest(marker=marker):
                self.assertEqual(1, control.count(marker))
                self.assertEqual(1, artifact.count(marker))
                for path in other_contracts:
                    self.assertNotIn(marker, path.read_text(encoding="utf-8"))

    def test_external_capabilities_do_not_take_parallel_orchestration_ownership(self):
        control = (
            PLUGIN / "shared" / "references" / "control-model.md"
        ).read_text(encoding="utf-8")
        artifact = (
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md"
        ).read_text(encoding="utf-8")
        master = (
            PLUGIN / "skills" / "project-bootstrap-master" / "SKILL.md"
        ).read_text(encoding="utf-8")
        markers = (
            "CAPABILITY AVAILABLE ≠ CAPABILITY MUST BE USED",
            "SKILL APPLICABLE ≠ SKILL OWNS WORKFLOW",
            "METHODOLOGY AVAILABLE ≠ FULL METHODOLOGY REQUIRED",
            "ONE ORCHESTRATION OWNER AT A TIME",
        )
        for marker in markers:
            with self.subTest(marker=marker):
                self.assertEqual(1, control.count(marker))
                self.assertEqual(1, artifact.count(marker))

        decision_order = (
            "USER INTENT",
            "COMPLEXITY / RISK / DURABILITY",
            "SMALLEST SUFFICIENT WORKFLOW",
            "AVAILABLE CAPABILITIES",
            "SELECT BOUNDED SPECIALIST OR EXTERNAL WORKFLOW",
        )
        for item in decision_order:
            self.assertIn(item, control)
        positions = [control.index(item) for item in decision_order]
        self.assertEqual(sorted(positions), positions)
        for phrase in (
            "one bounded stage",
            "reuse existing specification, plan, task, verification",
            "return orchestration to Project Bootstrap",
            "explicitly asks another lifecycle system to own the entire",
        ):
            self.assertIn(phrase, control)
        self.assertIn("bounded specialist capability", master)
        self.assertIn("reuse existing", master.lower())

    def test_bounded_external_stage_checks_prerequisites_and_user_gates(self):
        control = (PLUGIN / "shared" / "references" / "control-model.md").read_text(
            encoding="utf-8"
        )
        master = (PLUGIN / "skills" / "project-bootstrap-master" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("CAPABILITY SELECTED ≠ STAGE IS EXECUTABLE", control)
        self.assertRegex(control, r"(?is)before invoking.*?prerequisites.*?when practical")
        self.assertRegex(control, r"(?is)do not.*?predictably unusable.*?prerequisite failure")
        self.assertIn("current project state", control)
        self.assertIn("Reuse a valid prerequisite artifact", control)
        self.assertIn("substantive prerequisite stage", control)
        self.assertIn("must not insert a user approval gate merely", control)
        self.assertIn("Accepted architecture and external artifacts remain usable", control)
        self.assertRegex(master, r"(?is)before invoking.*?verify that the stage can run")
        self.assertIn("unnecessary external approval gate", master)
        self.assertNotIn("Spec Kit", control)
        self.assertNotIn("Superpowers", control)

    def test_role_is_not_chat_or_mandatory_new_session(self):
        control = (PLUGIN / "shared" / "references" / "control-model.md").read_text(
            encoding="utf-8"
        )
        manager = (PLUGIN / "skills" / "project-bootstrap-manager" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        master = (PLUGIN / "skills" / "project-bootstrap-master" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        for marker in ("ROLE ≠ CHAT", "TASK ROLE ≠ NEW SESSION REQUIRED"):
            self.assertEqual(1, control.count(marker))
        self.assertIn("known from the current context or durable evidence", control)
        self.assertIn("do not invent an unknown context", control)
        self.assertIn("physical execution topology only when", control)
        self.assertIn("rather than asking the user to label a chat", manager)
        self.assertIn("Reuse a known suitable execution context", master)
        self.assertNotIn("TASK ≠ SUBAGENT", control)

    def test_normal_task_result_is_not_durable_handoff_terminology(self):
        task = (
            PLUGIN / "skills" / "project-bootstrap-task" / "SKILL.md"
        ).read_text(encoding="utf-8")
        master = (
            PLUGIN / "skills" / "project-bootstrap-master" / "SKILL.md"
        ).read_text(encoding="utf-8")
        recovery = (
            PLUGIN / "shared" / "references" / "recovery-and-continuity.md"
        ).read_text(encoding="utf-8")
        handoff = (
            PLUGIN / "shared" / "templates" / "task-handoff.md"
        ).read_text(encoding="utf-8")
        self.assertIn("NORMAL TASK RESULT ≠ DURABLE HANDOFF", recovery)
        self.assertNotIn("hand off only after convergence", task)
        self.assertIn("return the normal Task result", task)
        self.assertIn("Task results, checkpoints, and durable handoffs", master)
        self.assertIn("Do not label a normal Task response as a Handoff", handoff)

    def test_agent_generated_terminology_is_translated_for_the_user(self):
        control = (
            PLUGIN / "shared" / "references" / "control-model.md"
        ).read_text(encoding="utf-8")
        manager = (
            PLUGIN / "skills" / "project-bootstrap-manager" / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("translate the meaning into ordinary language", control)
        self.assertIn("Do not mirror agent-generated terminology", control)
        self.assertRegex(
            control,
            r"(?is)plain-language meaning.*?practical consequence.*?source/internal terminology",
        )
        self.assertIn("understandable without Bootstrap vocabulary", control)
        self.assertIn("another agent", control)
        self.assertIn("logs or a technical report", control)
        self.assertIn("translate agent-generated terminology", manager)
        self.assertIn("internal term secondarily", manager)

    def test_primary_explanation_and_action_are_plain_before_optional_mapping(self):
        control = (PLUGIN / "shared" / "references" / "control-model.md").read_text(
            encoding="utf-8"
        )
        artifact = (PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md").read_text(
            encoding="utf-8"
        )
        for text in (control, artifact):
            with self.subTest(contract="control" if text == control else "artifact"):
                self.assertIn("SOURCE JARGON ≠ USER LANGUAGE", text)
                slots = (
                    "1. Plain meaning:",
                    "2. Plain practical action:",
                    "3. Technical mapping only if useful:",
                )
                positions = [text.index(slot) for slot in slots]
                self.assertEqual(sorted(positions), positions)
                self.assertIn("complete primary explanation and primary next action", text)
                self.assertIn("remove all Bootstrap/internal terms", text)
                self.assertIn("what happened, why work stopped, and what needs to happen next", text)
                self.assertIn("rewrite the explanation and action before adding technical mapping", text)
                self.assertIn("Do not ban technical terminology", text)
                self.assertIn("no Bootstrap internal terminology in either primary part", text, "jargon boundary missing")
                self.assertIn("short quote or term is genuinely necessary to identify the source", text, "source-identification exception missing")
                self.assertIn("whether anything is known to be lost or broken", text, "loss/uncertainty question missing")
                self.assertIn("check the actual files, inspect current Git state", text, "plain practical action missing")

    def test_current_codex_snapshot_is_established_once_before_recommendation(self):
        # Static contract guards; consuming-agent tests remain a separate runtime gate.
        for path in (
            PLUGIN / "shared" / "references" / "execution-profiles.md",
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md",
        ):
            text = path.read_text(encoding="utf-8")
            requirements = {
                "first concrete advice checks once": r"recommendation is needed.*?no applicable accepted snapshot.*?ONE bounded current Codex check",
                "current target lineup, not one model page": r"first-party OpenAI.*?Codex / Work\+Codex.*?current lineup.*?not.*?one model.*?exhaustive catalog",
                "small usable bands": r"3-5 practical.*?bands.*?concrete current model.*?default supported reasoning.*?optional.*?escalation",
                "no forced model diversity": r"three or four.*?sufficient.*?same model.*?several or all bands.*?different models",
                "user facts outrank general sources": r"sources conflict.*?actual.*?selector/list/screenshot.*?highest priority",
                "fresh target sources then generation": r"without user data.*?materially fresher target-specific.*?comparably fresh.*?newer generation.*?general snapshot",
                "supported older isn't default": r"older supported.*?not.*?default.*?available.*?older model.*?user.*?newer.*?unavailable.*?material.*?task-specific",
                "new generation isn't universally best": r"newer generation.*?not.*?best for every task.*?lineup.*?assign bands",
                "accept before advice": r"accept the snapshot BEFORE recommending.*?current task from it",
                "first advice needs no selector": r"general snapshot is usable immediately.*?no selector.*?before the first recommendation",
                "explicit mandatory invitation once": r"MUST explicitly invite.*?ONCE.*?first general snapshot.*?first usable recommendation.*?list.*?selector screenshot",
                "invite does not block": r"invitation.*?must not block.*?handoff.*?do not repeat.*?later handoffs",
                "compact commentary outside prompt": r"show.*?snapshot once.*?commentary.*?prompt.*?recommendation.*?short reason.*?outside the durable.*?prompt",
            }
            for semantic, pattern in requirements.items():
                with self.subTest(path=path.name, semantic=semantic):
                    self.assertTrue(re.search(pattern, text, re.S | re.I), semantic)

    def test_snapshot_default_bands_stay_in_primary_lineup_unless_justified(self):
        # Static contract guard, not proof of consuming-agent runtime behavior.
        for path in (
            PLUGIN / "shared" / "references" / "execution-profiles.md",
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md",
        ):
            text = path.read_text(encoding="utf-8")
            for semantic, pattern in {
                "closed default set": r"default.*?snapshot bands.*?models from.*?primary lineup",
                "positive exception required": r"older.*?default band only.*?positive.*?reason.*?actual.*?options.*?primary option.*?unavailable.*?current.*?comparative.*?prefer",
                "mere support/page is not an exception": r"existence.*?support.*?separate official page.*?not.*?exception reason",
            }.items():
                with self.subTest(path=path.name, semantic=semantic):
                    self.assertTrue(re.search(pattern, text, re.I | re.S), semantic)

    def test_known_user_availability_satisfies_selector_invitation(self):
        for path in (
            PLUGIN / "shared" / "references" / "execution-profiles.md",
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md",
        ):
            text = path.read_text(encoding="utf-8")
            for semantic, pattern in {
                "known availability satisfies invitation": r"user-specific.*?availability.*?already known.*?invitation.*?satisfied.*?list.*?screenshot.*?actual.*?set",
                "personalize and reuse without asking again": r"create or refine.*?personal snapshot.*?reuse.*?later handoffs.*?do not.*?invite.*?list.*?screenshot again",
                "only availability invalidation permits another request": r"request again only after\s+concrete availability invalidation.*?changed selector.*?added/removed models.*?explicit.*?refresh",
                "no invitation tracking subsystem": r"no separate.*?state machine.*?state file",
            }.items():
                with self.subTest(path=path.name, semantic=semantic):
                    self.assertTrue(re.search(pattern, text, re.I | re.S), semantic)

    def test_model_short_reason_localizes_level_explanation_not_english_reasoning(self):
        for path in (
            PLUGIN / "shared" / "references" / "execution-profiles.md",
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md",
        ):
            text = path.read_text(encoding="utf-8").split("## Presentation\n", 1)[1]
            for semantic, pattern in {
                "localized short reason level explanation": r"non-English.*?short reason.*?localize.*?level.*?do not use.*?English.*?`reasoning`.*?explanation",
                "narrow rule, not general blacklist": r"narrow.*?model-reason.*?rendering rule.*?not.*?general.*?blacklist",
            }.items():
                with self.subTest(path=path.name, semantic=semantic):
                    self.assertTrue(re.search(pattern, text, re.I | re.S), semantic)

    def test_later_handoffs_use_snapshot_bands_until_concrete_invalidation(self):
        for path in (
            PLUGIN / "shared" / "references" / "execution-profiles.md",
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md",
        ):
            text = path.read_text(encoding="utf-8")
            requirements = {
                "classify then consume band": r"CLASSIFY TASK.*?ACCEPTED BAND.*?USE ITS MODEL.*?SUFFICIENT SUPPORTED REASONING.*?RECOMMEND",
                "no repeat research or re-selection": r"do not.*?model research.*?documentation.*?compare models.*?general model knowledge.*?fresh external.*?facts",
                "task reason derives from band": r"reason.*?task.*?accepted band",
                "specific invalidation only": r"refresh only.*?concrete invalidation.*?unavailable model.*?list.*?screenshot.*?new models.*?explicit refresh.*?destination.*?concrete.*?non-applicability",
                "task/time alone aren't invalidation": r"another handoff.*?difficulty change.*?new message.*?elapsed time.*?hypothetical.*?not invalidation.*?No TTL.*?polling.*?per-handoff research",
            }
            for semantic, pattern in requirements.items():
                with self.subTest(path=path.name, semantic=semantic):
                    self.assertTrue(re.search(pattern, text, re.S | re.I), semantic)

    def test_snapshot_overrides_opt_out_and_last_resort_fallback_remain(self):
        for path in (
            PLUGIN / "shared" / "references" / "execution-profiles.md",
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md",
        ):
            text = path.read_text(encoding="utf-8")
            requirements = {
                "advice without magic words": r"ready-to-copy Codex handoff.*?unless.*?opted out.*?no explicit model question",
                "reuse available context": r"conversation.*?ChatGPT Project.*?durable.*?runtime.*?without.*?repeat",
                "personal options replace general": r"user.*?list.*?screenshot.*?refine or replace.*?general snapshot.*?only.*?actually available.*?personal snapshot",
                "single-model override": r"only one model.*?usable bands.*?reasoning independently",
                "opt-out preserves handoff": r"suppress model advice until.*?reverses.*?handoffs continue",
                "fallback only after failed check and clarification": r"unknown-model fallback only when.*?recommendation.*?no accepted snapshot.*?ONE bounded check failed.*?usable.*?small useful clarification cannot resolve.*?invention",
                "unknown selector alone never fallback": r"last resort.*?not.*?unknown exact selector",
            }
            for semantic, pattern in requirements.items():
                with self.subTest(path=path.name, semantic=semantic):
                    self.assertTrue(re.search(pattern, text, re.S | re.I), semantic)
        manager = (PLUGIN / "skills" / "project-bootstrap-manager" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("omit recommendation and reason, not the handoff", manager)

    def test_current_codex_snapshot_policy_does_not_freeze_a_catalog(self):
        profile = (PLUGIN / "shared" / "references" / "execution-profiles.md").read_text(encoding="utf-8")
        self.assertNotRegex(profile, r"https?://|(?i:\bGPT-[\dX-Z]|\b(?:Plus|Pro|Business|Enterprise)\b)")
        self.assertNotRegex(profile, r"(?i)\bgeneration\s+\d")
        self.assertRegex(profile, r"(?is)no permanent model names.*?rankings.*?URLs.*?plan names.*?registry.*?mandatory.*?file")

    def test_cloud_local_mutable_workspace_routes_to_codex_by_default(self):
        cloud = (
            PLUGIN / "shared" / "references" / "cloud-manager-delivery.md"
        ).read_text(encoding="utf-8")
        artifact = (
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md"
        ).read_text(encoding="utf-8")
        for text in (cloud, artifact):
            self.assertIn("Cloud Manager → Codex", text)
            self.assertIn("exact required workspace", text)
            self.assertIn("Do not suggest ChatGPT Work as an exploratory intermediate hop", text)
            self.assertIn("direct Cloud → Codex", text)

    def test_copy_ready_prompt_uses_plain_fenced_text_presentation(self):
        manager = (
            PLUGIN / "skills" / "project-bootstrap-manager" / "SKILL.md"
        ).read_text(encoding="utf-8")
        artifact = (
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md"
        ).read_text(encoding="utf-8")
        for text in (manager, artifact):
            section = text.split("Codex handoff presentation", 1)[1]
            section = section.split("\n## ", 1)[0]
            self.assertIn("plain fenced `text` block", section)
            self.assertIn("```text", section)
            self.assertIn("writing blocks", section)
            self.assertIn("durable documents", section)
            self.assertIn("first visible content", section)

    def test_new_project_discovery_is_incremental_before_solutioning(self):
        control = (
            PLUGIN / "shared" / "references" / "control-model.md"
        ).read_text(encoding="utf-8")
        manager = (
            PLUGIN / "skills" / "project-bootstrap-manager" / "SKILL.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "most important unknown about the desired outcome",
            "Usually ask one primary question at a time",
            "small tightly coupled group",
            "architecture, stack, tooling, repository layout, or release process",
        ):
            self.assertIn(phrase, control)
        self.assertIn("incremental discovery", manager)
        self.assertIn("premature implementation choices", manager)
        self.assertIn("Across new, portable, and migration work", control)
        self.assertIn("determining facts are known or the choice is already accepted", control)
        self.assertIn("“portable” alone does not determine", control)

    def test_participation_question_is_about_project_development(self):
        manager = (PLUGIN / "skills" / "project-bootstrap-manager" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("decisions about developing the project", manager)
        self.assertIn("not in using the future product", manager)
        for option in ("Совместно", "По ключевым решениям", "Делегированно"):
            self.assertIn(option, manager)

    def test_quick_start_project_instructions_match_canonical_and_generated(self):
        paths = (
            PLUGIN / "shared/references/cloud-manager-delivery.md",
            PLUGIN / "docs/QUICK_START_RU.md",
            PLUGIN / "docs/CHATGPT_CLOUD_MANAGER.md",
        )
        blocks = []
        for path in paths:
            text = path.read_text(encoding="utf-8")
            section = re.search(r"(?ms)^#{2,4} (?:Готовый блок )?Project Instructions\s*\n(.*?)(?=^#{1,4} |\Z)", text)
            self.assertIsNotNone(section, f"copyable Project Instructions missing in {path.name}")
            fenced = re.findall(r"(?ms)^```text\n(.*?)^```", section.group(1))
            self.assertEqual(1, len(fenced), f"one complete activation block required in {path.name}")
            blocks.append(fenced[0].strip())
        self.assertEqual(blocks[0], blocks[1], "Quick Start activation instructions drifted from their source")
        self.assertEqual(blocks[0], blocks[2], "generated activation instructions drifted from their source")

    def test_cloud_artifact_supports_chat_attachment_and_project_source(self):
        cloud = (
            PLUGIN / "shared" / "references" / "cloud-manager-delivery.md"
        ).read_text(encoding="utf-8")
        artifact = (
            PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md"
        ).read_text(encoding="utf-8")
        for text in (cloud, artifact):
            self.assertRegex(text, r"(?m)^#{3,4} Вариант 1 .* обычному чату$")
            self.assertRegex(text, r"(?m)^#{3,4} Вариант 2 .* ChatGPT Project$")
        setup = cloud.split("## Подключение к ChatGPT", 1)[1].split("## Project Instructions", 1)[0]
        self.assertIn("для одного разговора", setup)
        self.assertIn("для долгой работы в нескольких чатах", setup)
        self.assertIn("Настройки Project Instructions для этого варианта не нужны", setup)

    def test_task_results_are_required_while_durable_artifacts_remain_lazy(self):
        task = (
            PLUGIN / "skills" / "project-bootstrap-task" / "SKILL.md"
        ).read_text(encoding="utf-8")
        recovery = (
            PLUGIN / "shared" / "references" / "recovery-and-continuity.md"
        ).read_text(encoding="utf-8")
        handoff = (
            PLUGIN / "shared" / "templates" / "task-handoff.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Every separate Task returns a usable result", task)
        self.assertIn("PASS, FAIL, NOT TESTED, OPEN, or BLOCKED", task)
        self.assertIn("normal Task result is evidence for Master Review", recovery)
        self.assertIn("does not require a durable Handoff artifact", recovery)
        self.assertIn("For short work, return the result in the normal response", handoff)
        self.assertIn("durable completed cross-role result", handoff)

    def test_master_review_compresses_coordination_without_hiding_misses(self):
        master = (
            PLUGIN / "skills" / "project-bootstrap-master" / "SKILL.md"
        ).read_text(encoding="utf-8")
        for marker in (
            "review the complete available result",
            "one consolidated correction request",
            "review miss",
            "Correct the gap rather than leaving the project incorrect",
            "current access",
            "existing authority",
            "safe and trivial",
            "does not require implementation or correction",
            "one-active-writer boundary",
            "directly observable",
            "cheaper and clearer",
        ):
            self.assertIn(marker, master)

    def test_user_expertise_requires_user_attributed_evidence(self):
        control = (
            PLUGIN / "shared" / "references" / "control-model.md"
        ).read_text(encoding="utf-8")
        evidence = (
            PLUGIN / "shared" / "references" / "evidence-and-authority.md"
        ).read_text(encoding="utf-8")
        manager = (
            PLUGIN / "skills" / "project-bootstrap-manager" / "SKILL.md"
        ).read_text(encoding="utf-8")
        marker = "AGENT-GENERATED TERMINOLOGY IS NOT EVIDENCE OF USER EXPERTISE"
        self.assertEqual(1, control.count(marker))
        self.assertIn("user-attributed or user-accepted communication preference", evidence)
        self.assertIn("unclear provenance", evidence)
        self.assertIn("asks what a term means", control)
        self.assertIn("Shared Core user-facing disclosure contract", manager)

    def test_portable_credentials_are_gated_and_reuse_accepted_strategy(self):
        environments = (
            PLUGIN
            / "shared"
            / "references"
            / "environments-git-portable-migration.md"
        ).read_text(encoding="utf-8")
        evidence = (
            PLUGIN / "shared" / "references" / "evidence-and-authority.md"
        ).read_text(encoding="utf-8")
        self.assertIn("NO PORTABILITY NEED → NO PORTABLE CREDENTIALS WORKFLOW", environments)
        self.assertIn("NO AUTHENTICATED SERVICE → NO CREDENTIAL STORAGE DISCUSSION", environments)
        self.assertIn("credential availability or placement affects the next work", environments)
        self.assertIn("still-applicable accepted credential strategy", environments)
        self.assertIn("credentials configured separately on each machine", environments)
        self.assertIn(
            "credentials stored with the portable working environment but outside Git",
            environments,
        )
        self.assertIn("Do not standardize an encrypted credential store", environments)
        self.assertIn("Do not silently collapse", environments)
        self.assertIn("Participation", environments)
        self.assertIn("Never persist credentials", evidence)

    def test_targeted_runtime_gate_records_user_accepted_pass_without_blanket_pass(self):
        testing = (ROOT / "docs" / "TESTING.md").read_text(encoding="utf-8")
        scenarios = (
            "Cloud: first-use auto-establish",
            "Cloud: reuse after auto-establish",
            "Cloud: normal engineering reuse",
            "Spec Kit: missing prerequisite",
            "Spec Kit: satisfied-prerequisite control",
        )
        targeted = testing.split("## Targeted 0.1.7 runtime regression", 1)[1]
        targeted = targeted.split("## Behavioral lifecycle", 1)[0]
        self.assertEqual(len(scenarios), len(re.findall(r"(?m)^### ", targeted)))
        for scenario in scenarios:
            with self.subTest(scenario=scenario):
                block = re.search(
                    rf"(?ms)^### {re.escape(scenario)}\s*$"
                    rf"(?P<body>.*?)(?=^### |^## |\Z)",
                    targeted,
                )
                self.assertIsNotNone(block, f"missing targeted scenario: {scenario}")
                if scenario.startswith("Cloud:"):
                    self.assertIn("Status: PASS", block.group("body"))
                    self.assertIn("user-reported", block.group("body"))
                    self.assertNotIn("READY FOR TARGETED RERUN", block.group("body"))
                else:
                    self.assertIn("Status: PASS", block.group("body"))
                    self.assertNotIn("READY FOR TARGETED RERUN", block.group("body"))
        self.assertIn("model-guidance selection/reuse/refresh behavior accepted", testing)
        self.assertIn("INVALID UX EXPECTATION", testing)
        self.assertIn("Exactly three Cloud scenarios formed the accepted runtime gate", targeted)
        self.assertIn("Model-guidance: CLOSED", targeted)
        self.assertIn("No new Cloud runtime was performed in this release task", targeted)
        self.assertIn("Run B/C only after A PASS", targeted)
        self.assertIn("preserve the visible sources", targeted)
        self.assertIn("strict known-model presentation where demonstrated", testing)
        self.assertIn("BLOCKED_BY_MISSING_INPUT is correct behavior", testing)
        self.assertIn("Historical SEO Daemon regression evidence", testing)
        self.assertIn("not that subagents are invalid", testing)
        self.assertIn("outside the user-authorized workspace", testing)
        self.assertIn("Ask before creating a harness root", testing)
        self.assertIn("PB-017-Final-SpecKit-Harness-20261003-165946-993e1d", testing)
        self.assertIn("ENVIRONMENT BLOCKER", testing)
        self.assertIn("NO behavioral evidence", testing)

    def test_task_policy_references_do_not_require_repeated_metadata(self):
        task_prompt = (
            PLUGIN / "shared" / "templates" / "master-to-task.md"
        ).read_text(encoding="utf-8")
        for marker in (
            "stable canonical policy location is sufficient",
            "revision or version only when",
            "minimum necessary excerpt",
            "task-specific deviation",
            "Do not add an empty policy metadata block",
        ):
            self.assertIn(marker, task_prompt)

    def test_execution_profile_is_current_localized_and_outside_handoff(self):
        profile = (
            PLUGIN / "shared" / "references" / "execution-profiles.md"
        ).read_text(encoding="utf-8")
        native = (
            PLUGIN / "shared" / "templates" / "manager-to-master.md"
        ).read_text(encoding="utf-8")
        fallback = (
            PLUGIN / "shared" / "templates" / "cloud-to-codex-fallback.md"
        ).read_text(encoding="utf-8")
        self.assertRegex(profile, r"(?is)accept the snapshot BEFORE recommending.*?current task from it")
        self.assertNotIn("exact current model availability is known", profile)
        self.assertIn("user's current language", profile)
        self.assertIn("Keep actual product and model names unchanged", profile)
        self.assertRegex(profile, r"(?is)model selection.*?reasoning effort.*?separate decisions")
        self.assertIn("lowest sufficient current model", profile)
        self.assertIn("independently from model choice", profile)
        reasoning = profile.split("## Reasoning effort", 1)[1].split("## Presentation", 1)[0]
        for semantic, pattern in {
            "LOW mechanical": r"LOW — mechanical reading.*?extraction.*?bounded inspection",
            "MEDIUM engineering": r"MEDIUM — ordinary implementation.*?engineering.*?local debugging.*?bounded review",
            "HIGH reconciliation": r"HIGH — architecture.*?difficult debugging.*?repository-wide review.*?recovery/reconciliation.*?conflicting evidence.*?verification",
            "exceptional escalation": r"XHIGH / MAX — exceptional escalation only.*?never routine.*?model support.*?material task justification",
            "no scoring or model-effort coupling": r"not a scoring engine.*?stronger model does not require higher effort",
        }.items():
            with self.subTest(semantic=semantic):
                self.assertTrue(re.search(pattern, reasoning, re.S), f"missing reasoning semantics: {semantic}")
        self.assertNotRegex(profile, r"(?i)\bGPT-\d")
        for template in (native, fallback):
            self.assertNotRegex(template, r"(?i)\bGPT-\d")
            self.assertNotIn("Recommended execution profile", template)

    def test_cloud_manager_language_guard_and_behavioral_status(self):
        artifact = (PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md").read_text(
            encoding="utf-8"
        )
        testing = (ROOT / "docs" / "TESTING.md").read_text(encoding="utf-8")
        self.assertIn("USER-FACING → user's language", artifact)
        self.assertIn(
            "AGENT-FACING → English by default where appropriate", artifact
        )
        self.assertIn("English canonical source text", artifact)
        for scenario in (
            "Russian onboarding",
            "Participation",
            "Russian Codex handoff presentation",
            "Native handoff",
            "Fallback handoff",
            "English Codex return interpretation",
            "Explicit user-requested language change",
        ):
            self.assertIn(scenario, testing)
        self.assertIn(
            "Cloud Manager: accepted targeted behavioral evidence retained; "
            "current Codex snapshot A/B/C PASS — user-reported; model-guidance CLOSED.",
            testing,
        )
        self.assertIn(
            "Codex Plugin runtime: accepted targeted testing completed, including "
            "both final Spec Kit prerequisite reruns; broader lifecycle incomplete.",
            testing,
        )
        self.assertIsNone(
            re.search(r"(?i)Cloud Manager behavioral\s*:\s*PASS", testing)
        )

    def test_coordination_compression_scenarios_remain_not_tested(self):
        testing = (ROOT / "docs" / "TESTING.md").read_text(encoding="utf-8")
        scenarios = (
            "Short Task result without durable Handoff",
            "Durable continuity for long work",
            "Complete result without redundant follow-up",
            "Consolidated visible gaps",
            "New evidence justifies another cycle",
            "Master review miss is corrected",
            "No avoidable repeat without new evidence",
            "Direct trivial verification",
            "Durable evidence instead of retelling",
            "Small work uses the smallest workflow",
            "User-attributed preference survives sessions",
            "Agent-generated terminology does not imply expertise",
            "Clarification lowers technical density",
            "Stable policy reference without revision metadata",
            "Revision metadata for stale-policy risk",
            "Portable credentials relevance gate",
            "Accepted credential strategy is reused",
            "Material credential change reopens the decision",
            "Russian copy-ready handoff order",
            "Model guidance stays outside the durable prompt",
            "Unknown model availability uses canonical fallback",
            "Durable policy is referenced instead of copied",
        )
        for scenario in scenarios:
            with self.subTest(scenario=scenario):
                block = re.search(
                    rf"(?ms)^### {re.escape(scenario)}\s*$"
                    rf"(?P<body>.*?)(?=^### |^## |\Z)",
                    testing,
                )
                self.assertIsNotNone(block, f"missing behavioral scenario: {scenario}")
                self.assertIn("Status: NOT TESTED", block.group("body"))

    def test_master_skill_frontmatter_and_links(self):
        self._assert_skill("project-bootstrap-master")

    def test_task_skill_frontmatter_and_links(self):
        self._assert_skill("project-bootstrap-task")

    def _assert_skill(self, name):
        path = PLUGIN / "skills" / name / "SKILL.md"
        fields, text = parse_frontmatter(path)
        self.assertEqual(name, fields.get("name"))
        description = fields.get("description", "")
        self.assertTrue(description.startswith("Use when"))
        self.assertLessEqual(len(description), 500)
        self.assertIsNone(
            re.search(r"\b(?:first|then|next|step|workflow)\b", description, re.I),
            f"{name} description looks like a workflow summary",
        )
        links = LINK.findall(text)
        self.assertGreater(len(links), 0, f"{name} must route to shared resources")
        for target in links:
            if re.match(r"^[a-z]+://", target):
                continue
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            self.assertTrue(resolved.is_file(), f"broken link in {path}: {target}")

    def test_all_shared_core_files_are_reachable_from_skills(self):
        targets = set()
        for name in SKILLS:
            skill = PLUGIN / "skills" / name / "SKILL.md"
            for target in LINK.findall(skill.read_text(encoding="utf-8")):
                if not re.match(r"^[a-z]+://", target):
                    targets.add((skill.parent / target.split("#", 1)[0]).resolve())
        critical = {
            (PLUGIN / "shared" / "references" / name).resolve()
            for name in SHARED_REFERENCES
        } | {
            (PLUGIN / "shared" / "templates" / name).resolve()
            for name in SHARED_TEMPLATES
        }
        self.assertEqual(set(), critical - targets, "orphan shared core files")

    def test_skills_only_package_has_no_desktop_only_components(self):
        forbidden_names = {".mcp.json", "mcp.json", ".app.json"}
        found = [
            str(path.relative_to(ROOT))
            for path in ROOT.rglob("*")
            if path.is_file() and path.name in forbidden_names
        ]
        self.assertEqual([], found)
        for manifest_path in (
            PLUGIN / "plugin.json",
            PLUGIN / ".codex-plugin" / "plugin.json",
        ):
            manifest = load_json(manifest_path)
            self.assertNotIn("apps", manifest)
            self.assertNotIn("mcpServers", manifest)
            self.assertNotIn("hooks", manifest)
            extension = manifest.get("extensions", {}).get("com.openai", {})
            self.assertNotIn("apps", extension)
            self.assertNotIn("mcpServers", extension)
            self.assertNotIn("hooks", extension)

    def test_repository_copy_is_free_of_placeholders_secrets_and_local_paths(self):
        placeholder = re.compile(r"\b(?:TODO|TBD)\b|\[TODO(?::[^\]]*)?\]", re.I)
        local_path = re.compile(r"(?:[A-Za-z]:\\(?:Users|Documents|Desktop)\\|/home/|/Users/)")
        findings = []
        for path in product_text_files():
            if path.suffix not in {".md", ".json"}:
                continue
            text = path.read_text(encoding="utf-8")
            for label, pattern in (
                ("placeholder", placeholder),
                ("local path", local_path),
                ("secret", SECRET),
            ):
                if pattern.search(text):
                    findings.append(f"{path.relative_to(ROOT)}: {label}")
        self.assertEqual([], findings)

    def test_publishable_text_has_no_obsolete_repository_identity(self):
        obsolete = "ryazanovgpt" + "-bit"
        findings = []
        for path in product_text_files():
            if path.suffix not in {".md", ".json"}:
                continue
            if obsolete in path.read_text(encoding="utf-8"):
                findings.append(str(path.relative_to(ROOT)))
        self.assertEqual([], findings)

    def test_public_markdown_links_resolve(self):
        findings = []
        for path in product_text_files():
            if path.suffix.lower() != ".md":
                continue
            for target in LINK.findall(path.read_text(encoding="utf-8")):
                if re.match(r"^[a-z]+://|^#", target):
                    continue
                destination = (path.parent / target.split("#", 1)[0]).resolve()
                if not destination.is_file():
                    findings.append(f"{path.relative_to(ROOT)} -> {target}")
        self.assertEqual([], findings, "broken public Markdown links")

    def test_user_entry_points_link_to_downloadable_cloud_manager(self):
        artifact = (PLUGIN / "docs" / "CHATGPT_CLOUD_MANAGER.md").resolve()
        entry_points = (
            ROOT / "README.md",
            PLUGIN / "README.md",
            PLUGIN / "docs" / "QUICK_START_RU.md",
            PLUGIN / "docs" / "USER_GUIDE_RU.md",
            ROOT / "docs" / "MARKETPLACE_INSTALL_RU.md",
        )
        missing = []
        for path in entry_points:
            destinations = {
                (path.parent / target.split("#", 1)[0]).resolve()
                for target in LINK.findall(path.read_text(encoding="utf-8"))
                if not re.match(r"^[a-z]+://|^#", target)
            }
            if artifact not in destinations:
                missing.append(str(path.relative_to(ROOT)))
        self.assertEqual([], missing, "Cloud Manager download link missing")

    def test_no_unexpected_binary_or_cache_files_in_distribution(self):
        allowed_suffixes = {".md", ".json", ".png"}
        bad = []
        for base in (ROOT / ".agents", PLUGIN, ROOT / "docs"):
            if not base.exists():
                continue
            for path in base.rglob("*"):
                if path.is_file() and path.suffix.lower() not in allowed_suffixes:
                    bad.append(str(path.relative_to(ROOT)))
                if path.name in {"__pycache__", ".pytest_cache", ".DS_Store"}:
                    bad.append(str(path.relative_to(ROOT)))
        self.assertEqual([], bad)

    def test_docs_use_exact_marketplace_values_without_claiming_behavioral_pass(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        install = (ROOT / "docs" / "MARKETPLACE_INSTALL_RU.md").read_text(
            encoding="utf-8"
        )
        testing = (ROOT / "docs" / "TESTING.md").read_text(encoding="utf-8")
        combined = "\n".join((readme, install, testing))
        self.assertIn(
            "https://github.com/gipsy-teapsy/project-bootstrap", combined
        )
        self.assertRegex(install, r"(?im)^Branch:\s*`?main`?\s*$")
        self.assertRegex(install, r"(?im)^Path:\s*(?:`<blank>`|пусто)\s*$")
        self.assertIn("Sync now", install)
        self.assertRegex(testing, r"(?i)behavioral lifecycle.*NOT TESTED")
        self.assertIsNone(re.search(r"(?i)behavioral(?: lifecycle)?\s*:\s*PASS", combined))


if __name__ == "__main__":
    unittest.main(verbosity=2)
