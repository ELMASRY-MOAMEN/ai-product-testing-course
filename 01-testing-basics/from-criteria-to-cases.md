---
type: concept
status: reviewed
audience: [qa, product-owner, engineering]
---

# From criteria to test cases

## One criterion, several cases

A criterion says what must hold. A test case checks it in one precise situation. One criterion almost always needs several cases, because a product rarely breaks on the obvious path: it breaks on the edge, on the empty field, on the second click.

Seven techniques, in the order to apply them:

| Technique | Gives you | ClaimTriage example |
|---|---|---|
| **Nominal path** | One case per distinct valid outcome | An entitled agent opens a motor claim and gets its card |
| **Equivalence classes** | One case per group of inputs the rule treats the same way | Entitled role, non-entitled role |
| **Boundary values** | Cases on every limit and on the first value either side of it | 19, 20, 2,000 and 2,001 characters |
| **Errors and failing dependencies** | One case per rejection, and per failure of something the product relies on | The entitlement service does not answer |
| **States and sequences** | Cases for the transitions that matter | Opening the same claim twice; opening it after it was closed |
| **Permissions** | One case per role that must be allowed or refused | Front-office, supervisor, auditor |
| **Regression** | One case per defect fixed | R-06, the critical travel claim, kept forever |

**Equivalence classes** are about economy: if the rule treats every entitled role the same way, one entitled role is enough. **Boundary values** are about where bugs live: a developer who writes `<` instead of `<=` produces a product that is right everywhere except exactly on the limit. A limit tested only in the middle is a limit not tested.

## Worked example: the entitlement rule

Criterion: *an agent whose role is not entitled to a claim's product line gets `ENTITLEMENT_DENIED` and no card. The entitlement matrix is maintained by Compliance.*

| Case | Technique | Expected result | Source |
|---|---|---|---|
| Front-office, entitled to motor, opens a motor claim | Nominal | The card is returned | Entitlement matrix |
| Front-office, not entitled to motor, opens a motor claim | Equivalence class: not entitled | `ENTITLEMENT_DENIED`, no card | Entitlement matrix |
| Supervisor, entitled to every line, opens a liability claim | Permissions | The card is returned | Entitlement matrix |
| The entitlement service does not answer | Failing dependency | ‹to confirm with the engineering lead›: refuse, or let through? | Not written anywhere |
| An agent loses the motor entitlement, then opens a motor claim in the same session | State | `ENTITLEMENT_DENIED`, no card | Entitlement matrix |

Look at the fourth row. Nobody has decided what ClaimTriage must do when the entitlement service is down: the matrix says who may see what, not what happens when it cannot be read. The case is written, and its expected result stays to confirm, with its owner. **Writing "refuse" because it seems safer would be inventing a specification.** It may well be the right answer; it is not yours to give.

Each case also names the **source** of its expected result. That column is what makes a review possible: anyone can check the case against the matrix without asking you.

## Check yourself

### Why does the case "the entitlement service does not answer" matter more than a third nominal case would?

<details>
<summary>Answer</summary>

Because it is where the product's behaviour is **not decided**. A third nominal case would test the matrix again on a path that already works. The failing dependency asks a question nobody answered: in production, the day the service is down, ClaimTriage will do something, and today nobody knows whether it lets every agent see every claim. Finding that question is worth more than any number of passing cases.

| | | |
|:--:|---|---|
| A | It tests an undecided behaviour, and the answer could be a disclosure of claims to people not entitled to them | ✅ |
| B | "Error cases find more bugs" | ⚠️ Often true, and it misses the point: here the expected result itself is missing |
| C | "It does not matter much, the service is reliable" | ❌ Reliability is exactly what nobody has tested |
</details>

The next note answers the question this table skipped: at which level does each of these cases run?

---

Previous: [Exercise: judge and rewrite criteria](exercises/judge-and-rewrite-criteria.md) · [Course map](../00-orientation/progression.md) · Next: [The right level for each test](test-levels.md)
