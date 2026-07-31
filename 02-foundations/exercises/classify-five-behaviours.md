---
type: example
status: reviewed
audience: [qa, product-owner, engineering]
---

# Exercise — Classify five behaviours

**Time:** 25 minutes. **Do it before opening [the solution](solutions/classify-five-behaviours.md).**

## The capability

*ClaimTriage* is an assistant used by an insurer's front-office staff. An agent pastes in a customer's claim description and the assistant returns a triage card.

Behind the card, the product does five things:

| | Behaviour |
|:--:|---|
| **B1** | Rejects the request if the staff member's role is not entitled to the claim's product line. The entitlement matrix is a documented table maintained by Compliance. |
| **B2** | Assigns the claim an **urgency level** — `standard`, `priority` or `critical`. The level is produced by a model trained on three years of past claims. There is no written rule linking a description to a level. |
| **B3** | Returns the triage card as JSON with the fields `claim_id`, `urgency`, `summary`, `recommended_queue`, all required, `urgency` restricted to the three values above. |
| **B4** | Writes a two-sentence **summary** of the claim for the queue owner who picks it up. |
| **B5** | Routes the claim to a queue by applying: *critical claims go to queue A; everything else goes to the queue for the product line, per the routing table in the ops runbook.* |

## What to produce

For each behaviour, a row:

| Behaviour | Nature | Gate | Question 2 answer | One-line justification |
|---|---|---|---|---|

Where **nature** is deterministic or probabilistic, **gate** is DoD or DoT, and **question 2 answer** is either *specified* or *annotated*.

Then answer:

1. **What is the capability's class overall** — DoD-only, DoT-only or Hybrid? State the rule that decides it.
2. **Two of these five look alike and are not.** Which pair, and what separates them?
3. B4 has no acceptance criterion yet. Business tells you: "the summary must be accurate." **What do you do with that sentence?** Do not write the criterion — write what you do.
4. Compliance states that an entitlement error is never acceptable, not even once in ten thousand. Someone proposes handling B1 behind DoT with a threshold of 0.9999. **Answer them.**

## Constraint

You have no thresholds, no dataset and no approvals. You are not expected to invent any. If a question cannot be answered without a decision you do not own, say so and name the role that owns it — that is a correct answer here, not an evasion.
