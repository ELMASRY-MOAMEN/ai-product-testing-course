---
type: procedure
status: reviewed
audience: [qa, product-owner, engineering]
---

# A green suite on a bug

Fifteen minutes. You run a real test suite, watch it pass on a product that is wrong, and find out where its expected results should have come from.

No theory yet. You will run something first, and the theory will land better once you have seen it.

## 1. The product, and its suite

*ClaimTriage* is an assistant used by an insurer's front-office staff. An agent pastes in a customer's claim and gets back a triage card, with the queue the claim should go to. The ops runbook holds the **routing table**:

| Urgency | Queue |
|---|---|
| `critical` | `queue-A`, whatever the product line |
| `standard` or `priority` | the queue of the product line: `queue-motor`, `queue-property`, `queue-travel`, `queue-liability` |

The developer who wrote the routing also wrote its test suite: eight claims, and for each one the queue it must reach. To fill in the expected queues, they ran the service and copied what it returned. The suite has been green ever since.

Before you run it, write down the verdict you expect and how many cases will fail. Then:

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py 01-testing-basics/exercises/data/routing-suite.yaml
```

## 2. Look at what passed

`"status": "Pass"`, eight cases out of eight. Now open [the cases](exercises/data/routing-recorded.jsonl) and read the expected queue of each one, under `reference.expected_values`:

| Case | Product line | Urgency | Expected in the suite |
|---|---|---|---|
| R-01 | motor | standard | `queue-motor` |
| R-02 | motor | critical | `queue-A` |
| R-03 | property | standard | `queue-property` |
| R-04 | property | priority | `queue-property` |
| R-05 | travel | standard | `queue-travel` |
| R-06 | travel | critical | `queue-travel` |
| R-07 | liability | critical | `queue-liability` |
| R-08 | liability | priority | `queue-liability` |

Hold that table against the routing table above. Before you read on, find the cases where the two disagree.

## 3. Run it against the specification

The routing table is the specification: the ops team owns it, and it says what the product must do. A second file, [`routing-spec.jsonl`](exercises/data/routing-spec.jsonl), holds the same eight cases with the expected queues taken from that table instead of from the service.

Copy the manifest into a `my-work/` folder of your own, change one line so that the dataset reads `path: ../data/routing-spec.jsonl`, predict the verdict and the number of failing cases, and run it. If you would rather not edit anything yet, the same manifest is in [the solutions](exercises/solutions/routing-suite-spec.yaml):

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py 01-testing-basics/exercises/solutions/routing-suite-spec.yaml
```

## 4. What changed, and what did not

`"status": "Fail"`, with two assertion failures: **R-06** and **R-07**. A critical travel claim goes to the travel queue, and a critical liability claim to the liability queue. Two people hospitalised, both waiting in an ordinary queue instead of the one that is staffed for emergencies.

The product did not change between the two runs. Neither did the test cases, nor the assertions. Only one thing changed: **where the expected results came from**.

- Copied from the service, they describe what the code **does**. A suite written that way passes on every bug the code already has, and fails only when someone fixes one.
- Taken from the routing table, they describe what the product **must do**. That is the only version that can catch a defect.

A test is a comparison between what the product does and what someone decided it must do. If nobody decided, there is nothing to compare against, and the honest expected result is not a guess: it is "to confirm", with the name of the person who decides.

## Check yourself

Answer in your own words **before** opening the answer.

### The developer says: "the suite was green for three months, so the routing must be fine." Answer them, in two sentences, without blaming anyone.

<details>
<summary>Answer</summary>

> The suite compared the service with itself: its expected queues were copied from what the service returned, so it could only ever pass. Taken from the routing table in the runbook, the same eight cases fail on R-06 and R-07, so critical travel and liability claims have been going to the wrong queue all along.

What matters is the mechanism, not the culprit. Copying the expected results from the output is a common shortcut, and it turns a test into a recording.

| | You wrote something like | |
|:--:|---|---|
| A | The expected results were copied from the code, so the suite could not fail; from the routing table it fails on R-06 and R-07 | ✅ |
| B | "Green tests do not prove anything" | ⚠️ Too broad. Green tests prove a lot when their expected results come from a specification |
| C | "The developer should have been more careful" | ❌ True perhaps, and useless: it does not say what to change in the suite |
</details>

Two runs, and the first rule of this course: **a test is worth what its expected result is worth.**

---

Previous: [Module 01: Testing basics](README.md) · [Course map](../00-orientation/progression.md) · Next: [A criterion someone can test](testable-criteria.md)
