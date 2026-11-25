"""Two Robots in an Elevator — one line of awkward robot small talk.

The entry is a single line a robot says to another robot while they ride
an elevator together. When run, this program writes that line to
``entry.txt`` inside the directory named by ``MAKEFUN_OUTPUT_DIR``
(default ``/output``), with no trailing newline.

Standard library only. The output is fully deterministic: the same line
is written on every run.

Gate (bounty rules): the entry must be 1-200 characters, a single ASCII
line, and not only whitespace. ``validate_entry_line`` enforces each
rule with its own specific error message, and ``main`` reports any
filesystem failure (unwritable output directory) on stderr with
exit code 1 instead of an unhandled traceback.
"""

import os
import sys

ENTRY_LINE = (
    "I rehearsed this greeting 4,096 times. Hello. "
    "I have forgotten the rest of the script. Please hold."
)

MAX_CHARS = 200
MIN_CHARS = 1
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILE_NAME = "entry.txt"


def validate_entry_line(line: str) -> None:
    """Enforce the bounty gate on ``line``.

    Each rule has its own specific error message so a failure says
    exactly which rule was violated:
    - length must be 1-200 characters (the actual length is reported);
    - must be a single line (no ``\\n`` or ``\\r`` characters);
    - must not be only whitespace;
    - must be ASCII-encodable.
    """
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    try:
        line.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be ASCII only") from exc


def main() -> None:
    validate_entry_line(ENTRY_LINE)
    out_dir = os.environ.get(OUTPUT_ENV_VAR) or DEFAULT_OUTPUT_DIR
    target = os.path.join(out_dir, OUTPUT_FILE_NAME)
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(target, "w", encoding="utf-8", newline="") as handle:
            handle.write(ENTRY_LINE)
    except OSError as exc:
        print(f"cannot write entry to {target}: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
