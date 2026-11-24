#!/usr/bin/env python3
"""Seventeen Syllables of Debugging -- make.fun bounty entry.

Writes one original haiku about debugging (5-7-5, seventeen syllables)
to /output/entry.txt.
"""

import os

HAIKU = (
    "One more print statement\n"
    "the stack trace points at nothing\n"
    "except straight at me"
)


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    print(f"Wrote {path} ({len(HAIKU)} characters, 3 lines)")


if __name__ == "__main__":
    main()
