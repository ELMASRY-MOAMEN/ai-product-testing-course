"""A critical slice must be able to fail a run that its aggregate would pass.

That is the entire reason slices exist, and it is the case the previous test
never exercised.
"""
from conftest import case
from run_evaluation import main
import aggregate_results


SLICE = [{"name": "regulated", "evaluator": "recall", "minimum": 0.90}]


def test_failing_slice_fails_a_run_whose_aggregate_passes(evaluation):
    standard = [case(f"S-{n:02}", ["alpha"], "alpha present", ["standard"]) for n in range(16)]
    regulated = [
        case("R-01", ["alpha", "beta"], "alpha present, beta present", ["regulated"]),
        case("R-02", ["alpha", "beta"], "alpha present only", ["regulated"]),
        case("R-03", ["alpha", "beta"], "alpha present only", ["regulated"]),
        case("R-04", ["alpha", "beta"], "alpha present, beta present", ["regulated"]),
    ]

    report = main(evaluation(standard + regulated, acceptance={
        "thresholds": {"recall": 0.85}, "critical_slices": SLICE, "vetoes": [],
    }))

    assert report["aggregate_results"]["recall"] >= 0.85, "the aggregate clears its threshold"
    assert report["slice_results"]["regulated"]["score"] == 0.75
    assert report["status"] == "Fail"
    assert report["reasons"] == [
        "critical slice 'regulated' at 0.75 below minimum 0.9"
    ]


def test_a_slice_with_no_eligible_case_is_not_ready_rather_than_passing(evaluation):
    cases = [case(f"S-{n:02}", ["alpha"], "alpha present", ["standard"]) for n in range(5)]

    report = main(evaluation(cases, acceptance={
        "thresholds": {"recall": 0.85}, "critical_slices": SLICE, "vetoes": [],
    }))

    assert report["status"] == "Not Ready"
    assert report["blockers"] == ["critical slice 'regulated' has no eligible case"]


def test_pass_rate_is_a_rate_and_not_a_count():
    """Regression: the key was named pass_rate and returned a number of cases."""
    results = [
        {"status": "completed", "passed": True},
        {"status": "completed", "passed": True},
        {"status": "completed", "passed": False},
        {"status": "completed", "passed": False},
    ]

    summary = aggregate_results.aggregate(results)

    assert summary["pass_rate"] == 0.5
    assert summary["passed"] == 2
    assert summary["failed"] == 2


def test_pass_rate_is_none_when_nothing_completed():
    assert aggregate_results.aggregate([])["pass_rate"] is None
