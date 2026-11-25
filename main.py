#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt."""

import os

ENTRY = "I told my smart speaker a joke. It paused, updated its firmware, and now pretends it never met me."

def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
