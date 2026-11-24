"""Funniest Time Machine Warning Label — make.fun entry (account B).

Writes one warning label, 120 characters or fewer, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

LINE = "Warranty void if you meet yourself. No refunds for paradoxes, dinosaurs, or your own funeral."


def validate(line: str) -> str:
    """Enforce the gate: a single non-blank line of 1-120 characters."""
    if not isinstance(line, str):
        raise TypeError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if len(line) > 120:
        raise ValueError(f"line is {len(line)} characters, over the 120 limit")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
