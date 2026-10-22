---
type: moc
status: reviewed
audience: [qa, product-owner, engineering]
---

# Module 01: Testing basics

**Objective:** design the tests of a behaviour that has one right answer, from an expected result someone specified, at the level that can prove it.

This is part 1 of the course, with module 02. It holds for any product, with or without AI. If you already know the basics of testing, you can go straight to [module 03](../03-first-evaluation/run-your-first-evaluation.md): nothing in part 2 depends on part 1 being done, only on what it teaches.

## Notes, in order

| # | Note | Answers |
|:--:|---|---|
| 1 | [A green suite on a bug](a-green-suite-on-a-bug.md) | What a test proves, and where its expected result must come from |
| 2 | [A criterion someone can test](testable-criteria.md) | What makes an acceptance criterion testable, and what to do with one that is not |
| 3 | [From criteria to test cases](from-criteria-to-cases.md) | Nominal path, equivalence classes, boundary values, errors, states, permissions, regression |
| 4 | [The right level for each test](test-levels.md) | Component, integration or system, and what no level proves |

## Exercises

[Judge and rewrite criteria](exercises/judge-and-rewrite-criteria.md) · [One criterion, end to end](exercises/one-criterion-end-to-end.md)

## Mastery criterion

Given an acceptance criterion with a limit in it, you write its cases, each with an expected result **and its source**, the four boundary values, and the lowest level that proves each one; and you leave "to confirm", with its owner, every expected result nobody decided.

If you cannot, reread [note 3](from-criteria-to-cases.md), the worked example and the row nobody decided.

---

Previous: [Prerequisites](../00-orientation/prerequisites.md) · [Course map](../00-orientation/progression.md) · Next: [A green suite on a bug](a-green-suite-on-a-bug.md)
