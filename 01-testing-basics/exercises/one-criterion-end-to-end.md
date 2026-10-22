---
type: example
status: reviewed
audience: [qa, product-owner, engineering]
---

# Exercise: one criterion, end to end

**Time:** 30 minutes. **Do it before opening [the solution](solutions/one-criterion-end-to-end.md).**

## The rule

The product owner has decided it, and the decision is in the backlog:

> **Description length.** Given an agent pastes a claim description, when they submit it, then ClaimTriage accepts it if it has **from 20 to 2,000 characters, both included**. Otherwise ClaimTriage rejects it with the error `DESC_LENGTH`, shows the agent the accepted range, and sends nothing to the model.

## 1. The boundaries

Five figures: the shortest description that must be accepted, the length just below it, the longest that must be accepted, the length just above it, and the number of equivalence classes for the length. Then check them:

```bash
python tools/check_answer.py boundaries lowest_accepted=0 below=0 highest_accepted=0 above=0 classes=0
```

## 2. The levels

At which level is each of these six behaviours proven: `component`, `integration`, `system`, or `ai` (an AI evaluation, part 2 of this course)?

| | Behaviour |
|:--:|---|
| **L1** | The routing function returns `queue-A` for every critical claim |
| **L2** | The card sent matches the claims system's published schema |
| **L3** | An agent without the motor entitlement, signed in through single sign-on, cannot open a motor claim |
| **L4** | The description rule rejects 19 characters and accepts 20 |
| **L5** | When the claims system is down, the card is resent later and never lost |
| **L6** | The two-sentence summary keeps the facts the queue owner needs |

```bash
python tools/check_answer.py levels L1=component L2=component L3=component L4=component L5=component L6=component
```

## 3. The cases

List the test cases for the length rule. For each: what is typed, the expected result, the technique it comes from, and its level. Then name at least one question the rule does not answer, and who answers it.

---

Previous: [The right level for each test](../test-levels.md) · [Course map](../../00-orientation/progression.md) · Next: [Module 02: Running a campaign](../../02-running-a-campaign/README.md)
