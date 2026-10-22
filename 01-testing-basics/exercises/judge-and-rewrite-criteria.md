---
type: example
status: reviewed
audience: [qa, product-owner, engineering]
---

# Exercise: judge and rewrite criteria

**Time:** 15 minutes. **Do it before opening [the solution](solutions/judge-and-rewrite-criteria.md).**

## 1. Four criteria

Here are four acceptance criteria from ClaimTriage's backlog. For each, decide: **testable as written**, or **not testable as written**?

- **AC1.** The triage card is returned in under 3 seconds for 95% of requests, measured on the test environment.
- **AC2.** The summary on the card should be user-friendly.
- **AC3.** Given an agent without the motor entitlement, when they open a motor claim, then they get the error `ENTITLEMENT_DENIED` and no card.
- **AC4.** The routing must be correct.

Check your four answers. The checker says which ones are wrong and which question to re-ask, never the answer:

```bash
python tools/check_answer.py criteria AC1=testable AC2=testable AC3=testable AC4=testable
```

## 2. Rewrite one

This criterion is in the backlog: *"The claim description must be short enough and the triage should be fast."* Rewrite it so it can be tested. You know of no decision about lengths or times.

Write your version down before you open the solution.

---

Previous: [A criterion someone can test](../testable-criteria.md) · [Course map](../../00-orientation/progression.md) · Next: [From criteria to test cases](../from-criteria-to-cases.md)
