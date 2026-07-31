---
type: procedure
status: reviewed
audience: [qa, data-ai]
---

# AI-as-a-judge: useful, but not an oracle

An AI judge can help scale semantic evaluation, but only within a controlled protocol.

## Minimum calibration flow

```mermaid
sequenceDiagram
    actor Experts as Qualified human reviewers
    participant Cases as Calibration cases
    participant Rubric as Versioned rubric
    participant Judge as Candidate AI judge
    participant Review as Disagreement review

    Experts->>Cases: Label representative examples
    Experts->>Rubric: Apply explicit scoring anchors
    Cases->>Judge: Submit the same examples and rubric
    Judge-->>Review: Return scores and evidence
    Experts->>Review: Compare human and judge decisions
    Review->>Rubric: Clarify ambiguous criteria
    Review->>Judge: Re-run calibration on revised version
    Experts->>Rubric: Approve scope and remaining human gates
```

## Governance rules

- version the judge model, prompt and rubric;
- require the judge to return evidence for its decision;
- inspect disagreement categories, not only one agreement score;
- retain human review for cases where the judge is not sufficiently reliable;
- do not use the same unverified judge to define and validate its own truth;
- never treat a fluent explanation as proof of correctness.

> **Takeaway:** An AI judge is another evaluator that must itself be tested, calibrated and versioned.

---

Previous: [How many cases is enough](how-many-cases-is-enough.md) · [Course map](../00-orientation/progression.md) · Next: [Exercise — Calibrate a judge](exercises/calibrate-a-judge.md)
