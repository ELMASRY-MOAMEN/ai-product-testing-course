---
type: reference
status: reviewed
audience: [product-owner, qa, engineering, data-ai, compliance]
---

# Glossary

Alphabetical, for lookup. Every term below is used elsewhere in these notes or in the skills.

| Term | Meaning |
|---|---|
| **Adapter** | The component that submits a controlled input to the candidate and returns its output and execution trace in a normalised shape |
| **Annotation status** | Whether a case's reference or rubric has been reviewed and approved; an unapproved case is not eligible |
| **Baseline** | A previously accepted or reference candidate used for comparison |
| **Calibration** | The process of comparing an evaluator with qualified human decisions and refining its rubric or scope |
| **Candidate** | The exact product, model, prompt, code and tool configuration being evaluated |
| **Critical slice** | A risk-sensitive slice that must meet its threshold independently, whatever the aggregate result |
| **Deterministic output** | An output that can be checked exactly against a fixed rule, and is therefore validated by DoD |
| **DoD — Definition of Done** | The gate proving deterministic behaviour conforms exactly to specification |
| **DoT — Definition of Trustworthy** | The gate proving a probabilistic output reaches the quality required for a declared use and risk level |
| **Eligibility** | Whether a case may take part in a given run; ineligible cases are excluded before execution, not after scoring |
| **Evaluator** | Code, rule, rubric, human process or calibrated AI judge that measures an output |
| **Evidence** | The case outputs, scores, traces and versions retained after a run so the result can be re-examined |
| **Frozen** | Fixed for the duration of a run. Candidate, evaluator and dataset are frozen so a result stays attributable to a known configuration |
| **Golden Dataset** | A versioned set of representative cases with reviewed references or annotations |
| **Groundedness** | The extent to which claims are supported by the permitted source evidence |
| **Human gate** | The point where an authorized person accepts the result and owns the residual risk; automation may recommend, never decide |
| **Hybrid** | A behaviour requiring more than one gate, typically DoD and DoT, and UAT when user-facing |
| **Manifest** | The versioned declaration approved before a run: candidate, adapter, data, evaluators, thresholds, slices, vetoes, evidence locations and owners |
| **Metric** | The defined calculation used to express evaluation quality |
| **Not Ready** | The outcome when a mandatory input, approval, owner or executable resource is missing. Distinct from Fail: nothing was measured |
| **Probabilistic output** | An output that may take several acceptable forms for the same input, and is therefore evaluated by DoT rather than matched exactly |
| **Regression** | A result that became worse compared with the accepted baseline |
| **Residual risk** | Known risk that remains after controls and requires an authorized decision |
| **Runner** | The component that executes the approved protocol: validates prerequisites and versions, loads eligible cases, invokes the candidate, calls the evaluators and aggregates results |
| **Slice** | A meaningful subset of cases analysed independently |
| **Threshold** | The approved minimum, maximum or interval required to pass |
| **UAT** | User Acceptance Testing of the complete workflow in its intended business context |
| **Variability control** | The declared model, prompt, tools, parameters and repetition count that make a probabilistic run comparable across executions |
| **Veto** | A critical failure that blocks acceptance regardless of average scores |

---

[Course map](../00-orientation/progression.md) · Reference — consult it, do not read it once.
