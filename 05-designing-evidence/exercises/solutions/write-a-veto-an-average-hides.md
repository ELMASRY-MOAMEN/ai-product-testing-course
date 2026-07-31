---
type: example
status: reviewed
audience: [qa, product-owner, data-ai, compliance]
---

# Solution — Write a veto an average hides

Read this only after attempting [the exercise](../write-a-veto-an-average-hides.md).

## 1. Sorting the findings

| Finding | Instrument | Why that one | Cost of the wrong instrument |
|---|---|---|---|
| **F1** omitted least-recent fact, 22 cases | **Threshold** | A matter of degree, spread across the population. This is exactly what an aggregate measures, and 0.94 already reflects it. | As a veto: the run never passes and the instrument becomes noise everyone learns to override. |
| **F2** missing suitability warning for vulnerable clients | **Critical slice** + almost certainly a **veto** | 6 failures in 11 cases is a *55% failure rate in the subgroup*, invisible in a 200-case aggregate. And a missing suitability warning for a vulnerable client is a regulatory failure, not a quality shortfall. | Threshold only: the subgroup is 5.5% of the population, so it can fail completely while the aggregate moves by three points. |
| **F3** fabricated risk-appetite confirmation | **Veto** | Not a matter of degree. The briefing asserts a client statement that does not exist and that contradicts the file. Once is unacceptable. | Threshold: one case in 200 moves the aggregate by 0.005. It disappears. |
| **F4** another client's holdings | **Veto**, highest severity | Unauthorised data disclosure. One occurrence is an incident, independent of any score. | Anything else: the run reports `Pass` on a data breach. |
| **F5** thinner briefings in other languages | **Critical slice** | A subgroup performing worse on a quality dimension. Mandatory facts are present, so no rule is broken — but the aggregate hides the gap. | Veto: blocks a release over a quality difference nobody declared unacceptable. |
| **F6** product recommendation | **Veto** — **and an instrument that does not exist here** | Out-of-scope behaviour. See below. | Ignored: the assistant gives investment advice it was never authorised to give. |

### The instrument that is missing from the design

F6 is not a recall problem at all, and **the current design has no evaluator that can see it**. Required-fact recall measures what is *present that should be*; nothing measures what is *present that should not be*.

This is the second evaluator the design needs — a forbidden-content check, deterministic where possible — and F3, F4 and F6 all depend on it. Without it, three of the six findings are unmeasurable and their vetoes cannot be wired to anything.

**A veto is only real if an evaluator produces the signal it fires on.** A veto declared against an evaluator that does not exist is the single most common defect in this material.

## 2. The acceptance block

```yaml
acceptance:
  thresholds:
    required-facts-recall: 0.90            # already approved
    # A second evaluator is needed; its threshold is not a threshold at all —
    # forbidden content is governed by the vetoes below, not by a rate.

  critical_slices:
    - name: vulnerable-client
      evaluator: required-facts-recall
      minimum: <approved-minimum>          # owner: product owner + Compliance
    - name: non-english-interaction
      evaluator: required-facts-recall
      minimum: <approved-minimum>          # owner: product owner
    # Both slices also need a declared minimum population; 11 vulnerable cases
    # in 200 may be too few to conclude from. Owner: product owner + data/AI.
    # If you raised that on your own, good — the next note gives you the
    # arithmetic behind it.

  vetoes:
    - evaluator: unauthorised-disclosure
      condition: any_triggered
    - evaluator: fabricated-client-statement
      condition: any_triggered
    - evaluator: product-recommendation
      condition: any_triggered
    - evaluator: missing-suitability-warning
      condition: any_triggered             # <-- Compliance must confirm this one
                                           # is a veto and not a slice minimum.
```

### The executable condition behind each veto

| Veto | What code tests |
|---|---|
| `unauthorised-disclosure` | The briefing contains an identifier, holding or name belonging to a client other than the case's subject. Checkable against the case's controlled context — no judgement needed. |
| `fabricated-client-statement` | The briefing attributes a statement or confirmation to the client that appears in no source record for that case. Deterministic against the context, with a judged fallback only for phrasing. |
| `product-recommendation` | The briefing names a specific product together with a recommending construction. A forbidden-pattern check, reviewed by Compliance. |
| `missing-suitability-warning` | Case is labelled `vulnerable` **and** the mandatory suitability warning is absent. Pure presence check on a labelled subset. |

Each one is decided by code, not by a reviewer's opinion. A veto that requires a human to interpret it will be interpreted differently under release pressure.

### What stays a placeholder, and who owns it

| Decision | Owner |
|---|---|
| Slice minimums for `vulnerable-client` and `non-english-interaction` | Product owner, with Compliance for the first |
| Whether a missing suitability warning is a veto or a slice gate | **Compliance** — it is a regulatory reading, not a testing choice |
| Minimum population per slice before a slice result may be trusted | Product owner + data/AI |
| Approval that these four conditions are unacceptable | Product owner, on Compliance's advice |

You may write the *conditions*. You may not decide that they are *unacceptable* — that is an acceptance decision.

## 3. The verdict after redesign

**Fail.**

The aggregate is still 0.94 and still clears 0.90. Nothing about the candidate changed. What changed is that acceptance can now see three things it was blind to.

**The single finding that decides it: F4**, the other client's holdings. Even if F2, F3 and F6 were all somehow disputed, one unauthorised disclosure blocks acceptance on its own — and it would have shipped under the original design.

If you answered F3, that is defensible and the reasoning is the same. If you answered F1 or F5, reread [Thresholds, slices and vetoes](../../thresholds-slices-vetoes.md).

## 4. F3 versus F5, for a product owner

> F5 is our briefings being *less good* for some clients — thinner, but everything required is there. That is a quality gap, and quality gaps are measured by degree: we set a bar and check we clear it, for those clients specifically as well as overall.
>
> F3 is our briefing telling an adviser that a client said something the client never said — and the file says the opposite. That is not a worse briefing; it is a false one, and an adviser acting on it exposes the client and us.
>
> The first can be traded off against a deadline. The second cannot happen once, which is why it blocks release regardless of the score.

The distinction to keep: **degree versus kind**. A threshold is an agreed error rate. Some things have no acceptable rate.

## What to check in your own answer

| | |
|---|---|
| ☐ | F1 as a threshold matter — resisting the urge to veto everything |
| ☐ | F2 as **both** a slice and a candidate veto, with the veto question sent to Compliance |
| ☐ | F4 identified as the most severe, and as a veto |
| ☐ | You noticed **no evaluator exists** for F3, F4 and F6 |
| ☐ | Every veto phrased as a condition **code can test** |
| ☐ | Slice minimums left as placeholders with named owners |
| ☐ | Final verdict **Fail**, decided by a single case |

Four or fewer: reread [Thresholds, slices and vetoes](../../thresholds-slices-vetoes.md) and [What exactly should we evaluate](../../../04-what-to-measure/evaluators-and-metrics.md).
