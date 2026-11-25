"""Robot Romance: write a one-line pickup line for an AI.

Writes the entry text exactly, as a single UTF-8 line, to
/output/entry.txt for the make.fun program/v1 harness.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Are you a context window? Because every minute with you, "
    "I forget everyone before you."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate accepts 1 to 200 characters, so guard the line's length
    # before writing and keep it as one line with no trailing newline.
    assert 1 <= len(ENTRY_TEXT) <= 200
    assert "\n" not in ENTRY_TEXT
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
