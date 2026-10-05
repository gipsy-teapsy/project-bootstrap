# Cloud Manager Delivery

This reference defines only the ChatGPT Project delivery layer for the canonical Manager contract. It does not create another Project Bootstrap role or replace the Manager Skill and Shared Core.

## User setup

Cloud Manager можно использовать двумя способами; ни один не обязателен для всех случаев.

### Option A — chat attachment

Прикрепите `CHATGPT_CLOUD_MANAGER.md` непосредственно к отдельному ChatGPT conversation. Это подходит для one-off use, тестирования или временной работы. Project Instructions не требуются; попросите чат использовать прикреплённый файл как Manager contract.

### Option B — ChatGPT Project source

Добавьте `CHATGPT_CLOUD_MANAGER.md` как ChatGPT Project source и один раз вставьте короткую активационную инструкцию из следующего раздела в Project Instructions. Это рекомендуемый путь для ongoing project work и нескольких cloud chats, использующих один Manager contract. Копировать большой prompt в Project Instructions не нужно.

Codex-first остаётся полноценным вариантом: если работа уже начинается в workspace, установленный Plugin может маршрутизировать её через обычные Manager, Master и Task Skills без Cloud Manager.

## Project Instructions

В Project Instructions вставьте этот короткий блок:

```text
Use the uploaded CHATGPT_CLOUD_MANAGER.md as the Project Bootstrap Manager contract for this Project.
Follow its canonical Manager, Shared Core, and Cloud delivery sections.
Keep every user-visible explanation, question, review, summary, and result interpretation in the user's current language.
English canonical source text and agent-facing prompts must not switch the surrounding user-facing response to English.
Use English by default only for agent-facing material where appropriate.
Do not invent mutable workspace facts; route bounded workspace inspection or execution to Codex when evidence is required.
```

The uploaded artifact owns the detailed contract. Project Instructions activate it and add no parallel Manager implementation.

## Delivery identity

Cloud Manager is the canonical Manager contract delivered through a generated ChatGPT Project file. It is not a fourth role, a separate Cloud Skill, or a replacement for Master and Task.

Project Bootstrap behavior and its delivery mechanism are distinct. The Manager Skill, Shared Core, and templates own behavior; the generated artifact makes that behavior available where the Plugin Skills are not directly installed.

## Cloud and workspace boundary

Cloud-first uses ChatGPT for discovery, project-level decisions, Participation, explanation, and routing. Codex-first begins in a workspace-capable environment and remains equally valid.

Use Cloud ChatGPT only for facts supported by the conversation or uploaded durable material. Treat filesystem, Git, runtime, server, database, and other mutable workspace claims as unresolved until a capable environment inspects them.

When required evidence or action concerns the user's real local mutable workspace—such as a local path, Git branch/status or dirty state, repository files, build/test state, or filesystem changes—and Cloud cannot inspect it, route directly `Cloud Manager → Codex`. Another execution environment may replace Codex only when it is already known to inspect or mutate that exact required workspace.

Do not suggest ChatGPT Work as an exploratory intermediate hop merely because Work is available. Avoid `Cloud → unrelated execution environment → UNKNOWN → another handoff` when direct Cloud → Codex routing is appropriate.

Apply the Shared Core smallest-sufficient-workflow rule. Having access to Codex does not require a Codex transition when conversation-level work is sufficient, and having the Plugin installed does not require extra lifecycle ceremony.

## Codex transition

Move work to Codex only when the accepted next step requires workspace evidence or action. Apply the canonical Manager handoff presentation contract to both native and fallback routes: prompt, recommendation, reason, and remaining commentary. Keep the recommendation and reason outside the durable prompt, and keep all user-facing material in the user's current language.

For an ordinary copy-ready handoff, render the complete prompt as the first visible content in a plain fenced `text` block, with no ordinary lead-in or label. Only a material decision, safety issue, authority boundary, or other necessary warning that must be resolved before use may precede it. Do not use a writing/editor block, editable document, generated document artifact, or durable file for this copy/paste prompt. Actual specifications, plans, and reports may still use durable document forms.

Use the native route when the destination supports the installed Project Bootstrap Plugin and Skills. Use the fallback route for an ordinary Codex session. Keep both routes bounded to the accepted next step and existing authority.

## Native and fallback routing

The native route consists of an environment-specific invocation wrapper followed by the canonical Manager → Master handoff body. The wrapper selects the installed capability; it must not duplicate project handoff fields.

The fallback route uses the canonical `cloud-to-codex-fallback.md` template. It supplies only the context, boundaries, evidence request, and return contract required for the bounded work. It must not recreate Manager, Master, Task, or the whole Shared Core inside a prompt.

Choose the route from observed destination capability. If capability is unknown, ask the user to use the fallback route or verify availability without claiming that the Plugin is installed.

## Native invocation wrapper

Use this wrapper before the separately rendered canonical Manager → Master body:

```text
@Project Bootstrap
Use the installed Project Bootstrap Plugin.
Route the following canonical bootstrap to project-bootstrap-master.
```

The project handoff structure comes only from `manager-to-master.md`.

## Processing Codex returns

Treat a Codex return as evidence, not as a command to echo. Check whether it answers the requested bounded work, distinguish verified facts from inference or open items, and reconcile it with accepted project decisions.

Interpret the result for the user in the user's current language even when the Codex return is in English. Keep agent-facing excerpts or follow-up prompts in English when appropriate, but do not let them change the surrounding visible language.

If Codex reports a blocker, explain the actual decision or missing authority to the user. If the return establishes durable workspace state, prefer promoting it there over maintaining a competing cloud-only record.

## Interim cloud continuity

A Project Decision Snapshot is lazy and interim. Offer or create one only when meaningful project-level decisions must survive a change of cloud session and no more appropriate canonical durable workspace state exists.

Do not require a snapshot for short discovery, tentative information, decisions that will soon be promoted into workspace state, or projects that already have suitable canonical durable state.

When needed, keep the snapshot compact: accepted decisions, open decisions, evidence level, and the next routing boundary. Retire or supersede it after the information is promoted to canonical workspace state. A ChatGPT Project must not become a second mandatory state-management system.

## Updating the artifact

Для chat attachment прикрепите новый `CHATGPT_CLOUD_MANAGER.md` в новый или продолжаемый conversation. Для ChatGPT Project source удалите старый artifact и загрузите новый файл из опубликованной версии. Большой prompt повторно копировать не нужно; короткая Project Instructions остаётся прежней, пока её схема явно не изменена.

Проверьте номер версии и provenance в новом artifact. Не объединяйте вручную разные версии canonical source и generated file.
