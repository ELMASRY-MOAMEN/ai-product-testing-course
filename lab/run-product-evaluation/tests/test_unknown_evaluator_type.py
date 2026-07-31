"""An evaluator type the registry does not have must block before the run.

The prose in select-ai-evaluators lists evaluator categories as though they
were all available — "calculations and totals: exact value comparison" among
them. A manifest declaring a type the registry lacks used to raise KeyError
part-way through execution, after cases had already been invoked. A promised
measurement that nothing can make is a readiness failure, not a crash.
"""
from conftest import case
from run_evaluation import main
import evaluators
import readiness

PASSING = [case(f"C-{n:02}", ["alpha"], "alpha present", ["standard"]) for n in range(3)]

# Replacing the declared evaluators means replacing the acceptance section that
# refers to them. Leaving the fixture's default in place produces dangling
# references — which readiness now reports, correctly.
ASSERTIONS_ONLY = {"thresholds": {}, "critical_slices": [], "vetoes": []}


def test_an_unknown_type_is_not_ready_and_lists_what_exists(evaluation):
    report = main(evaluation(PASSING, acceptance=ASSERTIONS_ONLY, evaluators=[
        {"id": "premium", "type": "exact_value_comparison", "gate": "DoD", "version": "1.0.0"},
    ]))

    assert report["status"] == "Not Ready"
    blocker = next(b for b in report["blockers"] if "unknown type" in b)
    assert "'exact_value_comparison'" in blocker
    assert "exact_values" in blocker, "the blocker must name the types that do exist"
    assert report["case_results"] == [], "no case is invoked before readiness passes"


def test_every_registered_type_is_accepted_by_readiness():
    """The counterpart: readiness must not reject a type that exists."""
    for name in evaluators.REGISTRY:
        manifest = {
            "evaluation": {"id": "x", "version": "1", "framework": "DoT"},
            "candidate": {"name": "x", "version": "1", "frozen": True},
            "candidate_adapter": {"type": "mock"},
            "evaluation_data": {"path": "d.jsonl", "version": "1", "anonymisation": "synthetic"},
            "evaluators": [{"id": "e", "type": name, "gate": "DoD"}],
            "acceptance": {"thresholds": {}, "critical_slices": [], "vetoes": []},
            "evidence": {"output_dir": "e"},
            "ownership": {"decision_owner": "po"},
        }
        assert not [b for b in readiness.blockers(manifest) if "unknown type" in b], name


def test_exact_values_asserts_a_calculation(evaluation):
    """The evaluator the prose promised and the registry did not have."""
    cases = [
        {**case("P-01", [], "quoted", ["standard"]),
         "reference": {"expected_values": {"premium": 842.50, "rating_table": "TBL-C"}},
         "mock_output": {"premium": 842.50, "rating_table": "TBL-C"}},
        {**case("P-02", [], "quoted", ["standard"]),
         "reference": {"expected_values": {"premium": 842.50, "rating_table": "TBL-C"}},
         "mock_output": {"premium": 842.5001, "rating_table": "TBL-C"}},
    ]

    report = main(evaluation(cases, acceptance=ASSERTIONS_ONLY, evaluators=[
        {"id": "premium-exact", "type": "exact_values", "gate": "DoD", "version": "1.0.0"},
    ]))

    assert report["status"] == "Fail"
    assert report["gates"] == {"DoD": "Fail", "DoT": "Not evaluated"}
    failures = {entry["case_id"]: entry["findings"] for entry in report["assertion_failures"]}
    assert failures == {"P-02": ["premium was 842.5001, expected 842.5"]}


def test_arbitrary_domain_fields_reach_the_evaluators(evaluation):
    """A domain must not have to bend `answer` into meaning a premium."""
    cases = [
        {**case("P-01", [], "", ["standard"]),
         "reference": {"required_fields": ["premium", "decision_record_id"]},
         "mock_output": {"premium": 842.50, "decision_record_id": "PD-99213"}},
    ]

    report = main(evaluation(cases, acceptance=ASSERTIONS_ONLY, evaluators=[
        {"id": "output-schema", "type": "schema_conformance", "gate": "DoD", "version": "1.0.0"},
    ]))

    assert report["status"] == "Pass"
    assert report["case_results"][0]["candidate_output"]["premium"] == 842.50
