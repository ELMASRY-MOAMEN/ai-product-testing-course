# The lab

The evaluation runner used by the exercises. It is a self-contained copy of the `run-product-evaluation` skill from the companion repository, vendored here so the course runs offline against a mock candidate — no model, no API key, no network.

It needs `PyYAML` and `jsonschema`; see [prerequisites](../00-orientation/prerequisites.md).

## Running an evaluation

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py <path-to-manifest.yaml>
```

Paths inside a manifest — `evaluation_data.path`, `evidence.output_dir` — are relative to the **manifest**, not to where you run the command.

## What it will do

- Refuse to run and report `Not Ready`, listing every unresolved placeholder and every control that names something undeclared.
- Execute the cases, score them with the declared evaluators, aggregate globally and per slice, and apply vetoes independently.
- Write case-level evidence into the manifest's `evidence.output_dir`.

## What it will not do

- Invent an acceptance policy, approve its own evaluator, waive a critical failure, accept residual risk, or make a release decision.

That boundary is the subject of [module 07](../07-governance/README.md), and it is enforced in code, not by convention.

## The evaluators available

Listed in `run-product-evaluation/scripts/evaluators.py`. A manifest naming a type the registry does not have is blocked **before** the run, not part-way through it — a manifest that promises a measurement nothing can make must not produce a partial report.

## The runner's own tests

`run-product-evaluation/tests/` holds 29 tests that came with the skill. They are not part of the course and you never need to run them — but they are the reason you can trust that `Not Ready` really blocks, that a veto naming an undeclared evaluator is caught, and that secrets are redacted from evidence.

```bash
pip install -r requirements-dev.txt && pytest lab/run-product-evaluation/tests -q
```

They run on every push, along with the three validators. See [the workflow](../.github/workflows/validate.yml).

## Adapters

`run-product-evaluation/adapters/` holds the interface between the runner and a candidate. The exercises use the **mock** adapter: each dataset case carries its own `mock_answer`, so runs are deterministic, offline, and free.

Evaluating a real product means writing an adapter for it. That is engineering work, and it is out of scope for this course.

---

[Course map](../00-orientation/progression.md)
