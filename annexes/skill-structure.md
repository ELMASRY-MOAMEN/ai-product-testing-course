---
type: reference
status: reviewed
audience: [engineering]
---

# Minimal GitHub Copilot skill structure

A project skill can be organized under `.github/skills/`.

```text
.github/
└── skills/
    └── run-product-evaluation/
        ├── SKILL.md
        ├── scripts/
        │   ├── validate_manifest.py
        │   ├── run_evaluation.py
        │   └── create_report.py
        ├── schemas/
        │   ├── manifest.schema.json
        │   └── result.schema.json
        ├── references/
        │   ├── execution-policy.md
        │   └── verdict-rules.md
        ├── examples/
        │   ├── evaluation.yaml
        │   └── dataset.jsonl
        └── tests/
            ├── test_manifest_validation.py
            ├── test_slice_aggregation.py
            └── test_veto_logic.py
```

## Minimal `SKILL.md`

```markdown
---
name: run-product-evaluation
description: >
  Run an approved deterministic, probabilistic or hybrid product evaluation
  from a versioned evaluation manifest. Use when asked to execute AI product
  tests, compare a candidate with a baseline, calculate critical slices,
  check veto conditions, or generate an evaluation report.
---

# Run Product Evaluation

## Preconditions

Before execution, verify that:

1. An evaluation manifest exists.
2. Candidate, dataset and evaluator versions are declared.
3. Thresholds, slices and vetoes were approved before the run.
4. The dataset complies with the approved data-handling rules.
5. The configured tests, adapters and evaluator commands exist.

If a required item is missing, stop and return `Not Ready`.
Do not invent a metric, threshold, dataset, reference answer or approval.

## Procedure

1. Locate the requested evaluation manifest.
2. Run the manifest validator.
3. If validation fails, report every blocker and stop.
4. Run the deterministic tests declared in the manifest.
5. Invoke the candidate for every eligible case.
6. Run only the evaluators declared in the manifest.
7. Calculate aggregate and critical-slice results.
8. Apply vetoes independently of average scores.
9. Generate the versioned evidence files and report.
10. Return `Pass`, `Fail` or `Not Ready` with evidence locations.

## Safety and authority

- Never expose secrets in logs or reports.
- Never send protected data to an unapproved evaluator.
- Never change thresholds after viewing results.
- Never declare production acceptance solely from the automated result.
- Preserve the authorized human decision gate.
```

> **Takeaway:** A skill is not only a prompt. It needs explicit triggers, prerequisites, procedures, scripts, evidence rules and safety boundaries.

---

[Course map](../00-orientation/progression.md) · Reference — consult it, do not read it once.
