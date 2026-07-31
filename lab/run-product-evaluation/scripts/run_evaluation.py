"""Execute an approved evaluation manifest and produce a verdict with evidence.

The verdict order is fixed and each step can only end the run, never reverse
an earlier one: readiness, then vetoes, then critical slices, then aggregate
thresholds. A high aggregate can therefore never buy off a veto.
"""
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parents[1] / "adapters"))

import aggregate_results
import create_report
import evaluators as evaluator_registry
import readiness
from redact import redact
from validate_manifest import load, validate


def write_evidence(manifest_path, manifest, report):
    """Persist the report where the manifest says evidence lives.

    Returned reports used to exist only on stdout. Nothing was written to
    evidence.output_dir, although the schema requires the field and the
    evidence policy states that a result which cannot be located is not
    evidence. The directory is resolved relative to the manifest, so a run is
    self-contained wherever the manifest sits.
    """
    declared = ((manifest.get("evidence") or {}).get("output_dir") or "").strip()
    if not declared or declared.startswith("<"):
        return None

    directory = Path(declared)
    if not directory.is_absolute():
        directory = Path(manifest_path).parent / directory
    directory.mkdir(parents=True, exist_ok=True)

    (directory / "report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    create_report.create(report, directory / "report.md")
    return directory


def not_ready(blockers):
    return {
        "status": "Not Ready",
        "blockers": blockers,
        "case_results": [],
        "aggregate_results": {},
        "slice_results": {},
        "vetoes": [],
    }


def load_cases(manifest_path, manifest):
    path = Path(manifest_path).parent / manifest["evaluation_data"]["path"]
    if not path.exists():
        return None, [f"evaluation data not readable: {path.name}"]
    cases = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return cases, []


USABLE_ANNOTATION = {"approved", "derived"}


def eligible(cases):
    """Cases a run may include.

    Two annotation statuses are usable, for different reasons. `approved` means
    a qualified human judged what the right answer is and the judgement was
    reviewed. `derived` means the expected output follows from a specification,
    so there was nothing to judge — the correct status for a DoD case, which
    needs no annotated reference. Requiring `approved` on a formula-derived case
    stretches the word until it means nothing.
    """
    return [
        case for case in cases
        if case.get("eligibility", False) and case.get("annotation_status") in USABLE_ANNOTATION
    ]


def resolve_adapter(manifest):
    kind = manifest["candidate_adapter"]["type"]
    if kind != "mock":
        raise KeyError(f"no adapter registered for type {kind!r}")
    from mock_adapter import MockAdapter
    return MockAdapter()


def veto_evaluators(acceptance):
    """Only an evaluator named in acceptance.vetoes may veto.

    An evaluator that reports a triggering condition without being declared as
    a veto contributes findings, not a block: declaring the veto is an approval,
    and the runner does not grant itself one.
    """
    return {entry["evaluator"] for entry in acceptance.get("vetoes") or []}


def gate_of(spec):
    """DoD evaluators assert; DoT evaluators measure. Default is DoT."""
    return spec.get("gate", "DoT")


def evaluate_case(case, output, declared, vetoing):
    scores, findings, veto, veto_findings = {}, [], False, []
    assertions, assertion_findings = {}, {}
    for spec in declared:
        result = evaluator_registry.resolve(spec["type"])(case, output)
        scores[spec["id"]] = result.get("score")
        findings += result.get("findings", [])
        assertion_findings[spec["id"]] = result.get("findings", [])
        if gate_of(spec) == "DoD":
            # A DoD evaluator must say so explicitly. Inferring the assertion
            # from the score silently turns "nothing to check" — a score of
            # None — into a failed assertion.
            if "passed" not in result:
                raise KeyError(
                    f"DoD evaluator {spec['id']!r} ({spec['type']}) returned no 'passed' key; "
                    "an assertion must state whether it held"
                )
            assertions[spec["id"]] = result["passed"]
        if result.get("triggered") and spec["id"] in vetoing:
            veto = True
            veto_findings += result.get("findings", [])
    return scores, findings, veto, veto_findings, assertions, assertion_findings


def assertion_failures(case_results, declared):
    """Every DoD assertion that failed, with the case and its own findings.

    A DoD assertion carries no threshold, because there is nothing to average:
    a schema either conforms or it does not. One failure fails the gate, and no
    probabilistic score repairs it.

    Each entry carries the findings of *that* assertion. Attributing the case's
    combined findings to every failed assertion would tell a reader that two
    controls found the same thing, when each found its own.
    """
    return [
        {
            "case_id": result["case_id"],
            "assertion": evaluator_id,
            "findings": (result.get("assertion_findings") or {}).get(evaluator_id, []),
        }
        for result in case_results
        for evaluator_id, passed in (result.get("assertions") or {}).items()
        if not passed
    ]


def main(manifest_path):
    structural = validate(manifest_path)
    if structural:
        return not_ready(structural)

    manifest = load(manifest_path)

    blockers = readiness.blockers(manifest)
    if blockers:
        # A Not Ready outcome is evidence too: it records which decision was
        # missing, and when.
        report = not_ready(blockers)
        write_evidence(manifest_path, manifest, report)
        return report

    cases, data_blockers = load_cases(manifest_path, manifest)
    if data_blockers:
        report = not_ready(data_blockers)
        write_evidence(manifest_path, manifest, report)
        return report

    declared = manifest["evaluators"]
    acceptance = manifest["acceptance"]
    vetoing = veto_evaluators(acceptance)
    adapter = resolve_adapter(manifest)

    case_results = []
    for case in eligible(cases):
        invoked = adapter.invoke(case)
        if invoked.get("status") != "completed":
            case_results.append({
                "case_id": case["case_id"], "status": "error",
                "error": invoked.get("error"), "slices": case.get("slices", []),
            })
            continue
        output = invoked["candidate_output"]
        scores, findings, veto, veto_findings, assertions, assertion_findings = evaluate_case(
            case, output, declared, vetoing
        )
        case_results.append({
            "case_id": case["case_id"],
            "status": "completed",
            "slices": case.get("slices", []),
            "candidate_output": output,
            "scores": scores,
            "findings": findings,
            "assertions": assertions,
            "assertion_findings": assertion_findings,
            "passed": not findings and not veto,
            "veto": veto,
            "veto_findings": veto_findings,
        })

    coverage = aggregate_results.aggregate(case_results)
    scores = aggregate_results.by_evaluator(case_results, [spec["id"] for spec in declared])
    slices = aggregate_results.by_slice(case_results, acceptance["critical_slices"])
    vetoes = aggregate_results.triggered_vetoes(case_results)

    empty = [name for name, result in slices.items() if result["population"] == 0]
    if empty:
        report = not_ready([f"critical slice {name!r} has no eligible case" for name in empty])
        write_evidence(manifest_path, manifest, report)
        return report

    # Acceptance is conjunctive: the DoD gate and the DoT gate must both pass.
    # A strong probabilistic score never repairs a failed deterministic
    # assertion, which is why the two are reported separately and never merged
    # into one number.
    failed_assertions = assertion_failures(case_results, declared)

    reasons = []
    if failed_assertions:
        distinct = sorted({entry["assertion"] for entry in failed_assertions})
        reasons.append(
            f"DoD gate: {len(failed_assertions)} assertion failure(s) on {', '.join(distinct)}"
        )

    # Within the DoT gate: vetoes, then critical slices, then aggregate thresholds.
    if vetoes:
        reasons.append(f"{len(vetoes)} veto(es) triggered")
    for name, result in slices.items():
        if result["score"] is None or result["score"] < result["minimum"]:
            reasons.append(f"critical slice {name!r} at {result['score']} below minimum {result['minimum']}")
    for evaluator_id, threshold in acceptance["thresholds"].items():
        measured = scores.get(evaluator_id)
        if measured is None or measured < threshold:
            reasons.append(f"{evaluator_id} at {measured} below threshold {threshold}")

    dot_reasons = [reason for reason in reasons if not reason.startswith("DoD gate:")]

    report = {
        "status": "Fail" if reasons else "Pass",
        "reasons": reasons,
        "gates": {
            "DoD": ("Fail" if failed_assertions else "Pass")
            if any(gate_of(spec) == "DoD" for spec in declared)
            else "Not evaluated",
            "DoT": ("Fail" if dot_reasons else "Pass")
            if any(gate_of(spec) == "DoT" for spec in declared)
            else "Not evaluated",
        },
        "candidate": manifest["candidate"],
        "evaluators": declared,
        "dataset_version": manifest["evaluation_data"]["version"],
        "coverage": coverage,
        "case_results": case_results,
        "aggregate_results": scores,
        "slice_results": slices,
        "assertion_failures": failed_assertions,
        "vetoes": vetoes,
    }
    report = redact(report)
    written = write_evidence(manifest_path, manifest, report)
    if written is not None:
        report["evidence_written_to"] = str(written)
    return report


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1]), indent=2))
