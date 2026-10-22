---
type: example
status: reviewed
audience: [qa, product-owner, engineering]
---

# Solution: write a defect

Read this only after attempting [the exercise](../write-a-defect.md).

## 1. Three failures

| | In | Why |
|:--:|---|---|
| **K1** | The product | The expected result comes from the routing table, which the ops team owns; the product contradicts it |
| **K2** | The test | The product follows the current contract; the test does not. Fix the test and record why |
| **K3** | The environment | The test never got as far as looking at what ClaimTriage did |

## 2. The defect

> **Title.** Critical travel claim routed to queue-travel instead of queue-A
>
> **Steps.** On the test environment, build 2.3.0-142: as an agent entitled to the travel line, open claim 7731 (travel, urgency `critical`) and read the queue on the triage card.
>
> **Expected.** `queue-A`. Source: routing table, ops runbook, "critical goes to queue-A whatever the product line".
>
> **Observed.** `queue-travel`. Screenshot of the card attached. The same happens for critical liability claims (R-07 in the routing suite).
>
> **Severity.** Critical: an emergency claim waits in an ordinary queue. Priority: to set by the product owner.

| | Your defect | |
|:--:|---|---|
| A | Exact data and build, expected result **with its source**, observed result as seen, severity separate from priority, no guessed fix | ✅ |
| B | All of it, plus "probably the `if` on product line in the routing function" | ⚠️ Remove the guess. If you know the cause, say it to the developer, not in the record |
| C | "Routing is wrong for travel claims, please fix" | ❌ No data, no source: the developer starts by asking you everything you knew |

Once this defect is fixed, CT-02 is rerun on the fixed build: a pass closes the defect, and CT-02 stays in the suite as a regression case.
