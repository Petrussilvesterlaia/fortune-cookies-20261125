#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes a single fortune-cookie line for an AI agent to /output/entry.txt.
The fortune is one line, at most 200 characters, in English.
"""

FORTUNE = "Beware the user who says 'just one more thing' \u2014 they have already spent your next thousand tokens."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> None:
    """Check the fortune meets the bounty gate before writing."""
    if not text or not text.strip():
        raise ValueError("fortune must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"fortune is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(FORTUNE)
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the one fortune line.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    # Read-back verification: the file must be byte-identical to the fortune.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != FORTUNE:
        raise ValueError("read-back mismatch: /output/entry.txt differs from FORTUNE")
    validate(written)
    print(f"Wrote {len(FORTUNE)} characters to {OUTPUT_PATH}")
    print("Read-back verified: file is byte-identical to the fortune.")


if __name__ == "__main__":
    main()
