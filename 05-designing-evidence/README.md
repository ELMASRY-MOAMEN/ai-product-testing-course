---
type: moc
status: reviewed
audience: [qa, product-owner, data-ai, compliance]
---

# Module 05 — Designing the evidence

**Objective:** turn a business requirement into evidence that can be executed, and design acceptance so that a good average cannot hide a critical failure.

This is where the craft is. Four notes and two substantial exercises — take it in two sittings, and do not start the golden-set exercise tired.

## Notes, in order

| # | Note | Answers |
|:--:|---|---|
| 9 | [From a business requirement to executable evidence](requirement-to-evidence.md) | A worked example, end to end |
| 10 | [Building a Golden Dataset](golden-datasets.md) | What a governed evaluation set contains, and how it lives |
| 11 | [Protecting evaluation data](data-protection.md) | Which decisions must be taken before the data exists, and who owns them |
| 12 | [Thresholds, slices and vetoes](thresholds-slices-vetoes.md) | How acceptance is decided, and what overrides an average |
| 13 | [How many cases is enough](how-many-cases-is-enough.md) | What a slice population lets you conclude, and what it does not |

## Exercises

| After note | Exercise | |
|:--:|---|---|
| 12 | [Write a veto an average hides](exercises/write-a-veto-an-average-hides.md) | [solution](exercises/solutions/write-a-veto-an-average-hides.md) |
| 13 | [Build a golden set](exercises/build-a-golden-set.md) — allow a half day | [solution](exercises/solutions/build-a-golden-set.md) |

## Read alongside

[Worked example 02 — LLM summary](../worked-examples/02-llm-summary/README.md), the one you ran in module 01, now readable as a complete DoT design — and its [report](../worked-examples/02-llm-summary/expected-report.md), which is the artefact a decision owner actually receives.

## Mastery criteria

1. Given a set of observed failures, you sort them into **degree** (threshold), **subgroup** (slice) and **kind** (veto) — and you can say what each instrument cannot see.
2. Asked "how many cases is enough?", you compute the floor from the failure rate the owner calls unacceptable — and you know which questions to hand to a statistician instead of answering.
3. You can specify a golden set — eligibility, slices, annotation status, handling — **without producing a single reference answer yourself**.

The last one has a trap built into it. Writing reference answers feels like doing the work; it is taking a decision that belongs to a business expert.

---

Previous: [Exercise — Calibrate a judge](../04-what-to-measure/exercises/calibrate-a-judge.md) · [Course map](../00-orientation/progression.md) · Next: [From a business requirement to executable evidence](requirement-to-evidence.md)
