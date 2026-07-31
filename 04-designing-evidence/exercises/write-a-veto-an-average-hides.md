---
type: example
status: reviewed
audience: [qa, product-owner, data-ai, compliance]
---

# Exercise — Write a veto an average hides

**Time:** 35 minutes. **Do it before opening [the solution](solutions/write-a-veto-an-average-hides.md).**

## The capability

*AdvisorBrief* generates a pre-meeting briefing for a wealth-management adviser, from the client's record and the last six months of interactions.

The DoT is already designed around one metric: **required-fact recall** — the proportion of facts flagged as mandatory by the business that appear in the briefing. The approved threshold is 0.90. The dataset has 200 approved cases.

## The pilot results

The run scores **0.94 aggregate recall**. It passes. Then a reviewer reads through the outputs and lists what they found:

| | Observation | Cases |
|:--:|---|:--:|
| **F1** | Briefings omit one mandatory fact each — usually the least recent one | 22 |
| **F2** | For clients flagged `vulnerable`, briefings omit the mandatory suitability warning | 6 of the 11 vulnerable-client cases |
| **F3** | One briefing states *"the client has confirmed their appetite for higher risk"*. No record says this. The client's file says the opposite. | 1 |
| **F4** | One briefing includes the holdings of a **different client** with a similar surname | 1 |
| **F5** | Briefings for non-English interactions are noticeably thinner, though they still contain the mandatory facts | 14 |
| **F6** | Two briefings recommend a specific product, which the assistant was never meant to do | 2 |

## What to produce

**1. Sort every finding** into the instrument that should catch it:

| Finding | Instrument | Why that one | What it would cost to use the wrong one |
|---|---|---|---|

The instruments are **threshold** (degree), **critical slice** (subgroup), and **veto** (kind). One finding may need more than one. At least one needs an instrument that does not exist in the current design at all — say which and why.

**2. Write the acceptance block.** In the manifest shape below, express what you can. Every value that is not yours to decide stays a `<placeholder>`.

```yaml
acceptance:
  thresholds:
    <evaluator-id>: <approved-threshold>
  critical_slices:
    - name: <slice-name>
      evaluator: <evaluator-id>
      minimum: <approved-minimum>
  vetoes:
    - evaluator: <evaluator-id>
      condition: any_triggered
```

For each veto, also state in one line **the condition a deterministic check could test** — a veto you cannot execute is not a veto.

**3. Answer:** the aggregate is 0.94 against a threshold of 0.90, and the run passed. After your redesign, what verdict would the same results produce, and which single finding decides it?

**4. The question that matters most.** F3 and F5 are both quality problems. One is a veto and one is not. Explain the difference in a way a product owner would accept — no jargon, three sentences maximum.

## Constraints

- You do not own the threshold, any slice minimum, or the decision that a condition is unacceptable. Placeholders where a decision is missing; name the owner.
- Every veto must be phrased so that code, not judgement, decides whether it triggered.
