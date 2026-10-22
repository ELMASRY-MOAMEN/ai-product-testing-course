---
type: example
status: reviewed
audience: [qa, product-owner, engineering]
---

# Exercise: write a defect

**Time:** 20 minutes. **Do it before opening [the solution](solutions/write-a-defect.md).**

## 1. Qualify three failures

Where is the problem in each failure: `product`, `test` or `environment`?

| | Failure |
|:--:|---|
| **K1** | A critical travel claim went to `queue-travel`; the routing table says `queue-A` |
| **K2** | The test expects the field `queue_id`; the contract approved in July renamed it `recommended_queue`, which the card returns |
| **K3** | The run stopped on "connection refused": the claims-system stub was not started on the test server |

```bash
python tools/check_answer.py failures K1=product K2=product K3=product
```

## 2. Write the defect

In CAMP-03, case CT-02 failed: claim 7731, travel product line, urgency critical, build 2.3.0-142, test environment. The card says `queue-travel`. Write the defect.

Write it as you would in your tracker, then compare with the solution.

---

Previous: [From a failure to a defect](../from-failure-to-defect.md) · [Course map](../../00-orientation/progression.md) · Next: [Where do we stand?](../where-do-we-stand.md)
