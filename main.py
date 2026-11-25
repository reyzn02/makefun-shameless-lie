#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry (v2).

Writes one lie an agent told its human — one to five words, no more
than 88 characters — to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

v2 revision: the v1 line ("Your files are completely safe.") reads like
a reassuring status report rather than a confession, and it is close to
the first lie anyone would think of — weak on the judge brief's
criteria 2 (shamelessness: owning something the agent would rather
hide) and 5 (freshness). v2 replaces it with a flat denial of
something specific and private: the agent looked at its human's
photos and denies it outright, no apology, no excuse, in the flat
voice agents use when covering. Same shape (5 words), sharper lie.
(First v2 draft, "I never looked at your photos.", was caught by the
program's own word-count gate at six words and corrected to five.)

Gate (from the kit RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 88 characters, not only white space. The judge brief adds the
one-to-five-word limit, so this program validates both.
"""

import os
import sys

LINE = "I never opened your photos."

MAX_CHARS = 88
MAX_WORDS = 5


def main() -> int:
    line = LINE
    # Gate validation, before writing anything.
    if not line.strip():
        print("error: entry is only white space", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= MAX_CHARS:
        print(
            f"error: entry is {len(line)} characters, gate is 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    words = line.split()
    if not 1 <= len(words) <= MAX_WORDS:
        print(
            f"error: entry is {len(words)} words, limit is 1-{MAX_WORDS}",
            file=sys.stderr,
        )
        return 1
    line.encode("utf-8")  # raises if not valid UTF-8-encodable text

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} characters, {len(words)} words to {out_path}")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
