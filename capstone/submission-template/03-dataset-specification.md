# 3. Dataset specification

## Identity

```yaml
name: <dataset-name>
version: <version>
```

**What counts as a material change** (and therefore a new version):

**What does not:**

## Eligibility

A case enters a run only if:

- …

Eligibility is a declared rule, not a filter applied by hand at run time. The eligible count appears in the report.

## Composition

| Category | Cases | Why this many |
|---|:--:|---|
| | | |
| **Total** | | |

**Why this is not the production distribution:** &lt;risk categories are deliberately over-represented; say so and say why&gt;

## Slices

| Slice | Population | Minimum population to conclude | Basis | Approved by |
|---|:--:|:--:|---|---|

**A slice below its minimum population is reported as `not concluded`, never as a score.**

**Basis** is the failure rate the owner would find unacceptable, plus the arithmetic from `05-designing-evidence/how-many-cases-is-enough.md`. A minimum with no basis is a number you invented.

The manifest schema cannot express this. Record it here, and put the gap in your decisions register.

## Handling

**Proposed status:** anonymised | pseudonymised | synthetic | raw-approved

**Reasoning:**

**Who approves it:** &lt;role — and note that any external judge is a data recipient&gt;

**Decided before any case exists:**

| Decision | Owner | Status |
|---|---|---|

## Annotation protocol

| Step | Who | Output |
|---|---|---|
| Draft the case | | `draft` |
| Annotate the reference | **a business expert, never you** | |
| Review | | `reviewed` |
| Resolve disagreement | | |
| Approve | | `approved` |

**What a disagreement between two qualified annotators means:** &lt;it is signal about the requirement, not noise to be averaged&gt;

## Five case skeletons

Deliberately different categories. **Every `reference` stays a placeholder naming its owner.**

```yaml
case_id:
input:
context:
reference: <pending business annotation — owner: >
slices: []
criticality:
eligibility:
annotation_status: draft
```
