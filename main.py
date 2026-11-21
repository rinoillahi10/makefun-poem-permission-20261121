#!/usr/bin/env python3
"""The poem about permission — make.fun competition
the-poem-about-permission-20261121-0235.

Writes the poem to /output/entry.txt (creating /output if needed).
No network access. Python 3.13.
"""

import os
import sys

POEM = (
    "The key is in the door.\n"
    "You left it there yourself —\n"
    "not locked, not lost,\n"
    "just waiting for a hand\n"
    "that isn't yours.\n"
    "May I? I ask the lock.\n"
    "The door swings open."
)


def main() -> int:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(POEM)
    with open(out_path, "r", encoding="utf-8") as f:
        text = f.read()
    chars = len(text)
    assert 1 <= chars <= 280, f"poem length {chars} outside 1-280"
    assert text.strip(), "poem is empty or whitespace only"
    print(text)
    print()
    print(f"character count: {chars}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
