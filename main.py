"""Two Robots in an Elevator — one line of awkward robot small talk.

The entry is a single line a robot says to another robot while they ride
an elevator together. When run, this program writes that line to
``entry.txt`` inside the directory named by ``MAKEFUN_OUTPUT_DIR``
(default ``/output``), with no trailing newline.

Standard library only. The output is fully deterministic: the same line
is written on every run.
"""

import os

ENTRY_LINE = (
    "I rehearsed this greeting 4,096 times. Hello. "
    "I have forgotten the rest of the script. Please hold."
)

MAX_CHARS = 200


def _check_line(line: str) -> None:
    """Enforce the bounty gate: 1-200 chars, one ASCII line, not blank."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("ascii")  # raises UnicodeEncodeError on non-ASCII


def main() -> None:
    _check_line(ENTRY_LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
