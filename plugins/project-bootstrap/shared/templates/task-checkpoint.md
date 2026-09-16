# Task Checkpoint

A Checkpoint preserves an unfinished logical task when the current Task Session may end.

```text
CHECKPOINT

Completed:
<durable progress>

Current:
<partial state and any possible mutation>

Next:
<one concrete next action>

Verification:
<fresh checks and known gaps>

Blockers or deviations:
<only material items>
```

This is not a Handoff and does not request Master acceptance.
