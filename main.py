"""Roast Your Fridge: One Line, One Laugh.

Writes a single roast line (max 200 chars) to /output/entry.txt.
Standard library only (Python 3.13) — the grading sandbox installs
nothing, so this file imports nothing beyond the standard library.

The line: the fridge's hum is the one detail every fridge owner
recognises, and the twist is what the hum is *for* — a lullaby sung
to food that died years ago. One image, one sentence, payoff in the
last few words, reads cleanly aloud.
"""

import os

ROAST = (
    "My fridge hums all night like it's singing a lullaby "
    "to food that died in 2019."
)


def main() -> None:
    # Same gate as the sealed scorer: UTF-8 text, 1-200 chars, not blank.
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert text, "roast must not be blank"
    # The grader runs this in a sandbox that provides /output; allow an
    # override so the same file can be exercised in a local test dir.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {out_path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
