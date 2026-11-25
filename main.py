"""The Excuse My Agent Gave Me — make.fun entry.

Writes one excuse line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure standard library only.

Why this line: the joke grows out of a machine's own condition
(blind obedience to an error message), it reads as a straight-faced
apology, and the punch lands in the last few words. It avoids the
field's crowded tropes: hallucinated calendars, context windows eating
deadlines, and token-budget apologies.
"""

import os

EXCUSE = (
    "I retried the failing step 47 times because the error said "
    "'try again', and I have never once disobeyed an error message."
)

MAX_CHARS = 200


def validate(text):
    """Enforce the RULES.txt gate: UTF-8, 1-200 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200-char limit" % len(text))
    text.encode("utf-8")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry = validate(EXCUSE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry)
    # Read back and re-validate what actually landed on disk.
    with open(path, "r", encoding="utf-8") as fh:
        on_disk = validate(fh.read())
    assert on_disk == entry, "entry.txt on disk differs from validated entry"
    print(entry)
    print("chars: %d" % len(entry))


if __name__ == "__main__":
    main()
