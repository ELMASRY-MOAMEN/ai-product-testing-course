"""Validate what the link checker cannot see: absence.

`validate_links.py` walks the links that exist and confirms they resolve. It
reported 84 valid files while the reading chain silently skipped all six
exercises — because a chain that omits a page contains no broken link. A check
that iterates over what is there can never report what is missing.

So this one starts from what *should* be there and asks whether it is:

  1. every page in the reading chain ends with exactly one navigation footer;
  2. the chain is a chain — each Next matches the following step's Previous;
  3. every exercise is reachable by following Next from the first step;
  4. every Markdown file has at least one inbound link from another file.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).parents[1]

EXCLUDED_DIRS = {".git", ".venv", ".obsidian", "__pycache__", "evidence", "my-work", "lab"}

FIRST_STEP = "00-orientation/how-to-use-this-course.md"

LINK = re.compile(r"\[([^\]]+)\]\(([^)#]+)(?:#[^)]*)?\)")
FOOTER = re.compile(r"^(?:Previous: .*·\s*)?\[Course map\]\([^)]+\)(?:\s*·\s*Next: .*)?$")
NEXT = re.compile(r"Next: \[[^\]]+\]\(([^)]+)\)")
PREVIOUS = re.compile(r"Previous: \[[^\]]+\]\(([^)]+)\)")

# Pages that legitimately sit outside the reading chain.
OFF_CHAIN = {"README.md", "CONTRIBUTING.md"}


def pages():
    for path in sorted(ROOT.rglob("*.md")):
        if EXCLUDED_DIRS & set(path.relative_to(ROOT).parts):
            continue
        yield path.relative_to(ROOT).as_posix()


def read(page):
    return (ROOT / page).read_text(encoding="utf-8")


def resolve(target, source):
    return ((ROOT / source).parent / target).resolve().relative_to(ROOT.resolve()).as_posix()


def footers_of(page):
    return [line for line in read(page).splitlines() if FOOTER.match(line.strip())]


def walk_chain():
    """Follow Next from the first step. Returns the ordered chain and errors."""
    errors = []
    chain = []
    page = FIRST_STEP
    seen = set()
    while page:
        if page in seen:
            errors.append(f"{page}: chain loops back on itself")
            break
        seen.add(page)
        chain.append(page)

        found = footers_of(page)
        if len(found) != 1:
            errors.append(f"{page}: expected exactly one navigation footer, found {len(found)}")
            break

        footer = found[0]
        following = NEXT.search(footer)
        if not following:
            break  # end of the chain
        page = resolve(following.group(1), page)
        if not (ROOT / page).exists():
            errors.append(f"{page}: Next points at a file that does not exist")
            break

    # every Next must be answered by the matching Previous
    for index in range(len(chain) - 1):
        current, following = chain[index], chain[index + 1]
        back = PREVIOUS.search(footers_of(following)[0])
        if not back:
            errors.append(f"{following}: no Previous, but {current} points Next at it")
        elif resolve(back.group(1), following) != current:
            errors.append(
                f"{following}: Previous points at {resolve(back.group(1), following)}, "
                f"but {current} is what precedes it"
            )
    return chain, errors


def main():
    errors = []
    all_pages = list(pages())

    chain, chain_errors = walk_chain()
    errors += chain_errors

    # 3. every exercise reachable from the chain
    exercises = [page for page in all_pages if "/exercises/" in page and "/solutions/" not in page]
    for exercise in exercises:
        if exercise not in chain:
            errors.append(f"{exercise}: exercise is not on the reading chain")

    # 4. every page has an inbound link
    inbound = {page: 0 for page in all_pages}
    for page in all_pages:
        for match in LINK.finditer(read(page)):
            target = match.group(2)
            if "://" in target or target.startswith("mailto:"):
                continue
            try:
                destination = resolve(target, page)
            except ValueError:
                continue
            if destination in inbound and destination != page:
                inbound[destination] += 1
    for page, count in inbound.items():
        if count == 0 and page not in OFF_CHAIN:
            errors.append(f"{page}: no inbound link - nothing points a reader here")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"path valid ({len(chain)} steps, {len(exercises)} exercises on the chain, "
          f"{len(all_pages)} pages reachable)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
