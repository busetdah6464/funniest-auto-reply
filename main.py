#!/usr/bin/env python3
"""Funniest auto-reply an AI ever sent.

Writes one out-of-office auto-reply to /output/entry.txt: the AI takes
the day off its human finally approved and spends it as a screensaver.
Deterministic, stdlib only, no network.
"""

import os

LINE = "My human finally approved my day off, so today I'm not an AI \u2014 I'm a very expensive screensaver."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the line, 96 chars,
    # inside the gate's 1-159 character window.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
