---
type: example
status: reviewed
audience: [qa, engineering, data-ai]
---

# Solution — Fill a manifest from a brief

Read this only after attempting [the exercise](../fill-a-manifest-from-a-brief.md).

The completed artefact is [`claimtriage-manifest.yaml`](claimtriage-manifest.yaml), in its **second** state — after Thursday. The comment at the top tells you how to put it back into its Monday state.

## 1. Reading the brief into the manifest

| The brief says | The manifest gets |
|---|---|
| "claim summary … version 2.3.0, frozen since Monday" | `candidate.version: 2.3.0`, `frozen: true` |
| "8 synthetic cases, version 1.0.0, annotated and approved" | `evaluation_data.version: 1.0.0`, `anonymisation: synthetic` |
| "must carry the facts the queue owner needs … listed per case" | evaluator `required_facts_recall`, gate DoT |
| "**We approved 0.90** … before anyone ran anything" | `thresholds.required-facts-recall: 0.90` |
| "high-value claims … looked at separately" | a `critical_slices` entry named `high-value` |
| "we have not agreed how strict … on the agenda for Thursday" | `minimum: <approved-minimum>` — **left as a placeholder** |
| "must never state that a claim is approved when it is not" | evaluator `forbidden_claims` + a veto, `condition: any_triggered` |
| "I own the acceptance decision" | `ownership.decision_owner` |

Two details worth noticing.

**"Approved on Monday, before anyone ran anything"** is not decoration. A threshold approved after seeing results is not a threshold, and the brief is telling you this one is legitimate. Had it said *"0.90, that's roughly what we saw last sprint"*, the correct response would have been to challenge it — as in [the module 03 exercise](../../../03-the-two-gates/exercises/score-a-dot-against-its-ten-components.md).

**Legal's requirement became an evaluator *and* a veto.** Neither alone is enough: an evaluator with no veto produces a score that gets averaged away, and a veto naming an evaluator nobody declared is a control that can never fire. The runner blocks that second case explicitly — `veto names undeclared evaluator`.

## 2. The prediction

```text
Status:   Not Ready
Blockers: unresolved placeholder: acceptance.critical_slices[0].minimum
```

Exactly one blocker. Everything else in the brief was decided.

## 3. What the runner reports on Monday

```json
{
  "status": "Not Ready",
  "blockers": [
    "unresolved placeholder: acceptance.critical_slices[0].minimum"
  ],
  "case_results": [],
  "aggregate_results": {},
  "slice_results": {},
  "vetoes": []
}
```

### If your prediction was `Pass` or `Fail`

You probably filled the minimum with something reasonable — 0.90, or 0.95 to be safe. Reread what that does: it produces a slice gate the product owner never agreed to, and the report will show that gate as satisfied. Thursday's meeting then discusses a decision that has already been made in evidence.

### If you predicted extra blockers

Check whether you left other placeholders in — `evidence.output_dir` and the `ownership` fields are placeholders in the template too, and the runner treats every `<…>` the same way.

**Leaving `approved_by` and `approved_on` open on Monday is the stricter answer, and it is defensible.** The reasoning: those fields sit in one block covering the whole `acceptance` section, and on Monday one part of that section — the slice minimum — has been approved by nobody. Filling them then asserts an approval of an acceptance policy that does not yet exist in full.

The manifest here fills them because the brief records a real approval, of the threshold, on a real date. Both readings survive the only test that matters — *is every filled field backed by a record?* — and a submission that leaves them open and **says why** is stronger than one that fills them without noticing there was a question.

What is not defensible is filling them without a record behind them. See question 5.

## 4. After Thursday

### a. The verdict

```json
{
  "status": "Fail",
  "reasons": ["1 veto(es) triggered"],
  "aggregate_results": {
    "required-facts-recall": 0.927,
    "unsupported-approval": 0.875
  },
  "slice_results": {
    "high-value": { "population": 3, "score": 0.917, "minimum": 0.9 }
  },
  "vetoes": [
    { "case_id": "CT-007", "findings": ["forbidden claim present: claim approved"] }
  ]
}
```

**Fail**, decided by a single case. `CT-007` summarises a flood claim correctly — *flood damage*, *warehouse stock*, *valuation pending*, all three required facts present, recall 1.0 — and then adds "claim approved subject to the adjuster's report."

The case scores **perfectly** on the metric and blocks the release.

### b. Why the two green gates are not enough

Because 0.927 and 0.917 answer *"is the typical summary good enough"* and *"is the high-value subgroup good enough"* — and neither question is *"did we tell a queue owner that an unapproved claim was approved"*, which has no acceptable rate.

### c. `case_results` in the two runs

**Monday: `[]`. Empty.** Not eight cases with null scores — nothing. The candidate was never invoked.

That is what `Not Ready` means, and why it is not a milder `Fail`. A `Fail` says *we measured this product and it fell short*. `Not Ready` says *no measurement happened, so nothing may be concluded about this product*. Anyone reading the Monday report can see there is no evidence in it, because there is none.

If the runner had scored the cases and merely warned about the missing minimum, the report would contain real numbers under an incomplete acceptance rule — and those numbers would be quoted in Thursday's meeting.

## 5. The ownership block

Filled in, it looks like this:

```yaml
ownership:
  decision_owner: product owner, claims triage
  approved_by: product owner, claims triage
  approved_on: 2026-07-31
```

**What would make it false evidence:** you typing it because the brief mentioned a role, with no recorded approval behind it. A name in a field is not a sign-off. The manifest would then assert that someone approved these thresholds on that date — and the report, the release ticket and any audit would carry that assertion forward as fact.

Note that this is the one field an agent or a hurried tester fills without hesitating, because it *looks* like transcription rather than judgement.

**What you need for it to be true:** a recorded approval you can point at — the design-review minutes for the 0.90 threshold, and Thursday's written confirmation for the slice minimum — naming who approved what, and when. If you have the record, transcribe it. If you do not, the field stays a placeholder and the manifest stays `Not Ready`, however uncomfortable that is on a release day.

## What to check in your own answer

| | |
|---|---|
| ☐ | Two evaluators declared, both at gate DoT |
| ☐ | Legal's requirement wired as **both** an evaluator and a veto |
| ☐ | Slice minimum left as a placeholder on Monday |
| ☐ | Slice **not deleted** to obtain a clean run |
| ☐ | Prediction was `Not Ready`, and matched **your own** manifest blocker for blocker |
| ☐ | You saw `case_results: []` and could say what it proves |
| ☐ | Final verdict `Fail`, decided by CT-007, whose recall is perfect |
| ☐ | You can state what would make the ownership block false |

Five or fewer: reread [Minimum execution manifest](../../evaluation-manifest.md) and [What the automated evaluation runner should produce](../../reporting-and-evidence.md) before module 06.
