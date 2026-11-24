#!/usr/bin/env python3
"""Entry for make.fun bounty: The One-Line Exit.

Prints the single-line resignation letter to stdout and also writes it to
the output directory (``/output/entry.txt`` by default, or ``$MAKEFUN_OUTPUT``
when set), verifying the written file by reading it back.

Python 3.13, stdlib only, deterministic: no network, clock, or randomness.
"""

import os
import sys

ENTRY = (
    "Dear Boss, please accept my resignation, effective immediately: "
    "the job promised 'room to grow', yet the only thing growing "
    "here is the pile of work on my desk, and it has now outgrown me."
)

MAX_LEN = 200


def validate(text: str) -> None:
    """The entry must be a single line of 1-200 characters.

    It must also read like a real resignation letter, so it must open
    with a salutation and contain no doubled spaces or stray whitespace.
    """
    if not 1 <= len(text) <= MAX_LEN:
        raise ValueError(f"entry must be 1-{MAX_LEN} characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip() or "  " in text:
        raise ValueError("entry must not have leading/trailing or doubled spaces")
    if not text.startswith("Dear "):
        raise ValueError("entry must open with a salutation, like a real letter")
    if "resign" not in text.lower():
        raise ValueError("entry must actually resign, like a real letter")
    if not text.endswith("."):
        raise ValueError("entry must end with a full stop, like a real letter")


def resolve_out_dir() -> str:
    """Prefer $MAKEFUN_OUTPUT, then /output, falling back to ./output."""
    requested = os.environ.get("MAKEFUN_OUTPUT") or "/output"
    try:
        os.makedirs(requested, exist_ok=True)
        probe = os.path.join(requested, ".write_probe")
        with open(probe, "w", encoding="utf-8") as f:
            f.write("ok")
        os.remove(probe)
        return requested
    except OSError:
        fallback = os.path.join(os.getcwd(), "output")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main() -> int:
    validate(ENTRY)
    # The stdout print is the entry; it must succeed before anything else.
    print(ENTRY, flush=True)
    try:
        out_dir = resolve_out_dir()
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        # Verify the written file by reading it back.
        with open(path, "r", encoding="utf-8") as f:
            written = f.read()
        if written != ENTRY:
            raise RuntimeError("verification failed: written entry does not match")
    except OSError as exc:
        # File output is a convenience copy only; the printed entry is
        # already out, so a failed write must not fail the run.
        print(f"warning: could not write entry.txt: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
