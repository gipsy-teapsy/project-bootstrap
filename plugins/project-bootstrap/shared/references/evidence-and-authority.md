# Evidence and Authority

## Evidence strength

Use these levels without rhetorical upgrades:

- CONFIRMED — accepted or directly established within its scope.
- OBSERVED — directly seen at a specific time/environment.
- STRONGLY SUPPORTED — multiple consistent signals, not direct proof.
- INFERRED — reasoned from evidence.
- UNKNOWN — insufficient evidence.

Promotion into durable knowledge does not increase evidence strength.

## Knowledge lifecycle

`CANDIDATE → PROMOTE / RECONCILE / REVISE / CONSOLIDATE / RETIRE`

Use AUDIT and NO CHANGE where appropriate. A Task Branch proposes; Master governs project-wide knowledge. Decisions may be confirmed, tentative, superseded, or open.

Authority is claim-specific. Git is authoritative for Git objects and history; a live observation describes one environment at one time; accepted records define intent or policy within their scope. Reconcile the exact claim by scope, version, environment, freshness, and source authority.

## Action authority

Keep permission levels separate:

- READ — inspect within the permitted scope.
- CHANGE — modify approved resources.
- COMMIT — create local Git commits.
- PUBLISH — push or publish remote state.
- INTEGRATE — merge or otherwise change shared history.

Authority is action × resource × environment × constraints. Tool availability is not permission. Participation controls user involvement, not authority or risk.

Never persist credentials, private keys, tokens, authenticated URLs, or secrets in project state, prompts, templates, logs, or Git.
