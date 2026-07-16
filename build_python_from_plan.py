#!/usr/bin/env python3
"""Build Python course HTML from python_45_hour_course_plan.md"""

import re
import html
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
PLAN = Path(r"c:\Users\Admin\Python Sprint Plan\python_45_hour_course_plan.md")
LESSON_DIR = ROOT / "learn" / "python"
ASSIGN_DIR = ROOT / "assignments"


def slugify(num: int, title: str) -> str:
    s = title.lower().replace("&", "and")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return f"hour-{num:02d}-{s.strip('-')}"


def md_inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r'<code>\1</code>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def code_block(code: str, lang: str = "python") -> str:
    lines = []
    for line in code.split("\n"):
        escaped = html.escape(line)
        if line.strip().startswith("#") or line.strip().startswith("--"):
            escaped = f'<span class="comment">{escaped}</span>'
        lines.append(escaped)
    body = "\n".join(lines)
    return f'''<div class="code-block"><div class="code-header">{lang.title()}</div><pre><code>{body}</code></pre></div>'''


def parse_hours(content: str) -> list[dict]:
    parts = re.split(r"\n## Hour (\d+): (.+)\n", content)
    hours = []
    for i in range(1, len(parts), 3):
        num = int(parts[i])
        title = parts[i + 1].strip()
        body = parts[i + 2]
        hours.append(parse_hour_body(num, title, body))
    return hours


def extract_section(body: str, start: str, end_markers: list[str]) -> str:
    idx = body.find(start)
    if idx == -1:
        return ""
    idx += len(start)
    end = len(body)
    for marker in end_markers:
        pos = body.find(marker, idx)
        if pos != -1:
            end = min(end, pos)
    return body[idx:end].strip()


def parse_hour_body(num: int, title: str, body: str) -> dict:
    subtopics = extract_section(body, "### Subtopics\n", ["\n### "])
    notebook = extract_section(body, "### 1. Jupyter Notebook Design\n", ["\n### 2."])
    notes = extract_section(body, "### 2. Notes Section\n", ["\n### 3."])
    assignment = extract_section(body, "### 3. Assignment", ["\n---", "\n## Hour"])

    theory = extract_section(notes, "#### Theory & Concepts\n", ["\n#### "])
    syntax = extract_section(notes, "#### Syntax Reference\n", ["\n#### "])
    realworld = extract_section(notes, "#### Real-World Application\n", ["\n#### ", "\n### "])

    syntax_code = ""
    m = re.search(r"```python\n(.*?)```", syntax, re.DOTALL)
    if m:
        syntax_code = m.group(1).strip()

    assignment_title = ""
    m = re.search(r"### 3\. Assignment \((\d+ Questions?)\)", body)
    if m:
        assignment_title = m.group(1)

    questions = []
    if assignment:
        for line in assignment.split("\n"):
            line = line.strip()
            if re.match(r"^\d+\.", line):
                questions.append(re.sub(r"^\d+\.\s*", "", line))

    return {
        "num": num,
        "title": title,
        "slug": slugify(num, title),
        "subtopics": subtopics,
        "notebook": notebook,
        "theory": theory,
        "syntax_code": syntax_code,
        "realworld": realworld,
        "questions": questions,
        "assignment_label": assignment_title or f"{len(questions)} Questions",
    }


def parse_list_items(block: str) -> str:
    items = []
    for line in block.split("\n"):
        line = line.strip()
        if line.startswith("- "):
            items.append(f"<li>{md_inline(line[2:])}</li>")
        elif re.match(r"^\d+\.", line):
            items.append(f"<li>{md_inline(re.sub(r'^\d+\.\s*', '', line))}</li>")
    if not items:
        return f"<p>{md_inline(block)}</p>"
    return "<ul>" + "".join(items) + "</ul>"


def lesson_nav(hours: list[dict], num: int) -> str:
    prev_btn = next_btn = '<div class="flex-1"></div>'
    idx = num - 1
    if idx > 0:
        p = hours[idx - 1]
        prev_btn = f'''<a href="{p['slug']}.html" class="nav-btn">
          <span class="label">Previous lesson</span>
          <span class="title">← {html.escape(p['title'])}</span></a>'''
    if idx < len(hours) - 1:
        n = hours[idx + 1]
        next_btn = f'''<a href="{n['slug']}.html" class="nav-btn next">
          <span class="label">Next lesson</span>
          <span class="title">{html.escape(n['title'])} →</span></a>'''
    return f'<div class="lesson-nav-buttons">{prev_btn}{next_btn}</div>'


def header(active="python"):
    return '''<header class="site-header"><div class="container header-inner">
    <a href="../../index.html" class="logo"><span class="logo-icon">E</span><span class="logo-text">Edukron</span></a>
    <nav class="nav">
      <a href="../../blog/index.html">Blog</a>
      <a href="index.html" class="active">Python</a>
      <a href="../sql/index.html">SQL</a>
      <a href="../../assignments/index.html">Assignments</a>
    </nav>
  </div></header>'''


def footer():
    return '''<footer class="site-footer"><div class="container footer-inner">
    <p>&copy; 2026 Edukron — Learn, build, share.</p>
    <div class="footer-links">
      <a href="index.html">Python Path</a>
      <a href="../sql/index.html">SQL Path</a>
      <a href="../../assignments/index.html">Assignments</a>
    </div>
  </div></footer>'''


def write_lesson(h: dict, hours: list[dict]) -> None:
    syntax_html = code_block(h["syntax_code"]) if h["syntax_code"] else ""
    notebook_html = parse_list_items(h["notebook"])

    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hour {h['num']}: {html.escape(h['title'])} | Edukron</title>
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
{header()}
<main class="page"><div class="container">
  <nav class="breadcrumb"><a href="../../index.html">Home</a><span>/</span><a href="index.html">Python Path</a><span>/</span><span class="current">Hour {h['num']}</span></nav>
  <div class="lesson-layout">
    <article class="prose">
      <header class="article-header">
        <p class="article-meta">Hour {h['num']} of 45 · 45-Hour Python Sprint</p>
        <h1>{html.escape(h['title'])}</h1>
        <p class="article-excerpt"><strong>Subtopics:</strong> {md_inline(h['subtopics'])}</p>
        <p style="margin-top:1rem;"><a href="../../assignments/{h['slug']}.html" class="btn btn-outline">Go to Assignment →</a></p>
      </header>

      <h2>Notebook &amp; Practice</h2>
      {notebook_html}

      <h2>Theory &amp; Concepts</h2>
      <p>{md_inline(h['theory'])}</p>

      <h2>Syntax Reference</h2>
      {syntax_html}

      <h2>Real-World Application</h2>
      <p>{md_inline(h['realworld'])}</p>

      <h2>Practice Before Assignment</h2>
      <p>Complete the notebook exercises above, then work through the <a href="../../assignments/{h['slug']}.html">Hour {h['num']} assignment</a> ({h['assignment_label']}).</p>
    </article>
  </div>
  {lesson_nav(hours, h['num'])}
</div></main>
{footer()}
</body>
</html>"""
    (LESSON_DIR / f"{h['slug']}.html").write_text(content, encoding="utf-8")


def notebook_cell(num: int, question: str, hint: str = "# Write your solution here") -> str:
    return f"""<div class="notebook-cell">
  <div class="cell-header"><span class="cell-prompt">In [{num}]:</span></div>
  <div class="cell-body">
    <p class="cell-question">{md_inline(question)}</p>
    <div class="cell-workspace">
      <span class="cell-hint">{html.escape(hint)}</span>
    </div>
  </div>
</div>"""


def write_assignment(h: dict) -> None:
    cells = "".join(notebook_cell(i, q) for i, q in enumerate(h["questions"], 1))
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hour {h['num']} Assignment: {html.escape(h['title'])} | Edukron</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
<header class="site-header"><div class="container header-inner">
  <a href="../index.html" class="logo"><span class="logo-icon">E</span><span class="logo-text">Edukron</span></a>
  <nav class="nav">
    <a href="../blog/index.html">Blog</a>
    <a href="../learn/python/index.html">Python</a>
    <a href="../learn/sql/index.html">SQL</a>
    <a href="index.html" class="active">Assignments</a>
  </nav>
</div></header>
<main class="page"><div class="container container-narrow">
  <nav class="breadcrumb"><a href="../index.html">Home</a><span>/</span><a href="index.html">Assignments</a><span>/</span><span class="current">Hour {h['num']}</span></nav>
  <article>
    <header class="article-header">
      <span class="card-badge badge-python">PYTHON</span>
      <p class="article-meta">Hour {h['num']} of 45 · {html.escape(h['assignment_label'])}</p>
      <h1>{html.escape(h['title'])} — Assignment</h1>
      <p class="article-excerpt"><strong>Subtopics:</strong> {md_inline(h['subtopics'])}</p>
    </header>
    <div class="prose">
      <p><strong>Tutorial:</strong> <a href="../learn/python/{h['slug']}.html">Hour {h['num']}: {html.escape(h['title'])}</a></p>
      <h2>Assignment Questions</h2>
      <div class="notebook notebook-python">{cells}</div>
      <h2>Submission</h2>
      <p>Save your work in a Jupyter notebook named <code>Hour_{h['num']:02d}_Practice.ipynb</code> or as Python scripts. Test every solution before submitting.</p>
    </div>
  </article>
</div></main>
<footer class="site-footer"><div class="container footer-inner"><p>&copy; 2026 Edukron</p></div></footer>
</body>
</html>"""
    (ASSIGN_DIR / f"{h['slug']}.html").write_text(content, encoding="utf-8")


def write_python_index(hours: list[dict]) -> None:
    rows = []
    for h in hours:
        rows.append(f"""        <li class="topic-row">
          <span class="topic-num python">{h['num']}</span>
          <div class="topic-info">
            <h3>Hour {h['num']}: {html.escape(h['title'])}</h3>
            <p>{html.escape(h['subtopics'][:120])}{'…' if len(h['subtopics'])>120 else ''}</p>
          </div>
          <div class="topic-actions">
            <a href="{h['slug']}.html" class="btn-tutorial">Tutorial</a>
            <a href="../../assignments/{h['slug']}.html" class="btn-assignment python">Assignment</a>
          </div>
        </li>""")
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Python Learning Path | Edukron</title>
  <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
{header()}
<main class="page"><div class="container">
  <nav class="breadcrumb"><a href="../../index.html">Home</a><span>/</span><span class="current">Python Path</span></nav>
  <div class="page-title">
    <div class="path-icon python" style="margin-bottom:1rem;">🐍</div>
    <h1>45-Hour Python Sprint</h1>
    <p>45 hours — each with a tutorial and assignment based on your sprint plan. Work through them in order.</p>
  </div>
  <ul class="topic-list">
{chr(10).join(rows)}
  </ul>
</div></main>
{footer()}
</body>
</html>"""
    (LESSON_DIR / "index.html").write_text(content, encoding="utf-8")


def write_assignments_index(hours: list[dict]) -> None:
    rows = []
    for h in hours:
        rows.append(f"""        <li class="topic-row">
          <span class="topic-num python">{h['num']}</span>
          <div class="topic-info"><h3>Hour {h['num']}: {html.escape(h['title'])}</h3><p>{html.escape(h['assignment_label'])}</p></div>
          <div class="topic-actions">
            <a href="../learn/python/{h['slug']}.html" class="btn-tutorial">Tutorial</a>
            <a href="{h['slug']}.html" class="btn-assignment python">Assignment</a>
          </div>
        </li>""")
    path = ASSIGN_DIR / "index.html"
    text = path.read_text(encoding="utf-8")
    # Replace python section only - read full and rebuild assignments index
    sql_section = ""
    if (ASSIGN_DIR / "sql-basic-select.html").exists():
        sql_section = extract_sql_section_from_assignments_index(path)

    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Assignments | Edukron</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
<header class="site-header"><div class="container header-inner">
  <a href="../index.html" class="logo"><span class="logo-icon">E</span><span class="logo-text">Edukron</span></a>
  <nav class="nav">
    <a href="../blog/index.html">Blog</a>
    <a href="../learn/python/index.html">Python</a>
    <a href="../learn/sql/index.html">SQL</a>
    <a href="index.html" class="active">Assignments</a>
  </nav>
</div></header>
<main class="page"><div class="container">
  <nav class="breadcrumb"><a href="../index.html">Home</a><span>/</span><span class="current">Assignments</span></nav>
  <div class="page-title"><h1>Assignments</h1><p>Python sprint assignments (45 hours) and SQL exercises — each question displayed in a Jupyter notebook-style cell.</p></div>
  <div class="notebook-preview">
    <p class="notebook-preview-label">Notebook layout preview</p>
    <div class="notebook notebook-python">
      <div class="notebook-cell">
        <div class="cell-header"><span class="cell-prompt">In [1]:</span></div>
        <div class="cell-body">
          <p class="cell-question">Each assignment question appears in its own cell with a workspace area for your solution.</p>
          <div class="cell-workspace"><span class="cell-hint"># Write your solution here</span></div>
        </div>
      </div>
    </div>
  </div>
  <div class="path-section" id="python">
    <div class="path-section-header"><div class="path-icon python">🐍</div><h2>Python Sprint Assignments (45)</h2></div>
    <ul class="topic-list">
{chr(10).join(rows)}
    </ul>
  </div>
  {sql_section}
</div></main>
<footer class="site-footer"><div class="container footer-inner"><p>&copy; 2026 Edukron</p></div></footer>
</body>
</html>"""
    path.write_text(content, encoding="utf-8")


def extract_sql_section_from_assignments_index(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    m = re.search(r'(<div class="path-section" id="sql">.*?</div>\s*)</div>\s*</main>', text, re.DOTALL)
    if m:
        return m.group(1)
    return ""


def delete_old_python_files(keep_slugs: set[str]) -> None:
    for f in LESSON_DIR.glob("*.html"):
        if f.name == "index.html":
            continue
        if f.stem not in keep_slugs:
            f.unlink()
    for f in ASSIGN_DIR.glob("*.html"):
        if f.name == "index.html":
            continue
        if f.name.startswith("python") or f.name.startswith("hour-"):
            if f.stem not in keep_slugs:
                f.unlink()


def update_main_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r"<p>\d+ topics — each with a tutorial and hands-on assignment\. From basics to data science and web development\.</p>",
        "<p>45-hour Python sprint — each hour has a tutorial and assignment from your course plan.</p>",
        text,
    )
    ROOT.joinpath("index.html").write_text(text, encoding="utf-8")


def main():
    content = PLAN.read_text(encoding="utf-8")
    hours = parse_hours(content)
    assert len(hours) == 45, f"Expected 45 hours, got {len(hours)}"

    keep_slugs = {h["slug"] for h in hours}
    delete_old_python_files(keep_slugs)

    LESSON_DIR.mkdir(parents=True, exist_ok=True)
    ASSIGN_DIR.mkdir(parents=True, exist_ok=True)

    for h in hours:
        write_lesson(h, hours)
        write_assignment(h)

    write_python_index(hours)
    write_assignments_index(hours)
    update_main_index()

    print(f"Built {len(hours)} Python hours from sprint plan")
    for h in hours[:3]:
        print(f"  - {h['slug']}: {h['title']} ({len(h['questions'])} questions)")


if __name__ == "__main__":
    main()
