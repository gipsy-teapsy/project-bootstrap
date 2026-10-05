# Master → Task

Render only the task delta that is not already inherited from durable project policy.

In one confirmed current workspace, a stable canonical policy location is sufficient. Add a policy revision or version only when freshness, cross-environment transfer, portability, concurrent revisions, or stale-policy risk makes it materially useful. If the Task cannot access the canonical policy, include only the minimum necessary excerpt. Always include a task-specific deviation when one exists. Do not add an empty policy metadata block when no deviation or freshness risk exists.

```text
$project-bootstrap-task

TASK

Goal:
<bounded outcome>

Scope:
<included resources and explicit exclusions>

Relevant context:
<facts required for this task>

Authority:
<permitted actions, resources, environment, and constraints>

Done when:
<observable completion and evidence>

Expected evidence:
<tests, inspection, artifacts, or original-symptom check>
```

Add constraints, refresh conditions, or continuity requirements only when task-specific. Put the execution-profile recommendation outside the prompt.
