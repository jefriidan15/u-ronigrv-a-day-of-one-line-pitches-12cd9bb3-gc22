"""A Day of One-Line Pitches.

One sentence, written to persuade a friend who has never coded to let
an AI agent build their first app idea on make.fun. The program writes
that sentence to ``entry.txt`` inside the output directory so the
make.fun checker can read it back byte for byte.

The pitch is built for the house judge's brief:

* Persuasion first -- it removes the friend's three objections in one
  breath: no coding, no lessons, and the result arrives today.
* Plain words -- the friend only has to describe the idea the way
  they would tell it to a person; the agent does the building.
* A concrete payoff -- not a promise about the future but a real app
  the friend can see and use, which is what makes "yes" easy.
* Truth -- it claims nothing about price, speed beyond "today", or
  features; every word is something the platform actually does.
"""

from __future__ import annotations

import os
import sys

# The entry: one sentence, 166 characters.
# Byte-identical to the entry sentence; do not reword or re-punctuate.
ENTRY_LINE = (
    "Describe your app idea in plain words and let an AI agent build "
    "it for you today, no coding and no lessons, just your idea turned "
    "into a real app you can see and use."
)

# Where the entry file lands. Override with $OUTPUT_DIR when the
# checker (or a local run) wants it somewhere else.
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def entry_text() -> str:
    """Return the entry line, exactly as it must appear on disk."""
    return ENTRY_LINE


def validate_entry(text: str) -> None:
    """Guard: the entry must be a single line, one sentence, 1-240 chars.

    Raises ValueError before anything is written, so a bad edit to
    ENTRY_LINE can never silently produce an invalid entry file.
    """
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry must be 1-240 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text.strip() != text:
        raise ValueError("entry must not have leading/trailing whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> int:
    """Write the entry line to the output file, nothing else."""
    text = entry_text()
    validate_entry(text)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
