import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "project-bootstrap"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
SKILLS = (
    "project-bootstrap-manager",
    "project-bootstrap-master",
    "project-bootstrap-task",
)
SHARED_REFERENCES = (
    "control-model.md",
    "evidence-and-authority.md",
    "recovery-and-continuity.md",
    "environments-git-portable-migration.md",
    "execution-profiles.md",
)
SHARED_TEMPLATES = (
    "manager-to-master.md",
    "master-to-task.md",
    "task-state.md",
    "task-checkpoint.md",
    "task-handoff.md",
)
SEMVER = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


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


class PackageContractTests(unittest.TestCase):
    def test_expected_layout_exists(self):
        expected = [
            MARKETPLACE,
            PLUGIN / "plugin.json",
            PLUGIN / ".codex-plugin" / "plugin.json",
            PLUGIN / "README.md",
            PLUGIN / "CHANGELOG.md",
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
        missing = [str(path.relative_to(ROOT)) for path in expected if not path.is_file()]
        self.assertEqual([], missing, f"missing required files: {missing}")

    def test_marketplace_contract(self):
        data = load_json(MARKETPLACE)
        self.assertEqual("gipsy-project-bootstrap", data["name"])
        self.assertEqual("Project Bootstrap by Gipsy", data["interface"]["displayName"])
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
            self.assertEqual("0.1.0", manifest["version"])
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
        interface = compat["interface"]
        self.assertEqual("Project Bootstrap by Gipsy", interface["displayName"])
        self.assertEqual("Gipsy", interface["developerName"])
        self.assertEqual("Developer Tools", interface["category"])
        self.assertIsInstance(interface["capabilities"], list)
        self.assertGreater(len(interface["capabilities"]), 0)
        self.assertIsInstance(interface["defaultPrompt"], list)
        self.assertGreater(len(interface["defaultPrompt"]), 0)
        self.assertLessEqual(len(interface["defaultPrompt"]), 3)
        self.assertTrue(all(len(item) <= 128 for item in interface["defaultPrompt"]))

    def test_manager_skill_frontmatter_and_links(self):
        self._assert_skill("project-bootstrap-manager")

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
        secret = re.compile(
            r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|"
            r"\b(?:ghp|github_pat|sk-proj)-[A-Za-z0-9_-]{16,}\b"
        )
        findings = []
        for path in product_text_files():
            if path.suffix not in {".md", ".json"}:
                continue
            text = path.read_text(encoding="utf-8")
            for label, pattern in (
                ("placeholder", placeholder),
                ("local path", local_path),
                ("secret", secret),
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

    def test_no_unexpected_binary_or_cache_files_in_distribution(self):
        allowed_suffixes = {".md", ".json"}
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
