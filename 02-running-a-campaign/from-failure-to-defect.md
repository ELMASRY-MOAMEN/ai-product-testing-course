---
type: concept
status: reviewed
audience: [qa, product-owner, engineering]
---

# From a failure to a defect

## A failure is not yet a defect

A failed run says the product and the expected result disagree. It does not yet say **which one is wrong**. Before anyone writes a defect, the failure is **qualified**:

| The problem is in | The evidence | What follows |
|---|---|---|
| **The product** | The expected result comes from a specification someone owns, and the product differs from it | A **defect**, assigned to the team that fixes the product |
| **The test** | The expected result was never specified, or is out of date, or the test checks a detail nobody required | The test is fixed, and the reason recorded |
| **The environment** | Connection refused, missing data, a service not started: the test never reached the product | Fix the environment, rerun, keep both runs |

There is a fourth case, rarer and important: the product does exactly what was specified, and **the specification missed something**. That is not a defect in the code. It is a **gap**, and it goes back to the product owner as a missing requirement, not to a developer as a bug.

## A defect someone can reproduce

A defect report is written for a developer who was not there. They must be able to see the problem without asking you anything. It has:

- **a title** that says what happens, not what you feel: "Critical travel claim routed to queue-travel", not "Routing broken";
- **the steps**, with the exact data: which claim, which product line, which urgency, which build, which environment;
- **the expected result, and its source**: the routing table, version, section;
- **the observed result**, exactly as it appeared, with the screenshot or the log line;
- **the severity**: how bad it is for the people who use the product. **Priority**, how soon it must be fixed, is a separate field, and usually the product owner's call.

It does **not** contain the fix. Guessing at the cause in the report sends the developer in a direction before they have looked.

## Closing it

A defect is closed on **a new run that passes**, on a build that contains the fix. Not on "fixed, trust me", and not on a test that was changed to pass. That run becomes a **regression case**, kept in the suite for good, so that the same defect cannot come back unnoticed.

---

Previous: [Exercise: read a pipeline report](exercises/read-a-pipeline-report.md) · [Course map](../00-orientation/progression.md) · Next: [Exercise: write a defect](exercises/write-a-defect.md)
