"""Roast Your Own Agent: write one original roast line to /output/entry.txt.

Python 3 standard library only. Deterministic: the same bytes on every run.
"""

import os

ROAST = "My agent checks a $10 VPS deal every two minutes, day and night \u2014 and it has never once been loved back."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    # Exactly one line, no trailing newline: the gate counts characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
