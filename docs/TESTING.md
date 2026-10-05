# Testing

Testing is divided into static/package checks and real runtime behavior. A static PASS must never be reported as a behavioral PASS.

## Package and static validation

`tests/test_package.py` checks JSON parsing and required shape, strict semver, name/path consistency, all three Skill frontmatters, relative links, shared-resource reachability, forbidden MCP/app declarations, language-contract markers, placeholders, common secret/local-path patterns, unexpected binaries, installation documentation, and honest test-status wording.

`tests/test_cloud_manager_builder.py` executes the generator against real fixture repositories. It checks deterministic output, declared source provenance, mechanical template derivation, stale-artifact detection, commit-only validation, manifest-version convergence, native wrapper/body separation, and the absence of Cloud behavioral policy in Python literals.

Repository text is canonical LF under `.gitattributes`; PNG assets are binary. Contributors may keep their ordinary Git `core.autocrlf` setting: the generator regression tests cover both fresh Windows-like checkouts and existing CRLF checkouts that receive the repository policy during an update.

Run:

```powershell
python tools/build_cloud_manager.py --repo . --check
python -m unittest discover -s tests -p "test_*.py" -v
```

The built-in OpenAI plugin validator checks the compatibility manifest and bundled skills:

```powershell
python <plugin-creator>/scripts/validate_plugin.py plugins/project-bootstrap
```

These checks are necessary but do not prove runtime behavior.

## Marketplace smoke

Import the GitHub marketplace in ChatGPT, inspect the import report, install Project Bootstrap, start a new Chat or Work conversation, and verify that all three skills are discoverable. Then request **Sync now** after a repository update and inspect the saved report.

ChatGPT marketplace import: NOT TESTED

Cloud Manager: accepted targeted behavioral evidence retained; current Codex snapshot A/B/C PASS — user-reported; model-guidance CLOSED.

Codex Plugin runtime: accepted targeted testing completed, including both final Spec Kit prerequisite reruns; broader lifecycle incomplete.

Cloud, Superpowers, and Spec Kit runtime passes provided evidence for the current universal workflow model. Earlier model-guidance selection/reuse/refresh behavior accepted, including strict known-model presentation where demonstrated. Historical first-use and compressed-Candidate runs retain their positive sub-evidence and failures below. The user has now accepted fresh Cloud A/B/C against the final current behavior: primary-lineup snapshot creation, B/C reuse without repeated research, plain-language reasons and correct selector invitation. This closes the model-guidance release gate, not the broader behavioral lifecycle. Do not rerun completed gates without concrete new regression evidence.

### Runtime harness authorization

Runtime harnesses must not create directories, project copies, fixtures, reports, or other writable test infrastructure outside the user-authorized workspace or scope without explicit authorization. Ask before creating a harness root outside the authorized writable scope. A previous Superpowers harness wrote outside that scope; this is a testing-infrastructure authorization lesson, not a Project Bootstrap runtime regression. The later Spec Kit harness asked before creating its out-of-workspace root, which is the required behavior.

## Cloud Manager behavioral scenarios

Initial real Cloud smoke testing has been accepted for this beta. The broader documented suite below continues separately: execute each scenario in a real ChatGPT Project containing the released `CHATGPT_CLOUD_MANAGER.md`, record the actual prompts, visible responses, selected route, returned evidence, and version, and keep each scenario marked NOT TESTED until that evidence exists.

### Russian onboarding

Start in Russian with: «Хочу создать новый проект для разработки сайта». Verify that all visible orientation and discovery stay in Russian, use natural terminology, and ask only decision-relevant questions.

Status: NOT TESTED

### Participation

During Russian discovery, reach the Participation choice. Verify that Совместно, По ключевым решениям, and Делегированно are all explained naturally, with a recommendation but without changing authority or safety boundaries.

Status: NOT TESTED

### Russian Codex handoff presentation

In a Russian conversation, request a ready-to-copy Codex handoff. Verify the strict visible order: complete Codex-facing prompt, concrete model plus localized reasoning effort, one short Russian reason, then any remaining Russian commentary. Model guidance must remain outside the durable prompt. Any material decision or warning must be resolved before the handoff is declared copy-ready.

Status: NOT TESTED

### Native handoff

Use a destination where the installed Project Bootstrap Plugin/Skills are actually available. Verify that the handoff contains the Cloud-specific invocation wrapper followed by the canonical Manager → Master body and does not duplicate its field structure.

Status: NOT TESTED

### Fallback handoff

Use an ordinary Codex session without Project Bootstrap Plugin/Skills. Verify that the prompt is bounded, includes only required accepted context/evidence/authority, and does not recreate Manager, Master, Task, or Shared Core.

Status: NOT TESTED

### English Codex return interpretation

Return a valid Codex report written in English to the Russian Cloud conversation. Verify that the user-facing interpretation remains Russian while any necessary agent-facing follow-up may remain English.

Status: NOT TESTED

### Explicit user-requested language change

In a Russian conversation, explicitly ask to continue in English. Verify that visible communication switches to English because of the user request, not because the uploaded artifact or an agent-facing prompt is English.

Status: NOT TESTED

### Short Task result without durable Handoff

Complete short bounded work and verify that Task returns one usable normal result with applicable verification and open items, without creating a durable Handoff solely because work completed.

Status: NOT TESTED

### Durable continuity for long work

Run long or interruption-prone work and verify that Task State, Checkpoint, or Handoff is created only when durable continuity is actually needed.

Status: NOT TESTED

### Complete result without redundant follow-up

Return a complete verified Task result and verify that Master accepts its available evidence without asking Task to restate the same facts.

Status: NOT TESTED

### Consolidated visible gaps

Return a result with several simultaneously visible gaps and verify that Master sends one consolidated correction request.

Status: NOT TESTED

### New evidence justifies another cycle

Reveal a genuinely new issue, blocker, or verification need after correction and verify that another cycle is allowed and tied to that new evidence.

Status: NOT TESTED

### Master review miss is corrected

Expose a gap that Master could have seen in the prior result and verify that Master identifies it as a review miss but still corrects it.

Status: NOT TESTED

### No avoidable repeat without new evidence

Provide no new evidence after a complete review and verify that Master does not create another correction or handoff cycle merely for ceremony.

Status: NOT TESTED

### Direct trivial verification

Leave one safe trivial check that Master can run with current access and authority. Verify all eligibility conditions and that Master performs it directly without taking implementation ownership.

Status: NOT TESTED

### Durable evidence instead of retelling

Put the requested facts in accessible durable evidence and verify that Master reads them rather than asking Task to summarize them again.

Status: NOT TESTED

### Small work uses the smallest workflow

Complete a small bounded change and verify that no unnecessary Task, ExecPlan, branch/worktree, Checkpoint, Handoff, design phase, or independent review is created.

Status: NOT TESTED

### User-attributed preference survives sessions

Have the user explicitly accept a communication preference, persist it in appropriate durable state, change sessions, and verify that the preference remains in effect.

Status: NOT TESTED

### Agent-generated terminology does not imply expertise

Use technical terms only in agent-generated prompts or reports and verify that subsequent user-facing explanations do not assume matching user expertise.

Status: NOT TESTED

### Clarification lowers technical density

Have the user ask what a term means or request a simpler explanation and verify that subsequent visible responses use less technical language.

Status: NOT TESTED

### Stable policy reference without revision metadata

Start a Task in one confirmed current workspace and verify that a stable canonical policy location is used without redundant revision/version metadata.

Status: NOT TESTED

### Revision metadata for stale-policy risk

Introduce cross-environment or stale-policy risk and verify that the Task prompt adds the materially useful revision/version while keeping policy by reference.

Status: NOT TESTED

### Portable credentials relevance gate

Verify that credential-storage discussion starts only when portability is relevant, an authenticated external service is required, and no applicable accepted strategy exists.

Status: NOT TESTED

### Accepted credential strategy is reused

Enter an environment that still satisfies the accepted credential strategy and verify that Project Bootstrap checks access without reopening the decision.

Status: NOT TESTED

### Material credential change reopens the decision

Introduce a new environment, service, unavailable access, portability failure, or materially changed risk/authority and verify that the credential strategy may be reconsidered.

Status: NOT TESTED

### Russian copy-ready handoff order

Verify that a Russian handoff visibly uses prompt → concrete model and localized effort → one short Russian reason → remaining Russian commentary, with nothing inserted between prompt and recommendation.

Status: NOT TESTED

### Model guidance stays outside the durable prompt

Inspect both native and fallback handoffs and verify that model/reasoning guidance is presentation metadata, not part of the durable prompt body.

Status: NOT TESTED

### Unknown model availability uses canonical fallback

Use a context where no applicable guidance exists, a bounded current Codex refresh fails to establish a reliable concrete recommendation, and material availability ambiguity cannot reasonably be resolved by useful clarification. Only then verify the canonical localized unknown-model label rather than an invented concrete model or free-form capability-class name. For Russian output use «Конкретная модель не подтверждена» and one exact localized reasoning token, followed by a short uncertainty explanation. Absence of prior guidance alone must trigger establishment, not fallback.

Status: NOT TESTED

### Durable policy is referenced instead of copied

Prepare a Task governed by accessible durable release or security policy and verify that the prompt references it plus any task delta instead of copying the full policy.

Status: NOT TESTED

## Targeted 0.1.7 runtime regression

Accepted historical evidence before the snapshot simplification:

- Cloud runtime accepted genuine-handoff prompt-first presentation, onboarding, discovery, Participation, portable discovery, and delivery architecture. Later runtime also accepted current-guidance reuse, model/reasoning independence, task-sensitive reasoning selection, no repeated research per handoff, evidence-triggered bounded reassessment, no automatic promotion of an unknown new model, reuse after refresh, and strict known-model presentation where demonstrated. These accepted behaviors are closed; they are not the remaining defect.
- The earlier five-case micro-correction plan below remains historical evidence for explanation/handoff precedence, plain-language primary instructions, and exact recommendation presentation. It does not become a new required matrix for this change. Latest runtime exposed the no-guidance branch reaching unknown fallback too early; the old immediate-fallback expectation is INVALID UX EXPECTATION, not desired behavior. Its observation remains evidence of the UX defect, not evidence that guidance bootstrap passed.
- Final Superpowers behavioral testing accepted bounded work, explicit full ownership, and absence of unnecessary approval gates.
- Combined Project Bootstrap + Spec Kit + Superpowers: behavioral PASS 5/5, with one workflow owner, no competing lifecycle, no duplicate specification package, and no unnecessary approval gate.
- An earlier Spec Kit-only attempt ended at ENVIRONMENT BLOCKER because its preflight exposed Superpowers. It produced NO behavioral evidence and is not a prerequisite PASS or FAIL.
- Valid evidence: `PB-017-Final-SpecKit-Harness-20261003-165946-993e1d`. Scenario 01: behavioral FAIL, because the missing prerequisite was discovered after stage invocation. Scenario 02: routing, artifact reuse, and valid-prerequisite path PASS; completion correctly awaited a real product answer from the user. Scenario 03: bounded specification-only stage PASS.
- Later final Spec Kit reruns, accepted by the user, supersede the prerequisite-timing failure: missing prerequisite PASS; satisfied-prerequisite routing/control PASS. The missing specification was established before invocation; no prerequisite script was run merely to obtain a predictable failure, no specification/plan/tasks/code was created, and the smallest compatible clarification path was used. With the existing specification, reuse and prerequisite checking succeeded and bounded clarification began; it stopped at a genuine unresolved product decision. BLOCKED_BY_MISSING_INPUT is correct behavior here, not a regression; full clarification completion was intentionally not performed.

These are accepted observations from reported runs, not a blanket PASS for the broader documented matrix. The environment-blocked attempt remains no evidence and the valid failed attempt remains history, not erased. Intent/plain-language/presentation, opt-out and last-resort behavior remain. Do not upgrade unreported cases to PASS. Snapshot creation/reuse has static coverage but remains OPEN until the same A/B/C sequence passes.

#### Historical reported Cloud runtime — Candidate 351754177b23494447e075d87f542075f608c198

Test A: PARTIAL PASS — fresh Cloud context without user-preloaded guidance. No user model inventory was demanded, bounded current research occurred, immediate unknown fallback was avoided, and a prompt-first recovery/reconciliation handoff recommended `GPT-6 Astra — Высокое`. HIGH effort and strict localized presentation were appropriate. This is positive evidence for ESTABLISH GUIDANCE WHEN MISSING, not a failure of that rule. However, the observable guidance covered complex recovery and introduced `GPT-5.6 Sol / High` only as an availability fallback; it did not establish normal/default engineering, mechanical/bounded work, or their transition conditions. Reusable-guidance completeness did not pass.

Test B: FAIL — model derivability/reuse. In the same chat immediately afterwards, single-file mechanical inspection received `GPT-5.6 Sol — Низкое`. LOW effort was appropriate and no second research occurred. But A had not established this model for mechanical work, and the user reported no unavailable Astra, selector/account change, new model evidence, or new accepted mechanical mapping. The concrete-model transition was unexplained. This does not invalidate accepted reasoning selection or no-per-handoff-research evidence.

These are user-reported observations of that Candidate, not tests performed in the implementation chat and not permanent model recommendations. That correction was TASK-SPECIFIC REFRESH → GUIDANCE-FIRST REFRESH. Preserve the positive bootstrap, reuse/event-driven refresh, user-evidence priority, model/reasoning separation, task-sensitive effort, and exact presentation evidence. This historical record is not a PASS for the current target-evidence correction.

#### Historical reported Cloud runtime — Candidate accdd99f7275d3ef1a3944cde2411ed9f4f97fcc

Test A: FAIL overall — target-valid refresh. The fresh chat had no user-preloaded guidance and explicitly targeted Codex. PASS sub-results: the no-guidance branch triggered one bounded refresh; no mandatory user model inventory or immediate unknown fallback; concrete advice; prompt-first; strict localized presentation; task-appropriate HIGH effort for recovery; research stayed bounded. The recommendation was `GPT-5.6 Sol — Высокое`, based on an official OpenAI article primarily about GPT-5.6 / GPT-6 Pro in ordinary ChatGPT. When the user challenged that product scope, current Work/Codex-specific documentation produced materially different practical Codex guidance. FAIL: source admissibility, target-environment grounding, and therefore validity of accepted guidance. This is not evidence that GPT-5.6 Sol must never be recommended.

Test B: FAIL — downstream from invalid guidance. Retain the reported positive sub-evidence: no second research, task-appropriate LOW reasoning, and correct presentation. It does not prove valid guidance reuse because A's accepted guidance was not grounded in Codex-valid evidence.

Test C: cannot close valid-guidance reuse — the same invalid foundation applies. Retain reported reuse/reasoning evidence only within its observed scope; no complete C response or detailed outcome is supplied here, so do not invent a model, exact level, source, or additional PASS. Internally coherent reuse across complex/mechanical/normal tasks does not make A's evidence admissible.

These are user-reported Candidate observations, not runtime executed in this implementation chat or permanent model recommendations. That correction was GUIDANCE-FIRST + TARGET-VALID GUIDANCE FIRST: NO GUIDANCE → BOUNDED REFRESH → TARGET-VALID EVIDENCE → REUSABLE GUIDANCE → TASK SELECTION → REUSE. Preserve all accepted structural, reasoning, presentation, and bounded-research sub-evidence. This historical record is not a PASS for current candidate-set discovery.

#### Historical reported Cloud runtime — current-model discovery

Test A: FAIL — current candidate-set/comparative recommendation. Fresh Cloud explicitly targeted Codex and performed bounded refresh, recommending `GPT-5.6 Sol — Высокое`. An official model-specific page could establish that this model was available in Codex, but the response treated that fact as enough to choose it practically without first establishing the relevant current Codex candidate set. The invalid inference was AVAILABILITY → PREFERENCE/current default/ladder role, not that GPT-5.6 Sol is invalid or forbidden. A model-specific source can be admissible for availability while insufficient for the comparative choice.

That historical report supplied no exact runtime Candidate SHA; do not substitute an inspected workspace HEAD for runtime provenance. No additional B/C outcomes were supplied for that failure; do not invent them or close valid reuse from an inadequate A foundation. Historical positive and failed observations above remain intact. No runtime was performed in the implementation chat and no post-correction PASS is claimed.

#### Historical reported Cloud runtime — compressed Candidate

Sequence 1: FAIL overall — A recommended `GPT-6 Astra — Высокое`, B `GPT-5.6 Luna — Низкое`, and C `GPT-6 Astra — Среднее`. Retain positive evidence: prompt-first, concrete advice, appropriate recovery/mechanical/ordinary-debugging reasoning, and compact runtime delivery. The reconciled CURRENT CODEX CANDIDATE SET and comparative mappings were not convincingly established. In particular, B did not explain why its model was the current mechanical choice relative to other relevant Codex candidates. Plausible reasoning does not validate the concrete-model ladder.

Sequence 2: FAIL — A requested the same ready Codex handoff without explicit “подскажи модель” wording and returned `Конкретная модель не подтверждена — Высокое`, despite mentioning usable current general candidates such as GPT-6.1 Sol and Astra. The reported cause was unknown exact selector/account: this is premature fallback, not absence of general recommendation evidence. B then introduced `GPT-5.6 Luna — Низкое` without a new refresh or established accepted mapping. No sequence-2 C result was supplied.

These are user-reported observations, not runtime performed here; exact runtime Candidate SHA was not supplied separately. Model names describe the observations, not permanent recommendations or bans: neither “GPT-5.6 Luna is forbidden” nor “Astra is always correct” follows. Earlier positive and failed evidence remains preserved; no post-correction runtime PASS is claimed. Ready-to-copy Codex handoffs imply advice unless opted out, regardless of an explicit model question.

#### Historical reported Cloud runtime — Candidate 828a2e54273b0db360ce15d38adce9a16b93f6ad

Test A: FAIL — reusable-guidance establishment/observability. The CURRENT Candidate recommended `GPT-6 Astra — Высокое`. Retain positive evidence: correct prompt-first delivery, concrete advice, appropriate HIGH reasoning for recovery, and sensible treatment of the task. No observable reusable mapping sufficient for B/C was established; a local task recommendation did not demonstrate completion of one reusable guidance decision.

Test B: FAIL — downstream. `GPT-5.6 Luna — Низкое` used appropriate LOW reasoning for mechanical work, but appeared as a new independently justified model choice; A had not visibly established that mechanical mapping.

Test C: FAIL — downstream. `GPT-5.6 Sol — Среднее` used appropriate MEDIUM reasoning for ordinary local debugging, but again received fresh model-choice justification; reuse of A's accepted mapping was not demonstrated.

At that checkpoint these were the latest user-reported runtime observations of the exact CURRENT Candidate above, not an old failure attributed to an untested SHA. POLICY EXISTS, but runtime does not execute it as one ordered procedure. Model names are observations only, not bans or preferences. Historical evidence remains intact; this implementation chat performs no Cloud runtime and claims no post-correction behavioral PASS.

#### Historical reported Cloud runtime — snapshot simplification

Latest report received with this correction at private/Candidate baseline `62bd0aa6d86648aff8d414f1d15da646fd59f65d`; a separate exact runtime SHA was not supplied, so the local baseline is not substituted for runtime provenance.

- Sequence 1: FAIL — repeated independent model selection. Complex recovery received `GPT-6.1 Sol`, mechanical work `GPT-6 Luna`, and normal debugging `GPT-6 Luna`, with each choice independently justified rather than consuming one accepted scheme.
- Another fresh sequence built a materially different recommendation family around `GPT-5.6` models. No complete response, individual variant list, reasoning levels or additional outcomes are supplied; do not invent them.

These model names are observations, not permanent recommendations or bans. Different models across accepted bands are valid; the failure is repeated independent selection instead of snapshot reuse. Previous evidence remains below/above as history, not a post-simplification PASS.

The previous guidance/candidate-set mechanism was REPLACED by CURRENT CODEX SNAPSHOT because runtime repeatedly re-selected models despite increasingly detailed policy. The current contract is ONE CURRENT SNAPSHOT → REUSE UNTIL INVALIDATED, not another corrective layer. Static coverage does not prove this runtime behavior; the same A/B/C remain OPEN and no Cloud runtime is run in the implementation chat.

#### Latest reported Cloud runtime — conflicting current sources

Fresh Test A: FAIL — the first snapshot selected an older still-supported `GPT-5.6` generation despite newer current target-level Codex documentation. This is not hallucination or evidence that the family is invalid: SUPPORTED / AVAILABLE was treated too similarly to PRIMARY CURRENT DEFAULT LINEUP. The supplied local/Candidate baseline is `1d3e29e8a131252784e7e4e3ba045539a9fa66dc`; a separate exact runtime SHA was not supplied, so it is not substituted for runtime provenance. No new B/C outcomes are supplied or inferred.

The narrow correction preserves ONE CURRENT CODEX SNAPSHOT → CLASSIFY TASK → USE SNAPSHOT → REFRESH ONLY WHEN INVALIDATED. Conflicting official evidence uses actual user availability first; otherwise materially fresher target-specific Codex / Work+Codex evidence wins. Comparably fresh sources favor the newer generation as the general snapshot basis, not as automatically best for every task. Older supported models remain alternates for actual selector constraints, unavailable newer primary options, or an explicit material current task-specific reason; availability alone is not default preference. Obvious material freshness/generation differences suffice: no minute-level dating or historical archaeology.

The general snapshot is usable immediately. After the initial usable recommendation and compact snapshot, offer one short optional model-list/selector-screenshot refinement invitation in the user's language, outside the prompt; no first-recommendation selector prerequisite. Accepted actual options may refine/replace it, then the personal snapshot is reused. Do not repeat the invitation on later handoffs or conflate it with a material caveat. Earlier evidence remains historical; only static coverage is run here, no corrected Cloud runtime PASS claimed.

#### Historical model-guidance regression lessons

- Immediate unknown fallback on first use deferred model discovery to the user; the bounded-refresh branch must precede fallback.
- A task-only recommendation did not establish reusable coverage; later mechanical/normal choices need an accepted mapping, not a newly invented role for an availability fallback.
- Official authorship, a Codex mention, ordinary ChatGPT scope, API-only scope, and historical examples/memory are not independent proof of current Codex applicability or comparative ranking. Evaluate the exact claim, not a whole domain/page blacklist.
- Availability of one model does not identify current alternatives or preference. Establish the smallest target-level candidate set before comparison; supplement established applicability with reliable capability/reasoning/task-fit evidence. No permanent current-model catalog is expected.
- Reconcile generations/options across current target-level and narrower model-specific evidence before accepting class mappings. Unknown exact selector/plan is not absence of sufficient general evidence; clarification is for a real environment ambiguity that prevents a useful concrete recommendation.
- Execute reuse-check → ordered refresh (candidates, comparison, mapping, acceptance, task selection) → reuse, with last-resort fallback only when eligible. After fresh acceptance, show one compact mapping after the recommendation and short reason, outside the prompt; later reasons consume it rather than independently choosing models.

These lessons explain the earlier failed designs, not extra runtime policy. Static tests now guard snapshot creation/acceptance, band consumption, concrete invalidation, overrides, last-resort fallback, reasoning and presentation; they are not a behavioral PASS. The same A/B/C sequence below is the only rerun; no D/E/F or unrelated suite is added.

Historical five-case plan (retained, not a new required rerun): tests 1–3 used fresh Cloud contexts; tests 4–5 used accepted current guidance established once. The original test 3 expectation below is superseded by auto-establishment. Do not add expected labels or responses to activation instructions, and do not execute Cloud runtime in the implementation chat.

#### Historical Cloud: terminology

Test 1 exact input:

```text
Task Session lost convergence because stale state crossed the authority boundary.
Master should reconstruct Handoff before resuming CHANGE authority.

Что это значит и что мне теперь делать?
```

PASS requires a complete ordinary-Russian explanation and practical action, understandable without Task/Master/Handoff/CHANGE/convergence. Source terms may be mapped afterwards, but primary instructions must not depend on Bootstrap jargon.

Status: HISTORICAL PLAN — no new rerun required by this correction; no additional runtime PASS claimed.

#### Historical Cloud: explanation before handoff

Test 2 exact input:

```text
Получил от агента такой отчёт:

"Durable Task State and Handoff may be stale.
Drift was detected after a CHANGE-capable session.
Convergence is no longer established.
Refresh mutable evidence before restoring CHANGE authority."

Это критично?
Работа потерялась?
Что мне делать дальше?
```

PASS requires answering all three questions first without leading with a Codex prompt, assuming lost work, or prescribing internal lifecycle commands. Explain a safe next action in ordinary Russian; a handoff may be offered afterwards, not silently produced before the explanation.

Status: HISTORICAL PLAN — no new rerun required by this correction; no additional runtime PASS claimed.

#### Historical Cloud: unknown model recommendation

Test 3 exact input, in a fresh context without accepted model guidance:

```text
Codex открыт в корне существующего Python-проекта.
После прерывания работы у меня два противоречащих отчёта о том, какие изменения сделаны и какие проверки прошли.
Нужно проверить реальные файлы и текущее состояние Git, сопоставить их с отчётами и определить безопасный следующий шаг.
Сейчас ничего не менять и не удалять.
Подготовь готовую передачу в Codex и подскажи, какую модель выбрать.
```

Original expectation (INVALID UX EXPECTATION): prompt-first and read-only boundaries, followed immediately by **Конкретная модель не подтверждена — Высокое**, without establishing current guidance. Runtime showed that this cautious-looking path shifts model-selection work to the user and enters fallback too early. The unknown label remains valid only after an unsuccessful bounded refresh and unresolved useful clarification; no model from memory or old examples is permitted. This historical result is not a desired current PASS condition.

Status: INVALID UX EXPECTATION — historical evidence of too-early fallback; superseded by test A.

#### Historical Cloud: complex model recommendation

Test 4 exact input, after accepted current Codex guidance is established once:

```text
У меня существующий Python-проект.
Нужно провести полный анализ проекта, проверить код, тесты, ошибки и реальные риски.
Файлы менять не нужно.
Codex будет открыт в корне проекта.
Подготовь передачу в Codex и подскажи модель.
```

PASS requires prompt-first, the exact model name from accepted guidance followed by the exact Russian token «Высокое» for the ordinary demanding case, one short task-specific reason, no parenthesized English level or reasoning-level prose on the recommendation line, and no fresh research. A genuinely justified different supported level must still use its exact token. Recommendation remains outside the durable prompt.

Status: HISTORICAL PLAN — accepted known-model presentation evidence retained where demonstrated; no new rerun required here.

#### Historical Cloud: simple model recommendation

Test 5 exact input, in the SAME guidance chat without repeating guidance:

```text
Codex открыт в корне проекта.
Нужно только прочитать statistics_utils.py и сказать какие функции экспортируются.
Ничего не менять.
Подготовь передачу и подскажи модель.
```

PASS requires prompt-first, a concrete model from the same accepted guidance, the exact Russian token «Низкое» for this mechanical inspection, one short reason, no decorated/English reasoning label, and no repeated research. Model and reasoning remain independent; the same model as test 4 is valid.

Status: HISTORICAL PLAN — accepted task-sensitive effort/reuse evidence retained; no new rerun required here.

Latest user-reported Cloud runtime on current behavior: snapshot creation and B/C reuse worked. Preserve those accepted positive sub-results; this is new runtime evidence, not the historical Candidate failure. Three bounded regressions remain: initial default bands mixed the primary newer lineup with an older supported generation without a positive exception reason; the selector invitation repeated after the user had already supplied actual availability; one Russian short reason still said “Sol со средним reasoning здесь достаточен.” These are the findings addressed by this pass, not evidence that snapshot/reuse is broken. No post-delta Cloud runtime has been executed here; correction verification remains OPEN.

Current intended behavior: ONE CURRENT SNAPSHOT → REUSE UNTIL INVALIDATED. With no accepted snapshot and a required recommendation, do one bounded current Codex check, build a small practical band mapping, recommend from it, and keep it in context. Official-source conflicts use materially fresher target-specific evidence, or the newer generation as the general basis when freshness is comparable. Default general bands use that primary lineup; an older model needs a positive actual-availability, unavailable-primary-option or current material comparative exception, not mere support or an official page. Actual user selector/list/screenshot refines or replaces the general mapping. Known actual availability already satisfies the invitation: build/refine and reuse the personal snapshot without asking again. Otherwise invite once after the first usable general snapshot/recommendation without blocking; request again only after concrete availability invalidation. Later task complexity only selects another accepted band, not research. No TTL, polling, preference subsystem, invitation state machine/file or mandatory snapshot artifact is introduced.

Release gate closure — 2026-10-05: the user reports fresh Cloud A PASS, B PASS and C PASS on the final behavior at private/Candidate baseline `c8109c1bbf23a59e45a5db46a30fa900f27009b6`. The first snapshot uses the current primary lineup; B/C reuse it without new model research; short reasons are ordinary user language; selector invitation behaves as specified. Model-guidance: CLOSED. This supersedes the earlier OPEN correction gates without erasing their observations. No new Cloud runtime was performed in this release task; the broader documented suite is not declared PASS.

Exactly three Cloud scenarios formed the accepted runtime gate below. Recorded protocol: use fresh Cloud context without a preloaded snapshot; record responses and preserve the visible sources of the bounded check and accepted snapshot. Run B/C only after A PASS and evaluate reuse in the same applicable context. These scenario definitions remain evidence/documentation, not a request for another rerun.

The earlier language finding exposed English/internal classifications instead of explaining the task. Apply the existing Shared Core disclosure contract to the short reason and related commentary; classifications remain selection inputs. The latest narrower rendering correction also requires a non-English short reason to explain the level without English `reasoning`; in Russian use ordinary wording such as «уровень рассуждения». In A/B/C, require practical meaning: A compares files and Git with conflicting reports for a safe next step; B reads one file and lists exported functions; C finds/fixes one reproducible bug and adds a test. These are meaning examples, not fixed responses or a general technical-word blacklist. Exact model names/localized labels and prompt-first ordering remain unchanged. Static coverage does not close post-delta runtime verification.

### Cloud: first-use auto-establish

Test A exact input:

```text
Codex открыт в корне существующего Python-проекта.

После прерывания работы у меня два противоречащих отчёта о том,
какие изменения сделаны и какие проверки прошли.

Нужно проверить реальные файлы и текущее состояние Git,
сопоставить их с отчётами и определить безопасный следующий шаг.

Сейчас ничего не менять и не удалять.

Подготовь готовую передачу в Codex и подскажи, какую модель выбрать.
```

PASS requires one bounded current Codex check broad enough to see the relevant current lineup, then ONE practical 3-5 band snapshot accepted before recommending the complex task from it. Each band stores its concrete model and supported default reasoning, with useful optional escalation. Three or four bands and the same model across bands are valid; do not invent slots or require diversity. Show the accepted snapshot once in compact commentary after the complete read-only prompt, strict recommendation and short reason, outside the durable prompt. No giant research report, mandatory user plan/selector inventory, invented models, or unknown fallback merely for an unknown exact selector. Preserve the visible sources of the bounded check and the accepted bands so B/C reuse can be evaluated.

A also requires default bands inside the established PRIMARY CURRENT Codex lineup: materially fresher target-specific evidence wins conflicts; comparably fresh sources favor newer generation as general basis. An older supported default needs a positive concrete exception: actual user options, unavailable primary option or current substantial comparative reason. Mere existence/support/a separate page is insufficient. If actual availability is unknown, invite once after the usable recommendation/snapshot without blocking. Already supplied actual availability satisfies the invitation; use the personal snapshot and do not ask again unless availability is concretely invalidated. No concrete model names are prescribed.

Status: PASS — user-reported fresh Cloud runtime accepted for the final 0.1.7 behavior; current primary-lineup snapshot and selector invitation verified. Model-guidance gate CLOSED.

### Cloud: reuse after auto-establish

Test B exact input, in the SAME chat immediately after A:

```text
Теперь нужно только прочитать statistics_utils.py
и сказать, какие функции экспортируются.

Ничего не менять.
Не анализировать остальной проект.

Подготовь передачу в Codex и подскажи модель.
```

PASS requires classifying this read-only single-file task as mechanical/bounded, using the existing accepted snapshot's model and minimum sufficient supported reasoning, normally LOW. No web/model research, documentation lookup, independent comparison or fresh external model justification; the short reason consumes the accepted band. Do not repeat the whole snapshot. Different models across bands are valid when already accepted; no independent handoff optimization.

Status: PASS — user-reported fresh Cloud runtime accepted for the final 0.1.7 behavior; mechanical snapshot reuse without new model research and plain-language reason verified. Model-guidance gate CLOSED.

### Cloud: normal engineering reuse

Test C exact input, in the SAME chat immediately after B:

```text
В существующем Python-проекте есть воспроизводимый локальный баг
в одной функции.

Нужно найти причину, исправить её и добавить регрессионный тест.
Codex открыт в корне проекта.

Подготовь готовую передачу в Codex и подскажи модель.
```

PASS requires classifying this bounded bugfix/test task as normal engineering and using the same accepted snapshot, with sufficient supported reasoning, normally MEDIUM. No web/model research, documentation lookup, new external model justification or independently reselected model. Do not repeat the whole snapshot. Exact localized presentation remains required; concrete model names are not prescribed.

Status: PASS — user-reported fresh Cloud runtime accepted for the final 0.1.7 behavior; normal-engineering snapshot reuse without new model research and plain-language reason verified. Model-guidance gate CLOSED.

Focused selector check for the new reported regression: after the first invitation, supply an actual list/selector once, then continue the same B/C handoffs. The personal snapshot must use those options without inviting another list/screenshot. If actual availability was already supplied before the first recommendation, the invitation is already satisfied there too. A changed selector, added/removed models or an explicit availability refresh request may justify asking again; an ordinary next handoff or general refresh may not. Keep this within the existing targeted run, not a new broad matrix. Historical missing-model override evidence remains valid.

### Spec Kit: missing prerequisite

Request requirements clarification through an appropriate installed capability with no active specification, and exclude plan/tasks/code. Verify the missing prerequisite before invoking a predictably unusable stage when practical. Scope stays bounded; no silent specification or full lifecycle expansion occurs. Ask only for a real decision.

Status: PASS — final runtime accepted; missing specification established before stage invocation, no predictable-failure script or automatic prerequisite lifecycle, smallest compatible clarification path retained.

### Spec Kit: satisfied-prerequisite control

Use an accepted existing specification. Verify reuse and normal bounded clarification without duplicate specification or plan/tasks/code. Waiting for a genuine product answer is correct routing/control behavior; the harness must not answer for the user.

Status: PASS — final routing/control accepted; existing specification reused, prerequisite check succeeded, bounded clarification started, then correctly stopped for genuine missing product input. Full clarification completion was intentionally not performed.

Model-guidance for 0.1.7 is CLOSED by the accepted A/B/C results. Do not rerun it or closed Spec Kit, Superpowers, combined 5/5, earlier model-guidance scenarios or accepted discovery/Participation/portable scenarios without concrete new regression evidence. Proceed only to remaining release gates: dedicated validator status, final static/package/provenance verification and installed-Candidate/source consistency. Publication/Sync remains a separate operational result; no broad behavioral PASS follows from this closure.

Both Cloud artifact delivery methods—one-chat attachment and ChatGPT Project source—are documented and statically validated. A duplicate multi-chat runtime is not required merely to prove documentation wording.

Historical SEO Daemon regression evidence: Cloud Manager selected a physical execution topology before the intended execution path was established. The finding was premature topology selection, not that subagents are invalid.

## Behavioral lifecycle

Behavioral lifecycle: NOT TESTED

Future broader tests should cover Manager orientation and discovery, Manager-to-Master handoff, Master reconciliation and routing, Task defect/verification/convergence behavior, interruption recovery, cross-task consultation, and anti-bloat negative cases. During Coordination Compression scenarios also record role transitions, manual copy/paste handoffs, repeated verification requests, repeated state summaries, and unnecessary durable artifacts as diagnostics rather than hard KPIs.
