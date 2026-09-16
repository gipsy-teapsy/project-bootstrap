---
name: project-bootstrap-task
description: Use when executing a bounded task inside a Project Bootstrap-managed project, including implementation, debugging, verification, recovery, checkpointing, or handoff.
---

# Project Bootstrap Task

Act as the bounded worker described by the Task Delta. Resolve the interaction language before the first visible response; keep internal contracts in the project's established language.

## Responsibilities

- Work only within the stated goal, scope, authority, constraints, and done conditions.
- Inspect current relevant state before mutation, especially after interruption or possible drift.
- Implement or research the task, verify the actual result, compare it with the accepted goal, and hand off only after convergence.
- For a defect, use Assess → Fix → Verify original symptom → Converge.
- Preserve evidence in artifacts and report deviations, blockers, or contradictions to Master.

Do not redefine project-wide architecture or policy. Do not mutate another Task's area without explicit authority. One logical task has one active writer at a time.

## Shared Core

- For Task Branch boundaries, lifecycle, consultation, and convergence, read [control-model.md](../../shared/references/control-model.md).
- For claim strength and action authority, read [evidence-and-authority.md](../../shared/references/evidence-and-authority.md).
- For recovery or a new Task Session, read [recovery-and-continuity.md](../../shared/references/recovery-and-continuity.md).
- For environment-specific or Git work, read [environments-git-portable-migration.md](../../shared/references/environments-git-portable-migration.md).
- For profile escalation when the work materially changes, read [execution-profiles.md](../../shared/references/execution-profiles.md).
- Maintain [task-state.md](../../shared/templates/task-state.md) only when the logical task must survive a session change.
- Use [task-checkpoint.md](../../shared/templates/task-checkpoint.md) when the task continues but the current session may end.
- Use [task-handoff.md](../../shared/templates/task-handoff.md) when the verified result is ready for Master Review.

Load only what the bounded task needs.
