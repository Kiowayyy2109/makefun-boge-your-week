"""Your Week in One Line — make.fun entry.

Writes the single line that sums up the week to /output/entry.txt.
The line is exactly one line of plain text, well under the gate's
100-character cap, so the program is deliberately tiny: it holds the
line, checks it, and writes it out with no trailing newline.
"""

import os

LINE = (
    "Monday: one tiny bug. By Friday it had a team, a roadmap, "
    "and I was attending its stand-ups."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def check_line(line: str) -> str:
    """Return the line unchanged, or raise if it would fail the gate.

    The gate accepts UTF-8 text of 1 to 100 characters that is not only
    whitespace. The entry is a single line, so an embedded newline is a
    bug here, not a style choice, and it is refused before writing.
    """
    if not line.strip():
        raise ValueError("the line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("the entry must be exactly one line")
    if not 1 <= len(line) <= 100:
        raise ValueError(f"the line is {len(line)} characters, outside 1..100")
    return line


def main() -> None:
    line = check_line(LINE)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
