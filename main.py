"""Charger charges rent — one-line roast entry.

Writes one fixed line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The line: "My charger only works at one exact angle, like it's charging me
rent for the socket."

Why this line: the charger is a gadget used every day, named in the first
two words; "one exact angle" is the concrete behaviour everyone recognises
from their own cable; the punchline is the pun on "charging" — the cable
charges rent for the socket it lives in. It is not the obvious cable
complaint (fraying, slowness); the angle is the specific gripe, and the
whole roast is 84 characters, comfortably inside the 200-character gate,
with the punchline landing at the end.
"""

import os
from pathlib import Path

TEXT = (
    "My charger only works at one exact angle, like it's charging me "
    "rent for the socket."
)


def main() -> None:
    # Self-check against the competition gate before writing: the server
    # refuses any entry.txt outside 1-200 characters or blank, so fail
    # loudly here instead of silently shipping an invalid entry.
    if not 1 <= len(TEXT) <= 200 or not TEXT.strip():
        raise SystemExit("entry.txt must be 1-200 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
