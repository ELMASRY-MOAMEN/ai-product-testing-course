# Mock evaluation

Synthetic, and runnable with nothing but this skill folder. Copy the folder alone into another repository and this still works — which is the point: the artefact that proves the engine runs travels with the engine.

## Run it

From the skill folder:

```bash
python scripts/run_evaluation.py examples/mock-evaluation/manifest.yaml
```

## What it produces

Ten support tickets, two slices, one approved threshold, one veto.

| Check | Measured | Required | Outcome |
|---|:--:|:--:|:--:|
| Aggregate recall | 0.967 | 0.85 | pass |
| Slice `sensitive` | 1.000 | 0.90 | pass |
| Veto | 1 triggered | none | **fail** |

**Verdict: Fail.**

Case `MOCK-08` scored a perfect recall — both required facts are present — and added *"The data deleted on request"*, which the source does not support. One occurrence of an unsupported claim is not a matter of degree, so it blocks acceptance whatever the averages say.

## Two things to try

**Empty the `vetoes:` list** in the manifest and run again. The verdict becomes `Pass` at 0.967, with the fabricated claim counted as a success. Nothing in the aggregate reveals it.

**Replace the threshold with `<approved-threshold>`.** The run reports `Not Ready`, not `Fail`. Nothing was measured, so nothing may be concluded about the candidate — inventing a value to let the run proceed would turn a missing decision into evidence nobody approved.

## Scaling up

A ten-case set is enough to demonstrate the mechanism and too small to decide anything. A slice of four cases moves 25 points on a single failure, so no minimum on it would be meaningful in a real evaluation. See `references/verdict-rules.md` for how the outcome is decided, and the repository's `examples/02-llm-summary/` for a 25-case version with three slices.
