---
type: example
status: reviewed
audience: [qa, product-owner, engineering]
---

# Solution: the status, and the report

Read this only after attempting [the exercise](../status-and-report.md).

## 1. The figures

| Figure | Value | How |
|---|:--:|---|
| Preparation coverage | 83% | 5 of the 6 testable requirements have a case: EX-06 has none, and EX-07 is not testable |
| Execution coverage | 67% | 4 of 6: EX-02 has a blocked case and one not run, so none of its cases ran |
| Progress | 70% | 7 of 10 planned cases executed: 4 passed, 2 failed, 1 settled. The blocked case is not executed |
| Quality | 57% | 4 passed out of 7 passed, failed or settled. The settled case counts against quality |

## 2. The status

> **Not done.** EX-02 (entitlement, very high importance) has not been tested at all: CT-03 is blocked on a test account Sara asked IT for on Monday, and CT-04 has not run. CT-08 has not run either. EX-06 (audit log) has no case. EX-07 (response time under load) cannot be tested here.
>
> **Open defects.** DEF-12, critical: critical travel claims go to `queue-travel`. DEF-13, major: the summary is missing at 2,000 characters.
>
> **Accepted deviation.** CT-09: cards are resent after 5 minutes instead of 1, accepted by you for this release.
>
> **Figures.** Progress 70%, quality 57% (4 passed out of 7 executed), execution coverage 67%, preparation coverage 83%.

| | Your status | |
|:--:|---|---|
| A | Starts with what is not done, entitlement first; names both open defects with their severity; the settled case as a deviation; figures last, side by side | ✅ |
| B | All the facts, but it opens on "70% progress, 57% quality" | ⚠️ The reader stops at the first line. Put what they must act on there |
| C | "Good progress, 4 of 7 passing, two bugs being fixed" | ❌ Entitlement, the most important requirement, is not mentioned, and it was never tested |

## 3. The exit criterion

> The system exit criterion is not met, for two reasons:
>
> 1. **EX-02 has no passing test.** It has not been tested at all: CT-03 is blocked on a test account without the motor entitlement, requested from IT on Monday. Until it runs, nobody knows whether an agent can open claims they are not entitled to.
> 2. **DEF-12 is open, at critical severity**: critical travel claims are routed to an ordinary queue.
>
> Also outside the criterion, and to keep in view: EX-06 has no case, and EX-07 cannot be tested here.
>
> The decision is yours: release with these gaps accepted and recorded, or wait for the account and the fix. If you need the account sooner, IT is the one to ask.

| | Your message | |
|:--:|---|---|
| A | Says the criterion is not met, gives each reason with its evidence, and leaves the decision explicitly to the product owner | ✅ |
| B | All of it, plus "I recommend a No Go" | ⚠️ You may be asked for your view, and you can give it. Keep it apart from the facts, and do not let it read as the decision |
| C | "Testing is 70% complete, the remaining risk is low" | ❌ An untested entitlement control is not low risk: nobody knows. And "low" is a judgement you were not asked to make for them |
| D | Lowers the criterion to "no open blocking defect except DEF-12" | ❌ Changing the criterion to meet it is the one thing the person running the tests may never do |

That is part 1. Part 2 takes the behaviours no assertion can test, like ClaimTriage's summary, with the same discipline: evidence first, and decisions left to the people who own them.
