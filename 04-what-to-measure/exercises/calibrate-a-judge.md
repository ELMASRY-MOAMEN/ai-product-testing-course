---
type: example
status: reviewed
audience: [qa, data-ai, compliance]
---

# Exercise — Calibrate a judge

**Time:** 25 minutes. **Do it before opening [the solution](solutions/calibrate-a-judge.md).**

Bring a calculator. This is the one exercise in the course with arithmetic in it, and the arithmetic is the easy part.

## The situation

*AdvisorBrief* generates a pre-meeting briefing for a wealth-management adviser, from the client's record and recent interactions. You will design its evidence in module 05. The team has built an LLM judge to score whether a briefing is **grounded** — every claim in it supported by the client record. The judge returns `accept` or `reject`.

Before using it, they ran it against **30 cases a senior adviser had already labelled by hand**. Here is the comparison.

**Overall, all 30 cases:**

| | Human: accept | Human: reject |
|---|:--:|:--:|
| **Judge: accept** | 20 | 3 |
| **Judge: reject** | 0 | 7 |

**The same 30 cases, restricted to the 6 that contain a fabricated client statement** — the failure mode the veto exists for:

| | Human: accept | Human: reject |
|---|:--:|:--:|
| **Judge: accept** | 0 | 3 |
| **Judge: reject** | 0 | 3 |

The team's summary: *"90% agreement with our senior adviser. Good enough — let's wire it up to the groundedness metric and the fabrication veto."*

## What to produce

**1. The numbers.**

- **a.** Overall agreement. Confirm or correct the 90%.
- **b.** Of the cases the human rejected, what fraction did the judge also reject? Of the cases the judge rejected, what fraction did the human also reject?
- **c.** The same two figures **within the fabrication subgroup**.
- **d.** One of the four cells in the overall table is empty. Which, and what would it have meant if it were not?

**2. The reading.** In three sentences a product owner would accept: what does this calibration actually show about the judge?

**3. The decision.** The team wants to use this judge for two things — the groundedness **metric** and the fabrication **veto**. Answer each separately, with a reason. If your answer differs between the two, say what makes them different.

**4. What is missing.** The calibration itself has gaps. Name at least three things you would require before this judge scores anything that reaches a decision owner — and for each, say who owns it.

**5. The sentence you send.** The judge's author is a capable engineer who has spent two weeks on this and believes the 90% settles it. Write what you actually send them.

## Check your arithmetic before you open the solution

Part 1 is four numbers, and numbers can be checked without your help:

```bash
python tools/check_answer.py calibrate agreement=90 reject_recall=70 reject_precision=100 fabrication_recall=50
```

Substitute your own figures. If one is wrong it names the cells it comes from, not the value it should be. Parts 2 to 5 are judgement and stay yours.

## Constraints

- You do not own the answer to *what agreement rate is sufficient*. If you find yourself picking a number, stop and name the role that picks it instead.
- Thirty cases is a population. Before concluding anything from a subgroup of six, re-read [how many cases is enough](../../05-designing-evidence/how-many-cases-is-enough.md).

---

Previous: [AI-as-a-judge: useful, but not an oracle](../ai-judge-calibration.md) · [Course map](../../00-orientation/progression.md) · Next: [Module 05 — Designing the evidence](../../05-designing-evidence/README.md)
