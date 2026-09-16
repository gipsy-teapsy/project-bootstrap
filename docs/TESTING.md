# Testing

Testing is divided into three layers.

## Package and static validation

`tests/test_package.py` checks JSON parsing and required shape, strict semver, name/path consistency, all three Skill frontmatters, relative links, shared-resource reachability, forbidden MCP/app declarations, placeholders, common secret/local-path patterns, unexpected binaries, installation documentation, and honest test-status wording.

Run:

```powershell
python -m unittest tests.test_package -v
```

The built-in OpenAI plugin validator checks the compatibility manifest and bundled skills:

```powershell
python <plugin-creator>/scripts/validate_plugin.py plugins/project-bootstrap
```

These checks are necessary but do not prove runtime behavior.

## Marketplace smoke

Import the GitHub marketplace in ChatGPT, inspect the import report, install Project Bootstrap, start a new Chat or Work conversation, and verify that all three skills are discoverable. Then request **Sync now** after a repository update and inspect the saved report.

ChatGPT marketplace import: NOT TESTED

Cloud Manager: NOT TESTED

Codex plugin use: NOT TESTED

## Behavioral lifecycle

Behavioral lifecycle: NOT TESTED

Future behavioral tests should cover Manager orientation and discovery, Participation differences, Manager-to-Master handoff, Master reconciliation and routing, Task defect/verification/convergence behavior, interruption recovery, cross-task consultation, and anti-bloat negative cases. A static PASS must never be reported as a behavioral PASS.
