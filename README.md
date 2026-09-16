# Project Bootstrap

Project Bootstrap is an installable, skills-only plugin for durable project setup, coordination, and bounded execution across ChatGPT and Codex.

It separates three roles:

- **Manager** — the control plane for orientation, discovery, project architecture, environments, Git strategy, participation, and handoff into an actual workspace.
- **Master** — the workspace coordinator that reconciles durable state, routes work, reviews handoffs, and drives project-level convergence.
- **Task** — the bounded worker that implements or researches a task, verifies it, and returns evidence.

Version 0.1.2 is a plugin beta. It packages the corrected beta.3 control model into three discoverable skills plus a shared core. It contains no MCP server, app, OAuth flow, backend, or hooks. Cloud Manager availability is a core goal; live marketplace, cloud, Codex, and behavioral lifecycle testing is still pending.

## Documentation

Keep **Manager**, **Master**, and **Task** enabled and describe the project or task in natural language. Start with the [Russian quick-start guide](plugins/project-bootstrap/docs/QUICK_START_RU.md), or use the [detailed Russian user guide](plugins/project-bootstrap/docs/USER_GUIDE_RU.md) for roles, continuity, recovery, Git, authority, portability, migration, and verification.

## Install from the GitHub marketplace

Workspace admins can import the repository marketplace with:

- Source: `https://github.com/gipsy-teapsy/project-bootstrap`
- Git ref: `main`
- Path: leave blank

See [docs/MARKETPLACE_INSTALL_RU.md](docs/MARKETPLACE_INSTALL_RU.md) for the exact ChatGPT UI flow. After repository updates, use **Admin → Plugins → Marketplaces → Sync now**.

## Package layout

The plugin uses a portable Agent Plugins 1.0 root manifest and retains the supported `.codex-plugin/plugin.json` compatibility fallback. The repo marketplace is at `.agents/plugins/marketplace.json`.

## Validation

Run:

```powershell
python -m unittest tests.test_package -v
python <plugin-creator>/scripts/validate_plugin.py plugins/project-bootstrap
```

Static validation cannot prove marketplace import or runtime behavior. See [docs/TESTING.md](docs/TESTING.md).

No license has been selected for this beta.
