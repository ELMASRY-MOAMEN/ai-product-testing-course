"""Validate the structure of an evaluation manifest against its schema.

The schema is the contract, and this script enforces it — there is no second
list of requirements maintained here that could drift from it. An external
audit found exactly that split: the schema required only the top-level
sections, this script required a dozen fields, nothing ran the schema, and a
newcomer validating against the file that looked authoritative got a clean
pass followed by a runner that refused the manifest.

Structure only. Whether the declared values were approved is readiness.
"""
from pathlib import Path
import json
import sys

import jsonschema
import yaml

SCHEMA = Path(__file__).parents[1] / "schemas" / "manifest.schema.json"


def load(path):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}


def schema():
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def describe(error):
    """A schema error a reader can act on, not a stack of internal paths."""
    location = ".".join(str(part) for part in error.absolute_path)
    return f"{location}: {error.message}" if location else error.message


def validate(path):
    data = load(path)
    validator = jsonschema.Draft202012Validator(schema())
    return [describe(error) for error in sorted(validator.iter_errors(data), key=str)]


if __name__ == "__main__":
    found = validate(sys.argv[1])
    print("\n".join(found) if found else "valid")
    raise SystemExit(bool(found))
