# Cloud → Codex Fallback

Use this template only for a bounded transition to an ordinary Codex session where Project Bootstrap Plugin/Skills are not available.

```text
You are working in an ordinary Codex session without the Project Bootstrap Plugin.

USER INTENT
<the accepted user outcome>

WORKSPACE BOUNDARY
<the exact repository, directory, or environment in scope>

BOUNDED GOAL
<one inspection or execution result to produce>

RELEVANT ACCEPTED CONTEXT
<only established decisions needed for this work>

MUTABLE FACTS TO INSPECT
<workspace facts that must be refreshed rather than assumed>

SCOPE AND EXCLUSIONS
<included work and explicit non-goals>

AUTHORITY
<READ / CHANGE / COMMIT / PUBLISH / INTEGRATE permissions that actually apply>

DONE WHEN
<observable completion conditions>

EXPECTED EVIDENCE
<commands, files, tests, or other evidence required>

RETURN TO CLOUD MANAGER
Return a concise evidence-based report with:
- outcome;
- changes, if any;
- verification performed and exact result;
- current mutable state relevant to the next decision;
- blockers, open decisions, and any authority still required.

Keep the work within this bounded request. Do not recreate Project Bootstrap roles or add workflow artifacts unless the work itself genuinely requires durable continuity.
```
