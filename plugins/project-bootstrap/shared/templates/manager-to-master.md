# Manager → Master Bootstrap

Render a ready-to-copy prompt. Include only established or explicitly open project facts.

Include CURRENT ACCEPTED WORK only when a concrete next work item has already been accepted. If no concrete next work is accepted, omit the entire CURRENT ACCEPTED WORK section; do not invent a Task or fill it with UNKNOWN. This is an optional part of this bootstrap, not a separate handoff format.

Active work records continuity state; it is not a substitute for CURRENT ACCEPTED WORK. Project-level authority defaults do not override narrower restrictions accepted for the current work.

```text
$project-bootstrap-master

PROJECT
Purpose: <accepted purpose>
Participation: <COLLABORATIVE | ESSENTIAL | DELEGATED>

ARCHITECTURE
Accepted: <project-level decisions>
Open: <unresolved decisions that affect coordination>

ENVIRONMENT MAP
<material environments and evidence level>

GIT
Canonical repository: <repository or not applicable>
Strategy and authority: <READ / CHANGE / COMMIT / PUBLISH / INTEGRATE as applicable>

CONTINUITY
Durable project state: <locations or current limitation>
Active work: <known state or UNKNOWN>

CURRENT ACCEPTED WORK
Outcome: <already accepted result to achieve>
Scope: <included work and resources>
Exclusions: <explicitly excluded work and actions>
Authority: <permitted actions, resources, environment, and work-specific restrictions>
Expected result: <report or deliverable and required evidence>

MASTER START
Verify the actual workspace, reconcile mutable claims, and preserve accepted decisions.
If CURRENT ACCEPTED WORK is present, execute or route that accepted work next;
preserve its outcome, scope, exclusions, authority, and expected result.
Work-specific restrictions take precedence over broader project authority defaults.
Workspace findings may adapt the execution method, such as following a renamed resource,
while preserving the accepted outcome. Findings do not automatically expand scope or authority.
A read-only inspection is not permission to fix, edit files, or investigate an unrelated area.
If CURRENT ACCEPTED WORK is absent, verify the workspace and determine the smallest
necessary next work from confirmed project state within existing authority.
If the accepted work cannot proceed or a material scope/authority change is needed,
report the finding and resolve that decision; do not silently choose unrelated work.
Do not repeat the initial Manager interview.
```

Provide the execution-profile recommendation separately from this prompt.
