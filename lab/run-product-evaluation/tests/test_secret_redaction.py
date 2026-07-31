import sys
from pathlib import Path

SCRIPTS = Path(__file__).parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from redact import redact  # noqa: E402
from create_report import create  # noqa: E402


def test_redacts_assigned_secret():
    assert redact("token=abc123") == "token=[REDACTED]"


def test_redacts_colon_form_and_keeps_the_key_visible():
    assert redact("api_key: placeholder-value") == "api_key: [REDACTED]"


def test_redacts_nested_evidence_structures():
    evidence = {"headers": {"Authorization": "Bearer abc"}, "notes": ["secret=hunter2"]}
    assert redact(evidence) == {"headers": {"Authorization": "[REDACTED]"}, "notes": ["secret=[REDACTED]"]}


def test_leaves_ordinary_evidence_untouched():
    assert redact("the run completed 12 cases with 2 failures") == "the run completed 12 cases with 2 failures"


def test_report_creation_redacts_case_evidence(tmp_path):
    """The guardrail must hold on the path that actually writes evidence.

    An earlier version of this test built a case result with a `result` key,
    which case results have never carried — so it exercised a field the report
    renderer read and the runner never produced, and passed on the defect.
    """
    destination = tmp_path / "report.md"
    create({
        "status": "Fail",
        "reasons": ["DoD gate: 1 assertion failure(s) on schema"],
        "case_results": [{
            "case_id": "c1",
            "status": "completed",
            "findings": ["token=abc123 was rejected"],
        }],
        "assertion_failures": [{
            "case_id": "c1", "assertion": "schema", "findings": ["password=hunter2 in payload"],
        }],
    }, destination)

    written = destination.read_text(encoding="utf-8")

    assert "hunter2" not in written
    assert "abc123" not in written
    assert "password=[REDACTED]" in written
    assert "token=[REDACTED]" in written
    assert "c1" in written, "the case must still be identifiable"
