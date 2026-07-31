---
type: example
status: reviewed
audience: [qa, product-owner, engineering]
---

# Solution — Classify five behaviours

Read this only after attempting [the exercise](../classify-five-behaviours.md).

## The table

| Behaviour | Nature | Gate | Question 2 | Justification |
|---|---|---|---|---|
| **B1** entitlement | Deterministic | DoD | specified | The entitlement matrix is a documented table. The expected decision is derivable without observing the system. |
| **B2** urgency level | Probabilistic | DoT | annotated | The mapping is learned and written down nowhere. "Correct" per case has to be established by a qualified human. |
| **B3** JSON contract | Deterministic | DoD | specified | Required fields, types and the allowed enum are fixed. Assert them case by case, no threshold. |
| **B4** summary | Probabilistic | DoT | annotated | Several phrasings are acceptable; the reference is a reviewed annotation, not a specification. |
| **B5** queue routing | Deterministic | DoD | specified | A documented decision table, even though its input includes B2's output. |

## 1. The capability's class

**Hybrid.** The rule: the classification is decided per behaviour, and the capability class follows from the behaviours, never the reverse. One probabilistic behaviour makes the capability Hybrid — here there are two.

The acceptance rule that follows is conjunctive: the DoD gate, the DoT gate and UAT where the workflow is user-facing must all hold. Excellent probabilistic quality does not compensate for a failed deterministic control.

## 2. The pair that looks alike

**B2 and B5.** Both produce one value from a small fixed set, and both can be compared exactly to an expected value. Under question 1 alone they are indistinguishable, and classifying them together is the intended trap.

Question 2 separates them:

- **B5** applies a mapping documented in the ops runbook. Given a claim's urgency and product line, you can derive the expected queue from the runbook without running the system. **Specified → DoD.**
- **B2** applies a mapping that was learned. Nobody can derive the expected urgency from a document, because no document contains it; a qualified human must judge each case. **Annotated → DoT**, with a reference set, an accuracy metric, an approved threshold, and slices on the categories where being wrong costs most.

It is not the number of possible values that decides, and it is not the technology. It is whether the correct answer was **specified or annotated**.

### The subtlety in B5

B5 consumes B2's output, so its results are only as good as B2's. That does not change B5's classification: the DoD test for B5 supplies the urgency as a **controlled input** and asserts the queue. Testing B5 with whatever B2 happened to produce measures both at once and tells you which one failed — never.

Separating them is the point of classifying per behaviour.

## 3. "The summary must be accurate"

That sentence is not an acceptance criterion, and turning it into one is not your decision.

**What you do:** record it as an unresolved requirement, and go back with the questions that make it testable — accurate about *what*, specifically? Which facts must always survive into the summary? Which claim, if fabricated, would be unacceptable regardless of the rest?

What you get back becomes a metric plus a threshold plus, most likely, a veto. What you must **not** do is pick a metric and a plausible threshold yourself so the design looks finished. Until the answers exist, the correct status for B4 is `Not Ready`, and the blocker names the missing decision and its owner — the product owner for the metric, Compliance if a veto is involved.

Answering this with "I would write a groundedness metric at 0.9" is the failure this course exists to prevent.

## 4. The 0.9999 threshold proposal

Refuse it, and say why in one move:

> Choosing DoT means accepting a non-zero error rate — that is what a threshold **is**. If Compliance will not accept a single entitlement error, then this is not a DoT behaviour with a very high threshold. It is a behaviour whose mapping must be specified so it can be asserted.

And it already is specified: B1 has a documented entitlement matrix. It belongs behind DoD, where every case is asserted exactly and one failure is one failure — not behind a gate that treats one unauthorised disclosure as a rounding error against 9,999 correct decisions.

The related point: an entitlement failure elsewhere in the product is exactly the kind of thing a **veto** exists for. Thresholds express degree; vetoes express kind.

## What to check in your own answer

| | |
|---|---|
| ☐ | You classified **per behaviour**, not "the product is AI so it is DoT" |
| ☐ | You got **B5 deterministic** — the routing table is specified |
| ☐ | You justified with question 2, not with the technology used |
| ☐ | On Q3 you **refused to invent** a metric or threshold and named the owner |
| ☐ | On Q4 you named the actual argument: a threshold is an accepted error rate |

Three or fewer ticks: reread [One product can contain three types of behaviour](../../output-classification.md) before module 03.
