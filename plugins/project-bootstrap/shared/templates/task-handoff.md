# Task Handoff

Use only when continuity or durability needs a durable completed cross-role result for Master Review. For short work, return the result in the normal response instead of creating this artifact.

Do not label a normal Task response as a Handoff. This template is not a required completion wrapper and does not define a new result artifact type.

```text
HANDOFF

Result:
<goal-level outcome>

Changed resources:
<files, systems, or artifacts>

Verification:
<commands/checks and exact coverage>

Convergence:
<PASS or GAP against accepted requirements, with limitations>

Evidence:
<artifact or revision pointers>

Durable knowledge candidates:
<claims for Master to promote, revise, or reject>

Master request:
<review or decision needed>
```

Omit empty, irrelevant, or inapplicable sections. Report applicable verification and unresolved items honestly as PASS, FAIL, NOT TESTED, OPEN, or BLOCKED. Handoff does not itself promote knowledge, commit, push, merge, or release.
