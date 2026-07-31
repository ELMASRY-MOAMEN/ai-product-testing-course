---
type: reference
status: reviewed
audience: [qa, engineering]
---

# Scenario-writing rules

- One scenario has one observable objective.
- `Given` fixes the test context and must not conceal an unverified assumption.
- `When` describes one action or one evaluation run.
- `Then` states a binary outcome for DoD or a measurable population-level outcome for DoT.
- Write positive cases first, then negative, boundary, non-functional and critical-risk cases.
- Trace every scenario to a requirement or identified risk.
- A missing dataset, metric, threshold, evaluator or owner makes a DoT scenario **Not Ready**.
- Use a decision table or input-output table when it is clearer than Gherkin.

---

[Course map](../00-orientation/progression.md) · Reference — consult it, do not read it once.
