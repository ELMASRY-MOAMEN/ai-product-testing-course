# Capstone submission — &lt;capability name&gt;

Copy this folder into `my-work/` before filling it in. Assessed against [the rubric](../rubric.md).

---

## Handover — one page, for the decision owner

**Capability evaluated:** &lt;name, version&gt;

**What this package is:** &lt;one sentence a product owner reads without decoding&gt;

**Current status:** `Not Ready` | `Ready to run` | `Run complete — Pass` | `Run complete — Fail`

**What I am asking you to decide:**

| # | Decision | Owner | Blocks |
|:--:|---|---|---|
| 1 | &lt;…&gt; | &lt;role&gt; | &lt;what cannot proceed&gt; |

**What happens once you decide:** &lt;how long to a verdict, and what the verdict will and will not tell you&gt;

**What this evaluation will not tell you, whatever the result:** &lt;the honest limits — behaviours out of scope, slices too small to conclude from, risks nobody has agreed to measure&gt;

That last line is not a disclaimer. A decision owner who does not know the limits of the evidence will over-read it.

---

## The artefacts

| # | File | |
|:--:|---|---|
| 1 | [Classification](01-classification.md) | Every behaviour, its nature, its gate |
| 2 | [DoT design](02-dot-design.md) | The ten mandatory components |
| 3 | [Dataset specification](03-dataset-specification.md) | Composition, governance, five case skeletons |
| 4 | [Manifest](04-manifest.yaml) | Runnable |
| 5 | [Readiness assessment](05-readiness.md) | The checklist, scored honestly |
| 6 | [Decisions register](06-decisions-register.md) | Everything you did not decide |

## Run record

```bash
python lab/run-product-evaluation/scripts/run_evaluation.py my-work/<your-folder>/04-manifest.yaml
```

**Blockers I predicted before running:**

**Blockers the runner reported:**

**Where they differed, and why:**
