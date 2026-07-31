---
type: concept
status: reviewed
audience: [product-owner, qa, engineering]
---

# The Hybrid validation model

A Hybrid product is accepted only when every applicable gate passes independently.

```mermaid
flowchart LR
    A[Candidate version] --> B[DoD gate<br/>Deterministic conformance]
    B -->|Pass| C[DoT gate<br/>Probabilistic trust]
    B -->|Fail| X[Reject or correct]
    C -->|Pass| D{User-facing workflow?}
    C -->|Fail or veto| X
    D -->|No| E[Human acceptance decision]
    D -->|Yes| F[UAT gate<br/>Usefulness and control]
    F -->|Accepted| E
    F -->|Rejected| X
```

## Acceptance rule

```text
Hybrid accepted = DoD passed
                  AND DoT passed
                  AND UAT accepted when applicable
```

The results must remain separately visible.

- A high quality score cannot compensate for broken access control.
- A valid schema cannot compensate for unsupported content.
- A technically correct workflow cannot compensate for an unusable user experience.

> **Takeaway:** Never blend all results into one reassuring global score.

---

Previous: [One product can contain three types of behaviour](output-classification.md) · [Course map](../00-orientation/progression.md) · Next: [Exercise — Classify five behaviours](exercises/classify-five-behaviours.md)
