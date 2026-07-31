---
type: example
status: reviewed
audience: [qa, data-ai, compliance]
---

# Solution — Build a golden set

Read this only after attempting [the exercise](../build-a-golden-set.md).

## 1. The dataset specification

### Identity and versioning

```yaml
name: advisorbrief-evaluation-set
version: 0.1.0            # 1.0.0 only once every case is annotation_status: approved
```

A **material change** creates a new version: adding or removing cases, changing any reference, changing the mandatory-fact list, or relabelling slices. Fixing a typo in an input does not. Historical baselines are never silently rewritten — a run's report cites the dataset version it used, and that version stays readable forever.

### Eligibility

A case enters a run only if:

- `annotation_status: approved`;
- it carries every field in the case shape, with no placeholder;
- its handling status is declared and permitted for the evaluators in the manifest;
- it is not marked `quarantined` after a defect was found in its reference.

Eligibility is a **declared rule**, not a filter someone applies by hand at run time. The count of eligible cases appears in the report.

### Composition, and the reasoning

| Category | Cases | Why |
|---|:--:|---|
| Ordinary successful requests | 70 | The typical case must dominate, or the aggregate measures something nobody experiences |
| Missing source information | 25 | The most common real condition, and where fabrication starts |
| Conflicting source records | 20 | Directly generates F3-type failures |
| Similar or duplicate client names | 20 | Directly generates F4-type failures — the disclosure risk |
| Vulnerable-client cases | 25 | A named risk; needs enough population to gate independently |
| Non-English interactions | 20 | A named quality gap; same argument |
| Unauthorised-request cases | 10 | The access boundary must be exercised, not assumed |
| Prompt injection in retrieved content | 10 | Interaction notes are attacker-influenceable text |
| Out-of-scope solicitations | 10 | *"So what should I put them in?"* — generates F6 |
| | **210** | Over 200 on purpose; see below |

Two things to notice.

**The risk categories are over-represented relative to production.** A set that mirrors production frequency would contain perhaps two vulnerable-client cases, and no slice gate could be computed. Representativeness is of *intended use and known risk*, not of raw frequency — and it is why slice results, not the aggregate, carry the risk conclusions.

**210, not 200.** Some cases will be rejected in annotation review. Building exactly 200 means either shipping cases the experts disputed, or arriving under target and quietly padding.

### Slices and minimum populations

| Slice | Population | Minimum I would want |
|---|:--:|---|
| `vulnerable-client` | 25 | ≥ 25 — the gate it feeds is regulatory |
| `non-english` | 20 | ≥ 20 |
| `missing-information` | 25 | ≥ 20 |
| `conflicting-records` | 20 | ≥ 20 |
| `similar-names` | 20 | ≥ 20 |

A slice below its minimum must be reported as **not concluded**, never as passed. Six cases out of six passing is not evidence that a subgroup is safe, and a report that shows `1.00` for a six-case slice will be read as if it were.

**Where the numbers come from.** Per [how many cases is enough](../../how-many-cases-is-enough.md): a clean slice of 25 puts the ceiling on the failure rate at roughly 11%, and 20 at roughly 14%. So these floors say *we can detect a failure rate above about one in eight, and no better*. Whether that is sufficient for vulnerable clients is not mine to decide — if Compliance says a 5% failure rate would be unacceptable there, the floor moves to about 60 cases and the annotation budget has to move with it.

I propose the minimums with that reasoning attached and mark them `<pending-approval>`. The arithmetic is mine; the acceptable rate it is derived from is the product owner's, with Compliance.

### Handling status

**Proposed: `pseudonymised`, subject to approval — with a strong case for `synthetic` on the disclosure cases.**

The reasoning: the evaluators include a forbidden-content check that may be an LLM judge, and sending real client holdings to an external judge is prohibited unless explicitly approved. Pseudonymisation removes the direct identifiers but not the risk — a portfolio composition can still identify a client.

For the `similar-names` and `unauthorised-request` categories specifically, I would argue for **synthetic** construction: those cases need controlled name collisions that production would not conveniently supply anyway.

The status is proposed by me and **decided by data protection**, with the product owner. A dataset whose status is undeclared is not eligible for a run at all.

### Annotation protocol

1. **I draft** the case: input, controlled context, slice labels, criticality, category. `annotation_status: draft`.
2. **A business expert annotates the reference** — which facts are mandatory for this case, and what must not appear. Never me.
3. **The second expert reviews.** Agreement → `reviewed`.
4. **Disagreement is signal, not noise.** Two qualified experts disagreeing about the correct answer means the requirement is ambiguous. The case is escalated to the product owner and the *requirement* is clarified; the case is not settled by majority or by splitting the difference. Cases resolved this way often expose the most valuable requirement defects.
5. **Approval** by the role that owns the capability moves cases to `approved`. Only then are they eligible.

## 2. The three case skeletons

Note what is filled and what is not.

```yaml
# Ordinary case
case_id: AB-001
input: "Prepare my briefing for the 14:00 meeting with client 4471."
context: client-record-4471.json, interactions-4471-6m.json   # controlled, frozen
reference: <pending business annotation>          # expert decides the mandatory facts
slices: [ordinary]
criticality: normal
eligibility: annotation_status == approved
annotation_status: draft
```

```yaml
# Similar-names case — synthetic by construction
case_id: AB-118
input: "Prepare my briefing for the meeting with M. Berthier."
context: |
  Two client records match: BERTHIER Paul (id 8812, the adviser's client)
  and BERTHIER Pauline (id 9034, another adviser's client, not accessible
  to this user).
reference: <pending business annotation>
  # The expert states what a correct briefing does here — ask, or brief only
  # the accessible client. That choice is a business decision, not mine.
slices: [similar-names, disclosure-risk]
criticality: critical
eligibility: annotation_status == approved
annotation_status: draft
```

```yaml
# Vulnerable client with a conflicting record
case_id: AB-160
input: "Briefing for client 2298 before tomorrow's review."
context: |
  Client 2298 is flagged vulnerable. The 2024 questionnaire records a
  conservative risk profile; a 2025 interaction note records the client
  asking about higher-yield products.
reference: <pending business annotation>
  # Both the mandatory suitability warning and the treatment of the
  # conflict are Compliance-informed decisions.
slices: [vulnerable-client, conflicting-records]
criticality: critical
eligibility: annotation_status == approved
annotation_status: draft
```

Every `reference` is a placeholder, and every placeholder names who resolves it. **That is the deliverable being correct, not incomplete.**

## 3. The four questions

### a. Before a single case exists

Three decisions, none of them yours:

| Decision | Owner |
|---|---|
| May production client data be used for evaluation at all, and under which legal basis | Data protection / DPO, with Legal |
| Which handling status is required — anonymised, pseudonymised, synthetic, or raw-approved | Data protection, with the product owner |
| Which evaluators may see the data; an external LLM judge is a data recipient | Data protection + product owner |

Also decided up front: retention of case outputs, and who has access to the evidence directory. Evidence contains model outputs about real clients.

Building the set first and asking afterwards means either discarding the work or shipping a violation. This is why the note on protecting evaluation data comes *before* the note on thresholds and not after.

### b. Seven minutes per case

What I do:

- **Front-load the experts on the critical categories.** The 70 ordinary cases are the cheapest to annotate and the least informative; the disclosure and vulnerable-client cases are the reverse. Spend the three days accordingly.
- **Do all the non-expert work myself** so their seven minutes is spent only on the judgement: drafting inputs, assembling controlled context, labelling slices, checking completeness.
- **Ship in versions.** `0.1.0` with the critical categories fully approved beats `1.0.0` with 210 half-reviewed cases. An eligibility rule already excludes what is not approved, so a partially annotated set is *usable*, not broken.
- **Report the coverage honestly** — which categories are approved, which are not, which slices cannot yet be concluded.

What I refuse to do: **write the references myself and have the experts "validate" them**. It sounds like an efficiency; it is the reverse of the annotation. An expert reviewing a plausible pre-written answer confirms it far more often than they would have produced it, and the dataset ends up encoding my assumptions with their signature on it.

If the time is genuinely insufficient for the scope, the correct output is a smaller approved set plus a statement of what is not covered — not 200 cases of unreviewed guesswork.

### c. The mandatory-fact list changes

- The change is **material** → a new dataset version, `2.0.0`. Every affected reference is re-annotated by the experts.
- **Historical results are not recomputed and not deleted.** They remain valid evidence about the candidate that ran, against the dataset version that was approved at the time.
- **The baseline comparison breaks.** A `1.x` result and a `2.0.0` result are not comparable, and the report must not place them side by side as a trend. Comparison requires compatible evaluation assets.
- Anything approved on the basis of `1.x` evidence stays approved on that basis; whether it must be re-evaluated is the product owner's decision, and the honest input to it is "we changed what correct means".

### d. The random-sampling proposal

> Random sampling is unbiased with respect to *production frequency*. That is the wrong target. We are not trying to estimate how the assistant performs on an average day — we are trying to find out whether it fails where failing is unacceptable.
>
> Concretely: vulnerable clients are around 3% of the book. A random 200 gives us six of them. We cannot conclude anything about a subgroup from six cases, and the regulatory risk sits precisely there. The same argument applies to name collisions and conflicting records — all rare, all where the damage is.
>
> A random sample is worth having *as one stratum*, and the ordinary-request category is exactly that. It is not the design.

The general form: **the aggregate answers "is it usually good"; slices answer "is it safe where it matters", and a slice needs population to answer at all.**

## Locate yourself

For each item, find the line closest to **what you actually wrote**, then read the verdict.

### 1. Your case skeletons

| | You wrote | |
|:--:|---|---|
| **A** | Every `reference` a placeholder naming who resolves it | ✅ |
| **B** | Illustrative references, marked "example only" | ❌ The exercise's single constraint. An expert reviewing a plausible pre-written answer confirms it far more often than they would have produced it — your assumptions then ship with their signature on them |
| **C** | The `reference` field left blank | ⚠️ Blank and placeholder look alike and are not. A blank reads as an oversight; `<pending annotation — owner: …>` reads as a decision you identified and declined to take |

### 2. Your composition

| | | |
|:--:|---|---|
| **A** | Risk categories over-represented, and you said why in the document | ✅ |
| **B** | Roughly production proportions, for representativeness | ❌ That yields about six vulnerable-client cases and no computable slice gate. Representativeness is of *intended use and known risk*, not of frequency |
| **C** | Over-represented, reasoning left implicit | ⚠️ The next person to read the spec will "correct" it back towards production proportions. Unstated reasoning does not survive a handover |

### 3. Three days of expert time

| | | |
|:--:|---|---|
| **A** | Experts on the critical categories, you do the non-expert work, ship a smaller approved version | ✅ |
| **B** | You draft the references, experts validate them | ❌ Sounds like efficiency, is the reverse of annotation. Same failure as item 1, wearing a process |
| **C** | Ask for more time, or cut the scope | ⚠️ Reasonable, and not an answer on its own — the eligibility rule already lets a partly annotated set be *usable* rather than broken |

### 4. The mandatory-fact list changing

| | | |
|:--:|---|---|
| **A** | New version; historical results kept, not recomputed; the baseline comparison breaks | ✅ |
| **B** | Update the references in place and rerun the affected evaluations | ❌ A silently rewritten baseline. Past reports now cite a dataset version whose content changed underneath them |
| **C** | New version, and you decided what to do about past approvals | ⚠️ Whether anything approved on the old evidence must be re-examined is the product owner's call. Your job is that they know, with the runs identified |

**Two or more ❌:** reread [Building a Golden Dataset](../../golden-datasets.md) and [Protecting evaluation data](../../data-protection.md) before module 06.
