---
type: procedure
status: reviewed
audience: [qa, engineering]
---

# Testing the evaluation skill itself

The skill also requires tests.

## Mandatory behaviour tests

The skill should:

- activate for a relevant evaluation request;
- locate the intended manifest;
- detect missing mandatory fields;
- refuse to invent thresholds;
- stop before candidate execution when Not Ready;
- run all eligible cases when ready;
- calculate slice results correctly;
- make vetoes override aggregate passes;
- preserve all declared versions in the report;
- avoid including secrets in evidence;
- distinguish evaluation result from human acceptance.

## Example skill acceptance scenario

```gherkin
Scenario: Stop an evaluation when the groundedness threshold is missing
  Given a valid candidate and evaluation dataset are configured
  And groundedness is a mandatory metric
  But no approved groundedness threshold is declared
  When the evaluation skill validates the manifest
  Then the verdict is Not Ready
  And the missing threshold is listed as a blocker
  And the candidate is not executed
```

> **Takeaway:** An evaluation agent must be evaluated like any other product capability.

---

[Course map](../00-orientation/progression.md) · Reference — consult it, do not read it once.
