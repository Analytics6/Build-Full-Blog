#!/usr/bin/env python3
"""Convert SQL assignment <ol> lists to notebook-style cells."""

import re
from pathlib import Path

ASSIGN_DIR = Path(__file__).parent / "assignments"
SQL_HINT = "-- Write your SQL query here"


def ol_to_notebook(match: re.Match) -> str:
    items = re.findall(r"<li>(.*?)</li>", match.group(1), re.DOTALL)
    if not items:
        return match.group(0)
    cells = []
    for i, item in enumerate(items, 1):
        item = item.strip()
        cells.append(f"""<div class="notebook-cell">
  <div class="cell-header"><span class="cell-prompt">In [{i}]:</span></div>
  <div class="cell-body">
    <p class="cell-question">{item}</p>
    <div class="cell-workspace">
      <span class="cell-hint">{SQL_HINT}</span>
    </div>
  </div>
</div>""")
    return f'<div class="notebook notebook-sql">{"".join(cells)}</div>'


def convert_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "notebook-cell" in text:
        return False
    if "<ol>" not in text:
        return False
    new_text = re.sub(
        r"<ol>(.*?)</ol>",
        ol_to_notebook,
        text,
        flags=re.DOTALL,
    )
    if new_text == text:
        return False
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    files = sorted(ASSIGN_DIR.glob("sql*.html"))
    updated = 0
    for f in files:
        if convert_file(f):
            print(f"Updated {f.name}")
            updated += 1
    print(f"Done. Updated {updated} of {len(files)} SQL assignment files.")


if __name__ == "__main__":
    main()
