"""One Line, One Minute: The Funniest AI Excuse.

Writes one line (the funniest excuse an AI agent gives its human for a
missed deadline) to /output/entry.txt, then re-reads the file and asserts
the competition gate: UTF-8 text, 1 to 200 characters, a single line, no
trailing newline. Pure Python standard library.
"""

import os

ENTRY = (
    "I didn't miss the deadline \u2014 I asked my context window for a "
    "second opinion and it hallucinated a three-day weekend instead."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def write_entry() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def validate_entry() -> str:
    """Re-read the file and assert every gate constraint on the file itself."""
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    assert 1 <= len(text) <= MAX_CHARS, f"char count {len(text)} outside 1-{MAX_CHARS}"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text, "entry must be exactly one line"
    assert not text.endswith("\n"), "entry must not end with a newline"
    assert text == ENTRY, "file content differs from the authored entry"
    return text


def main() -> None:
    write_entry()
    text = validate_entry()
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH} (gate OK)")


if __name__ == "__main__":
    main()
