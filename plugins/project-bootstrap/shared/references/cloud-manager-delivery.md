# Cloud Manager Delivery

This reference defines only the ChatGPT Project delivery layer for the canonical Manager contract. It does not create another Project Bootstrap role or replace the Manager Skill and Shared Core.

## User setup

Для Cloud-first работы создайте ChatGPT Project и загрузите в него только сгенерированный файл `CHATGPT_CLOUD_MANAGER.md`. Вставьте короткую активационную инструкцию из следующего раздела в Project Instructions. После этого начинайте обычным запросом на своём языке; копировать большой prompt вручную не нужно.

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

Capability available != capability must control the workflow. Having access to Codex does not require a Codex transition when conversation-level work is sufficient, and having the Plugin installed does not require extra lifecycle ceremony.

## Codex transition

Move work to Codex only when the accepted next step requires workspace evidence or action. Before the transition, explain to the user what Codex will do, why it is needed, which execution profile is appropriate, what prompt to copy, and what result should return.

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

При обновлении Project Bootstrap удалите старый `CHATGPT_CLOUD_MANAGER.md` из ChatGPT Project и загрузите новый файл из опубликованной версии. Большой prompt повторно копировать не нужно; короткая Project Instructions остаётся прежней, пока её схема явно не изменена.

Проверьте номер версии и provenance в новом artifact. Не объединяйте вручную разные версии canonical source и generated file.
