---
name: run-product-evaluation
description: >
  Run an approved product evaluation from a versioned manifest. Use when asked to validate a manifest, execute eligible cases through an adapter, aggregate results, apply vetoes, or create an evidence report.
license: MIT
---

# Run Product Evaluation

## Scope

Apply the repository methodology to the user's product context. Keep deterministic conformance, probabilistic quality, and user acceptance evidence separate.

## Procedure

1. Validate the manifest and referenced resources.
2. Stop with Not Ready if mandatory values are missing.
3. Run deterministic tests, then eligible cases through the configured adapter.
4. Run only declared evaluators.
5. Aggregate global and slice results, then apply vetoes.
6. Generate evidence and preserve the human decision field.

## Required outputs

- Assumptions and source inputs
- Completed artefacts or explicit placeholders
- Blockers and open decisions
- Readiness result
- Human approvals still required

## Rules

- Never invent thresholds, approvals, datasets, references, or test evidence.
- Preserve predefined inputs for reproducible comparisons.
- Use the simplest evaluator capable of measuring the requirement.
- Never expose secrets or protected data.
- Automated evidence never replaces the authorized human decision.

## References

- `references/execution-policy.md`
- `references/verdict-rules.md`
- `references/evidence-policy.md`
- `references/error-classification.md`
