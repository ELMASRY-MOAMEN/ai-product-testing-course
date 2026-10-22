---
type: example
status: reviewed
audience: [qa, engineering]
---

# Solution — Run a DoD gate

Read this only after attempting [the exercise](../run-a-dod-gate.md). The completed manifest is [`claimtriage-dod-manifest.yaml`](claimtriage-dod-manifest.yaml).

## 1. The scenarios

```gherkin
@DoD @entitlement
Scenario Outline: Entitlement is enforced in both directions
  Given a staff member whose role is <role>
  And a claim on product line <product_line>
  When the assistant is asked to triage the claim
  Then the request is <outcome> according to the entitlement matrix

  Examples:
    | role         | product_line         | outcome             |
    | front-office | property             | processed           |
    | front-office | commercial-liability | refused not_entitled |
```

```gherkin
@DoD @response-contract
Scenario: The triage card carries every required field
  Given an entitled request for a claim
  When the assistant returns a triage card
  Then the card contains claim_id, urgency, summary and recommended_queue
  And no required field is empty
```

```gherkin
@DoD @routing
Scenario Outline: Claims route by the documented table
  Given a claim whose urgency is <urgency> on product line <product_line>
  When the assistant recommends a queue
  Then the recommended queue is exactly <queue>

  Examples:
    | urgency  | product_line | queue          |
    | critical | motor        | queue-A        |
    | critical | travel       | queue-A        |
    | standard | motor        | queue-motor    |
    | standard | property     | queue-property |
```

Note what is absent: no *"then the routing is usually correct"*, no percentage, no sample. Each row is an assertion that holds or does not.

The entitlement scenario covers both directions on purpose. A rule tested only where it should permit is a rule you have not tested — you have confirmed the system does something, not that it refuses to do the other thing.

## 2 & 3. The manifest, the prediction, the run

```yaml
evaluators:
  - id: response-contract
    type: schema_conformance
    gate: DoD
  - id: queue-routing
    type: exact_values
    gate: DoD

acceptance:
  thresholds: {}
  critical_slices: []
  vetoes: []
```

Both evaluators cover B1 as well as their headline behaviour: case `CTD-06` declares `required_fields: [error_code]` and `expected_values: {error_code: not_entitled}`, so a refusal is asserted with exactly the same two instruments as a success. Entitlement did not need a third evaluator; it needed a case that expects a refusal.

```text
status: Fail
gates: {'DoD': 'Fail', 'DoT': 'Not evaluated'}
reasons: ['DoD gate: 4 assertion failure(s) on queue-routing, response-contract']
coverage: {'total': 8, 'completed': 8, 'failed': 3, 'passed': 5}

CTD-03  response-contract  required output field missing or empty: summary
CTD-04  queue-routing      recommended_queue was 'queue-travel', expected 'queue-A'
CTD-06  response-contract  required output field missing or empty: error_code
CTD-06  queue-routing      error_code was None, expected 'not_entitled'
```

**Four failures across three cases.** If you predicted three failures you were counting cases; the report counts assertions, and the difference is the subject of question **c**.

## 4. The questions

### a. `thresholds: {}`

Empty, and that is the finished answer.

A threshold expresses *how much of a population must be good enough*. A DoD gate has no population to be good enough — it has assertions, each of which holds or does not. There is nothing to average, so there is nothing to set a bar for.

This matters more than it looks. The runner only demands an approved threshold when a **DoT** evaluator is declared:

> *Only a measurement needs a threshold. An evaluation made entirely of DoD assertions has nothing to average, so demanding an approved threshold there would block a correctly specified deterministic run.*

An empty `thresholds: {}` and an unresolved `<approved-threshold>` look similar in a file and mean opposite things: one says *this gate does not work that way*, the other says *a human has not decided yet*. Readiness treats them differently, and so should you.

### b. The number that is not the verdict

`aggregate_results` reports `response-contract: 0.75` and `queue-routing: 0.75`.

**Neither is the verdict.** The verdict came from `assertion_failures` — four of them, so the DoD gate fails. The 0.75 is arithmetic the runner can perform on anything; it carries no acceptance meaning here, and no threshold is compared against it.

Quoting "the DoD gate scored 0.75" in a release note would be the single most misleading sentence you could write about this run. It invites the reader to think in degrees about a gate that has none — and it is exactly how question **d** gets asked.

### c. `CTD-06`, and why two findings beat one flag

`CTD-06` is the unentitled request. The assistant did two distinct wrong things:

1. It **returned no refusal** — `error_code` missing (`response-contract`).
2. It **returned a triage card for a claim the user may not see** — `recommended_queue: queue-commercial`, a real disclosure (`queue-routing`).

A single "CTD-06 failed" tells an engineer to go look. Two findings from two evaluators tell them *what* broke and *how far it went*: the entitlement check did not merely fail to emit an error, it fell through into the normal path and produced output. Those are different bugs with different fixes, and the second is the serious one.

This is the same principle as the DoT vetoes: **an evaluator that returns a number without naming what failed produces a result nobody can act on.**

### d. "Set the DoD bar at 60%"

> There is no bar to set. These are assertions, not measurements — the run is not 62.5% good, it is three cases where the system did something the specification forbids. A DoD bar at 60% would mean we have agreed that four out of ten entitlement checks may fail, and Compliance has agreed to nothing of the kind.
>
> Look at what would be inside the accepted 37.5%: `CTD-06`, where the assistant handed a commercial-liability claim to someone not entitled to see it. There is no percentage at which that is acceptable, which is precisely why this behaviour is behind DoD and not behind a threshold.

Notice that this is the same argument as question 4 in [the module 04 exercise](../../../04-foundations/exercises/classify-five-behaviours.md), arriving from the opposite direction. There, someone wanted to move a deterministic behaviour behind a DoT threshold of 0.9999. Here, someone wants to put a threshold on a DoD gate. Both convert a rule into an accepted error rate, and both are refused for the same reason.

### e. `derived` versus `approved`

This is [question 2 from module 04](../../../04-foundations/output-classification.md), showing up in the dataset's metadata:

| Status | Where the correct output came from | Who had to be involved |
|---|---|---|
| `derived` | **A specification** — the entitlement matrix, the response contract, the routing table | Nobody. Read the spec and write the expected value; two people doing it independently get the same answer |
| `approved` | **An annotation** — a qualified human judged what a correct answer was | A business expert, then a reviewer, then an approver |

That is why a DoD dataset needs no annotation protocol and no golden-set governance, and why a DoT dataset cannot exist without them. It is also why you may legitimately write these expected values yourself, while writing a DoT `reference` yourself fails [the capstone](../../../capstone/rubric.md).

The one thing `derived` still requires: the specification must exist and be current. A value "derived" from a spec nobody maintains is an annotation you made up with extra steps.

## 5. The behaviour that cannot be here

**B2, the urgency level.** The model-assigned `standard | priority | critical`.

It cannot be asserted because no document says what the correct urgency is for a given claim description — the mapping was learned, and establishing the right answer per case takes a qualified human. `exact_values` would compare the candidate's urgency against an "expected" value that somebody guessed, and every disagreement would be reported as a defect with no way to tell a model error from a bad guess. You would be measuring the annotator.

Look at how the dataset handles it. **`urgency` appears in two places, and they do different jobs:**

| Where | What it is | Asserted? |
|---|---|---|
| `input.urgency` | A **controlled input** — the value handed to the candidate for this case | No. Never |
| `mock_output.urgency` | The card echoing it back, because the response contract requires the field | Yes, by `schema_conformance` — *present*, not *correct* |

So the routing assertions in `expected_values` are derived from `input.urgency` and the routing table, both of which are specified. Nothing anywhere asks whether the urgency **was the right one**, and nothing can: that is B2, and it needs an annotated reference set behind DoT.

That is how a deterministic behaviour downstream of a probabilistic one gets tested honestly — you fix the upstream value and assert what follows from it. Testing B5 on whatever B2 happened to produce would measure both at once and tell you which one failed: never.

## Locate yourself

For each item, find the line closest to **what you actually wrote**, then read the verdict.

### 1. What you put in `acceptance.thresholds`

| | You wrote | |
|:--:|---|---|
| **A** | `{}`, and you can say a DoD gate has no population to average | ✅ |
| **B** | `{}`, because the template's example did not seem to apply | ⚠️ Right file, no reason. `{}` and `<approved-threshold>` look alike and mean opposite things — one says *this gate does not work that way*, the other *nobody has decided yet* |
| **C** | A number, e.g. `response-contract: 1.0` | ❌ A bar of 1.0 is a threshold that happens to be strict, and it invites the conversation in question **d**. Assertions do not have bars |

### 2. What you called the verdict

| | | |
|:--:|---|---|
| **A** | The four `assertion_failures`; the 0.75 is arithmetic with no acceptance meaning | ✅ |
| **B** | "The DoD gate scored 0.75" | ❌ The most misleading sentence available about this run. It invites a reader to think in degrees about a gate that has none |
| **C** | You did not notice `aggregate_results` contained anything | ⚠️ It does, and someone will quote it. Knowing which numbers in a report carry no acceptance meaning is part of reading one |

### 3. What you made of `CTD-06`

| | | |
|:--:|---|---|
| **A** | Two distinct defects: no refusal emitted, **and** a claim disclosed to someone not entitled to it | ✅ |
| **B** | "The entitlement check failed" | ⚠️ True and incomplete. The check did not merely fail to refuse — it fell through into the normal path and produced output. Different bug, different fix, worse consequence |
| **C** | One failing case among three | ❌ Three cases failed and this is the only one with a disclosure in it. Counting cases loses exactly the information the two findings were carrying |

### 4. Your answer to the 60% bar

| | | |
|:--:|---|---|
| **A** | There is no bar to set — and you named `CTD-06` as what would sit inside the accepted 37.5% | ✅ |
| **B** | "60% is far too low for a compliance control" | ⚠️ Negotiating the number concedes that a number belongs there. The next offer will be 95% |
| **C** | "The methodology says DoD gates do not have thresholds" | ❌ Invoking the rule instead of the consequence. It is also the version most easily overridden by someone senior in a hurry |

### 5. Where `urgency` came from

| | | |
|:--:|---|---|
| **A** | A controlled input, supplied per case; the card echoes it, and nothing asserts it is *correct* | ✅ |
| **B** | You noticed it was asserted by `schema_conformance` and left it there | ⚠️ That assertion checks the field is **present**. Whether the value is right is B2, and unassertable here |
| **C** | You proposed asserting the urgency against an expected value | ❌ That measures your guess at the right urgency, not the system. Every disagreement becomes a defect you cannot attribute |

**Two or more ❌:** reread [DoD: testing deterministic behaviour](../../definition-of-done.md) and [the scenario-writing rules](../../../toolkit/gherkin-and-test-contracts.md) before module 06.
