"""Summarise one or more JUnit XML reports by test level.

Usage: python scripts/summarize_junit.py <report.xml> [<report.xml> ...]

Prints a JSON summary: totals, results per level (component, integration,
system, unclassified), and every failure, error and skip with its message.
A level with no test is reported as "not tested", never as passing; a skipped
or errored test is never counted as passed.

Exit codes: 0 when the reports were read (whatever the results), 2 when a
report is missing or is not JUnit XML.
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

LEVELS = ("component", "integration", "system")
LEVEL_TOKENS = {
    "unit": "component",
    "component": "component",
    "integration": "integration",
    "system": "system",
    "e2e": "system",
}
TOKEN_SPLIT = re.compile(r"[\\/.:_\-\s\[\]()]+")


class ReportError(Exception):
    """A report that cannot be read as JUnit XML."""


def infer_level(*labels):
    """The level named by the first recognised token in the labels, or None."""
    for label in labels:
        for token in TOKEN_SPLIT.split((label or "").lower()):
            if token in LEVEL_TOKENS:
                return LEVEL_TOKENS[token]
    return None


def outcome(testcase):
    """(status, message) for one <testcase>: passed, failed, error or skipped."""
    for tag, status in (("failure", "failed"), ("error", "error"), ("skipped", "skipped")):
        element = testcase.find(tag)
        if element is not None:
            message = element.get("message") or (element.text or "").strip()
            return status, message.splitlines()[0][:500] if message else ""
    return "passed", ""


def read_report(path):
    path = Path(path)
    if not path.is_file():
        raise ReportError(f"{path}: file not found")
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as error:
        raise ReportError(f"{path}: not valid XML ({error})") from error
    if root.tag not in ("testsuites", "testsuite"):
        raise ReportError(f"{path}: root element is <{root.tag}>, expected <testsuites> or <testsuite>")
    results = []
    for testcase in root.iter("testcase"):
        file_label = testcase.get("file", "")
        classname = testcase.get("classname", "")
        name = testcase.get("name", "")
        status, message = outcome(testcase)
        results.append({
            "test": f"{classname}::{name}" if classname else name,
            "file": file_label,
            "level": infer_level(file_label, classname, name) or "unclassified",
            "status": status,
            "message": message,
            "time": float(testcase.get("time") or 0),
        })
    return results


def empty_counts():
    return {"tests": 0, "passed": 0, "failures": 0, "errors": 0, "skipped": 0}


def level_status(counts):
    if counts["tests"] == 0:
        return "not tested"
    if counts["failures"]:
        return "failed"
    if counts["errors"]:
        return "incomplete"
    if counts["passed"] == 0:
        return "not tested"
    return "passed"


def summarise(paths):
    results = [result for path in paths for result in read_report(path)]
    totals = empty_counts()
    levels = {level: empty_counts() for level in (*LEVELS, "unclassified")}
    key = {"passed": "passed", "failed": "failures", "error": "errors", "skipped": "skipped"}
    for result in results:
        for counts in (totals, levels[result["level"]]):
            counts["tests"] += 1
            counts[key[result["status"]]] += 1
    for level, counts in levels.items():
        counts["status"] = level_status(counts)

    def listed(status):
        return [
            {"test": r["test"], "level": r["level"], "message": r["message"]}
            for r in results if r["status"] == status
        ]

    return {
        "reports": [str(path) for path in paths],
        "totals": totals,
        "levels": levels,
        "failures": listed("failed"),
        "errors": listed("error"),
        "skipped": listed("skipped"),
        "unclassified": [r["test"] for r in results if r["level"] == "unclassified"],
    }


def main(argv):
    if not argv:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    try:
        summary = summarise(argv)
    except ReportError as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):  # Windows pipes default to the ANSI code page
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
