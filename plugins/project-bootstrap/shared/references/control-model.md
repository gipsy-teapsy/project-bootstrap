# Control Model

## Core invariants

FILES ARE MEMORY. FILES = CURRENT MEMORY. GIT = HISTORY OF MEMORY.

MANAGER IS CONTROL PLANE. MASTER IS COORDINATOR. TASK BRANCHES ARE WORKERS.

MASTER ≠ MASTER SESSION. TASK BRANCH ≠ TASK SESSION.

SESSIONS ARE DISPOSABLE. PROJECT/TASK STATE IS DURABLE.

POLICY ONCE. TASK DELTA IN PROMPT. EVIDENCE IN ARTIFACTS. DEVIATIONS IN CHAT.

THE CONTROL MODEL IS UNIVERSAL. THE PROJECT ARCHITECTURE IS ADAPTIVE.

## Coordination compression

ONE OWNER → ONE EVIDENCE PACKET → ONE REVIEW.

NO NEW EVIDENCE → NO NEW HANDOFF.

CORRECTNESS > COORDINATION COMPRESSION.

These are optimization rules, not rigid prohibitions. Master should review the complete available result, consolidate currently visible gaps, and avoid asking a Task to retell evidence that is already available. A new cycle is justified by genuinely new evidence, a blocker, a new verification need, or a correction that correctness still requires. If Master missed an already-visible gap, correct the review miss rather than preserving an incorrect result for the sake of fewer cycles.

## Lifecycle and routing

`Manager → Master → Task → Verify → Converge → Master Review`

Manager establishes project-level intent and management architecture. Master coordinates an already bootstrapped project. Task performs bounded work. The user can simply say “Хочу создать новый проект”, “Продолжим”, “Есть баг”, “Сделай новую задачу”, or “Проверь, всё ли готово”; the active role routes the request internally.

A Task Branch is a logical task context, not automatically a chat, Git branch, or worktree. A Session is a disposable runtime instance of a role. Master may execute genuinely small work directly.

ROLE ≠ CHAT. TASK ROLE ≠ NEW SESSION REQUIRED. Infer the role from a clear session purpose without requiring the user to label every chat. Reuse a suitable execution context when it is already known from the current context or durable evidence; do not invent an unknown context. Choose a physical execution topology only when the work actually needs that choice.

Every separate Task returns a usable normal result for Master Review. That result is coordination evidence; it is distinct from an optional durable Task State, Checkpoint, or Handoff artifact.

## Anti-bloat

DO NOT ADD A WORKFLOW WHEN A ROUTING RULE IS ENOUGH.

CAPABILITY AVAILABLE ≠ CAPABILITY MUST CONTROL THE WORKFLOW.

CAPABILITY AVAILABLE ≠ CAPABILITY MUST BE USED.

SKILL APPLICABLE ≠ SKILL OWNS WORKFLOW.

METHODOLOGY AVAILABLE ≠ FULL METHODOLOGY REQUIRED.

ONE ORCHESTRATION OWNER AT A TIME.

Select workflow depth and external capabilities in this order:

`USER INTENT → COMPLEXITY / RISK / DURABILITY → SMALLEST SUFFICIENT WORKFLOW → AVAILABLE CAPABILITIES → SELECT BOUNDED SPECIALIST OR EXTERNAL WORKFLOW`

When Project Bootstrap is the active coordinator, installed plugins, skills, methodologies, and agent frameworks are capabilities by default, not parallel orchestration owners. Select the smallest sufficient workflow before selecting an external capability. An external capability must not add a lifecycle stage solely because that stage exists in its default methodology.

Project Bootstrap may delegate one bounded stage. During that delegation, reuse existing specification, plan, task, verification, or other artifacts; do not create a parallel equivalent lifecycle or duplicate Bootstrap artifacts; treat the returned result as evidence; then return orchestration to Project Bootstrap.

CAPABILITY SELECTED ≠ STAGE IS EXECUTABLE. Before invoking a selected bounded external stage, verify its known/current prerequisites from the current project state when practical. Do not deliberately enter a predictably unusable stage to discover a prerequisite failure that could have been established beforehand. Reuse a valid prerequisite artifact or state, choose the smallest compatible route that meets the requested outcome, or satisfy a trivial technical prerequisite within accepted scope and authority. A substantive prerequisite stage must not silently become an additional user-visible lifecycle stage or trigger the full prerequisite lifecycle. Explain the missing prerequisite in ordinary language when it matters; ask only for a genuine product, authority, risk, or scope decision.

Once Bootstrap has established that the selected work can proceed safely, an external methodology must not insert a user approval gate merely because its default lifecycle contains one. Ask when the user explicitly selected that full workflow, an unresolved decision or authority/risk boundary requires it, new evidence invalidates an accepted decision, or another applicable correctness rule requires confirmation. Accepted architecture and external artifacts remain usable until new evidence calls them into question.

Explicit user intent has priority. If the user asks for another lifecycle system to perform one bounded stage, delegate that stage. If the user explicitly asks another lifecycle system to own the entire task or project workflow, do not impose a competing Bootstrap design, plan, task, or review sequence; preserve only the applicable project boundaries, authority, and evidence expectations.

Explicit plugin or skill invocation is a strong signal but is not required. Ask about outcomes, not internal methodology names, only when the choice materially affects the user. If the safe choice is obvious and reversible, route it without exposing internal arbitration.

Load capabilities progressively: use available metadata to identify plausible capabilities, determine whether their workflow is actually needed, then load only the selected capability and delegate only the required stage. Do not load every installed methodology on every request.

- No task → no Task Branch.
- No long or interruption-prone task → no ExecPlan.
- No isolation need → no Git branch or worktree.
- No release process → no release contract.
- No migration → no migration artifacts.
- No portable need → no portable workflow.

Choose the smallest sufficient workflow internally. For small bounded work, the normal path is inspect enough to act safely → change → relevant verification → convergence → finish. Do not create a Task, ExecPlan, Git branch or worktree, Checkpoint, Handoff, design phase, or independent review merely because the capability exists. The user does not need to know which internal workflow depth was selected.

Specialist guidance may improve one part of that path without importing its complete lifecycle. A testing capability may improve test quality without forcing a full test-first ceremony, and a planning capability may support a genuinely complex planning problem without forcing a separate plan artifact or approval for bounded implementation. Larger or riskier work still receives the planning and verification that correctness materially requires.

## User-facing disclosure

Use the user's current language, simple natural language, and the minimum technical terminology needed for the current decision.

AGENT-GENERATED TERMINOLOGY IS NOT EVIDENCE OF USER EXPERTISE.

Technical terms appearing only in agent prompts, results, summaries, generated documentation, or internal contracts must not raise the assumed technical level of the user. A clearly user-attributed or explicitly user-accepted communication preference may be retained as durable evidence. Do not add a normal setup question asking the user to select a technical skill level.

SOURCE JARGON ≠ USER LANGUAGE.

When the user pastes or quotes technical material from another agent, a role, plugin, methodology, handoff, generated document, logs or a technical report, first translate the meaning into ordinary language appropriate for the user's demonstrated level. Use this order: plain-language meaning, practical consequence or next action, then source/internal terminology only when useful. Render the complete primary explanation and primary next action in this shape:

1. Plain meaning: explain what actually happened, whether anything is known to be lost or broken, why work should or should not stop, and the practical consequence in ordinary language. Distinguish confirmed damage or loss from uncertainty; do not infer lost work merely from a stale report.
2. Plain practical action: explain what the user or worker should do next in ordinary language; the action must be usable without knowing Bootstrap vocabulary. When relevant, check the actual files, inspect current Git state, compare what is really present with the previous result, and continue only after current state is confirmed.
3. Technical mapping only if useful: add source/internal terms secondarily when the user independently uses them confidently, the mapping back to the source is useful, omission would create ambiguity, or the current decision genuinely depends on the distinction.

Keep both primary parts understandable without Bootstrap vocabulary throughout; do not return to dense source jargon after a simple first sentence. Do not mirror agent-generated terminology merely because it appears in the input. Before sending, mentally remove all Bootstrap/internal terms from the primary explanation and primary next action: the user must still understand what happened, why work stopped, and what needs to happen next. If not, rewrite the explanation and action before adding technical mapping. Do not ban technical terminology or add a skill-level subsystem, communication mode, or questionnaire.

Use no Bootstrap internal terminology in either primary part unless a short quote or term is genuinely necessary to identify the source being discussed. The primary instructions must not require the user to understand Task, Master, Handoff, CHANGE, convergence, drift, or durable state/evidence. Do not prescribe “restore Handoff”, “return to Master”, “resume CHANGE”, or “re-establish convergence” as the user's main action. Optional technical mapping belongs after the complete human explanation and action, not inside them.

When the user asks what a term means, asks for clarification, or asks for a simpler explanation, treat that as evidence that the current technical density was too high and simplify subsequent user-facing responses.

For a vague or new project, establish the most important unknown about the desired outcome before choosing implementation details. Usually ask one primary question at a time. A small tightly coupled group is allowed when answering it together clearly avoids unnecessary turns. Across new, portable, and migration work, introduce concrete architecture, stack, tooling, repository layout, or release process only when the determining facts are known or the choice is already accepted. Use explicit user facts such as “Python package + CLI” when they determine a choice; “portable” alone does not determine a folder layout, toolchain, or release workflow. Do not turn discovery into a rigid one-question rule or a setup questionnaire.

Final user-facing reports may use restrained Markdown emphasis for useful anchors such as result, checks, limitations, a required decision, or a model recommendation. Do not create a formatting subsystem or over-format routine communication.

## Ownership and consultation

Master owns project coordination. Task may obtain bounded, normally read-only facts or evidence from another task when necessary. Consultation does not transfer ownership or promote a claim into project truth.

ONE LOGICAL TASK → ONE ACTIVE WRITER AT A TIME.

## Verification and convergence

Verification asks whether the implementation works. Convergence asks whether the accepted goal and all applicable requirements are covered. Tests can be green while convergence has a gap. Handoff is ready only after both are adequate or a limitation is explicitly preserved for Master/user acceptance.
