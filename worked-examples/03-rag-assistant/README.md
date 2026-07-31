# RAG assistant — a run that fails on a slice, not on an average

Synthetic, runnable end to end. Where [the LLM summary example](../02-llm-summary/README.md) shows a **veto** overriding a passing aggregate, this one shows the other way a good-looking run gets refused: **a critical slice below its minimum**, with every aggregate comfortably clear and no veto in sight.

Together the two examples cover the verdict order: vetoes first, then critical slices, then aggregates.

## What it evaluates

A mock assistant answering HR policy questions over a company handbook.

| | |
|---|---|
| Framework | DoT |
| Cases | 24 across three slices: 14 standard, 6 policy-change, 4 multi-source |
| Evaluators | `retrieval_recall`, `required_facts_recall`, `citation_support` |
| Approved thresholds | retrieval ≥ 0.85, answer facts ≥ 0.85 |
| Critical slices | policy-change ≥ 0.85, multi-source ≥ 0.85 |
| Veto | any citation to a source that was not retrieved |

## Run it

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py worked-examples/03-rag-assistant/manifest.yaml
```

## What it produces

| Check | Measured | Required | Outcome |
|---|:--:|:--:|:--:|
| Aggregate retrieval recall | 0.958 | 0.85 | pass |
| Aggregate answer-facts recall | 0.889 | 0.85 | pass |
| Veto | none triggered | — | pass |
| Slice `multi-source` | 1.000 | 0.85 | pass |
| Slice `policy-change` | **0.833** | 0.85 | **fail** |

**Verdict: Fail**, on one reason.

## The failure it models

`P-01` and `P-02` retrieved the **superseded** version of a policy that had recently changed. The assistant answered fluently, cited a genuine handbook document, and told the employee the entitlement that applied last year.

This is the characteristic failure of a retrieval-backed system, and it is concentrated: it only shows up on content that changed. An aggregate over a corpus that is mostly stable dilutes it to invisibility — here, to a 0.958 that looks excellent.

Two cases out of twenty-four decide the run. That is what a critical slice is for.

## Three separate questions

The example is built on three evaluators because retrieval-backed answers fail in three different ways, and one metric cannot see all of them:

| Evaluator | Answers | Failure it catches |
|---|---|---|
| `retrieval_recall` | Was the passage that holds the answer actually fetched? | Right-sounding answer from the wrong document |
| `required_facts_recall` | Does the answer contain what it must? | Incomplete answer |
| `citation_support` | Is every cited source one that was retrieved? | Fabricated citation |

Note what `citation_support` reports here: **1.000, no veto**. The candidate cited exactly what it retrieved. The citations are honest and the retrieval was not — a system can be perfectly grounded in the wrong document. Groundedness and correctness are different questions, and conflating them is how a RAG evaluation passes a stale-content failure.

## Try it

Raise the `policy-change` minimum to 0.90 in the manifest: the run still fails, on the same slice, further from its bar.

Remove the `policy-change` slice entirely: the run reports **Pass**, on a 0.958 aggregate, with the wrong parental-leave entitlement in the evidence.

## Related

- [Thresholds, slices and vetoes](../../05-designing-evidence/thresholds-slices-vetoes.md)
- [Building a Golden Dataset](../../05-designing-evidence/golden-datasets.md) — why a slice needs enough cases to be measurable
- [What exactly should we evaluate](../../04-what-to-measure/evaluators-and-metrics.md)
