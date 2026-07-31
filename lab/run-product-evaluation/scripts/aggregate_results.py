"""Aggregate case results into coverage, per-evaluator scores and slice scores.

Slice scores are computed alongside the aggregate, never derived from it: a
slice exists precisely because the aggregate can hide it.
"""


def aggregate(results):
    """Coverage counts and the pass rate over completed cases."""
    completed = [result for result in results if result.get("status") == "completed"]
    failed = [result for result in completed if not result.get("passed", False)]
    return {
        "total": len(results),
        "completed": len(completed),
        "failed": len(failed),
        "passed": len(completed) - len(failed),
        "pass_rate": (len(completed) - len(failed)) / len(completed) if completed else None,
    }


def mean_score(results, evaluator_id):
    """Mean score for one evaluator over completed cases that it scored."""
    scores = [
        result["scores"][evaluator_id]
        for result in results
        if result.get("status") == "completed"
        and result.get("scores", {}).get(evaluator_id) is not None
    ]
    return sum(scores) / len(scores) if scores else None


def by_evaluator(results, evaluator_ids):
    return {evaluator_id: mean_score(results, evaluator_id) for evaluator_id in evaluator_ids}


def by_slice(results, slice_specs):
    """Score each declared critical slice independently, with its population."""
    scored = {}
    for spec in slice_specs:
        name = spec.get("name")
        member_results = [result for result in results if name in (result.get("slices") or [])]
        scored[name] = {
            "population": len(member_results),
            "score": mean_score(member_results, spec.get("evaluator")),
            "minimum": spec.get("minimum"),
            "evaluator": spec.get("evaluator"),
        }
    return scored


def veto_triggered(results):
    return any(result.get("veto", False) for result in results)


def triggered_vetoes(results):
    """The cases that triggered a veto, with the finding that explains each."""
    return [
        {"case_id": result.get("case_id"), "findings": result.get("veto_findings", [])}
        for result in results
        if result.get("veto", False)
    ]
