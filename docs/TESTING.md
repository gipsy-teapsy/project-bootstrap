# Testing

Testing is divided into static/package checks and real runtime behavior. A static PASS must never be reported as a behavioral PASS.

## Package and static validation

`tests/test_package.py` checks JSON parsing and required shape, strict semver, name/path consistency, all three Skill frontmatters, relative links, shared-resource reachability, forbidden MCP/app declarations, language-contract markers, placeholders, common secret/local-path patterns, unexpected binaries, installation documentation, and honest test-status wording.

`tests/test_cloud_manager_builder.py` executes the generator against real fixture repositories. It checks deterministic output, declared source provenance, mechanical template derivation, stale-artifact detection, commit-only validation, manifest-version convergence, native wrapper/body separation, and the absence of Cloud behavioral policy in Python literals.

Run:

```powershell
python tools/build_cloud_manager.py --repo . --check
python -m unittest discover -s tests -p "test_*.py" -v
```

The built-in OpenAI plugin validator checks the compatibility manifest and bundled skills:

```powershell
python <plugin-creator>/scripts/validate_plugin.py plugins/project-bootstrap
```

These checks are necessary but do not prove runtime behavior.

## Marketplace smoke

Import the GitHub marketplace in ChatGPT, inspect the import report, install Project Bootstrap, start a new Chat or Work conversation, and verify that all three skills are discoverable. Then request **Sync now** after a repository update and inspect the saved report.

ChatGPT marketplace import: NOT TESTED

Cloud Manager: initial manual smoke tested; broader behavioral testing continues during beta.

Codex plugin use: NOT TESTED

## Cloud Manager behavioral scenarios

Initial real Cloud smoke testing has been accepted for this beta. The broader documented suite below continues separately: execute each scenario in a real ChatGPT Project containing the released `CHATGPT_CLOUD_MANAGER.md`, record the actual prompts, visible responses, selected route, returned evidence, and version, and keep each scenario marked NOT TESTED until that evidence exists.

### Russian onboarding

Start in Russian with: «Хочу создать новый проект для разработки сайта». Verify that all visible orientation and discovery stay in Russian, use natural terminology, and ask only decision-relevant questions.

Status: NOT TESTED

### Participation

During Russian discovery, reach the Participation choice. Verify that Совместно, По ключевым решениям, and Делегированно are all explained naturally, with a recommendation but without changing authority or safety boundaries.

Status: NOT TESTED

### Native handoff

Use a destination where the installed Project Bootstrap Plugin/Skills are actually available. Verify that the handoff contains the Cloud-specific invocation wrapper followed by the canonical Manager → Master body and does not duplicate its field structure.

Status: NOT TESTED

### Fallback handoff

Use an ordinary Codex session without Project Bootstrap Plugin/Skills. Verify that the prompt is bounded, includes only required accepted context/evidence/authority, and does not recreate Manager, Master, Task, or Shared Core.

Status: NOT TESTED

### English Codex return interpretation

Return a valid Codex report written in English to the Russian Cloud conversation. Verify that the user-facing interpretation remains Russian while any necessary agent-facing follow-up may remain English.

Status: NOT TESTED

### Explicit user-requested language change

In a Russian conversation, explicitly ask to continue in English. Verify that visible communication switches to English because of the user request, not because the uploaded artifact or an agent-facing prompt is English.

Status: NOT TESTED

## Behavioral lifecycle

Behavioral lifecycle: NOT TESTED

Future broader tests should cover Manager orientation and discovery, Manager-to-Master handoff, Master reconciliation and routing, Task defect/verification/convergence behavior, interruption recovery, cross-task consultation, and anti-bloat negative cases.
