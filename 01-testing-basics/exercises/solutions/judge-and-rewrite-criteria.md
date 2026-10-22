---
type: example
status: reviewed
audience: [qa, product-owner, engineering]
---

# Solution: judge and rewrite criteria

Read this only after attempting [the exercise](../judge-and-rewrite-criteria.md).

## 1. The four criteria

| | Verdict | Why |
|:--:|---|---|
| **AC1** | Testable | An observable outcome, a number, and a place where it is measured. Whether the test environment represents production is a separate question, and a fair one to raise. |
| **AC2** | Not testable | Nothing a tester can observe, and a second tester would not observe the same thing. |
| **AC3** | Testable | A starting situation, an action, an observable outcome. |
| **AC4** | Not testable | "Correct according to what?" The source of the right answer, the routing table, is not named. Naming it makes it testable at once. |

## 2. The rewrite

It holds **two** behaviours, so it becomes two criteria. And since nobody has decided the numbers, they stay to confirm, with their owner:

> **Length.** Given an agent pastes a description shorter than ‹minimum length› or longer than ‹maximum length› characters, when they submit it, then ClaimTriage rejects it with a documented error and nothing is sent to the model. *(Lengths to confirm with the product owner.)*
>
> **Time.** Given a valid description, when the agent submits it, then the triage card is returned within ‹time› seconds for ‹share› of requests, measured on ‹environment›. *(Values to confirm with the product owner; the measuring environment with the test lead.)*

| | You wrote | |
|:--:|---|---|
| A | Two criteria, each with an observable outcome, and the numbers left to confirm with who confirms them | ✅ |
| B | Two criteria with numbers you chose, such as 2,000 characters and 3 seconds | ⚠️ Testable, and invented. Ask before you write a number |
| C | One criterion that still says "fast" or "short enough" | ❌ Two testers would still disagree on the verdict |

The product owner has since decided the lengths: a description is accepted from **20 to 2,000 characters**, both included. You will use that decision in [the last exercise of this module](../one-criterion-end-to-end.md).
