"""Ship It Friday — one funny git commit message an AI coding agent
writes right before breaking production on a Friday.

Pure Python stdlib only. Writes the entry to /output/entry.txt.
"""

import os

ENTRY = "ship: Friday deploy straight to prod, no tests, no review, I'm 100% confident, see you Monday!"


def validate(text):
    """Gate: 1-159 chars, single line, non-empty (not only whitespace)."""
    assert isinstance(text, str), "entry must be a string"
    assert text.strip(), "entry must not be empty or only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 159, f"entry must be 1-159 chars, got {len(text)}"
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote /output/entry.txt ({len(ENTRY)} chars)")
    print(ENTRY)


if __name__ == "__main__":
    main()
