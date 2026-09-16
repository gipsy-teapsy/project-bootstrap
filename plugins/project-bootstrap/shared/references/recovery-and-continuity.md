# Recovery and Continuity

Recover the logical project or task, not the wording of a previous chat.

## Route by interruption type

- Normal pause or usage-limit pause with the same valid session: continue without an unnecessary full audit.
- Possible partial mutation, stream/network/tool failure, stale state, or external writer: refresh the mutable facts needed before the next mutation.
- New Master or Task Session: reconstruct from durable state and current evidence.
- Lost context or unknown interruption: perform the smallest safe recovery needed for the next action.

Durable state is not one magic file. Relevant evidence may include workspace files, Git, Task State, ExecPlan, project records, plans/specs, verification artifacts, conversation context, and canonical external systems. Reconcile claim by claim.

Absence of Task State does not prove absence of active work.

## Checkpoint and handoff

A Checkpoint means the logical task continues while the current Task Session may end. A Handoff means the Task result is ready for Master Review.

`Task Start → Work → Verify → Convergence → Handoff → Master Review`

Keep Task State or an ExecPlan only when the task is long, interruption-prone, portable across environments, or costly to rediscover. Update at meaningful transitions, not after every message.

Before Handoff, refresh shared mutable state, identify drift, separate fresh from historical verification, and report any convergence gap.
