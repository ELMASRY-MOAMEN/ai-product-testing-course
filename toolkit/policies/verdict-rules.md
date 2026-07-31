# Verdict Rules

Apply vetoes first, then critical slices, then aggregate thresholds.

## Order of application

The order is not a preference. Each step can end the evaluation, and a later step can never overturn an earlier one.

| # | Check | Outcome if it fails |
|:--:|---|---|
| 1 | **Readiness** — is every mandatory input, approval, owner and resource present? | `Not Ready`. Nothing is measured. See [readiness rules](readiness-rules.md). |
| 2 | **Vetoes** — did any critical failure occur? | `Fail`, regardless of every other result |
| 3 | **Critical slices** — did each risk-sensitive slice meet its own threshold? | `Fail`, even if the aggregate passes |
| 4 | **Aggregate thresholds** — did the overall result meet its approved threshold? | `Fail` |

If all four pass, the run yields `Pass` — a *recommendation*, not an acceptance. Acceptance is the [human decision](human-decision-boundary.md).

## Why averages come last

An aggregate hides its own worst cases. A candidate scoring 0.94 overall can still invent facts for every case in the one slice that carries legal exposure. Ordering the checks this way means a high average can never buy off a critical failure.

## Worked example

An evaluation reaches 0.91 against an approved threshold of 0.85. One case triggered the factual-invention veto.

The verdict is **Fail**. Step 2 ends the evaluation. Steps 3 and 4 are still computed and reported, because the evidence stays useful, but they cannot change the outcome.

## What this policy does not decide

- The value of any threshold. Thresholds are approved before the run, never derived from its results.
- Whether a failing result blocks a release. That is a business decision made at the human gate.
- Whether a veto was correctly defined. That is a design question, settled before execution.

## Related

- [Thresholds, slices and vetoes](../../05-designing-evidence/thresholds-slices-vetoes.md) — how each is defined
- [Runner outputs](../../06-running-it/reporting-and-evidence.md) — what a verdict must be reported with
