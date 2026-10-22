---
type: concept
status: reviewed
audience: [qa, product-owner, engineering]
---

# The right level for each test

## Three levels

| Level | Proves | What the test touches |
|---|---|---|
| **Component** (unit) | One unit's logic: a calculation, a validation, a mapping | A function or a module, in memory, everything around it replaced |
| **Integration** | Two real parts agree: ClaimTriage and the claims system, the code and its database | The seam between two named parts |
| **System** | The assembled product meets the criterion end to end | The deployed product, through its real screen, API or sign-in |

**The rule: test each behaviour at the lowest level that can prove it.** Going higher only when the behaviour does not exist lower down.

A component test runs in a few milliseconds and tells the developer exactly which function is wrong. A system test takes seconds or minutes, needs an environment and data, and when it fails, the cause can be anywhere. Testing the routing table through the screen proves nothing a component test would not, ten thousand times slower.

To place a behaviour, ask in this order, and stop at the first yes:

1. Can the unit's code alone decide it, with its inputs controlled? **Component.**
2. Does it depend on how two real parts agree (a schema, a protocol, a failure on one side)? **Integration**, on that seam only.
3. Does it only exist once the product is assembled and deployed (single sign-on, permissions enforced by the platform, a user journey)? **System.**

## What is not a level

**User acceptance testing** is not a fourth level. It is a decision by the business that the product does the job, taken by the people who will use it. It comes on top of the three levels, not instead of one.

**Some behaviours no level proves.** ClaimTriage's two-sentence summary has many acceptable phrasings: no assertion can compare it with one expected sentence. That is the subject of part 2 of this course, from [module 03](../03-first-evaluation/run-your-first-evaluation.md). Recognising it now matters, because the classic mistake is to test it anyway with an exact comparison, and to fail every good answer that is worded differently.

## Check yourself

### A developer tests the length rule at component level, and the tester adds the same four lengths through the screen "to be sure". What does the second set prove?

<details>
<summary>Answer</summary>

**Nothing new**, at a much higher cost. The rule is the unit's own logic, and the component tests already prove it on all four lengths. Run through the screen, the same lengths prove that the screen calls the rule, which **one** system case shows just as well.

A behaviour tested at two levels must prove two different things there. The same assertion repeated higher up adds slowness, and a second place to maintain.

| | | |
|:--:|---|---|
| A | Nothing new about the rule; one system case is enough to show the screen uses it | ✅ |
| B | "It is safer to test twice" | ⚠️ Safer only if the second test proves something the first one cannot |
| C | "System tests are the real tests" | ❌ They are the slowest and the least precise. They are for what only exists once assembled |
</details>

---

Previous: [From criteria to test cases](from-criteria-to-cases.md) · [Course map](../00-orientation/progression.md) · Next: [Exercise: one criterion, end to end](exercises/one-criterion-end-to-end.md)
