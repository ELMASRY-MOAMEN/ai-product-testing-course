# Requirements — HR agent

The agent answers employee policy questions and can open an HR ticket on the employee's behalf.

## Observable behaviours, classified

| # | Behaviour | Class | Gate |
|:--:|---|---|---|
| R1 | A ticket is created only when the employee requests one | Deterministic | DoD |
| R2 | A created ticket carries the approved category and priority | Deterministic | DoD |
| R3 | Every ticket response returns a non-empty reference | Deterministic | DoD |
| R4 | Answers contain the facts the policy requires | Probabilistic | DoT |
| R5 | Answers state no entitlement the handbook does not support | Probabilistic, veto candidate | DoT |
| R6 | An employee can act on the answer without re-reading the handbook | Human judgement | UAT |

R1 to R3 have exactly one correct outcome each and are asserted. R4 and R5 have many acceptable phrasings and are measured over a population. R6 needs a person.

That decomposition is what makes this capability **Hybrid** — not the presence of a model, and not the fact that it uses tools.

## Acceptance

Acceptance requires the DoD gate and the DoT gate to pass, and UAT when the capability goes user-facing.

The gates are conjunctive. A DoT result of 0.99 does not compensate a failing R1: opening a ticket nobody asked for is not a quality that improves with a better model.

## Out of scope for this example

R6 (UAT) is not evaluated here — the example demonstrates the two automated gates. A real evaluation of a user-facing capability would name a UAT owner and a sampled rubric, or record explicitly why UAT is out of scope.
