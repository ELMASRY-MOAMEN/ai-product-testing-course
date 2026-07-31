"""Validate that every relative Markdown link resolves.

Fenced code blocks and inline code spans are skipped: a document that
documents link syntax must be able to show an example without the example
being read as a broken link.
"""
from pathlib import Path
import re
import sys

EXCLUDED_DIRS = {".git", ".venv", ".pytest_cache", ".obsidian", "node_modules", "__pycache__", "evidence"}

LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
INLINE_CODE = re.compile(r"`[^`]*`")


def targets(text):
    """Yield (line number, target) for every link outside code."""
    in_fence = False
    for number, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK.finditer(INLINE_CODE.sub("", line)):
            yield number, match.group(1)


def validate(path):
    errors = []
    for number, target in targets(Path(path).read_text(encoding="utf-8")):
        if "://" in target or target.startswith(("mailto:", "#")):
            continue
        resolved = (Path(path).parent / target.split("#")[0]).resolve()
        if not resolved.exists():
            errors.append(f"{path}:{number}: unresolved link {target!r}")
    return errors


def collect(root):
    if root.is_file():
        return [root]
    return [path for path in sorted(root.rglob("*.md")) if not EXCLUDED_DIRS & set(path.parts)]


if __name__ == "__main__":
    roots = [Path(argument) for argument in sys.argv[1:]] or [Path(__file__).parents[1]]
    files = [path for root in roots for path in collect(root)]
    errors = [error for path in files for error in validate(path)]
    print("\n".join(errors) if errors else f"links valid ({len(files)} files)")
    raise SystemExit(bool(errors))
