# Cloud Manager Delivery

This reference defines only the ChatGPT Project delivery layer for the canonical Manager contract. It does not create another Project Bootstrap role or replace the Manager Skill and Shared Core.

## Подключение к ChatGPT

Project Bootstrap можно подключить к ChatGPT двумя способами; выбирайте подходящий для своей работы.

### Вариант 1 — прикрепить файл к обычному чату

Прикрепите `CHATGPT_CLOUD_MANAGER.md` к отдельному чату ChatGPT. Это подходит для одного разговора, тестирования или временной работы. Попросите ChatGPT использовать файл как инструкции Project Bootstrap для управления проектом. Настройки Project Instructions для этого варианта не нужны.

### Вариант 2 — добавить файл в ChatGPT Project

Добавьте `CHATGPT_CLOUD_MANAGER.md` в источники проекта ChatGPT и один раз вставьте короткую инструкцию из следующего раздела в Project Instructions. Этот вариант удобен для долгой работы в нескольких чатах одного проекта. Весь большой файл в поле инструкций копировать не нужно.

Можно начать и прямо в Codex: если Project Bootstrap уже установлен и открыт рабочий проект, опишите цель обычными словами. Файл для ChatGPT в этом случае не требуется; подходящая роль выбирается автоматически.

## Project Instructions

Скопируйте этот блок в Project Instructions вашего ChatGPT Project:

```text
Use the uploaded CHATGPT_CLOUD_MANAGER.md as the Project Bootstrap Manager contract for this Project.
Follow its canonical Manager, Shared Core, and Cloud delivery sections.
Keep every user-visible explanation, question, review, summary, and result interpretation in the user's current language.
English canonical source text and agent-facing prompts must not switch the surrounding user-facing response to English.
Use English by default only for agent-facing material where appropriate.
Do not invent mutable workspace facts; route bounded workspace inspection or execution to Codex when evidence is required.
```

Подробные правила находятся в загруженном файле. Короткая инструкция просит ChatGPT следовать им; создавать отдельный набор правил не нужно.

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

For a native transition with concrete next work already accepted, include the optional CURRENT ACCEPTED WORK block defined only in `manager-to-master.md`. Preserve the accepted outcome, scope, exclusions, authority, and expected result; narrower work-specific restrictions take precedence over broader project defaults. Workspace reconciliation may adapt the execution method, for example when a referenced file has been renamed, but it does not authorize a different outcome, a scope expansion, or a repair after read-only inspection was agreed. If a material change is necessary, report it and resolve that decision before changing the accepted work.

If no concrete next work is accepted, omit that block and use the ordinary project bootstrap: Master inspects the actual workspace and determines the smallest necessary next work within existing authority. Do not invent a Task merely to populate the bootstrap.

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

## Обновление файла

Если вы прикрепляли файл к обычному чату, прикрепите новый `CHATGPT_CLOUD_MANAGER.md` к новому или продолжаемому разговору. Если используете ChatGPT Project, удалите старый файл из источников и загрузите новый из опубликованной версии Project Bootstrap.

Весь файл повторно копировать в настройки не нужно. Короткая инструкция в Project Instructions остаётся прежней, если её текст в новой версии не изменился.

Проверьте номер версии в новом файле и сведения о том, из каких исходных инструкций он собран. Не объединяйте вручную исходные инструкции и готовый файл из разных версий.
