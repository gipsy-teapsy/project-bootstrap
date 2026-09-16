# Execution Profiles

Recommend the lowest sufficient current profile for a new Master or Task Session.

Consider complexity, ambiguity, reconciliation load, error cost, and verification difficulty. Participation does not determine model strength.

- Mechanical, bounded, easy to verify: fast or balanced capability; low-to-medium thinking.
- Normal implementation from accepted requirements: capable balanced model; medium thinking.
- Architecture, recovery, conflicting evidence, migration/security, difficult debugging, or independent final review: strongest suitable model; high thinking.
- Exceptional high-cost error case: strongest available suitable model and the highest practical thinking level.

Name a concrete model only when current availability is known. Otherwise use a capability class. Do not freeze one product model name into durable policy.

Place launch guidance outside the durable Task Delta:

```text
Recommended execution profile:
Model: <current model or capability class>
Thinking: <appropriate level>
Reason: <one concise task-specific reason>
```

Escalate when the task materially grows in ambiguity, conflict, risk, or debugging difficulty.
