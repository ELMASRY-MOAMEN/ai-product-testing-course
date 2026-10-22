---
type: concept
status: reviewed
audience: [qa, product-owner, engineering]
---

# The frame of a campaign

## Why a frame first

A **campaign** is one round of testing on one version of the product: for a sprint, a release, a recette. Its results only mean something against what it set out to test. "Eighty per cent of the tests pass" says nothing until you know eighty per cent of what, and what was left out.

So the frame is written **before** the first run, and it has five parts.

## 1. The scope, in and out

What the campaign tests, at which level, and whether a person or a report proves it. And just as visibly, **what it does not test, with the reason**. An item out of scope is a limit of every report the campaign will produce. Hidden, it becomes a lie by omission.

## 2. The requirements

Each requirement has an **importance**, set by the product owner, and the case that tests it inherits it. Some requirements **cannot be tested** in this campaign: a response time under load, with no load environment. They are not dropped. They are listed as not testable, with the reason, and they stay in every report.

## 3. The cases, and their status

A case goes from *draft* to *to approve* to *approved*. Only approved cases are run. Approval is a person's decision that the case tests the right thing with the right expected result: it is the moment the "to confirm" from [module 01](../01-testing-basics/testable-criteria.md) must have been answered.

## 4. The entry and exit criteria

Each level has a criterion to start and a criterion to finish, written before testing:

| Level | May start when | Is finished when |
|---|---|---|
| Component | The code builds; the criteria and the cases exist | Every component test passes; every new rule has a test; no test skipped without a reason |
| Integration | Component is finished; the other side is available at a known version | Every integration test passes against those versions |
| System | Integration is finished; the product is deployed at a known build, with its test data | Every testable requirement has a passing test; no open defect of the blocking severity |

An exit criterion is an **approved** value. "Ninety per cent of cases passing" is a decision, and if nobody has taken it, it stays to confirm, like any other.

## 5. The campaign

The approved cases it will run, on which build, in which environment. One campaign per round: the next sprint is a new campaign.

## ClaimTriage, CAMP-03

The frame used in the rest of this module and its exercises:

| Requirement | Importance |
|---|---|
| **EX-01** Routing follows the routing table | Very high |
| **EX-02** An agent without the entitlement gets `ENTITLEMENT_DENIED` and no card | Very high |
| **EX-03** The card carries its four required fields | High |
| **EX-04** A description is accepted from 20 to 2,000 characters | High |
| **EX-05** A card is never lost when the claims system is down | High |
| **EX-06** Every refusal is written to the audit log | Medium |
| **EX-07** The card in under 3 seconds for 95% of requests, under load | Not testable: no load environment |

**Out of scope:** the quality of the generated summary (an AI evaluation, part 2 of this course), and accessibility (a dedicated audit is planned next quarter).

**Planned:** ten approved cases, CT-01 to CT-10, on build 2.3.0-142.

## Check yourself

### At the end of CAMP-03, a manager asks for "the percentage of passing tests" to put in a slide. Which parts of the frame must appear next to that number, and why?

<details>
<summary>Answer</summary>

At least: **EX-07, not testable** (response time was never measured), **the out-of-scope items** (summary quality and accessibility were not tested at all), and **the requirements with no case**, if any. Without them, the slide says "the product passes X%" when it should say "of what we could and chose to test, X% passes".

A percentage alone invites the reader to fill the gaps with the best assumption. The frame is what stops them.

| | | |
|:--:|---|---|
| A | The not-testable requirement and the out-of-scope items, because the number is only true of what was tested | ✅ |
| B | "The number of cases behind the percentage" | ⚠️ Useful, and still silent about what no case covers |
| C | Nothing, the percentage is what was asked | ❌ The slide will be read as a verdict on the whole product |
</details>

---

Previous: [Module 02: Running a campaign](README.md) · [Course map](../00-orientation/progression.md) · Next: [Run, and read the results](run-and-read-results.md)
