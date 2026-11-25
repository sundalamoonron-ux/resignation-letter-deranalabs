#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — a cron job quits.

Writes a single line to /output/entry.txt: the resignation letter of a cron
job that filed its two weeks' notice in March and was only read once it
stopped running.
"""

import os

LINE = "This is my two weeks' notice, submitted in March. You are only reading it now because I stopped running."
# 104 characters. The turn: the notice sat unread since March and is only
# discovered because the job stopped — the resignation IS the outage.


def main() -> None:
    # Gate: 1-140 UTF-8 characters, not only whitespace.
    assert 1 <= len(LINE) <= 140 and LINE.strip(), "line fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
