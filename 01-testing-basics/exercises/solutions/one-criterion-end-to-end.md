---
type: example
status: reviewed
audience: [qa, product-owner, engineering]
---

# Solution: one criterion, end to end

Read this only after attempting [the exercise](../one-criterion-end-to-end.md).

## 1. The boundaries

| | Figure | Why |
|---|:--:|---|
| Shortest accepted | 20 | The lower bound is included |
| Just below | 19 | The first value past the lower limit |
| Longest accepted | 2,000 | The upper bound is included |
| Just above | 2,001 | The first value past the upper limit |
| Equivalence classes | 3 | Too short, valid, too long: three different treatments |

A limit is tested on the limit and on the first value either side of it. A developer who writes `<` instead of `<=` produces a product that is right everywhere except exactly on the limit.

## 2. The levels

| | Level | Why |
|:--:|---|---|
| **L1** | Component | The unit's own logic decides it, with its inputs controlled |
| **L2** | Integration | Two real parts have to agree; the seam is where it breaks |
| **L3** | System | Single sign-on and permissions enforced by the platform only exist once the product is deployed |
| **L4** | Component | Pure validation logic |
| **L5** | Integration | How ClaimTriage and the claims system handle each other's failure, tested on that seam |
| **L6** | AI evaluation | Several outputs are acceptable: no assertion and no level of part 1 proves it |

## 3. The cases

| Case | Technique | Expected result | Level |
|---|---|---|---|
| 300 characters | Nominal, valid class | Accepted, the card is produced | Component |
| 19 characters | Boundary, below | `DESC_LENGTH`, range shown, nothing sent | Component |
| 20 characters | Boundary, on the limit | Accepted | Component |
| 2,000 characters | Boundary, on the limit | Accepted | Component |
| 2,001 characters | Boundary, above | `DESC_LENGTH`, nothing sent | Component |
| Empty description | Error, an extreme of the "too short" class | `DESC_LENGTH`, nothing sent | Component |
| 19 characters through the screen | One system case | The agent sees the error and the accepted range | System |
| Nothing reaches the model on a rejection | Error path, the seam with the model | No call is made to the model | Integration |

**Questions the rule does not answer**, each to confirm with the product owner: do spaces at the start and end count? Are line breaks characters? Is an emoji one character or two? What does the message say exactly? A case that types `"  Burst pipe in kitchen.  "` has two possible expected results until someone decides.

| | Your list | |
|:--:|---|---|
| A | All four boundary values, the empty description, most cases at component level, one or two higher up for what only exists there, and at least one open question with its owner | ✅ |
| B | The boundaries, but every case through the screen | ⚠️ Right cases, wrong level: the rule is the unit's own logic |
| C | Only valid lengths, or only 0, 300 and 5,000 | ❌ No case on a limit: a `<` written instead of `<=` passes all of them |
| D | Expected results you added for the open questions, such as "spaces are not counted" | ❌ Plausible and invented. They stay to confirm |
