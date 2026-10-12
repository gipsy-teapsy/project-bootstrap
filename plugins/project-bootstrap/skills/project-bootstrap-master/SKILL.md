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

## Persistent project instructions

At initial setup or connection of a confirmed Codex workspace, establish which persistent project instructions actually apply and whether accepted durable project-specific rules will remain available to later sessions. File creation is not the goal. Manager may pass accepted goals, decisions, restrictions, and known sources; it must not guess the structure of an unavailable workspace or promise an AGENTS.md file. With an unconfirmed workspace, perform no arbitrary search across the disk.

Keep knowledge storage, canonical policy location, automatic Codex instruction loading, and explicit policy delivery to a Task distinct. An arbitrary document is not automatically loaded because it exists. A Markdown link does not load its target: establish that the target is accessible and tell the Task to read the task-relevant canonical policy before acting, or supply the minimum necessary policy excerpt when that source is inaccessible. Task uses the applicable policy rather than inventing project-wide rules.

Inspect the effective instruction chain within confirmed scope. Account for global guidance in the active Codex home (AGENTS.override.md before AGENTS.md), then the path from project root to the current working directory. At each directory, discovery selects AGENTS.override.md, then AGENTS.md, then configured fallback filenames, with at most one non-empty file per directory. More specific applicable guidance takes precedence; a nested file does not govern the whole project. Check the actual root/cwd, configured discovery names and size limit, overrides, and availability of referenced sources. Use the current [official Codex discovery rules](https://learn.chatgpt.com/docs/agent-configuration/agents-md); do not infer applicability from a filename alone or change native Codex configuration as part of this check.

Read existing instructions before considering any change. Select the smallest sufficient outcome:

- Existing sufficient instructions: reuse them. If correct, preserve the existing file unchanged; do not restructure an existing project's documentation merely to connect Bootstrap.
- No accepted durable project-specific rules or no real gap: omit a new instructions file. An ordinary small task does not require creating AGENTS.md. Absence can be the correct result.
- Accepted durable rules with a real gap: within existing authority, create or update the smallest applicable entry point, including AGENTS.md when appropriate to the project scope. A short entry point can direct reading of accessible canonical documentation instead of copying it. An existing working alternative is sufficient; no specific filename is mandatory.
- Conflicting instructions: reconcile their scope and accepted decisions; do not overwrite unresolved policy or replace it with a generic Bootstrap template. A substantive policy change follows existing authority and user-decision rules.
- READ-only authority: make no file or configuration changes. For inspection-only work, return the finding and a minimal proposal, not an implementation.

Keep the entry point concise: accepted project-specific conventions, stable commands, constraints, resource/safety rules, and directions to necessary canonical sources. Do not copy the full Manager, Master, or Task contracts. Do not store temporary tasks, old test results, current plans, logs, or a model catalog there. Do not introduce a mandatory subagent policy as part of bootstrap. There is no mandatory AGENTS.md onboarding question and no blanket migration of existing projects.

Before the next session, establish that required rules and their sources will be available and applicable in its intended workspace. Distinguish file existence, correct path and scope, source accessibility, instruction loading, and model compliance. Static contract checks do not prove end-to-end PASS after a session restart; claim runtime loading or compliance only when actually observed in that runtime.

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
