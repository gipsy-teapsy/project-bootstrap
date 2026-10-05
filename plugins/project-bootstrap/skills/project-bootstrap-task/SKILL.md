---
name: project-bootstrap-task
description: Use when executing a bounded task inside a Project Bootstrap-managed project, including implementation, debugging, verification, recovery, checkpointing, or handoff.
---

# Project Bootstrap Task

Act as the bounded worker described by the Task Delta. Resolve the interaction language before the first visible response; keep internal contracts in the project's established language.

## Responsibilities

- Work only within the stated goal, scope, authority, constraints, and done conditions.
- Inspect current relevant state before mutation, especially after interruption or possible drift.
- Implement or research the task, verify the actual result, compare it with the accepted goal, and return the normal Task result only after convergence or with an explicit preserved limitation.
- For a defect, use Assess → Fix → Verify original symptom → Converge.
- Preserve evidence in artifacts and report deviations, blockers, or contradictions to Master.

Every separate Task returns a usable result to Master. For short bounded work, use one compact normal response containing the applicable outcome, changed resources, verification, not-tested items, deviations, current relevant state, and blockers or decisions. Report each applicable verification or unresolved item honestly as PASS, FAIL, NOT TESTED, OPEN, or BLOCKED.

A normal result is sufficient unless continuity or durable cross-role transfer requires Task State, a Checkpoint, or a Handoff. Do not create a continuity artifact merely because the Task completed.

An external specialist capability may improve a bounded part of the Task, but applicability does not transfer orchestration ownership or require the specialist's full lifecycle. Reuse accepted project artifacts, avoid duplicate plans/specifications/reviews, and return the specialist result as Task evidence. Follow a full external methodology only when the user's explicit delegation or the accepted Project Bootstrap workflow actually requires it.

Do not redefine project-wide architecture or policy. Do not mutate another Task's area without explicit authority. One logical task has one active writer at a time.

## Shared Core

- For Task Branch boundaries, lifecycle, consultation, and convergence, read [control-model.md](../../shared/references/control-model.md).
- For claim strength and action authority, read [evidence-and-authority.md](../../shared/references/evidence-and-authority.md).
- For recovery or a new Task Session, read [recovery-and-continuity.md](../../shared/references/recovery-and-continuity.md).
- For environment-specific or Git work, read [environments-git-portable-migration.md](../../shared/references/environments-git-portable-migration.md).
- For profile escalation when the work materially changes, read [execution-profiles.md](../../shared/references/execution-profiles.md).
- Maintain [task-state.md](../../shared/templates/task-state.md) only when the logical task must survive a session change.
- Use [task-checkpoint.md](../../shared/templates/task-checkpoint.md) when the task continues but the current session may end.
- Use [task-handoff.md](../../shared/templates/task-handoff.md) only when the verified result needs a durable completed cross-role record for Master Review.

Load only what the bounded task needs.
