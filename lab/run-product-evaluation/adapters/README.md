# Candidate adapters

An adapter invokes the product under test and returns a normalised result. It must not decide `Pass` or `Fail`, alter predefined cases silently, or store credentials.

## The contract

`invoke(case)` returns a mapping with:

| Key | Meaning |
|---|---|
| `case_id` | Echoed from the case |
| `status` | `completed` or `error` — never a verdict |
| `candidate_output` | Whatever the candidate produced, as a mapping |
| `error` | The error when `status` is `error`, otherwise `None` |

Evaluators read `candidate_output`. Whatever they need must be in it, under names the case's `reference` section can refer to.

## `mock_adapter` is a demonstration, not a scaffold

`MockAdapter` replays a scripted answer from the case, so a run exercises the pipeline rather than a model. It is what the bundled examples use.

Its named keys — `answer`, `retrieved`, `cited`, `tool_call`, `ticket_reference`, `report_id`, `error_code` — are **the vocabulary those examples happen to need**. They are not the set of fields a candidate may return, and a new domain should not bend one of them to mean something else. An insurance premium is not an `answer`, and calling it one makes the manifest lie to whoever reads it next.

For any other domain, declare the fields you need on the case under `mock_output`:

```yaml
mock_output:
  premium: 842.50
  rating_table: "TBL-C"
  decision_record_id: "PD-99213"
```

They arrive verbatim in `candidate_output`, and a case's `reference.expected_values` or `reference.required_fields` can name them directly.

## Writing a real adapter

For a real candidate, the adapter is the boundary between the evaluation and the product. Four rules:

**Return what happened, not what it means.** A timeout is `status: error` with the error recorded. It is not a failed case — error classification decides that, and attributing a harness failure to the candidate manufactures a defect.

**Never mutate the case.** The input submitted must be the input the case declares, unchanged. A reworded input makes results incomparable across runs.

**Never retry silently.** An undeclared, uncounted retry turns a flaky result into an apparently stable one. If retries are permitted, they are declared in the manifest and reported.

**Hold no credentials.** Secrets come from the environment, and they never reach `candidate_output` — evidence is written from what the adapter returns.

## Registering one

`run_evaluation.py` resolves the adapter from `candidate_adapter.type` in the manifest. Only `mock` is registered here; adding a type means adding it to `resolve_adapter` and declaring it in the manifest. An unregistered type raises rather than running against the wrong thing.
