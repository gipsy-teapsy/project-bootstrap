# Project Bootstrap plugin

Project Bootstrap v0.1.2 packages three user-facing skills:

- `project-bootstrap-manager`
- `project-bootstrap-master`
- `project-bootstrap-task`

## Start here

Keep all three components enabled. Describe the project, problem, or next action in natural language; Project Bootstrap routes the request to the appropriate role.

- [Быстрый старт](docs/QUICK_START_RU.md) — a concise installation-to-first-use guide.
- [Подробное руководство пользователя](docs/USER_GUIDE_RU.md) — detailed roles, continuity, recovery, Git, authority, portability, migration, and verification guidance.

Shared references and templates live under `shared/` and are loaded progressively by the role that needs them. Shared Core is not a user-facing skill.

The root `plugin.json` is the portable Agent Plugins 1.0 manifest. `.codex-plugin/plugin.json` is the supported compatibility fallback and declares the skills path and OpenAI presentation metadata.

This beta is skills-only. It deliberately contains no MCP or app declaration, so packaging does not make it Desktop only.

Behavioral lifecycle testing has not been performed for v0.1.2.
