---
type: concept
status: reviewed
audience: [qa, data-ai]
---

# Does the metric measure the thing

You have picked the simplest valid evaluator for the requirement. One question remains, and it is the one nobody asks until the results are in dispute:

> **Does this metric actually measure the property you care about, or something correlated with it?**

A metric that measures the wrong thing does not announce itself. It produces numbers in the right range, moves when the candidate changes, and survives every review — because reviewing a number tells you nothing about what it counts.

## A concrete failure

`required_facts_recall`, the evaluator you have run several times in this course, works by checking whether each annotated required fact appears in the output.

Consider a chart-description capability. The annotator writes the required fact as `"upward trend"`. The candidate produces *"revenue has risen every quarter since 2021"*.

**The fact is present. The metric scores it missing.** What the evaluator measures is not whether the output conveys the required information; it is whether the output reuses the annotator's wording. For meeting minutes, where business terms are standard, those two things travel together closely enough to be useful. For descriptive prose they come apart, and the metric quietly becomes a vocabulary-overlap score.

## Two directions, and the second is worse

| | What happens | Cost |
|---|---|---|
| **False alarm** | A correct output is scored wrong | Visible. Someone investigates, finds the output was fine, and trust in the metric drops |
| **Blind spot** | A wrong output is scored right | **Invisible.** Nobody investigates a passing case |

You have already met a blind spot. In [module 03](../03-first-evaluation/what-just-happened.md), case `MR-020` scored **1.000 on recall** while asserting an approval that was never given. Recall measures what is present that should be; it is structurally incapable of seeing what is present that should not be. That is not a bug in the evaluator — it is the boundary of what it measures, and the reason the design needed a second evaluator and a veto.

**Every metric has such a boundary.** The work is knowing where yours is before someone finds it for you.

## How to check, in an afternoon

Calibration is usually discussed for [AI judges](ai-judge-calibration.md). It applies to *every* evaluator, including deterministic ones:

1. Take **10 to 20 cases**, deliberately including the awkward ones — near misses, paraphrases, partially correct outputs.
2. Have a qualified human score them **against the requirement**, not against the metric's definition.
3. Run the evaluator on the same cases.
4. **Look at every disagreement individually.**

A disagreement is not noise to be averaged away. It is one of two things, and both are findings:

- the **metric** is wrong about this case — its boundary is closer than you thought;
- the **requirement** is ambiguous, and two competent people would score it differently. That is a defect in the requirement, and it was going to surface eventually as a dispute about a release.

## What to do when the metric does not fit

In rough order of preference, because each step costs more and explains less:

| Option | When |
|---|---|
| **Sharpen what is annotated** — ask for the fact *and* its acceptable expressions | The requirement is clear and only the surface form varies |
| **Add a second evaluator for the other direction** | The metric is sound but blind, as recall is to fabrication |
| **Use a rubric with human scoring** on a smaller set | The judgement is genuinely expert and low-volume |
| **Use a calibrated AI judge** | The judgement is semantic and the volume makes humans impossible — and only under [the controls](ai-judge-calibration.md) |

What is not on the list: keeping the metric and hoping. A number you have never checked against human judgement is not a measurement, it is a habit.

## Where this lands in your deliverable

The DoT component *Metric* asks how quality is calculated. Answering it fully means stating **what the metric cannot see**, next to how it is computed. A design that names its own blind spot is stronger than one that appears not to have any — and the second kind does not exist.

> **Takeaway:** Choosing a metric is half the job. Knowing what it is blind to, and saying so in the design, is the other half.

---

Previous: [What exactly should we evaluate](evaluators-and-metrics.md) · [Course map](../00-orientation/progression.md) · Next: [AI-as-a-judge: useful, but not an oracle](ai-judge-calibration.md)
