"""Not Ready must be distinguishable from Fail.

Fail means the candidate was measured and fell short. Not Ready means nothing
was measured, so nothing may be concluded about the candidate. Collapsing the
two either slanders the candidate or claims evidence that does not exist.
"""
from conftest import case
from run_evaluation import main


PASSING = [case(f"C-{n:02}", ["alpha"], "alpha present", ["standard"]) for n in range(5)]


def test_missing_threshold_is_not_ready_not_fail(evaluation):
    report = main(evaluation(PASSING, acceptance={
        "thresholds": {}, "critical_slices": [], "vetoes": [],
    }))

    assert report["status"] == "Not Ready"
    assert "no approved threshold declared" in report["blockers"]
    assert report["case_results"] == [], "nothing may be measured before readiness"


def test_unresolved_placeholder_is_not_ready(evaluation):
    report = main(evaluation(PASSING, acceptance={
        "thresholds": {"recall": "<approved-threshold>"}, "critical_slices": [], "vetoes": [],
    }))

    assert report["status"] == "Not Ready"
    assert "unresolved placeholder: acceptance.thresholds.recall" in report["blockers"]


def test_unfrozen_candidate_is_not_ready(evaluation):
    report = main(evaluation(PASSING, candidate={"name": "mock", "version": "1.0.0", "frozen": False}))

    assert report["status"] == "Not Ready"
    assert "candidate is not frozen for the run" in report["blockers"]


def test_threshold_naming_an_undeclared_evaluator_is_not_ready(evaluation):
    report = main(evaluation(PASSING, acceptance={
        "thresholds": {"groundedness": 0.9}, "critical_slices": [], "vetoes": [],
    }))

    assert report["status"] == "Not Ready"
    assert "threshold names undeclared evaluator 'groundedness'" in report["blockers"]


def test_slice_without_an_approved_minimum_is_not_ready(evaluation):
    report = main(evaluation(PASSING, acceptance={
        "thresholds": {"recall": 0.85},
        "critical_slices": [{"name": "regulated", "evaluator": "recall"}],
        "vetoes": [],
    }))

    assert report["status"] == "Not Ready"
    assert "critical slice regulated has no approved minimum" in report["blockers"]


def test_a_complete_manifest_is_allowed_to_run(evaluation):
    """The counterpart: readiness must not block a manifest that declares everything."""
    report = main(evaluation(PASSING))

    assert report["status"] == "Pass"
    assert len(report["case_results"]) == 5
