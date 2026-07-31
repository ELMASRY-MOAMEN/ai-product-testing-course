"""A control that is declared must be a control that can fire.

An external audit found that acceptance.vetoes was never checked against the
declared evaluators: a manifest could promise a blocking condition that no
case would ever be scored against, and the report would read as though the
control had held. That is the failure mode this repository's own audit
reference uses as its worked example, and the reference implementation did
not catch it.
"""
from conftest import case
from run_evaluation import main
import readiness

PASSING = [case(f"C-{n:02}", ["alpha"], "alpha present", ["standard"]) for n in range(5)]


def test_a_veto_naming_an_undeclared_evaluator_is_not_ready(evaluation):
    report = main(evaluation(PASSING, acceptance={
        "thresholds": {"recall": 0.85},
        "critical_slices": [],
        "vetoes": [{"evaluator": "factual-invention", "condition": "any_triggered"}],
    }))

    assert report["status"] == "Not Ready"
    assert "veto names undeclared evaluator 'factual-invention'" in report["blockers"]
    assert report["case_results"] == [], "a promised control that cannot fire stops the run"


def test_a_slice_naming_an_undeclared_evaluator_is_not_ready(evaluation):
    report = main(evaluation(PASSING, acceptance={
        "thresholds": {"recall": 0.85},
        "critical_slices": [{"name": "regulated", "evaluator": "groundedness", "minimum": 0.9}],
        "vetoes": [],
    }))

    assert report["status"] == "Not Ready"
    assert "critical slice 'regulated' names undeclared evaluator 'groundedness'" in report["blockers"]


def test_an_undeclared_anonymisation_status_is_not_ready(evaluation):
    """The data policy's central rule, previously enforced by no code at all."""
    report = main(evaluation(PASSING, evaluation_data={"path": "dataset.jsonl", "version": "1.0.0"}))

    assert report["status"] == "Not Ready"
    assert "evaluation data declares no anonymisation status" in report["blockers"]


def test_a_declared_anonymisation_status_lets_the_run_proceed(evaluation):
    report = main(evaluation(PASSING))
    assert report["status"] == "Pass"


def test_the_audited_manifest_shape_is_caught_in_full():
    """The exact combination an external audit found passing: nothing declared."""
    manifest = {
        "evaluation": {"id": "x", "version": "1", "framework": "DoT"},
        "candidate": {"name": "x", "version": "latest"},
        "candidate_adapter": {"type": "http"},
        "evaluation_data": {"path": "cases.jsonl", "version": "2026-06"},
        "evaluators": [{"id": "category-accuracy", "type": "exact_match"}],
        "acceptance": {
            "thresholds": {"category-accuracy": 0.85},
            "critical_slices": [],
            "vetoes": [{"evaluator": "factual-invention", "condition": "any_triggered"}],
        },
        "evidence": {"output_dir": "/tmp"},
        "ownership": {"decision_owner": "Product Owner"},
    }

    blockers = readiness.blockers(manifest)

    assert "veto names undeclared evaluator 'factual-invention'" in blockers
    assert "evaluation data declares no anonymisation status" in blockers
    assert "candidate is not frozen for the run" in blockers
