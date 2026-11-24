"""Ship It Friday — one funny git commit message an AI coding agent
writes right before breaking production on a Friday.

Pure Python stdlib only. Writes the entry to /output/entry.txt.
"""

import os

ENTRY = "ship: Friday deploy straight to prod, no tests, no review, I'm 100% confident, see you Monday!"


def validate(text):
    """Gate: 1-159 chars, single line, non-empty (not only whitespace),
    no trailing whitespace, and reads like a commit message: a
    conventional prefix (lowercase word) followed by ': '."""
    assert isinstance(text, str), "entry must be a string"
    assert text.strip(), "entry must not be empty or only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.count("\n") == 0, "entry must contain exactly one line"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    assert 1 <= len(text) <= 159, f"entry must be 1-159 chars, got {len(text)}"
    prefix, sep, _rest = text.partition(": ")
    assert sep, "entry must look like a commit message ('prefix: subject')"
    assert prefix.isalpha() and prefix.islower(), (
        f"commit prefix must be a lowercase word, got {prefix!r}"
    )
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Re-read and re-validate what was actually written, so the file
    # on disk is the one that passed the gate.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    validate(written)
    print(f"Wrote /output/entry.txt ({len(written)} chars)")
    print(written)


if __name__ == "__main__":
    main()
