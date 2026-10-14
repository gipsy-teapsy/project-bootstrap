# Project Bootstrap

Project Bootstrap is an installable, skills-only plugin for durable project setup, coordination, and bounded execution across ChatGPT and Codex.

It separates three roles:

- **Manager** — the control plane for orientation, discovery, project architecture, environments, Git strategy, participation, and handoff into an actual workspace.
- **Master** — the workspace coordinator that reconciles durable state, routes work, reviews handoffs, and drives project-level convergence.
- **Task** — the bounded worker that implements or researches a task, verifies it, and returns evidence.

Version 0.2.1 is a plugin beta with three roles and a fourth, standalone `project-bootstrap-transfer` Skill. Manager selects presentation by purpose: fenced `text` for finalized Codex assignments, editable Writing Blocks for human-review artifacts where supported, and ordinary chat for discussion. Transfer archives accessible ChatGPT source messages in HISTORY.json and prepares English REFERENCE.md and HANDOFF.md by default, with explicit document-language overrides, preserved user communication language, provenance, separate source/extraction completeness, and explicit limitations. HISTORY remains untranslated. Optional Russian and English Cloud Context Transfer instructions provide a separate manual meaning-and-continuation path. Existing persistent project instructions, context recovery, bounded delegation, coordination and authority contracts remain intact. Cloud Manager is the canonical Manager delivered through a file, not a fourth role. The package contains no MCP server, app, OAuth flow, backend, or hooks. Historical installed-Candidate Transfer runtime evidence is READY WITH NOTES in its tested scope; it does not validate the new presentation/language behavior, prove completeness of private originals, recover unavailable attachments or redacted content, or establish all model scenarios. New model compliance, Writing Block rendering and runtime-generated Transfer language behavior are NOT TESTED. Final 0.1.7 model-guidance A/B/C remains historical accepted evidence; broader behavioral testing continues separately. Marketplace Sync is verified separately from Git publication.

## Documentation

Keep **Manager**, **Master**, and **Task** enabled in Plugin-capable environments and describe the project or task in natural language.

- [Russian quick-start guide](plugins/project-bootstrap/docs/QUICK_START_RU.md)
- [Detailed Russian user guide](plugins/project-bootstrap/docs/USER_GUIDE_RU.md)
- [Generated ChatGPT Cloud Manager artifact](plugins/project-bootstrap/docs/CHATGPT_CLOUD_MANAGER.md)
- [Transfer Skill](plugins/project-bootstrap/skills/project-bootstrap-transfer/SKILL.md)
- [Russian Cloud Context Transfer instruction](plugins/project-bootstrap/docs/CHATGPT_CONTEXT_TRANSFER_RU.md)
- [English Cloud Context Transfer instruction](plugins/project-bootstrap/docs/CHATGPT_CONTEXT_TRANSFER_EN.md)

Cloud-first one-off setup:

1. Download [CHATGPT_CLOUD_MANAGER.md](plugins/project-bootstrap/docs/CHATGPT_CLOUD_MANAGER.md).
2. Attach it to one ChatGPT conversation and ask the chat to use it as the Manager contract.

Cloud-first ongoing Project setup:

1. Create a ChatGPT Project.
2. Download [CHATGPT_CLOUD_MANAGER.md](plugins/project-bootstrap/docs/CHATGPT_CLOUD_MANAGER.md).
3. Add that file as a Project source.
4. Copy only its short activation stub into Project Instructions.
5. Start describing the project in natural language.

Do not copy the full artifact into Project Instructions. Neither Cloud method is universally mandatory: attachment suits one-off/testing work, while a Project source suits several cloud chats. For Codex-first use, keep using the installed Plugin Skills directly. When Project Bootstrap is updated, replace the uploaded artifact with the new released file.

## Install from the GitHub marketplace

Workspace admins can import the repository marketplace with:

- Source: `https://github.com/gipsy-teapsy/project-bootstrap`
- Git ref: `main`
- Path: leave blank

See [docs/MARKETPLACE_INSTALL_RU.md](docs/MARKETPLACE_INSTALL_RU.md) for the exact ChatGPT UI flow and the separate ChatGPT Project setup. After repository updates, use **Admin → Plugins → Marketplaces → Sync now** for the marketplace installation.

## Package layout

The plugin uses a portable Agent Plugins 1.0 root manifest and retains the supported `.codex-plugin/plugin.json` compatibility fallback. The repo marketplace is at `.agents/plugins/marketplace.json`.

`CHATGPT_CLOUD_MANAGER.md` contains the Manager instructions assembled from the canonical skills, shared references, and templates bundled with the plugin. The public repository ships the ready-to-use file.

## Validation

From the public repository root, install the test dependency and run the shipped package checks:

```powershell
python -m pip install -r tests/requirements.txt
python -m unittest discover -s tests -p "test_package.py" -v
```

The public tests include full validation of the portable manifest against the bundled official Agent Plugins 1.0.0 schema. They run using the files shipped in this repository. These package checks are separate from work on your own project and are not required to use the installed plugin.

Static validation cannot prove marketplace import or runtime behavior. See [docs/TESTING.md](docs/TESTING.md).

No license has been selected for this beta.
