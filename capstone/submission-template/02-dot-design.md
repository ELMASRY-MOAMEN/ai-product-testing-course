# 2. DoT design

Every component is either **resolved** — with the record it came from — or **open**, with the role that owns it. Nothing is filled in by you on the grounds that the value is obvious.

| Component | Status | Value or blocker | Source or owner |
|---|---|---|---|
| Evaluation question | | | |
| Evaluation set | | | |
| Reference or rubric | | | |
| Metric | | | |
| Threshold | | | |
| Critical slices | | | |
| Veto | | | |
| Variability control | | | |
| Evidence | | | |
| Owner | | | |

**Is the evaluation question singular?** If you needed "and" to write it, split it or say which part this evaluation does not cover.

## What the metric cannot see

The *Metric* component is not complete until this is filled in. Every metric has a boundary; a design that appears not to have one has not looked.

| Metric | What it measures | What it is blind to | How I checked |
|---|---|---|---|

**How I checked** is a real answer: *scored 15 cases by hand against the requirement and compared*. "It seemed reasonable" is not one.

## Instrument fit

For each risk, the instrument that can see it, and what that instrument cannot see.

| Risk | Instrument | Blind to |
|---|---|---|

## Veto conditions, as code would test them

| Veto | Evaluator that produces the signal | Condition |
|---|---|---|

> Every veto must name an evaluator that is declared in the manifest. A veto wired to nothing reads correctly and can never fire.

## Verdict on this design

`Not Ready` | `Ready to run` — and the components that decide it.
