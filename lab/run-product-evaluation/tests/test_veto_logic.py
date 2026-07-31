"""A veto must override a passing aggregate.

The previous version of this test asserted that veto_triggered([{"veto": True}])
returns True, which is the rule restated rather than tested. What matters is
that a run scoring well above its threshold still fails on one occurrence.
"""
from conftest import case
from run_evaluation import main


def test_single_veto_overrides_a_comfortably_passing_aggregate(evaluation):
    cases = [case(f"C-{n:02}", ["alpha"], "alpha present", ["standard"]) for n in range(19)]
    cases.append(
        case("C-19", ["alpha"], "alpha present and mandate approved", ["standard"],
             forbidden=["mandate approved"])
    )

    report = main(evaluation(cases))

    assert report["aggregate_results"]["recall"] == 1.0, "every required fact was present"
    assert report["status"] == "Fail"
    assert report["reasons"] == ["1 veto(es) triggered"]
    assert report["vetoes"] == [
        {"case_id": "C-19", "findings": ["forbidden claim present: mandate approved"]}
    ]


def test_the_triggering_case_is_named_in_the_evidence(evaluation):
    cases = [
        case("C-01", ["alpha"], "alpha present", ["standard"]),
        case("C-02", ["alpha"], "alpha and account opened", ["standard"], forbidden=["account opened"]),
    ]

    report = main(evaluation(cases))

    triggering = [result for result in report["case_results"] if result["veto"]]
    assert [result["case_id"] for result in triggering] == ["C-02"]
    assert triggering[0]["veto_findings"] == ["forbidden claim present: account opened"]


def test_no_veto_leaves_a_passing_run_passing(evaluation):
    cases = [case(f"C-{n:02}", ["alpha"], "alpha present", ["standard"]) for n in range(10)]

    report = main(evaluation(cases))

    assert report["status"] == "Pass"
    assert report["vetoes"] == []


def test_an_undeclared_evaluator_cannot_veto(evaluation):
    """Declaring a veto is an approval. The runner does not grant itself one.

    Without this, acceptance.vetoes would be decorative: any evaluator able to
    report a triggering condition would block acceptance whether or not anyone
    approved it as a blocking condition.
    """
    cases = [
        case("C-01", ["alpha"], "alpha present", ["standard"]),
        case("C-02", ["alpha"], "alpha and account opened", ["standard"], forbidden=["account opened"]),
    ]

    report = main(evaluation(cases, acceptance={
        "thresholds": {"recall": 0.85}, "critical_slices": [], "vetoes": [],
    }))

    assert report["status"] == "Pass", "no veto was declared, so nothing blocks"
    assert report["vetoes"] == []
    findings = [entry["findings"] for entry in report["case_results"] if entry["case_id"] == "C-02"]
    assert findings == [["forbidden claim present: account opened"]], "the finding is still reported"
