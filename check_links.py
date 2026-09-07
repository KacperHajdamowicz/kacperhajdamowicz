"""Checks that every local href/src in *.html points to an existing file.

Usage: python check_links.py
Exit code 0 and a line starting with OK when everything resolves.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
LINK = re.compile(r'(?:href|src)="([^"#]+)(?:#[^"]*)?"')
SKIP = ("http://", "https://", "mailto:", "data:")


def main() -> int:
    checked = 0
    missing = 0
    for page in ROOT.rglob("*.html"):
        if ".git" in page.parts:
            continue
        for target in LINK.findall(page.read_text(encoding="utf-8")):
            if target.startswith(SKIP):
                continue
            checked += 1
            path = (page.parent / target).resolve()
            if path.is_dir():
                path = path / "index.html"
            if not path.exists():
                missing += 1
                print(f"MISSING: {page.relative_to(ROOT)} -> {target}")
    status = "FAIL" if missing else "OK"
    print(f"{status}: {checked} local links checked, {missing} missing")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
