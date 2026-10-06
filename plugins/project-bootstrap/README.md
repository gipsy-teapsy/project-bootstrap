# Project Bootstrap plugin

Project Bootstrap v0.1.8 packages three user-facing skills:

- `project-bootstrap-manager`
- `project-bootstrap-master`
- `project-bootstrap-task`

Cloud Manager is not a fourth skill. It is the canonical Manager contract rendered into [CHATGPT_CLOUD_MANAGER.md](docs/CHATGPT_CLOUD_MANAGER.md) for delivery through a ChatGPT Project.

## Start here

In a Plugin-capable environment, keep all three components enabled. Describe the project, problem, or next action in natural language; Project Bootstrap routes the request to the appropriate role.

For one-off Cloud-first use, download [CHATGPT_CLOUD_MANAGER.md](docs/CHATGPT_CLOUD_MANAGER.md), attach it to one ChatGPT conversation, and ask the chat to use it as the Manager contract.

For ongoing use in a ChatGPT Project:

1. Create a ChatGPT Project.
2. Download [CHATGPT_CLOUD_MANAGER.md](docs/CHATGPT_CLOUD_MANAGER.md).
3. Add it as a Project source.
4. Copy only its short activation stub into Project Instructions.
5. Start describing the project in natural language.

Do not copy the full artifact into Project Instructions. Chat attachment is intended for one-off/testing work; Project source is intended for several cloud chats. Neither is mandatory. For Codex-first use, start directly with the installed Plugin. Updating a Cloud Project requires replacing the uploaded artifact.

- [Быстрый старт](docs/QUICK_START_RU.md) — installation-to-first-use guidance for both paths.
- [Подробное руководство пользователя](docs/USER_GUIDE_RU.md) — roles, Cloud/Codex handoff, continuity, recovery, Git, authority, portability, migration, and verification.
- [Cloud Manager artifact](docs/CHATGPT_CLOUD_MANAGER.md) — generated upload for a ChatGPT Project.

Shared references and templates live under `shared/` and are loaded progressively by the role that needs them. Shared Core is not a user-facing skill. Cloud-specific behavior lives in a canonical reference; the generated artifact remains traceable to all of its Markdown inputs.

The root `plugin.json` is the portable Agent Plugins 1.0 manifest; OpenAI presentation metadata lives under `extensions.com.openai.interface`. `.codex-plugin/plugin.json` is the supported compatibility fallback and declares the skills path and OpenAI presentation metadata.

This beta is skills-only. It deliberately contains no MCP or app declaration, so packaging does not make it Desktop only.

Cloud Manager: initial manual smoke tested; final 0.1.7 model-guidance A/B/C passed in user-reported fresh Cloud runtime. Model-guidance is closed; broader behavioral testing continues separately during beta. Marketplace Sync is verified separately from Git publication.

The public GitHub repository provides the plugin package and installation catalog. After installation, open your own working project in Codex; the guides above explain how to start.
