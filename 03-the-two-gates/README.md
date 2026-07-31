---
type: moc
status: reviewed
audience: [qa, product-owner, engineering, data-ai]
---

# Module 03 — The two gates

**Objective:** know what each gate proves, what it refuses to conclude, and when an evaluation is not allowed to start.

## Notes, in order

| # | Note | Answers |
|:--:|---|---|
| 4 | [DoD: testing deterministic behaviour](definition-of-done.md) | What belongs in a Definition of Done, and how its gate runs |
| 5 | [DoT: evaluating probabilistic quality](definition-of-trustworthy.md) | What a Definition of Trustworthy proves, and its ten mandatory components |

## Exercise

[Score a DoT against its ten components](exercises/score-a-dot-against-its-ten-components.md) — then compare with [the solution](exercises/solutions/score-a-dot-against-its-ten-components.md).

## Read alongside

[Worked example 01 — Deterministic API](../worked-examples/01-deterministic-api/README.md) for the DoD gate, then [worked example 02 — LLM summary](../worked-examples/02-llm-summary/README.md), the one you ran in module 01, now readable as a complete DoT.

Both notes show Gherkin scenarios. The rules for writing them are in the toolkit — [scenario-writing rules](../toolkit/gherkin-and-test-contracts.md) — and you will want them for the capstone.

## Mastery criterion

Handed a real DoT design, you identify which of the ten mandatory components are missing and conclude **`Not Ready`** — without proposing values for them.

The tempting error is to notice the gap and immediately fill it, because a design with a hole feels unfinished. Naming the hole and its owner *is* the finished deliverable.

---

Previous: [Exercise — Classify five behaviours](../02-foundations/exercises/classify-five-behaviours.md) · [Course map](../00-orientation/progression.md) · Next: [DoD: testing deterministic behaviour](definition-of-done.md)
