---
type: moc
status: reviewed
audience: [qa, product-owner, engineering]
---

# Module 04 — Foundations

**Objective:** classify any observable behaviour, and know which gate it belongs behind.

Everything downstream depends on this. A behaviour put behind the wrong gate produces evidence that looks complete and proves the wrong thing.

## Notes, in order

| # | Note | Answers |
|:--:|---|---|
| 9 | [Why AI products need a different testing approach](testing-foundations.md) | Why exact-match assertions stop working |
| 10 | [One product can contain three types of behaviour](output-classification.md) | How to classify — **two** questions, not one |
| 11 | [The Hybrid validation model](dod-dot-hybrid.md) | How the gates combine, and what the acceptance rule is |

## Exercise

[Classify five behaviours](exercises/classify-five-behaviours.md) — then compare with [the solution](exercises/solutions/classify-five-behaviours.md).

## Read alongside

[Worked example 04 — Hybrid agent](../worked-examples/04-hybrid-agent/README.md). It decomposes one capability into deterministic and probabilistic behaviours, which is exactly what the exercise asks you to do.

Read [why you must never copy one of these](../worked-examples/READ-ME-BEFORE-COPYING.md) before you open your first example. It takes two minutes and it prevents the most common way to fail the capstone.

## Mastery criterion

Given five behaviours drawn from a real product, you classify each one and **justify it with question 2** — is the correct output specified, or did somebody have to annotate it? — getting the two genuinely ambiguous ones right.

If you cannot, reread [note 10](output-classification.md), specifically *Two questions, not one* and *Why classification appears in the probabilistic row*.

---

Previous: [What just happened](../03-first-evaluation/what-just-happened.md) · [Course map](../00-orientation/progression.md) · Next: [Why AI products need a different testing approach](testing-foundations.md)
