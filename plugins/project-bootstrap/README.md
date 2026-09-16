# Project Bootstrap plugin

Project Bootstrap v0.1.0 packages three user-facing skills:

- `project-bootstrap-manager`
- `project-bootstrap-master`
- `project-bootstrap-task`

Shared references and templates live under `shared/` and are loaded progressively by the role that needs them. Shared Core is not a user-facing skill.

The root `plugin.json` is the portable Agent Plugins 1.0 manifest. `.codex-plugin/plugin.json` is the supported compatibility fallback and declares the skills path and OpenAI presentation metadata.

This beta is skills-only. It deliberately contains no MCP or app declaration, so packaging does not make it Desktop only.

Behavioral lifecycle testing has not been performed for v0.1.0.
