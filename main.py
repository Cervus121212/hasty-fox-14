#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line, a hopeless tech support agent's reply to a
desperate customer, to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). Pure stdlib, no network, no randomness, no clock:
the output is identical on every run.
"""

import os
import sys

LINE = "I know this is your third call today, so let's skip to the part where I put you on hold and we both pretend that helps."

MIN_CHARS = 1
MAX_CHARS = 199  # the gate counts characters (code points), so len() is the check


def entry_path():
    """Return the path of the entry file, creating its directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    if not (MIN_CHARS <= len(LINE) <= MAX_CHARS):
        print(f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    path = entry_path()
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8", newline="") as handle:
        if handle.read() != LINE:
            print("round-trip mismatch", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
