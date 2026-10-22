---
type: example
status: reviewed
audience: [qa, product-owner, engineering]
---

# Exercise: read a pipeline report

**Time:** 20 minutes. **Do it before opening [the solution](solutions/read-a-pipeline-report.md).**

## 1. Six runs

Which verdict does each run get: `passed`, `failed`, `blocked`, `not-applicable`, `not-testable` or `settled`?

| | Run |
|:--:|---|
| **V1** | Every step matched its expected result |
| **V2** | At step 3 the card had no urgency field |
| **V3** | Step 1 could not start: no account without the motor entitlement in the environment |
| **V4** | The case covers a feature switched off for this market |
| **V5** | The requirement is a 2-second response under load, and there is no load environment |
| **V6** | The case failed, and the product owner accepted the deviation for this release, in writing |

```bash
python tools/check_answer.py verdicts V1=passed V2=passed V3=passed V4=passed V5=passed V6=passed
```

## 2. The pipeline report

[ClaimTriage's JUnit report](data/claimtriage-junit.xml), build 2.3.0-142, is exactly as the runner wrote it. Read it if you like. Then, **before you summarise it**, write down which level was not tested at all. Then:

```bash
python lab/test-results/summarize_junit.py 02-running-a-campaign/exercises/data/claimtriage-junit.xml
```

## 3. What each problem counts as

For each problem in the summary: `product` (a product defect), `test` (a test defect), `environment` (an environment problem), or `gap` (a gap to report)?

| | Problem |
|:--:|---|
| **J1** | `test_critical_travel_goes_to_queue_A`: `'queue-travel' != 'queue-A'` |
| **J2** | Two integration tests: `ConnectionRefusedError` on the claims-system stub |
| **J3** | `test_entitlement_matrix_liability`: skipped, "flaky, to look at later" |

```bash
python tools/check_answer.py report J1=product J2=product J3=product
```

---

Previous: [Run, and read the results](../run-and-read-results.md) · [Course map](../../00-orientation/progression.md) · Next: [From a failure to a defect](../from-failure-to-defect.md)
