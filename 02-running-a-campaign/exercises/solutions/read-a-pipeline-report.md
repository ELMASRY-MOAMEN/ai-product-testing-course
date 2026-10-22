---
type: example
status: reviewed
audience: [qa, product-owner, engineering]
---

# Solution: read a pipeline report

Read this only after attempting [the exercise](../read-a-pipeline-report.md).

## 1. Six runs

| | Verdict | Why |
|:--:|---|---|
| **V1** | Passed | The case proved what it was written to prove |
| **V2** | Failed | The step ran and differs from the specification |
| **V3** | Blocked | The test could not run; the product did nothing wrong. A blocked case is **not executed** |
| **V4** | Not applicable | The case no longer applies to this release |
| **V5** | Not testable | The case makes sense; the campaign has no means to test it. It stays listed in every report |
| **V6** | Settled | It failed, and someone with authority accepted the deviation. **Never a success** |

## 2. What the summary says

Seventeen tests, thirteen passed: a dashboard would show 76% green, or "1 failure". The summary by level says something else:

- **Component: failed.** One real assertion failure, the critical travel claim routed to `queue-travel`, the bug from [module 01](../../../01-testing-basics/a-green-suite-on-a-bug.md). And one test **skipped**, with "flaky, to look at later" as its only reason.
- **Integration: incomplete.** Two tests crashed with `ConnectionRefusedError` before checking anything: the claims-system stub was not running.
- **System: not tested.** Zero tests. Not "passed": **not tested**. No single sign-on, no permission enforced by the platform, no end-to-end path was checked by this pipeline.

If you wrote down "system" before running the script, you read the report by level. If you expected "all three ran", you read its last line.

## 3. What each problem counts as

| | Counts as | Why |
|:--:|---|---|
| **J1** | Product defect | The expected value comes from the routing table, a specification someone owns, and the product differs from it |
| **J2** | Environment problem | No assertion about ClaimTriage ran: the test never reached the product. Fix the environment, rerun, keep both runs |
| **J3** | A gap to report | It neither passed nor failed, so the report proves nothing about the liability entitlement; and "flaky" is not a reason to skip a test, which counts as failing until it is fixed |
