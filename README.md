# Project Bootstrap

Project Bootstrap is an installable, skills-only plugin for durable project setup, coordination, and bounded execution across ChatGPT and Codex.

It separates three roles:

- **Manager** — the control plane for orientation, discovery, project architecture, environments, Git strategy, participation, and handoff into an actual workspace.
- **Master** — the workspace coordinator that reconciles durable state, routes work, reviews handoffs, and drives project-level convergence.
- **Task** — the bounded worker that implements or researches a task, verifies it, and returns evidence.

Version 0.1.5 is a plugin beta. It preserves the 0.1.4 Manager, Master, Task, Shared Core, Cloud Manager, control-model, and workflow behavior while refining the packaged icon assets to reduce visual saturation. Cloud Manager is the canonical Manager delivered through a file, not a fourth role. The package contains no MCP server, app, OAuth flow, backend, or hooks. Cloud Manager: initial manual smoke tested; broader behavioral testing continues during beta. Marketplace Sync, Codex Plugin runtime testing, and the broader behavioral lifecycle remain separate and are not claimed as passed.

## Documentation

Keep **Manager**, **Master**, and **Task** enabled in Plugin-capable environments and describe the project or task in natural language.

- [Russian quick-start guide](plugins/project-bootstrap/docs/QUICK_START_RU.md)
- [Detailed Russian user guide](plugins/project-bootstrap/docs/USER_GUIDE_RU.md)
- [Generated ChatGPT Cloud Manager artifact](plugins/project-bootstrap/docs/CHATGPT_CLOUD_MANAGER.md)

Cloud-first setup:

1. Create a ChatGPT Project.
2. Download [CHATGPT_CLOUD_MANAGER.md](plugins/project-bootstrap/docs/CHATGPT_CLOUD_MANAGER.md).
3. Add that file as a Project source.
4. Copy only its short activation stub into Project Instructions.
5. Start describing the project in natural language.

Do not copy the full artifact into Project Instructions. For Codex-first use, keep using the installed Plugin Skills directly. When Project Bootstrap is updated, replace the uploaded artifact with the new released file.

## Install from the GitHub marketplace

Workspace admins can import the repository marketplace with:

- Source: `https://github.com/gipsy-teapsy/project-bootstrap`
- Git ref: `main`
- Path: leave blank

See [docs/MARKETPLACE_INSTALL_RU.md](docs/MARKETPLACE_INSTALL_RU.md) for the exact ChatGPT UI flow and the separate ChatGPT Project setup. After repository updates, use **Admin → Plugins → Marketplaces → Sync now** for the marketplace installation.

## Package layout

The plugin uses a portable Agent Plugins 1.0 root manifest and retains the supported `.codex-plugin/plugin.json` compatibility fallback. The repo marketplace is at `.agents/plugins/marketplace.json`.

`CHATGPT_CLOUD_MANAGER.md` is generated from the canonical Manager Skill, Shared Core, Cloud delivery reference, and handoff templates. `tools/build_cloud_manager.py` composes and validates those sources but owns no behavioral policy.

## Validation

Run:

```powershell
python tools/build_cloud_manager.py --repo . --check
python -m unittest discover -s tests -p "test_*.py" -v
python <plugin-creator>/scripts/validate_plugin.py plugins/project-bootstrap
```

Static validation cannot prove marketplace import or runtime behavior. See [docs/TESTING.md](docs/TESTING.md).

No license has been selected for this beta.
