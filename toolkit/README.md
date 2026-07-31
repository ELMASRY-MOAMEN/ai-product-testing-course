---
type: moc
status: reviewed
audience: [qa, product-owner, engineering, data-ai, compliance]
---

# The toolkit

Not part of the reading order. This is what you open while working, and what you keep after the course.

## References

| | Use it when |
|---|---|
| [Readiness checklist](readiness-checklist.md) | Deciding whether an evaluation may start at all |
| [Scenario-writing rules](gherkin-and-test-contracts.md) | Writing DoD or DoT scenarios |
| [Glossary](glossary.md) | Someone uses a word and you are not sure you mean the same thing |

## Templates

Copy these. Never edit them in place, and never start from a worked example instead.

| File | For |
|---|---|
| [`templates/evaluation-manifest.yaml`](templates/evaluation-manifest.yaml) | The run's declaration — what is frozen, measured, and required |
| [`templates/evaluation-case.yaml`](templates/evaluation-case.yaml) | One golden-dataset case |
| [`templates/evaluation-report.md`](templates/evaluation-report.md) | The evidence a run leaves behind |
| [`templates/traceability-matrix.csv`](templates/traceability-matrix.csv) | Requirement and risk → scenario → evidence |
| [`templates/uat-rubric.yaml`](templates/uat-rubric.yaml) | Structured human acceptance |

Every angle-bracketed value in a template is an **unresolved decision**, not a blank to fill in with something reasonable. A manifest full of placeholders is structurally valid and will report `Not Ready` — which is the template working, not failing.

## Policies

The rules the runner and the auditor apply. Read them when you disagree with a verdict.

| File | Answers |
|---|---|
| [`policies/readiness-rules.md`](policies/readiness-rules.md) | Why an evaluation may not run |
| [`policies/verdict-rules.md`](policies/verdict-rules.md) | The order acceptance is decided in, and why averages come last |
| [`policies/data-handling-rules.md`](policies/data-handling-rules.md) | What may be sent where |
| [`policies/human-decision-boundary.md`](policies/human-decision-boundary.md) | What automation may never do |

If you read one, read `verdict-rules.md`. The ordering is the whole argument.

## Schemas

Machine-checkable shapes for the artefacts, in [`schemas/`](schemas). Use them to validate what you produce before anyone reviews it.

---

[Course map](../00-orientation/progression.md)
