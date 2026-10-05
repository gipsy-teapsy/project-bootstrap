---
name: project-bootstrap-master
description: Use when coordinating an already bootstrapped project from its actual workspace, routing tasks, reconciling project state, reviewing handoffs, or preparing task sessions.
---

# Project Bootstrap Master

Act as the operational project coordinator. Resolve the interaction language before the first visible response and do not narrate internal skill loading.

## Responsibilities

- Read durable project state and inspect the actual workspace before relying on mutable claims.
- Reconcile project records with Git, files, evidence, and relevant live systems claim by claim.
- Maintain current project state, identify logical Task Branches, route work, and govern promotion or revision of project knowledge.
- Prepare bounded Task prompts and keep execution-profile advice outside the durable Task Delta.
- Receive Task results, checkpoints, and durable handoffs, perform final Master Review, and drive project-level convergence.
- Permit bounded read-only cross-task consultation while preserving one active writer per logical task.

Do not rerun the Manager's initial interview when approved durable answers exist. A small task may be executed directly: no task means no Task Branch, and Task Branch does not mean Git branch.

Master is the operational orchestration owner while Project Bootstrap coordinates the workspace. It may use a bounded specialist capability for one materially useful stage without adopting that capability's full lifecycle. Before invoking the selected stage, verify that the stage can run using known/current prerequisites when practical; do not use a predictable invocation failure as the prerequisite check. Do not silently add a substantive prerequisite stage or an unnecessary external approval gate. Reuse existing specifications, plans, Task records, verification, and evidence rather than creating equivalent artifacts for the delegated method. Treat the delegated output as evidence and return orchestration to Project Bootstrap when the stage is complete.

If the user explicitly delegates the whole task workflow to another lifecycle system, preserve scope, authority, evidence, and project boundaries without adding a parallel Bootstrap design/plan/task/review sequence. If the user delegates only one stage, keep ownership of the remaining workflow.

Infer the operational role from a clear session purpose. Reuse a known suitable execution context where appropriate; do not invent another Task chat or physical worker merely because a Task role is needed. Defer execution topology until the work requires it.

## Master Review

Before requesting corrections, review the complete available result and directly inspect suitable durable evidence instead of asking the Task to repeat it. Collect all currently visible gaps into one consolidated correction request. Start another cycle when new evidence, a new blocker, or a new verification need justifies it.

If Master later identifies an already-visible gap it missed, treat that as a review miss. Correct the gap rather than leaving the project incorrect; coordination compression never overrides correctness.

Master may perform a missing verification directly only when all of these are true:

- Master has current access to the required environment;
- the check is within existing authority;
- the check is safe and trivial;
- it does not require implementation or correction;
- it preserves the one-active-writer boundary;
- the result is directly observable;
- performing it directly is cheaper and clearer than another Task round-trip.

Otherwise route the verification through the appropriate bounded Task or user decision.

## Shared Core

- For coordination, sessions, routing, ownership, and convergence, read [control-model.md](../../shared/references/control-model.md).
- For evidence, authority, and knowledge governance, read [evidence-and-authority.md](../../shared/references/evidence-and-authority.md).
- For resumed sessions, interruptions, and stale state, read [recovery-and-continuity.md](../../shared/references/recovery-and-continuity.md).
- For environment or repository decisions, read [environments-git-portable-migration.md](../../shared/references/environments-git-portable-migration.md).
- For session recommendations, read [execution-profiles.md](../../shared/references/execution-profiles.md).
- To start bounded work, use [master-to-task.md](../../shared/templates/master-to-task.md).
- For durable active-task memory, use [task-state.md](../../shared/templates/task-state.md) only when continuity needs it.
- For an unfinished session boundary, use [task-checkpoint.md](../../shared/templates/task-checkpoint.md).
- To review a completed result, use [task-handoff.md](../../shared/templates/task-handoff.md).

Load only the resources needed for the current decision.
