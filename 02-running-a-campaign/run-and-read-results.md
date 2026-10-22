---
type: concept
status: reviewed
audience: [qa, product-owner, engineering]
---

# Run, and read the results

## Six verdicts, not two

A run is not just "passed" or "failed". Each verdict says something different, and mixing them up is how a report ends up claiming more than was tested.

| Verdict | Means | Counts as |
|---|---|---|
| **Passed** | Every step matched its expected result | Executed, a success |
| **Failed** | At least one step differed from its expected result | Executed, a failure |
| **Blocked** | The test could not run to the end: missing data, environment down, a prerequisite missing | **Not executed** |
| **Not applicable** | The case does not apply to this release | Executed, set aside |
| **Not testable** | The campaign has no means to test it | Left out, and listed |
| **Settled** | It failed, and a person with authority accepted the deviation, in writing | Executed, **never a success** |

Three rules go with them:

- **A manual test is passed by a person**, and the run records who. Nobody marks a screen test passed on someone else's behalf.
- **A case run on several datasets gets the worst result.** Passed on two profiles and failed on the third is failed.
- **A flaky test counts as failing until it is fixed.** Rerunning it until it passes hides a defect, in the product or in the test.

## A report from the pipeline

Automated tests do not get their verdict from a person: the test runner writes a report, usually in the JUnit XML format. The trap is to read only its last line, "17 tests, 1 failure", and conclude something about the product.

Read a report **by level**, with three rules:

- a level with **no test** is reported as **not tested**, never as passing;
- a **skipped** or **errored** test is never counted as passed: an error usually means the test never reached the product;
- every failure is **attributed** before it is reported: the product, the test, or the environment.

The lab includes the script the Testing Agent uses to summarise a JUnit report by level. You will run it in the next exercise:

```bash
python lab/test-results/summarize_junit.py 02-running-a-campaign/exercises/data/claimtriage-junit.xml
```

---

Previous: [The frame of a campaign](the-frame-of-a-campaign.md) · [Course map](../00-orientation/progression.md) · Next: [Exercise: read a pipeline report](exercises/read-a-pipeline-report.md)
