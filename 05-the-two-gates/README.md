---
type: moc
status: reviewed
audience: [qa, product-owner, engineering, data-ai]
---

# Module 05 — The two gates

**Objective:** know what each gate proves, what it refuses to conclude, and when an evaluation is not allowed to start.

## Notes, in order

| # | Note | Answers |
|:--:|---|---|
| 12 | [DoD: testing deterministic behaviour](definition-of-done.md) | What belongs in a Definition of Done, and how its gate runs |
| 13 | [DoT: evaluating probabilistic quality](definition-of-trustworthy.md) | What a Definition of Trustworthy proves, and its ten mandatory components |

## Exercises

One per gate, and the pair is the point — the same capability, two kinds of evidence, two kinds of verdict.

| After note | Exercise | |
|:--:|---|---|
| 12 | [Run a DoD gate](exercises/run-a-dod-gate.md) — you will run this one | [solution](exercises/solutions/run-a-dod-gate.md) |
| 13 | [Score a DoT against its ten components](exercises/score-a-dot-against-its-ten-components.md) | [solution](exercises/solutions/score-a-dot-against-its-ten-components.md) |

## Read alongside

[Worked example 01 — Deterministic API](../worked-examples/01-deterministic-api/README.md) for the DoD gate, then [worked example 02 — LLM summary](../worked-examples/02-llm-summary/README.md), the one you ran in module 03, now readable as a complete DoT.

Both notes show Gherkin scenarios. The rules for writing them are in the toolkit — [scenario-writing rules](../toolkit/gherkin-and-test-contracts.md) — and you will want them for the capstone.

## Mastery criteria

1. You can build and run a **DoD gate** with no threshold in it, and say why `thresholds: {}` is the finished answer rather than an unfinished one.
2. Handed a real DoT design, you identify which of the ten mandatory components are missing and conclude **`Not Ready`** — without proposing values for them.

The tempting error in the second is to notice the gap and immediately fill it, because a design with a hole feels unfinished. Naming the hole and its owner *is* the finished deliverable.

---

Previous: [Exercise — Classify five behaviours](../04-foundations/exercises/classify-five-behaviours.md) · [Course map](../00-orientation/progression.md) · Next: [DoD: testing deterministic behaviour](definition-of-done.md)
