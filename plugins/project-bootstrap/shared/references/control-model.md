# Control Model

## Core invariants

FILES ARE MEMORY. FILES = CURRENT MEMORY. GIT = HISTORY OF MEMORY.

MANAGER IS CONTROL PLANE. MASTER IS COORDINATOR. TASK BRANCHES ARE WORKERS.

MASTER ≠ MASTER SESSION. TASK BRANCH ≠ TASK SESSION.

SESSIONS ARE DISPOSABLE. PROJECT/TASK STATE IS DURABLE.

POLICY ONCE. TASK DELTA IN PROMPT. EVIDENCE IN ARTIFACTS. DEVIATIONS IN CHAT.

THE CONTROL MODEL IS UNIVERSAL. THE PROJECT ARCHITECTURE IS ADAPTIVE.

## Lifecycle and routing

`Manager → Master → Task → Verify → Converge → Handoff → Master Review`

Manager establishes project-level intent and management architecture. Master coordinates an already bootstrapped project. Task performs bounded work. The user can simply say “Хочу создать новый проект”, “Продолжим”, “Есть баг”, “Сделай новую задачу”, or “Проверь, всё ли готово”; the active role routes the request internally.

A Task Branch is a logical task context, not automatically a chat, Git branch, or worktree. A Session is a disposable runtime instance of a role. Master may execute genuinely small work directly.

## Anti-bloat

DO NOT ADD A WORKFLOW WHEN A ROUTING RULE IS ENOUGH.

- No task → no Task Branch.
- No long or interruption-prone task → no ExecPlan.
- No isolation need → no Git branch or worktree.
- No release process → no release contract.
- No migration → no migration artifacts.
- No portable need → no portable workflow.

## Ownership and consultation

Master owns project coordination. Task may obtain bounded, normally read-only facts or evidence from another task when necessary. Consultation does not transfer ownership or promote a claim into project truth.

ONE LOGICAL TASK → ONE ACTIVE WRITER AT A TIME.

## Verification and convergence

Verification asks whether the implementation works. Convergence asks whether the accepted goal and all applicable requirements are covered. Tests can be green while convergence has a gap. Handoff is ready only after both are adequate or a limitation is explicitly preserved for Master/user acceptance.
