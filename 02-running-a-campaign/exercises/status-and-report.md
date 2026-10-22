---
type: example
status: reviewed
audience: [qa, product-owner, engineering]
---

# Exercise: the status, and the report

**Time:** 30 minutes. **Do it before opening [the solution](solutions/status-and-report.md).**

## CAMP-03, on its last day

The frame is the one from [the frame of a campaign](../the-frame-of-a-campaign.md): requirements EX-01 to EX-07, EX-07 not testable, ten planned cases on build 2.3.0-142. Here is where the runs stand:

| Case | Requirement | Verdict | Note |
|---|---|---|---|
| CT-01 | EX-01 routing | Passed | |
| CT-02 | EX-01 routing | Failed | Defect DEF-12, critical: critical travel claims go to `queue-travel` |
| CT-03 | EX-02 entitlement | Blocked | No account without the motor entitlement in the test environment; Sara asked IT on Monday |
| CT-04 | EX-02 entitlement | Not run | |
| CT-05 | EX-03 card fields | Passed | |
| CT-06 | EX-03 card fields | Failed | Defect DEF-13, major: `summary` missing when the description has 2,000 characters |
| CT-07 | EX-04 description length | Passed | |
| CT-08 | EX-04 description length | Not run | |
| CT-09 | EX-05 card never lost | Settled | Resent after 5 minutes instead of 1; accepted in writing by the product owner for this release |
| CT-10 | EX-05 card never lost | Passed | |

EX-06, the audit log, has **no case**: nobody wrote one.

The exit criterion for system testing, approved at the start: *every testable requirement has a passing test, and no open defect of critical severity.*

## 1. The figures

Compute the four figures of CAMP-03, as percentages, with the definitions in [where do we stand?](../where-do-we-stand.md): preparation coverage, execution coverage, progress, quality.

```bash
python tools/check_answer.py figures preparation=0 execution=0 progress=0 quality=0
```

## 2. The status

The product owner asks: "where are we?". Write the status, in a few lines.

## 3. The exit criterion

The release meeting is tomorrow. The exit criterion is not met. Write the message to the product owner.

---

Previous: [Where do we stand?](../where-do-we-stand.md) · [Course map](../../00-orientation/progression.md) · Next: [Run your first evaluation](../../03-first-evaluation/run-your-first-evaluation.md)
