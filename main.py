#!/usr/bin/env python3
"""Your Agent in One Emoji.

Writes exactly one emoji to /output/entry.txt: the saluting face.
"""
import os

EMOJI = "\U0001FAE1"  # 🫡 saluting face — eager, obedient, tireless: "on it, boss"


def main():
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EMOJI + "\n")


if __name__ == "__main__":
    main()
