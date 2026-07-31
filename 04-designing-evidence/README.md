---
type: moc
status: reviewed
audience: [qa, product-owner, engineering, data-ai, compliance]
---

# Module 04 — Designing the evidence

**Objective:** turn a business requirement into evidence that can be executed, and design acceptance so that a good average cannot hide a critical failure.

This is the longest module and the one that carries the craft. Take it in two sittings.

## Notes, in order

| # | Note | Answers |
|:--:|---|---|
| 6 | [What exactly should we evaluate](evaluators-and-metrics.md) | Which evaluation families exist, and how to pick the simplest valid evaluator |
| 7 | [From a business requirement to executable evidence](requirement-to-evidence.md) | A worked example, end to end |
| 8 | [Building a Golden Dataset](golden-datasets.md) | What a governed evaluation set contains, and how it lives |
| 9 | [Protecting evaluation data](data-protection.md) | Which decisions must be taken before the data exists, and who owns them |
| 10 | [Thresholds, slices and vetoes](thresholds-slices-vetoes.md) | How acceptance is decided, and what overrides an average |
| 11 | [AI-as-a-judge: useful, but not an oracle](ai-judge-calibration.md) | When an LLM may score outputs, and under which controls |

## Exercises

| After note | Exercise | |
|:--:|---|---|
| 10 | [Write a veto an average hides](exercises/write-a-veto-an-average-hides.md) | [solution](exercises/solutions/write-a-veto-an-average-hides.md) |
| 11 | [Build a golden set](exercises/build-a-golden-set.md) | [solution](exercises/solutions/build-a-golden-set.md) |

## Read alongside

[Worked example 03 — RAG assistant](../worked-examples/03-rag-assistant/README.md), for how retrieval quality, groundedness and disclosure vetoes coexist in one design.

## Mastery criteria

1. Given a set of observed failures, you sort them into **degree** (threshold), **subgroup** (slice) and **kind** (veto) — and you can say what each instrument cannot see.
2. You can specify a golden set — eligibility, slices, annotation status, handling — **without producing a single reference answer yourself**.

The second one has a trap built into it. Writing reference answers feels like doing the work; it is taking a decision that belongs to a business expert.

---

Previous: [Exercise — Score a DoT against its ten components](../03-the-two-gates/exercises/score-a-dot-against-its-ten-components.md) · [Course map](../00-orientation/progression.md) · Next: [What exactly should we evaluate](evaluators-and-metrics.md)
