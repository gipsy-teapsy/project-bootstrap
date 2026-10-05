# Execution Profiles

Recommend the lowest sufficient current model/profile.
Model selection and reasoning effort are separate decisions; Participation determines neither.

## Current Codex Snapshot

For advice or a ready-to-copy Codex handoff, use ONE accepted current Codex snapshot unless the user opted out.
No explicit model question is required. Reuse accepted context from the conversation, ChatGPT Project, durable context
or runtime evidence without asking the user to repeat it; no mandatory file, model registry or separate state is needed.

CHECK ONCE → BUILD SIMPLE CURRENT SNAPSHOT → CLASSIFY TASK → RECOMMEND → REUSE UNTIL INVALIDATED.

Use 3-5 practical task bands. Each contains only a concrete current model, default supported reasoning,
and optional stronger reasoning escalation when useful:

- MECHANICAL — reading, extraction, very small deterministic inspection.
- SIMPLE / BOUNDED — optional small well-bounded change when distinct from mechanical work.
- NORMAL ENGINEERING — ordinary implementation, local debugging, tests, related files.
- COMPLEX — difficult debugging, architecture, recovery/reconciliation, conflicting evidence, broad repository analysis.
- EXCEPTIONAL — optional useful separate escalation supported by the current lineup.

Three or four bands are sufficient; the same model may cover several or all bands, and different models may cover different bands.

## Refresh

If a recommendation is needed and no applicable accepted snapshot exists, perform ONE bounded current Codex check.
Use current first-party OpenAI sources directly covering Codex / Work+Codex to see the relevant current lineup,
not one model's page or an exhaustive catalog. Determine only useful models, task fit and supported reasoning.

When official sources conflict, the user's actual Codex selector/list/screenshot has highest priority.
Without user data, prefer materially fresher target-specific Codex / Work+Codex evidence; for comparably fresh sources,
use the newer generation as the general snapshot basis. Older supported models are not wrong, but not default merely
because available. Newer generation is not best for every task:
establish the current primary lineup, then assign bands.

PRIMARY LINEUP FIRST: default general-snapshot bands use models from the established primary lineup.
An older model may enter a default band only for a positive concrete exception reason: actual user options restrict
the choice, a newer primary option is unavailable, or current evidence provides a material comparative task-specific
reason to prefer the older model for that band. Mere existence, support or a separate official page is not an exception reason.

Build and accept the snapshot BEFORE recommending the current task from it. Keep it in the available context.
The general snapshot is usable immediately: no selector is required before the first recommendation.

Use the unknown-model fallback only when a recommendation is needed, no accepted snapshot applies, ONE bounded check failed
to build a usable snapshot, a small useful clarification cannot resolve it, and a concrete name would require invention.
It is last resort, not a response merely to an unknown exact selector.

## Reuse / invalidation

While the accepted snapshot applies:
CLASSIFY TASK → ACCEPTED BAND → USE ITS MODEL → SELECT SUFFICIENT SUPPORTED REASONING → RECOMMEND.
The short reason explains the task's practical work using its accepted band internally, following Presentation below.
Do not repeat model research, inspect documentation,
compare models, select anew from general model knowledge, or justify the next recommendation using fresh external model facts.

Refresh only on concrete invalidation: an unavailable model, a user list or selector screenshot, reported new models,
an explicit refresh request, a destination change away from Codex, or other concrete evidence of non-applicability.
Another handoff, difficulty change, new message, elapsed time or hypothetical improvement is not invalidation.
No TTL, polling or per-handoff research. A report of new models triggers one bounded refresh, not invented capabilities.

The user's actual model list or screenshot may refine or replace the general snapshot: use only actually available options
in the personal snapshot thereafter. If the recommended model is unavailable, rebuild from known actual options;
ask a small clarification only if those options are missing. If told to use only one model, keep it for usable bands
and choose reasoning independently. Suppress model advice until the user reverses opt-out; normal handoffs continue.
No permanent model names, generation numbers, rankings, URLs or plan names; no registry or mandatory guidance file.

## Reasoning effort

Select effort independently from model choice. Use a supported sufficient level, not a scoring engine;
a stronger model does not require higher effort:

- LOW — mechanical reading, extraction, simple bounded inspection.
- MEDIUM — ordinary implementation, engineering, local debugging, routine bounded review.
- HIGH — architecture, difficult debugging, repository-wide review, recovery/reconciliation, conflicting evidence, difficult verification.
- XHIGH / MAX — exceptional escalation only, never routine; require model support and material task justification.

## Presentation

An explanation-only response does not need model advice. For a handoff, place advice immediately after the complete
copy-ready prompt, outside the durable Task Delta or handoff body: PROMPT → MODEL + REASONING → ONE SHORT REASON → COMMENTARY.

```text
**<Exact Model Name> — <Exact Localized Reasoning Label>**

<one short task-specific reason in the user's current language>
```

Apply the Shared Core user-facing disclosure contract to the short reason and directly related commentary.
The reason explains actual task work in the ordinary user's current language. Internal task/band classifications
and reasoning-level justification are selection inputs, not a user-facing explanation by themselves: translate
their practical meaning before rendering. If you remove internal Project Bootstrap terms, the reason must remain
understandable. Ordinary task terms and technical terms the user independently uses remain valid when useful;
no permanent word blacklist or separate language-policy subsystem is needed.

In a non-English user-facing short reason, localize the explanation of the level: do not use the English word
`reasoning` as that explanation. In Russian, use ordinary wording such as «уровень рассуждения» tied to actual task work.
This is a narrow model-reason rendering rule, not a general technical-word blacklist; internal labels remain unchanged.

Keep actual product and model names unchanged. Labels are exact localized tokens, not free-form prose:
no synonyms, English/internal duplicate, parenthetical level, or explanation on the recommendation line.

| Canonical level | Exact Russian label |
| --- | --- |
| LOW | Низкое |
| MEDIUM | Среднее |
| HIGH | Высокое |
| XHIGH | Очень высокое |
| MAX | Максимальное |

After a refresh, show the compact accepted snapshot once in commentary after the prompt, recommendation and short reason,
outside the durable Codex prompt; do not repeat it on later handoffs or turn the check into a research report.

If actual user availability is not already known, you MUST explicitly invite the user ONCE, after the first general snapshot and first usable recommendation,
to optionally provide their actual model list or Codex selector screenshot for personalization. Make this invitation
clear in the user's language; it must not block the current handoff. Do not repeat the invitation on later handoffs,
including general refreshes without availability invalidation. Their reply refines/replaces the general snapshot with actual options, then reuse it.
The invitation is mandatory only while actual availability is unknown; the user's response is optional.

If user-specific model availability is already known, the selector invitation is satisfied: a supplied list,
selector screenshot or other explicit actual model set suffices. Create or refine the personal snapshot from those options
and reuse it on later handoffs; do not invite the user to send a list or screenshot again. Request again only after
concrete availability invalidation, such as a changed selector, added/removed models or an explicit availability refresh request.
Use available conversation/context; no separate invitation state machine or state file.

For the eligible last-resort fallback:

```text
**Конкретная модель не подтверждена — <Exact Localized Reasoning Label>**

<one short uncertainty explanation in the user's current language>
```

Unknown means insufficient recommendation evidence, not uninstalled software. Never substitute a free-form
capability-class pseudo-model or invent a concrete name from stale examples/memory. Placeholders define syntax,
not current models or defaults.
