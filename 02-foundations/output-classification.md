---
type: concept
status: reviewed
audience: [product-owner, qa, engineering]
---

# One product can contain three types of behaviour

Before writing tests, classify the **observable output** of the capability.

| Output nature | Examples | Validation framework | Core question |
|---|---|---|---|
| **Deterministic** | Schema, access control, routing, calculations, fixed rules | **DoD: Definition of Done** | Did it behave exactly as specified? |
| **Probabilistic** | Summary, classification, extraction, recommendation, generated answer | **DoT: Definition of Trustworthy** | Is the output sufficiently reliable for the intended use? |
| **Hybrid** | Agent workflow combining tools, controls and generated content | **DoD + DoT + UAT when user-facing** | Are the controls correct, the output trustworthy and the workflow acceptable? |

The three are exclusive **at capability level**: a capability is DoD-only, DoT-only, or Hybrid the moment one of its behaviours is probabilistic. But the classification is decided **per behaviour**, and the capability class follows from the behaviours, never the reverse.

## Two questions, not one

The first question is familiar. The second is the one that decides the hard cases, and skipping it produces the wrong gate.

**1. Can the correct output be stated in advance and compared exactly?**

If no — several phrasings are acceptable, wording varies while meaning stays right — it is **probabilistic**. Stop here.

**2. Where does that correct output come from: a written specification, or a reference somebody had to annotate?**

| Source of the correct output | Nature | Why |
|---|---|---|
| **A specification** — a schema, an entitlement rule, a documented formula, a decision table | **Deterministic** | The expected output is derivable without observing the system. Assert it, case by case, no threshold. |
| **An annotated reference** — a human judged what the right answer was | **Probabilistic** | Correctness cannot be derived, only compared against a reference set. That needs a population, a metric and an approved threshold. |

The need for a reference set is the signal, and it is already built into the framework: a DoD gate needs no dataset, while a DoT gate lists *reference or rubric* among its ten mandatory components. If a behaviour cannot be checked without someone first annotating what "correct" means, it belongs behind DoT.

### Why classification appears in the probabilistic row

A classifier picking one of a fixed, small set of classes looks deterministic under question 1: there is exactly one correct class per case, and comparison is exact.

Question 2 separates two cases that look identical:

- **Routing by a documented decision table** — *if the region is X and the age band is Y, use table B*. The mapping is specified, so the expected class is derivable. **Deterministic, DoD.**
- **Routing by a trained classifier** — the mapping is learned, written down nowhere, and the "correct" class per case has to be established by a qualified human. **Probabilistic, DoT**, with a reference set, an accuracy metric, an approved threshold and slices on the categories where being wrong costs most.

The row says *classification* because in practice a classification behaviour is usually the second. It is not the class count that decides it, and it is not the technology either — it is whether the correct answer was specified or annotated.

A consequence worth stating: choosing DoT here means **accepting a non-zero error rate**, because that is what a threshold is. If the business will not accept any error on that behaviour, it is not a DoT behaviour with a very high threshold — it is a behaviour whose mapping must be specified so it can be asserted.

## Classification example: Client 360 assistant

A user asks:

> “Who owns the relationship with this client, and what should I know before the meeting?”

The workflow may contain:

| Behaviour | Nature | Why |
|---|---|---|
| Authenticate the user | Deterministic | The access decision must follow an exact rule |
| Retrieve the authorized client record | Deterministic and retrieval quality | Access must be exact; retrieval must return the right evidence |
| Return the approved response schema | Deterministic | Required fields and types are fixed |
| Generate the briefing | Probabilistic | Several phrasings may be acceptable |
| Avoid unsupported claims | Probabilistic quality with a critical veto | Plausible but ungrounded content may create business risk |
| Let the user review the output | UAT | The complete workflow must remain useful and controllable |

> **Takeaway:** Most AI agents are Hybrid. Classify each behaviour separately instead of labelling the entire product “AI”.

---

Previous: [Why AI products need a different testing approach](testing-foundations.md) · [Course map](../00-orientation/progression.md) · Next: [The Hybrid validation model](dod-dot-hybrid.md)
