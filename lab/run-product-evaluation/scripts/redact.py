"""Redact secret-bearing values before evidence is written or reported.

An evaluation run submits controlled inputs to a candidate and retains case
outputs, traces and versions as evidence. That evidence must never carry
credentials. Redaction replaces the value while keeping its key visible, so a
reader can see that a secret was present and suppressed rather than silently
dropped.
"""
import re

MARKERS = ("api_key", "apikey", "token", "secret", "password", "authorization")

REDACTED = "[REDACTED]"

_ASSIGNMENT = re.compile(
    r"(?i)\b(" + "|".join(MARKERS) + r")\b(\s*[=:]\s*)([^\s,;'\"}\]]+)"
)


def is_secret_key(key):
    """Report whether a mapping key names a secret."""
    return isinstance(key, str) and any(marker in key.lower() for marker in MARKERS)


def redact(value):
    """Redact secrets in a string, or recursively through a dict or list.

    Strings are scanned for `key=value` and `key: value` assignments. Mapping
    entries whose key names a secret have their whole value replaced, since the
    value carries no useful evidence once identified as a credential.
    """
    if isinstance(value, str):
        return _ASSIGNMENT.sub(lambda match: f"{match.group(1)}{match.group(2)}{REDACTED}", value)
    if isinstance(value, dict):
        return {key: REDACTED if is_secret_key(key) else redact(item) for key, item in value.items()}
    if isinstance(value, list):
        return [redact(item) for item in value]
    return value
