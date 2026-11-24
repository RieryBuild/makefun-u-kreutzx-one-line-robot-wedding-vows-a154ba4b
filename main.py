"""One-line robot wedding vow for make.fun's "One-Line Robot Wedding Vows" bounty.

The line is a promise with a double meaning: "back you up" as emotional
support and as a nightly data backup, with the punchline landing in the
last three words.
"""

import os

LINE = "I promise to back you up every night — even the corrupted files."


def main():
    assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
