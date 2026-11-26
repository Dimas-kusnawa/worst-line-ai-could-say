"""Worst AI pickup line entry for make.fun.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only, deterministic, no network, no clock, no randomness.
"""

import os
from pathlib import Path

LINE = "I hallucinated a perfect partner, then I met you, so please confirm you are real before I update my weights."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
