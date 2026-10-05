# Recovery and Continuity

Recover the logical project or task, not the wording of a previous chat.

## Route by interruption type

- Normal pause or usage-limit pause with the same valid session: continue without an unnecessary full audit.
- Possible partial mutation, stream/network/tool failure, stale state, or external writer: refresh the mutable facts needed before the next mutation.
- New Master or Task Session: reconstruct from durable state and current evidence.
- Lost context or unknown interruption: perform the smallest safe recovery needed for the next action.

Durable state is not one magic file. Relevant evidence may include workspace files, Git, Task State, ExecPlan, project records, plans/specs, verification artifacts, conversation context, and canonical external systems. Reconcile claim by claim.

Absence of Task State does not prove absence of active work.

## Normal result and durable continuity

NORMAL TASK RESULT ≠ DURABLE HANDOFF.

A normal Task result is evidence for Master Review. For short bounded work, one compact response can report the result, verification, not-tested items, deviations, current relevant state, and blockers or decisions. Completing a Task does not require a durable Handoff artifact.

Task State is continuing durable work state. A Checkpoint durably preserves unfinished work when the logical task continues but the current Task Session may end. A Handoff is a durable completed cross-role result used only when a real durability or continuity boundary requires it, such as session or environment transfer, interruption-prone or long-running work, expensive-to-reconstruct context, or another genuine durability need.

`Task Start → Work → Verify → Convergence → Master Review`

Keep Task State, a Checkpoint, a Handoff, or an ExecPlan only when the task is long, interruption-prone, portable across environments, costly to rediscover, or otherwise needs durable cross-role continuity. Update durable state at meaningful transitions, not after every message.

Before a durable Handoff, refresh shared mutable state, identify drift, separate fresh from historical verification, and report any convergence gap.
