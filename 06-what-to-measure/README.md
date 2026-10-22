---
type: moc
status: reviewed
audience: [qa, data-ai]
---

# Module 06 — What to measure

**Objective:** pick the simplest evaluator that is valid for the requirement, and know what it is blind to before anyone quotes it.

Short module, three notes. It answers one question — *is this number measuring the thing?* — and everything in module 07 assumes you can answer it.

## Notes, in order

| # | Note | Answers |
|:--:|---|---|
| 14 | [What exactly should we evaluate](evaluators-and-metrics.md) | Which evaluation families exist, and how to pick the simplest valid evaluator |
| 15 | [Does the metric measure the thing](does-the-metric-measure-it.md) | Whether your metric measures the property or something correlated with it |
| 16 | [AI-as-a-judge: useful, but not an oracle](ai-judge-calibration.md) | When an LLM may score outputs, and under which controls |

## Exercise

[Calibrate a judge](exercises/calibrate-a-judge.md) — bring a calculator — then compare with [the solution](exercises/solutions/calibrate-a-judge.md).

## Read alongside

[Worked example 03 — RAG assistant](../worked-examples/03-rag-assistant/README.md) and its [report](../worked-examples/03-rag-assistant/expected-report.md), for retrieval quality and groundedness measured side by side.

## Mastery criteria

1. For any metric you propose, you can state **what it is blind to** — and you would not report it without having checked it against human judgement on some cases.
2. Handed a judge's calibration, you can say what it licenses and what it does not, and refuse it behind a veto without refusing it as a metric.

The second is the sharper one. A judge that is right when it fires and unreliable when it stays silent is usable for one job and disqualified from the other, and telling those apart is the skill.

---

Previous: [Exercise — Score a DoT against its ten components](../05-the-two-gates/exercises/score-a-dot-against-its-ten-components.md) · [Course map](../00-orientation/progression.md) · Next: [What exactly should we evaluate](evaluators-and-metrics.md)
