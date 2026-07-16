# Edukron Site — Deep Content Analysis

**Date:** July 16, 2026
**Scope:** All content HTML files — 45 Python lessons + index, 30 SQL lessons + index, assignments index + 12 spot-checked assignment files, blog index + 3 posts, `index.html`, `login.html` (94 files covered individually below; every lesson file was read in full).
**Note:** Python data-type lessons (hours 5–10, 18–24, 29) are being improved by another agent concurrently — findings for those files reflect the state at analysis time and are flagged **[IN FLUX]**.

---

## 1. Executive Summary

Edukron is a structurally solid static learning site with a clean white theme, consistent header/breadcrumb/footer chrome, and a complete curriculum skeleton (45 Python hours, 30 SQL topics, matching assignments). Content quality, however, is **sharply uneven**:

- **Python hours 1–5 and 26–45** are genuinely good: staged explanations, styled code blocks with token highlighting, expected-output blocks, "Key takeaways," and assignment links.
- **Python hours 6–25** are a visibly older, thinner generation: plain unstyled code blocks, almost no output demonstrations, empty diagram-placeholder headings, mojibake encoding damage, "Practice Before Assignment" sections referencing notebook exercises that don't exist on the page, and several code examples that reference undefined variables.
- **SQL lessons** read fluently but contain **systemic correctness problems**: an inconsistent `hr.*` schema (columns like `category`, `lifetime_spend`, `requested_amount` appear and vanish between lessons), duplicate column definitions in `CREATE TABLE` examples, a self-referencing foreign key presented incorrectly, a no-op `RENAME COLUMN salary TO salary`, and corrupted find-and-replace tokens ("payrollsible", "payrollition", "the 30 ETL pattern") scattered through at least 7 files.
- **SQL assignments 6–30 are template stubs**: every one has the same four generic questions ("Review the tutorial… Implement a working solution… Include comments… Test with 3 inputs"). They provide near-zero practice value, in stark contrast to the well-crafted per-topic Python assignments.
- **SQL lessons 1–5 have no prev/next navigation and no assignment link**, breaking the course flow exactly where beginners start.

### Top 10 highest-impact improvements (prioritized)

1. **Replace SQL assignments 06–30 with real, topic-specific exercises** (like the Python ones — 8–12 concrete questions per topic against the hr schema). This is the single biggest content hole on the site.
2. **Fix the hr.\* schema inconsistencies across all 30 SQL lessons**: publish one canonical schema (employees, departments, jobs, locations, job_history with fixed column lists) in lesson 1 and audit every query against it. Currently many examples would error if run.
3. **Add prev/next navigation and "Go to Assignment" links to SQL lessons 01–05** to match lessons 06–30.
4. **Purge corrupted find-and-replace text** — "payrollsible", "payrollition", "the 30 ETL pattern", "Wireless HeadManagers" etc. (confirmed in sql 06, 10, 17, 20, 23, 24 and `assignments/sql-filtering.html`; audit the rest).
5. **Upgrade Python hours 6–25 to the newer lesson format**: styled/tokenized code blocks, an output block after every example, remove empty diagram-stub headings, fix mojibake (`?` for `→`/`$`), remove or fulfill "Practice Before Assignment" references.
6. **Fix broken code examples in Python lessons**: undefined `lessons_completed` (hour 13), `username_exists` (hour 14), wrong lambda key `x["spend"]` (hour 28), `zip` over undefined `amounts` (hour 29), `Learner()` instantiated instead of the class actually defined (hours 35–36), undefined `l.greet()` (hour 38).
7. **Repair `assignments/sql-basic-select.html` and `sql-filtering.html`** — question text is garbled ("every each employee row", "Find the jobs table with a price greater than 50", bonus asks to combine names into a `last_name` column) and expected-output blocks show nonsense data.
8. **Add meta descriptions and canonical titles to every page** — no page on the site has `<meta name="description">`, and SQL index/lessons use the awkward auto-generated "Sql" capitalization.
9. **Link or remove the two orphaned assignment files** (`sql-filtering.html`, `sql-joins-report.html`) — 32 SQL assignment files exist but only 30 are reachable from the assignments index.
10. **Add missing curriculum topics** (see §3): list comprehensions, dict/set comprehensions, string formatting depth, `is` vs `==`, scope/LEGB, generators, decorators, virtual environments and pip, testing for Python; GROUP BY semantics depth, `NULL` three-valued logic, index anatomy, stored procedures/functions, window frames for SQL.

---

## 2. Cross-Cutting Issues

1. **Two lesson generations in Python (format drift).** Hours 1–5 and 26–45 use styled `.code-block` markup with syntax-highlight spans, output blocks, and "Key takeaways". Hours 6–25 use plain `<pre>` code, no outputs, and thinner prose. The visual and pedagogical experience degrades mid-course and recovers later, which reads as neglect exactly in the foundational data-structure hours. **[hours 5–10, 18–24, 29 IN FLUX]**
2. **Missing output demonstrations.** Most examples in Python hours 6–25 and many SQL lessons show code but never the result. For a beginner audience, every example should end with what the learner will actually see.
3. **Empty diagram-stub headings.** Several older Python lessons contain headings like "Data Cleaning Flow" (hour 9) or "Input Flow" (hour 12) with no content beneath — remnants of removed diagrams. Site convention is "no flow diagrams", so these headings should be deleted.
4. **Encoding damage (mojibake).** `learn/python/index.html` contains `â€”`-style bytes; several older Python lessons render `?` where `→` or `$` was intended inside strings and comments.
5. **Corrupted global find-and-replace.** Words like "possible" → "payrollsible", "position" → "payrollition", "ETL" → "30 ETL", "Headphones" → "HeadManagers" indicate an automated rename (likely products→jobs / customers→employees) that damaged prose. Confirmed hits: `learn/sql/06, 10, 17, 20, 23, 24` and `assignments/sql-filtering.html`; the same rename also produced semantically broken sentences in `sql-basic-select.html` and `sql-filtering.html` ("the jobs table with a price greater than 50").
6. **hr.\* schema drift in SQL.** The schema implied by lesson 1 (employees, departments, jobs, locations, job_history) is repeatedly contradicted: `hr.jobs` gains `category` and `price`-like columns (lessons 12–14), `hr.employees` gains `lifetime_spend` (15) and `email` inconsistently, `hr.job_history` gains `total`/`requested_amount` (19). Learners cannot build a mental model of the sample database.
7. **Navigation inconsistency.** SQL lessons 01–05: no prev/next, no assignment link. SQL 06–30 and all 45 Python lessons: both present. Python hour 45 has only a Previous link (correct, it's last) but SQL lesson 30 should be checked for a dangling Next.
8. **"Practice Before Assignment" sections reference non-existent notebooks.** Python hours ~9–25 say "complete the notebook exercises above" when no notebook cells exist on the page.
9. **SEO/metadata.** No page has `<meta name="description">`, Open Graph tags, or favicon links. Titles are inconsistent ("Sql Learning Path" vs "SQL"). Blog posts lack author/date metadata in `<head>`.
10. **Accessibility.** Emoji path icons (🐍, 🗄️) have no `aria-hidden` or text alternative; code blocks lack `lang` hints; color is the only distinction between Python/SQL badges; skip-navigation links are absent site-wide.
11. **Client-side auth is cosmetic.** `js/auth.js` gates content in the browser with hard-coded demo credentials printed on the login page; every page is directly reachable by URL. Fine for a demo, but worth an explicit "demo only" note.
12. **Mobile/responsiveness of code blocks.** Long single-line SQL examples (e.g. the blog's one-line SELECT, several lesson queries) will force horizontal scrolling on phones; prefer wrapped, multi-line query formatting everywhere.

---

## 3. Curriculum Gaps

### Python (45-hour sprint)
- **List/dict/set comprehensions** — the single most glaring omission; nothing between loops and data structures covers them.
- **String formatting depth** — f-string format specs (`:.2f`, `:>10`), `format()` mini-language.
- **`is` vs `==`, mutability and copying** — `copy` vs `deepcopy` is never treated properly despite lists-of-dicts lessons.
- **Scope and namespaces (LEGB, `global`, `nonlocal`)** — functions are taught with no scope discussion.
- **Generators and iterators** (`yield`, generator expressions, `iter`/`next`) — absent.
- **Decorators and closures** — absent; even a single hour would round out the functions block.
- **Virtual environments and pip** (`venv`, `requirements.txt`) — setup lesson covers Jupyter only.
- **Testing** — no `assert`, `unittest`, or `pytest` anywhere; a "test your functions" hour before the mini-project would fit naturally.
- **JSON handling** (`json.load/dump`) — CSV is covered, JSON is not, despite being equally common in data work.
- **OOP extras**: `__str__`/`__repr__`, class vs instance attributes, `@property` — the OOP block (35–38) stops at basic inheritance.
- **Matplotlib / basic plotting** — a data-analytics-flavored course ending in Pandas would normally include one visualization hour.

### SQL (30 topics)
- **GROUP BY semantics depth** — what may appear in SELECT with GROUP BY, grouping by expressions, `GROUP BY 1` pitfalls, `WHERE` vs `HAVING` order of evaluation (touched but shallow).
- **NULL three-valued logic** — `NULL = NULL`, `NOT IN` with NULLs, `IS DISTINCT FROM`; lesson 16 covers COALESCE/NULLIF only.
- **Data type deep-dive per dialect** — VARCHAR vs TEXT, NUMERIC precision, date/time types across MySQL/Postgres/SQLite; lessons silently mix dialects.
- **Index anatomy** — B-tree vs hash, composite index column order, covering indexes, when indexes are ignored; lesson 11 stays at CREATE/DROP.
- **Stored procedures / user-defined functions / triggers** — completely absent.
- **Window frames** (`ROWS BETWEEN`), `NTILE`, `FIRST_VALUE`/`LAST_VALUE` — window block covers only ROW_NUMBER/RANK/LAG/LEAD.
- **Aggregate window functions** (`SUM() OVER`) for running totals — the classic use case is missing.
- **Isolation levels and locking** — transactions lesson stops at ACID + COMMIT/ROLLBACK.
- **Security basics** — SQL injection and parameterized queries deserve at least a section in the DML lesson.
- **Schema migration practice / seed data** — no downloadable script creating the hr schema so learners can actually run the examples.

---

## 4. Consistency Audit Table

| Section | Code block style OK? | Output shown? | Takeaways present? | Assignment linked? | Prev/Next nav? |
|---|---|---|---|---|---|
| Python hours 1–5 | ✅ styled + tokens | ✅ mostly | ✅ | ✅ | ✅ |
| Python hours 6–8 **[IN FLUX]** | ⚠️ mixed | ⚠️ partial | ✅ | ✅ | ✅ |
| Python hours 9–25 **[9–10, 18–24 IN FLUX]** | ❌ plain `<pre>` | ❌ rarely | ⚠️ inconsistent | ✅ | ✅ |
| Python hours 26–45 | ✅ styled + tokens | ✅ mostly | ✅ | ✅ | ✅ (45: prev only) |
| SQL lessons 01–05 | ✅ styled | ⚠️ partial | ⚠️ | ❌ missing | ❌ missing |
| SQL lessons 06–30 | ✅ styled | ⚠️ partial | ✅ | ✅ | ✅ |
| Python assignments (45) | ✅ notebook cells | n/a | n/a | ✅ tutorial linked | n/a |
| SQL assignments legacy (1–5) | ✅ notebook cells + starter/expected output | ⚠️ garbled outputs | n/a | ⚠️ not back-linked to tutorial | n/a |
| SQL assignments 06–30 | ✅ notebook cells | n/a | n/a | ✅ tutorial linked | n/a |
| Blog (3 posts + index) | ✅ | ✅ | n/a | n/a | ❌ no prev/next between posts |
| Top-level (index, login) | ✅ | n/a | n/a | n/a | n/a |

---

## 5. Per-File Analysis — Top-Level Pages

### index.html
- **Current state**: Landing page with hero, two path cards, and latest-blog grid. Clean, modern, and consistent with the brand. Good quality.
- **Strengths**: Clear CTAs, accurate course descriptions, responsive grid layout.
- **Gaps / issues**: `<a href="/logout">` uses a root-absolute path that breaks when served from a subfolder or `file://`; no meta description; inline styles in the "Latest from the Log" section instead of CSS classes; blog cards duplicated by hand (will drift from blog/index.html).
- **Suggestions**: (1) Change logout to a JS-handled link consistent with `auth.js`. (2) Add meta description + OG tags. (3) Move inline styles to `style.css`. (4) Consider a "How it works" strip (Tutorial → Assignment → Blog log) to explain site mechanics.

### login.html
- **Current state**: Standalone login card with username/password form, error message, and demo-credentials hint. Well styled; auth handled by `js/auth.js`.
- **Strengths**: Focused layout, proper `autocomplete` attributes, accessible labels, focus styles.
- **Gaps / issues**: The source file is double-spaced (blank line between every line — an artifact worth cleaning); demo credentials printed on the page make the "auth" purely decorative; all inline CSS (~200 lines) rather than in the stylesheet; no "show password" toggle or keyboard-visible error announcement (`aria-live`).
- **Suggestions**: (1) Normalize file whitespace. (2) Move styles into `css/style.css` as a `.login-*` block. (3) Add `aria-live="polite"` to the error div. (4) Add an explicit "demo site — not real authentication" note.

### learn/python/index.html
- **Current state**: Python path index listing all 45 hours with tutorial + assignment buttons. Complete and accurate linking. Good quality.
- **Strengths**: Every hour links to the correct lesson and assignment; duration hints; clear phase progression.
- **Gaps / issues**: Confirmed mojibake in the footer (`â€”` instead of `—`) — the file has a UTF-8/Windows-1252 double-encoding artifact; no grouping of the 45 rows into phases (Basics / Strings / Loops / Data structures / Functions / OOP / NumPy–Pandas), making the list a wall of 45 items; no per-hour completion indicators.
- **Suggestions**: (1) Fix the encoding artifact. (2) Add phase sub-headers every ~5–8 rows. (3) Add a short "how to study" intro (1 hour = tutorial + assignment). (4) Add meta description.

### learn/sql/index.html
- **Current state**: SQL path index listing all 30 topics with tutorial + assignment buttons, including the legacy assignment names for topics 1–5. Complete linking. Good quality.
- **Strengths**: Accurate hrefs for all 30 lessons and assignments; duration estimates; sensible topic ordering.
- **Gaps / issues**: Title/H1 say "Sql Learning Path" / "Sql Path" (should be "SQL"); topics 1–5 point to legacy-named assignments (`sql-basic-select.html` etc.) while 6–30 use numbered names — cosmetic but confusing to maintain; no phase grouping (foundations / DDL / intermediate queries / window functions / advanced); no meta description.
- **Suggestions**: (1) Fix "Sql" → "SQL" capitalization. (2) Group topics into 4–5 phases. (3) Rename legacy assignments to `sql-01…sql-05` for symmetry (with redirects or updated links). (4) State up front which SQL dialect the course uses.
---

## 6. Per-File Analysis — Python Lessons (learn/python/)

### hour-01-python-introduction.html
- **Current state**: Covers what Python is, history, use cases, installation, and Jupyter basics. Newer format with styled code blocks and outputs. Good quality.
- **Strengths**: Friendly on-ramp; Jupyter walkthrough matches assignment 1; takeaways present.
- **Gaps / issues**: No mention of running scripts outside Jupyter (`python file.py`), no `pip`/virtualenv primer, no troubleshooting section for failed installs (the most common hour-1 problem).
- **Suggestions**: (1) Add a "running Python three ways" section (REPL, script, notebook). (2) Add an install-troubleshooting box (PATH issues, `py` vs `python` on Windows). (3) Mention pip briefly and forward-reference hour 33 (modules).

### hour-02-python-syntax.html
- **Current state**: Indentation, comments, `print()`, statement structure. Newer format, good quality.
- **Strengths**: Indentation errors demonstrated explicitly — exactly the right hour-2 content.
- **Gaps / issues**: No `IndentationError` traceback shown as output; multi-line statements (`\`, implicit continuation in brackets) not covered; `print()` separators (`sep=`, `end=`) missing.
- **Suggestions**: (1) Show an actual `IndentationError` traceback. (2) Add `print(sep=, end=)` examples. (3) Add a "common syntax mistakes" checklist (missing colon, mixing tabs/spaces).

### hour-03-variables.html
- **Current state**: Variable creation, naming rules, dynamic typing, reassignment. Newer format, good quality.
- **Strengths**: Naming conventions (snake_case) and invalid-name examples included.
- **Gaps / issues**: Multiple assignment (`a, b = 1, 2`) and swapping absent; constants convention (UPPER_CASE) absent; no mention that variables are references (sets up later mutability confusion).
- **Suggestions**: (1) Add tuple-unpacking assignment and swap idiom. (2) Add constants-by-convention note. (3) One paragraph on names-are-references with an `id()` demo.

### hour-04-data-types-overview.html
- **Current state**: Primitive types tour, `type()`, casting. Newer format, good quality.
- **Strengths**: Casting pitfalls (e.g. `int("3.5")` failing) demonstrated.
- **Gaps / issues**: `isinstance()` not shown (better practice than `type() ==`); no complex/bytes mention even as a "you may see these" footnote; truthiness deferred entirely to hour 10 without a forward link.
- **Suggestions**: (1) Add `isinstance()` example. (2) Add a one-line forward reference to hour 10 for bool/None. (3) Add a type-conversion summary table (from/to, what fails).

### hour-05-numbers.html [IN FLUX]
- **Current state**: int, float, arithmetic operators, numeric built-ins. Newer format, good quality.
- **Strengths**: Full operator table including `//`, `%`, `**`; practical banking-flavored examples per site convention.
- **Gaps / issues**: Float precision (`0.1 + 0.2`) not demonstrated; `round()` banker's-rounding surprise absent; `math` module teased but not shown; integer division sign behavior (`-7 // 2`) missing.
- **Suggestions**: (1) Add float-precision demo + `round()` caveat. (2) Show `divmod()`. (3) Brief `math.floor/ceil` preview with forward link to hour 33.

### hour-06-strings-basics.html [IN FLUX]
- **Current state**: String creation, quotes, immutability, concatenation, repetition. Transitional format — some styled blocks, thin outputs. Fair quality.
- **Strengths**: Immutability demonstrated with an error example.
- **Gaps / issues**: Escape sequences (`\n`, `\t`, `\\`) not covered; raw strings absent; `len()` on strings not shown here (first natural place); output blocks missing for several examples.
- **Suggestions**: (1) Add escape-sequence table with printed outputs. (2) Add `len()` and `in` membership. (3) Normalize all code blocks to the styled format with outputs.

### hour-07-string-indexing.html [IN FLUX]
- **Current state**: Positive/negative indexing, `IndexError`. Transitional format. Fair quality.
- **Strengths**: Negative indexing given equal weight; error case shown.
- **Gaps / issues**: No index-position diagram substitute (a simple monospace ruler like `P y t h o n / 0 1 2 3 4 5` would fit the no-diagram convention); iteration over characters not previewed; outputs sparse.
- **Suggestions**: (1) Add a monospace index ruler in a code block. (2) Show `for ch in s` preview linking to hour 15. (3) Add outputs to every example.

### hour-08-string-slicing.html [IN FLUX]
- **Current state**: `s[start:stop:step]`, defaults, reversal idiom. Transitional format. Fair quality.
- **Strengths**: `[::-1]` reversal covered; out-of-range slice forgiveness mentioned.
- **Gaps / issues**: Negative steps beyond `-1` unexplained; slice-copy idiom `s[:]` absent; no practical examples (extracting file extensions, area codes); outputs missing on several blocks.
- **Suggestions**: (1) Add practical slicing tasks (filename extension, first/last name from "LAST, FIRST"). (2) Explain empty-result slices (`s[5:2]`). (3) Add outputs throughout.

### hour-09-string-methods.html [IN FLUX]
- **Current state**: upper/lower/strip/replace/split/join/find/count/format. Older thin format: plain code blocks, few outputs, empty "Data Cleaning Flow" heading. Weak quality relative to the 20-question assignment it feeds.
- **Strengths**: Method selection is right; the paired assignment is excellent (20 questions incl. `endswith`, `isdigit`, `swapcase`, `lstrip`).
- **Gaps / issues**: Lesson does not teach `endswith()`, `startswith()`, `isdigit()`, `isspace()`, `title()`, `swapcase()`, `lstrip()`/`rstrip()`, or `index()` vs `find()` — all of which the assignment requires; no outputs; "Practice Before Assignment" references non-existent notebook cells; empty diagram-stub heading.
- **Suggestions**: (1) **Priority: teach every method the assignment uses**, esp. `find()` vs `index()` error behavior. (2) Add a method summary table (method / purpose / returns / example). (3) Delete the "Data Cleaning Flow" stub. (4) Add outputs everywhere.

### hour-10-boolean-and-none.html [IN FLUX]
- **Current state**: True/False, None, truthy/falsy. Older thin format. Fair-to-weak quality.
- **Strengths**: Truthy/falsy table is genuinely useful and rare in beginner courses.
- **Gaps / issues**: `bool()` casting examples sparse; `None` vs `0` vs `""` comparisons not demonstrated; `is None` idiom absent; "Practice Before Assignment" references non-existent exercises; no outputs.
- **Suggestions**: (1) Add `is None` (correct) vs `== None` (discouraged). (2) Demonstrate truthiness driving an `if` on empty list/string. (3) Remove phantom practice reference; add outputs.

### hour-11-operators.html
- **Current state**: Arithmetic, comparison, logical, identity, membership operators. Older thin format. Fair quality.
- **Strengths**: Covers `is` and `in` — often skipped; feeds a solid 20-question assignment.
- **Gaps / issues**: Operator precedence never discussed; short-circuit evaluation (`and`/`or` returning operands) missing; augmented assignment (`+=`, `-=`…) missing; chained comparisons (`1 < x < 10`) missing; no outputs; phantom "Practice Before Assignment".
- **Suggestions**: (1) Add precedence table + one parenthesization example. (2) Demonstrate short-circuiting with `print` side effects. (3) Add augmented assignment and chained comparison. (4) Outputs throughout.

### hour-12-input-function.html
- **Current state**: `input()`, casting input, prompt strings. Older thin format with an empty "Input Flow" heading. Fair quality.
- **Strengths**: The str-in/str-out trap is called out early.
- **Gaps / issues**: No `try/except ValueError` around casting (forward link to hour 30 would do); no multi-value input (`split()`); mojibake `?` where a symbol was intended; empty diagram stub; no outputs (particularly bad for an interactive topic — show the console transcript).
- **Suggestions**: (1) Show a full console transcript (prompt, typed value, printed result). (2) Add "two numbers on one line" via `split()`. (3) Delete the "Input Flow" stub; fix mojibake.

### hour-13-conditional-statements.html
- **Current state**: if/elif/else with banking examples. Older thin format. Fair quality with a correctness bug.
- **Strengths**: elif chain ordering explained; good real-world framing.
- **Gaps / issues**: **Bug: example uses `lessons_completed` without defining it** — copy/paste artifact; no ternary expression (`x if cond else y`); no nested-vs-elif comparison (that's hour 14, but no link); no outputs.
- **Suggestions**: (1) Fix the undefined-variable example. (2) Add conditional expression syntax. (3) Add outputs; end with a decision-table exercise.

### hour-14-nested-conditions.html
- **Current state**: Nested if blocks, combining with logical operators. Older thin format. Fair quality with a correctness bug.
- **Strengths**: Shows flattening nested ifs with `and` — the key takeaway.
- **Gaps / issues**: **Bug: `username_exists` referenced but never defined**; no guard-clause / early-exit pattern; readability limits of deep nesting not quantified (max ~2 levels rule of thumb); no outputs.
- **Suggestions**: (1) Fix undefined variable. (2) Add guard-clause refactor example. (3) Outputs throughout.

### hour-15-for-loop.html
- **Current state**: for loops, `range()` variants, iterating strings. Older thin format. Fair quality.
- **Strengths**: All three `range()` signatures shown.
- **Gaps / issues**: Looping over lists deferred oddly (lists arrive hour 18) without a note; `enumerate()` absent (appears only in hour 29); accumulator pattern (sum/count in a loop) underdeveloped; no outputs.
- **Suggestions**: (1) Add accumulator pattern worked example (total, count, max-so-far). (2) Preview `enumerate()` with forward link. (3) Outputs everywhere.

### hour-16-while-loop.html
- **Current state**: while loops, condition updates, infinite-loop warning. Older thin format. Fair quality.
- **Strengths**: Infinite-loop pitfall covered with a fix.
- **Gaps / issues**: Sentinel-value pattern (loop until user types "quit") missing — the canonical while use case; `while True: ... break` idiom absent (partially in hour 17); for-vs-while decision guidance thin; no outputs.
- **Suggestions**: (1) Add sentinel-controlled input loop. (2) Add explicit "for when count is known, while when it isn't" rule. (3) Outputs.

### hour-17-loop-control.html
- **Current state**: break, continue, pass, loop-else. Older thin format. Fair quality.
- **Strengths**: Rare inclusion of `else` on loops — good differentiator.
- **Gaps / issues**: Loop-else explanation is brief enough to mislead (fires when no break) — needs a search-found/not-found worked example; `pass` use cases beyond placeholder not shown; nested-loop break behavior (only inner loop) not addressed; no outputs.
- **Suggestions**: (1) Full search example with else. (2) Nested-loop break demo. (3) Outputs.

### hour-18-lists-basics.html [IN FLUX]
- **Current state**: List creation, indexing, mutation, mixed types. Older thin format. Fair quality.
- **Strengths**: Mutability contrasted against strings explicitly.
- **Gaps / issues**: `len()`, `in`, concatenation/repetition on lists missing; list-from-`range()` conversion absent; aliasing (`b = a` sharing) not covered — the classic beginner trap; no outputs.
- **Suggestions**: (1) Add aliasing demo (`b = a; b.append(...)` affects `a`). (2) Add `len`/`in`/`+`/`*`. (3) Outputs.

### hour-19-list-methods.html [IN FLUX]
- **Current state**: append/extend/insert/remove/pop/clear/index/count/sort/reverse. Older thin format. Fair quality.
- **Strengths**: append vs extend distinction shown clearly.
- **Gaps / issues**: `sort()` vs `sorted()` (in-place vs copy, returns None) not contrasted; `sort(key=..., reverse=...)` absent; `remove()` ValueError and `pop()` on empty list not shown; `copy()` missing; no outputs.
- **Suggestions**: (1) Add `sort()` returns None trap. (2) Add `key=`/`reverse=` sorting. (3) Error cases + outputs.

### hour-20-list-indexing-and-slicing.html [IN FLUX]
- **Current state**: List slicing, slice assignment, shallow copies. Older thin format. Fair quality.
- **Strengths**: Slice assignment covered — unusual and valuable.
- **Gaps / issues**: Shallow-copy limits with nested lists not demonstrated; `del lst[i:j]` absent; negative-step list slicing absent; no outputs.
- **Suggestions**: (1) Nested-list shallow copy demo (`copy` vs `deepcopy` teaser). (2) Add `del` slice deletion. (3) Outputs.

### hour-21-tuples.html [IN FLUX]
- **Current state**: Tuple creation, immutability, unpacking. Older thin format. Fair quality.
- **Strengths**: Unpacking incl. swap idiom present.
- **Gaps / issues**: Single-element tuple `(x,)` trap missing; tuples as dict keys / function multi-return not shown; `*rest` extended unpacking absent; when-tuple-vs-list guidance thin; no outputs.
- **Suggestions**: (1) Add `(x,)` gotcha. (2) Multi-return function example. (3) `a, *rest = ...`. (4) Outputs.

### hour-22-sets.html [IN FLUX]
- **Current state**: Set creation, uniqueness, add/remove, union/intersection/difference. Older thin format. Fair quality.
- **Strengths**: All four set algebra operations with both operator and method forms.
- **Gaps / issues**: Empty-set `set()` vs `{}` trap missing; dedupe-a-list idiom (`list(set(x))`) absent; `discard` vs `remove` error behavior not contrasted; unordered nature not demonstrated; frozen sets absent; no outputs.
- **Suggestions**: (1) Add `{}`-is-a-dict gotcha. (2) Dedupe idiom + membership-test performance note. (3) Outputs.

### hour-23-dictionaries.html [IN FLUX]
- **Current state**: Dict syntax, key-value access, adding/updating keys. Older thin format. Fair quality.
- **Strengths**: KeyError shown for missing keys.
- **Gaps / issues**: `in` on keys, `len()`, deleting keys (`del`/`pop`) missing here (some deferred to 24 without links); allowed key types (hashability) not mentioned; iteration over a dict not previewed; no outputs.
- **Suggestions**: (1) Add `in`/`del` basics. (2) One line on valid key types. (3) Outputs.

### hour-24-dictionary-methods.html [IN FLUX]
- **Current state**: keys/values/items/get/update/pop/setdefault. Older thin format. Fair quality.
- **Strengths**: `get()` with default and `setdefault()` both present — good depth.
- **Gaps / issues**: Iterating with `.items()` unpacking not shown as the core pattern; counting-with-dict idiom (word counts) absent; `dict.fromkeys()` absent; merge (`{**a, **b}` or `|`) absent; no outputs.
- **Suggestions**: (1) Add the counting idiom (leads into real data work). (2) `for k, v in d.items()` as the canonical loop. (3) Dict merge syntax. (4) Outputs.

### hour-25-nested-data-structures.html
- **Current state**: Lists of dicts, dicts of lists, deep indexing. Older thin format. Fair quality.
- **Strengths**: Realistic records-style data (list of dicts) matching later Pandas framing.
- **Gaps / issues**: No looping over list-of-dicts to filter/aggregate (the payoff of the whole structure); JSON parallel not mentioned; safe deep access (`get` chaining) absent; no outputs.
- **Suggestions**: (1) Add filter/aggregate loop over records ("total salary of dept X"). (2) One-line JSON analogy. (3) Outputs.

### hour-26-functions-basics.html
- **Current state**: def, parameters, return vs print. Newer format, good quality.
- **Strengths**: return-vs-print confusion tackled head-on with outputs.
- **Gaps / issues**: Malformed formula rendering in one explanation block (formatting artifact); docstrings absent; functions-calling-functions absent; `None` implicit return only implied.
- **Suggestions**: (1) Fix the malformed formula text. (2) Add docstring convention + `help()`. (3) Show implicit `None` return explicitly.

### hour-27-function-arguments.html
- **Current state**: Positional, keyword, default, `*args`, `**kwargs`. Newer format, good quality.
- **Strengths**: Complete argument taxonomy with correct ordering rules.
- **Gaps / issues**: Mutable default argument trap (`def f(x, lst=[])`) missing — the most important pitfall in this topic; unpacking at call site (`f(*seq)`) absent; keyword-only args (`*,`) absent.
- **Suggestions**: (1) **Add the mutable-default trap** with the `None` sentinel fix. (2) Call-site unpacking. (3) Brief keyword-only mention.

### hour-28-lambda-functions.html
- **Current state**: Lambda syntax with map/filter/sorted. Newer format, good quality with one bug.
- **Strengths**: `sorted(key=lambda ...)` is exactly the practical use case to teach.
- **Gaps / issues**: **Bug: sorted example uses `key=lambda x: x["spend"]` on records that have a `score` field** — would raise KeyError; no guidance on when a named function beats a lambda; list-comprehension alternative to map/filter unmentioned (comprehensions are absent from the whole course).
- **Suggestions**: (1) Fix the `spend`/`score` key bug. (2) Add lambda-vs-def guidance. (3) Note comprehension alternative (and add comprehensions to curriculum, §3).

### hour-29-built-in-functions.html [IN FLUX]
- **Current state**: len/type/sum/max/min/sorted/zip/enumerate/any/all/abs/round. Newer format, good quality with one bug.
- **Strengths**: Broad, well-chosen set incl. any/all which most courses skip.
- **Gaps / issues**: **Bug: `zip` example references `amounts` where the defined list is `scores`**; `max/min(key=...)` absent; `reversed()` and `range` as a builtin absent; `round()` precision quirks not linked back to hour 5.
- **Suggestions**: (1) Fix `amounts`/`scores`. (2) Add `max(records, key=lambda r: ...)` — bridges hour 28. (3) Outputs verified for all.

### hour-30-exception-handling.html
- **Current state**: try/except/else/finally, specific exception types. Newer format, good quality.
- **Strengths**: else and finally both covered with correct semantics; specific-before-general except ordering shown.
- **Gaps / issues**: `raise` barely covered (assignment Q10 requires it); custom exception classes absent; `as e` message capture shown but traceback reading not taught; `finally` with return subtlety not needed but a cleanup file-handle example would tie to hour 31.
- **Suggestions**: (1) Add a `raise ValueError(...)` section (assignment depends on it). (2) Short "reading a traceback" box. (3) Forward-link to `with` in hour 31 as the better cleanup tool.

### hour-31-file-handling.html
- **Current state**: open() modes, with-statement, read/readline/readlines, write/append. Newer format, good quality.
- **Strengths**: `with` promoted as default; mode table complete.
- **Gaps / issues**: `FileNotFoundError` handling not integrated (natural tie to hour 30); encoding parameter (`encoding="utf-8"`) never mentioned — ironic given the site's own mojibake; iterating a file line-by-line (`for line in f`) missing; path handling (`os.path`/`pathlib`) absent.
- **Suggestions**: (1) Add `encoding="utf-8"` to every open() and explain why. (2) Add `for line in f` as the canonical read loop. (3) try/except around open().

### hour-32-csv-handling.html
- **Current state**: csv module — reader, writer, DictReader, DictWriter. Newer format, good quality.
- **Strengths**: Dict variants included; `newline=""` handled correctly.
- **Gaps / issues**: Header-row handling with plain `reader` (skip via `next()`) not shown; type conversion of read values (all strings!) not emphasized; delimiter/quoting parameters absent; no link forward to Pandas `read_csv` (hour 41) as the industrial alternative.
- **Suggestions**: (1) Add `next(reader)` header skip. (2) Emphasize str-typed cells with a casting example. (3) Forward-link to hour 41.

### hour-33-modules.html
- **Current state**: import forms, math/random/datetime tour, writing your own module. Newer format, good quality.
- **Strengths**: Custom module example with two files — concrete and runnable.
- **Gaps / issues**: `pip install` and third-party packages absent (needed before hours 39–43 which use numpy/pandas!); `if __name__ == "__main__"` absent; import aliasing (`import numpy as np`) not previewed; module search path not mentioned.
- **Suggestions**: (1) **Add a pip/install section** — learners hit hour 39 with no way to install NumPy. (2) Add `__main__` guard. (3) Preview `as` aliasing.

### hour-34-date-and-time.html
- **Current state**: datetime/date/time classes, strftime, strptime, timedelta. Newer format, good quality.
- **Strengths**: Both directions (format and parse) plus arithmetic — complete core.
- **Gaps / issues**: Format-code table incomplete (%j, %U niche ones fine to skip, but %A/%B weekday/month names are worth adding); timezone awareness completely absent (one warning box would do); date comparison (`<`, sorting dates) not shown.
- **Suggestions**: (1) Add %A/%B examples. (2) "Naive vs aware" warning box. (3) Sort-a-list-of-dates example.

### hour-35-oop-introduction.html
- **Current state**: Class vs object, attributes, dot notation. Newer format, good quality with a naming bug.
- **Strengths**: Clear conceptual framing before syntax.
- **Gaps / issues**: **Bug: lesson defines a `BankAccount`-style class but then instantiates `Learner(...)` with mismatched parameters** — copy/paste from another example set; class naming convention (PascalCase) implied but not stated.
- **Suggestions**: (1) Fix the class/instantiation mismatch so the example runs. (2) State PascalCase convention. (3) Add `type()` on an instance to connect back to hour 4.

### hour-36-constructor.html
- **Current state**: `__init__`, self, default parameter values. Newer format, good quality with bugs.
- **Strengths**: self explained mechanically (Python passes the instance) rather than hand-waved.
- **Gaps / issues**: **Bug: `SavingsAccount` example has parameters (`name`, `sku`, `stock_on_hand=0`) that don't match the attributes it assigns (`account_type`, `modules_completed`), and then instantiates `Learner` instead of `SavingsAccount`** — the example cannot run; `__init__` returning None rule unmentioned.
- **Suggestions**: (1) **Rewrite the example end-to-end with one coherent class** (site convention says banking names — make it genuinely `SavingsAccount(owner, balance=0)`). (2) Add "constructor must not return a value" note.

### hour-37-methods-in-class.html
- **Current state**: Instance methods reading and mutating state. Newer format, good quality.
- **Strengths**: Read vs mutate distinction made explicit — good design seed.
- **Gaps / issues**: Method chaining/return-self absent (fine), but `__str__` absent hurts — learners print objects and get `<object at 0x...>` with no explanation; class attributes vs instance attributes not distinguished.
- **Suggestions**: (1) Add `__str__` with before/after print output. (2) One class-attribute example (e.g. interest rate shared across accounts).

### hour-38-inheritance.html
- **Current state**: Parent/child, super(), overriding. Newer format, good quality with artifacts.
- **Strengths**: super() in `__init__` shown correctly.
- **Gaps / issues**: **Bug: calls undefined `l.greet()`; stray "Python Sprint" comment left in a code block**; `isinstance()` with inheritance absent; multiple inheritance rightly skipped but "when to prefer composition" absent.
- **Suggestions**: (1) Fix `l.greet()` and remove the stray comment. (2) Add `isinstance(child, Parent)` demo. (3) One-paragraph composition note.

### hour-39-numpy-introduction.html
- **Current state**: ndarray concept, properties (shape/dtype/ndim), creation functions. Newer format, good quality.
- **Strengths**: Contrasts list vs array performance rationale.
- **Gaps / issues**: No install instructions (`pip install numpy`) — compounds the hour-33 gap; `arange`/`linspace` coverage uneven; random arrays (used by assignment 45!) absent; dtype coercion surprises (int array truncating floats) missing.
- **Suggestions**: (1) Add install box. (2) Add `np.random` basics (assignment 45 needs it). (3) dtype coercion example.

### hour-40-numpy-operations.html
- **Current state**: Vectorized arithmetic, broadcasting, indexing/slicing, reshape, aggregations. Newer format, good quality.
- **Strengths**: Broadcasting introduced gently with shapes spelled out.
- **Gaps / issues**: Boolean masking (`arr[arr > 40]`) thin — it's the bridge to Pandas filtering and assignment 45's pass-rate question; `axis=` semantics on 2-D aggregations underexplained; views-vs-copies on slices not mentioned.
- **Suggestions**: (1) Expand boolean masking + conditional sums (`(marks >= 40).sum()`). (2) `axis=0/1` worked example on a 2-D array. (3) Slice-is-a-view warning.

### hour-41-pandas-introduction.html
- **Current state**: Series vs DataFrame, creation, read_csv, head/info/describe. Newer format, good quality.
- **Strengths**: Mirrors the assignment nearly 1:1 — best-aligned pair in the course.
- **Gaps / issues**: `shape`, `dtypes`, `columns`, `index` (all in the assignment) get little/no lesson coverage; no install box; no sample CSV provided to actually read.
- **Suggestions**: (1) Cover `shape/dtypes/columns/index` explicitly. (2) Ship a small `course_fees.csv` learners can download (referenced by hours 32/41/44 assignments). (3) Install box.

### hour-42-pandas-data-cleaning.html
- **Current state**: isnull/dropna/fillna, drop_duplicates, rename, astype. Newer format, good quality.
- **Strengths**: Covers the real top-4 cleaning operations in a sensible order.
- **Gaps / issues**: `inplace=` vs reassignment convention not settled (examples should standardize on reassignment); string cleaning via `.str` accessor absent; `pd.to_numeric(errors="coerce")` absent — the workhorse of dirty data; detecting duplicates before dropping (`duplicated()`) missing.
- **Suggestions**: (1) Standardize on reassignment, note `inplace` deprecation direction. (2) Add `.str.strip()/.str.lower()` examples. (3) Add `to_numeric(errors="coerce")`.

### hour-43-pandas-filtering.html
- **Current state**: Column/row selection, boolean indexing, .loc/.iloc. Newer format, good quality.
- **Strengths**: loc vs iloc contrast with the same target rows — clear.
- **Gaps / issues**: Combining conditions (`&`, `|`, parentheses requirement) needs stronger warning — the #1 Pandas beginner error; `isin()` absent; `between()` absent; sorting (`sort_values`) absent here and not clearly owned by any hour.
- **Suggestions**: (1) Add explicit `&`/`|` + parentheses trap with the error message shown. (2) Add `isin()`/`between()`. (3) Give `sort_values` a home (here or 44).

### hour-44-mini-project.html
- **Current state**: End-to-end ETL: read, clean, filter, groupby/agg, export. Newer format, good quality.
- **Strengths**: Ties the entire course together; groupby explained before use.
- **Gaps / issues**: The project narrative references data files not shipped with the site; `agg()` dict syntax shown but named aggregation (`agg(total=('fee','sum'))`) absent; no validation step (row counts before/after cleaning) which would model good practice; export `index=False` covered only in the assignment.
- **Suggestions**: (1) Provide the CSV dataset. (2) Add named aggregation. (3) Add a sanity-check step (shape before/after each stage).

### hour-45-final-assessment.html
- **Current state**: Revision guide, test format, project evaluation criteria. Newer format, good quality.
- **Strengths**: Clear rubric-style evaluation criteria; keeps scope realistic.
- **Gaps / issues**: Revision checklist doesn't map hours to topics (a table would make gaps obvious to learners); no practice exam questions; assignment 45 requires NumPy random + Pandas grading pipeline not fully rehearsed in lessons (see hours 39/40 gaps); only a Previous nav link (correct as final page, but a "Back to path index" CTA would close the loop).
- **Suggestions**: (1) Add an hour→topic revision table. (2) Add 5 sample exam questions with answers. (3) Add a completion CTA back to the index / blog.
---

## 7. Per-File Analysis — SQL Lessons (learn/sql/)

### 01-introduction.html
- **Current state**: Databases, tables, rows/columns, first SELECT/FROM against `hr.employees`. Prose is clear; structure is good.
- **Strengths**: Gentle framing ("asking questions of a table"); establishes the hr schema.
- **Gaps / issues**: **No prev/next navigation and no assignment link** (lessons 1–5 all lack them); "Query execution order" heading is an empty placeholder; some schema references already drift from the canonical column list; SELECT of specific columns vs `*` covered but no result-grid outputs for every query.
- **Suggestions**: (1) Add nav + assignment link (`sql-basic-select.html`). (2) Fill or delete the execution-order placeholder — a numbered list (FROM → WHERE → SELECT → ORDER BY) fits the no-diagram rule. (3) Print the full canonical hr schema here as the single source of truth, and provide a downloadable seed script.

### 02-filtering-where.html
- **Current state**: WHERE, comparison ops, AND/OR, LIKE/IN/BETWEEN, NULL checks. Good topical coverage.
- **Strengths**: LIKE wildcards and IS NULL both present — right depth for topic 2.
- **Gaps / issues**: Missing nav/assignment links; **contradictory example** `department_id = '50' AND (department_id = 'Mumbai' OR department_id = 'Delhi')` can never be true and mixes an ID with city names (rename damage); numeric IDs quoted as strings inconsistently; NOT operator absent; no outputs for several queries.
- **Suggestions**: (1) Fix the contradictory/mistyped predicate (cities belong to `locations.city`). (2) Standardize unquoted numeric IDs. (3) Add `NOT` and operator-precedence note (AND binds before OR). (4) Nav + assignment link.

### 03-sorting-and-limiting.html
- **Current state**: ORDER BY (single/multi/ASC/DESC), LIMIT, OFFSET. Sound explanation.
- **Strengths**: Multi-column sort with mixed directions shown.
- **Gaps / issues**: Missing nav/assignment links; NULL ordering behavior absent; LIMIT dialect differences (TOP/FETCH FIRST) unmentioned; OFFSET-pagination caveat (performance, drift) absent; sparse outputs.
- **Suggestions**: (1) Add NULLS FIRST/LAST note. (2) One dialect box (MySQL/Postgres/SQL Server). (3) Nav + assignment link.

### 04-joining-tables.html
- **Current state**: INNER JOIN, LEFT JOIN, aliases, joining employees→departments. Core content correct.
- **Strengths**: Alias discipline (`e`, `d`) used consistently; LEFT JOIN NULL rows explained.
- **Gaps / issues**: Missing nav/assignment links; "Table relationships" heading is an empty placeholder; RIGHT/FULL joins not even name-checked; join-on-wrong-column pitfall absent; multi-table (3-way) join absent though the schema supports employees→departments→locations.
- **Suggestions**: (1) Add a 3-table join example. (2) Fill/delete the relationships placeholder with a text-based key map (`employees.department_id → departments.department_id`). (3) Name RIGHT/FULL with one line each. (4) Nav + assignment link.

### 05-aggregations.html
- **Current state**: COUNT/SUM/AVG/MIN/MAX, GROUP BY, HAVING. Correct fundamentals.
- **Strengths**: WHERE-vs-HAVING distinction addressed.
- **Gaps / issues**: Missing nav/assignment links; "Aggregation pipeline" heading is an empty placeholder; `COUNT(*)` vs `COUNT(col)` vs `COUNT(DISTINCT col)` not contrasted; the classic error (selecting a non-grouped column) never shown; sparse outputs.
- **Suggestions**: (1) Add COUNT variants comparison with NULL data. (2) Show the non-grouped-column error message and fix. (3) Fill/delete the placeholder. (4) Nav + assignment link.

### 06-dml.html
- **Current state**: INSERT (single/multi), UPDATE with WHERE, DELETE. Structure fine; text corrupted.
- **Strengths**: "UPDATE/DELETE without WHERE" danger called out.
- **Gaps / issues**: **Corrupted text: "payrollsible" (×2) and "the 30 ETL pattern"**; INSERT...SELECT absent; RETURNING/verifying-affected-rows absent; no transaction safety note (BEGIN before mass UPDATE) though lesson 28 exists.
- **Suggestions**: (1) Fix corrupted words. (2) Add `INSERT ... SELECT`. (3) Add "wrap risky DML in a transaction" forward link to lesson 28. (4) Mention SQL injection/parameterized queries (§3 gap).

### 07-create-table.html
- **Current state**: CREATE TABLE, data types, NOT NULL, DEFAULT. Explanations fine; examples broken.
- **Strengths**: Data-type selection table is a good idea.
- **Gaps / issues**: **`CREATE TABLE hr.jobs` defines `job_id` and salary-related columns twice; `hr.employees` defines `employee_id` twice; `hr.job_history` gets a single-column PK where the real-world key is composite (employee_id, start_date)**; data-type table references a column that exists in no example; dialect of types (TEXT vs VARCHAR) unstated.
- **Suggestions**: (1) **Rewrite all three CREATE statements so they parse** and match the canonical schema from lesson 1. (2) State the dialect. (3) Add `IF NOT EXISTS` and `DROP TABLE` lifecycle.

### 08-keys.html
- **Current state**: PRIMARY KEY, FOREIGN KEY, composite keys. Conceptually fine; examples broken.
- **Strengths**: Composite keys covered — often omitted.
- **Gaps / issues**: **`hr.employees` again defines `employee_id` twice; the FK meant to model manager→employee is written as `FOREIGN KEY (employee_id) REFERENCES hr.employees(employee_id)` — should be `manager_id`**; ON DELETE/UPDATE actions absent; natural vs surrogate key discussion absent.
- **Suggestions**: (1) Fix the duplicate column and the manager FK. (2) Add `ON DELETE SET NULL / CASCADE` with one example each. (3) Brief surrogate-key note (AUTO_INCREMENT/SERIAL).

### 09-alter-table.html
- **Current state**: ADD/RENAME/DROP COLUMN. Fine structure; one broken example.
- **Strengths**: Warns that DROP COLUMN destroys data.
- **Gaps / issues**: **No-op example: `ALTER TABLE hr.jobs RENAME COLUMN salary TO salary;`**; ALTER ... ALTER COLUMN TYPE (changing types) absent; adding a NOT NULL column to a populated table (needs DEFAULT) not covered; renaming tables absent.
- **Suggestions**: (1) Fix the rename to actually rename (`salary` → `base_salary`). (2) Add change-type and add-NOT-NULL-with-DEFAULT recipes. (3) `RENAME TO` for tables.

### 10-constraints.html
- **Current state**: UNIQUE and CHECK constraints. Broken example table.
- **Strengths**: Both column-level and table-level constraint syntax shown.
- **Gaps / issues**: **Duplicate `job_id` definition again; CHECK applied to `job_title IN ('active','inactive','pending')` — a status list on a title column (rename damage); "payrollsible" typo**; violation error messages never shown; named constraints (`CONSTRAINT chk_...`) absent; NULL-passes-CHECK subtlety absent.
- **Suggestions**: (1) Rebuild the example table (put the status CHECK on a `status` column). (2) Show a violation error. (3) Name constraints and show dropping one. (4) Fix typo.

### 11-indexes.html
- **Current state**: CREATE/DROP INDEX, read-speed vs write-cost trade-off. Reasonable intro.
- **Strengths**: Trade-off framing is honest and correct.
- **Gaps / issues**: "payrollsible"-family typo; composite index column-order rule absent; UNIQUE INDEX vs UNIQUE constraint relation absent; "when the index is ignored" (functions on columns, leading wildcard LIKE) absent; no EXPLAIN tie-in despite lesson 30.
- **Suggestions**: (1) Add composite-index leftmost-prefix rule. (2) Add index-defeating query patterns. (3) Forward-link to lesson 30 with a before/after EXPLAIN. (4) Fix typo.

### 12-views.html
- **Current state**: CREATE VIEW, CREATE OR REPLACE, DROP VIEW. Clear mechanics.
- **Strengths**: Views-as-saved-queries framing is right; REPLACE covered.
- **Gaps / issues**: **View definitions select `p.category` and other columns that don't exist in `hr.jobs`** (schema drift); updatable-view limitations absent; materialized views not even name-checked; view-over-join example needed since that's the main use.
- **Suggestions**: (1) Fix column references to the canonical schema. (2) Add a view over the employees→departments join. (3) One-line updatable-view + materialized-view notes.

### 13-subqueries.html
- **Current state**: Subqueries in WHERE (scalar, IN), FROM-clause subqueries, EXISTS. Good breadth.
- **Strengths**: Scalar vs multi-row distinction with the > (SELECT AVG…) classic.
- **Gaps / issues**: Schema drift in examples (columns not in canonical hr tables); multi-row scalar error (`more than one row returned`) never shown; `NOT IN` + NULL trap absent; derived tables must-be-aliased rule not called out.
- **Suggestions**: (1) Align examples to canonical schema. (2) Show the more-than-one-row error. (3) Add the `NOT IN` NULL trap (ties to §3). (4) State the alias rule.

### 14-correlated-subqueries.html
- **Current state**: Correlated subqueries, correlated EXISTS, JOIN-vs-subquery comparison. Good conceptual level.
- **Strengths**: Explicit inner-query-runs-per-outer-row explanation; comparison with JOINs.
- **Gaps / issues**: **Examples reference `p.category` on hr tables that don't have it** (rename residue); performance implications stated but not demonstrated; "greatest per group" solved here but not connected to the window-function alternative (lessons 23–24).
- **Suggestions**: (1) Fix schema drift. (2) Cross-link "same problem via ROW_NUMBER" to lesson 23. (3) Add an EXISTS-vs-IN guidance box.

### 15-case-expressions.html
- **Current state**: Searched and simple CASE, CASE in aggregates and ORDER BY. Strong topic coverage.
- **Strengths**: CASE-inside-SUM pivot trick included — genuinely useful.
- **Gaps / issues**: Example buckets a `lifetime_spend` column that isn't in `hr.employees` (it's derived in another example — confusing); missing ELSE→NULL default behavior note; CASE in GROUP BY absent.
- **Suggestions**: (1) Rework the bucketing example around `salary` (a real column). (2) State ELSE default. (3) Add GROUP BY CASE example (salary bands).

### 16-null-functions.html
- **Current state**: COALESCE and NULLIF with practical defaults. Focused and clear.
- **Strengths**: NULLIF-to-avoid-division-by-zero pattern included.
- **Gaps / issues**: Real-world notes contain rename-damaged wording; COALESCE with multiple fallbacks shown but IFNULL/NVL dialect synonyms absent; interaction with aggregates (`AVG` ignoring NULLs) not connected.
- **Suggestions**: (1) Fix damaged wording. (2) Add dialect synonym table. (3) Add "AVG ignores NULLs — COALESCE first if you want zeros counted" example.

### 17-string-functions.html
- **Current state**: CONCAT, UPPER, LOWER, TRIM, SUBSTR, LENGTH, REPLACE. Correct core set.
- **Strengths**: Practical full-name concat example against hr.employees.
- **Gaps / issues**: **"payrollsible" typo in a description**; `||` vs CONCAT dialect split absent; INSTR/POSITION absent; LEFT/RIGHT absent; case-insensitive search recipe (`LOWER(col) LIKE ...`) absent.
- **Suggestions**: (1) Fix typo. (2) Add dialect concat note. (3) Add POSITION + LEFT/RIGHT. (4) Case-insensitive search example.

### 18-date-functions.html
- **Current state**: Current timestamp, EXTRACT, truncation, arithmetic, formatting, difference. Ambitious and mostly good.
- **Strengths**: Covers both extraction and arithmetic — the two real needs.
- **Gaps / issues**: Redundant/garbled table references like "the job_history table.hire_date" (rename residue); heavy dialect variance (DATE_TRUNC vs DATE_FORMAT vs strftime) not flagged per example; age-calculation recipe absent; date literals format unstated.
- **Suggestions**: (1) Fix garbled references. (2) Tag each example with its dialect. (3) Add tenure-in-years recipe on `hire_date`. (4) State ISO date literal convention.

### 19-union.html
- **Current state**: UNION vs UNION ALL, column-count/type rules. Mechanically correct prose.
- **Strengths**: Dedup-vs-keep-all distinction clear with row counts.
- **Gaps / issues**: **Examples misuse the schema — `hr.job_history` queried as if it had a `salary`-like `total` column, and `employee_id` treated as `department_id`** — the results shown are impossible; ORDER BY-applies-to-whole-union rule absent; mixing incompatible types unaddressed.
- **Suggestions**: (1) Rebuild both example queries against real columns (e.g. current vs historical job assignments). (2) Add the single-final-ORDER BY rule. (3) Add a type-mismatch error demo.

### 20-intersect-except.html
- **Current state**: INTERSECT and EXCEPT with row-set semantics. Clear and short.
- **Strengths**: Set semantics stated precisely; EXCEPT direction-sensitivity noted.
- **Gaps / issues**: **"payrollsible" typo**; MySQL's lack of INTERSECT/EXCEPT (pre-8.0.31) and the JOIN/NOT EXISTS equivalents absent; duplicate handling (ALL variants) absent.
- **Suggestions**: (1) Fix typo. (2) Add dialect-workaround box. (3) Mention INTERSECT ALL/EXCEPT ALL exist.

### 21-self-join-advanced.html
- **Current state**: Self joins for manager hierarchies and sequential-event comparison. Good, correct lesson.
- **Strengths**: employee↔manager join is the perfect schema fit; sequential-events example adds depth.
- **Gaps / issues**: LEFT self-join to keep the CEO (NULL manager) not shown; alias-naming guidance (e vs m) present but the "why aliases are mandatory here" rule not stated; no link to recursive CTEs (lesson 27) for multi-level hierarchies.
- **Suggestions**: (1) Add LEFT self-join with the NULL-manager row. (2) State the mandatory-alias rule. (3) Cross-link lesson 27.

### 22-cross-join.html
- **Current state**: CROSS JOIN and Cartesian products, with a legitimate use case. Solid short lesson.
- **Strengths**: Honest "usually a mistake, occasionally exactly right" framing.
- **Gaps / issues**: Row-count math (m×n) stated but no small worked grid output; accidental cross join via missing ON not demonstrated; generating date/series combinations (the main real use) could be more concrete.
- **Suggestions**: (1) Show a 3×3 grid output. (2) Demonstrate the missing-ON accident. (3) Add departments×months scaffold example.

### 23-window-row-number.html
- **Current state**: ROW_NUMBER with PARTITION BY/ORDER BY, top-N-per-group. Good, practical lesson.
- **Strengths**: Top-1-per-department recipe — the killer app — is present.
- **Gaps / issues**: **"the 30 pattern" corrupted phrase (was "ETL pattern")**; window-vs-GROUP BY conceptual contrast thin; can't-filter-window-in-WHERE rule (must wrap in subquery/CTE) shown but not named; ties behavior (arbitrary order without deterministic ORDER BY) absent.
- **Suggestions**: (1) Fix corrupted phrase. (2) Add "windows don't collapse rows" contrast table. (3) Add deterministic-tiebreaker advice.

### 24-window-rank.html
- **Current state**: RANK, DENSE_RANK, PERCENT_RANK with tie handling. Correct and well-scoped.
- **Strengths**: Gap-vs-no-gap tie difference demonstrated with the same data.
- **Gaps / issues**: **"payrollition" corrupted word**; NTILE absent (natural fit here); choosing between ROW_NUMBER/RANK/DENSE_RANK decision guidance thin; PERCENT_RANK formula given without a use case.
- **Suggestions**: (1) Fix typo. (2) Add NTILE quartile example on salaries. (3) Add a chooser table (need unique? gaps ok?).

### 25-window-lag-lead.html
- **Current state**: LAG/LEAD with offsets and defaults. Good, correct lesson.
- **Strengths**: Default-value third argument covered; month-over-month delta example.
- **Gaps / issues**: A stray "30" corruption in the real-world notes; first-row NULL handling shown but COALESCE wrap not connected to lesson 16; running totals (`SUM OVER`) absent from the whole window block (§3); frame clauses never mentioned.
- **Suggestions**: (1) Fix corruption. (2) COALESCE the first-row NULL, linking lesson 16. (3) Add a short SUM OVER running-total teaser or a new lesson.

### 26-cte.html
- **Current state**: WITH clauses, chained CTEs, readability refactor. Clear and well-motivated.
- **Strengths**: Shows the same query before/after CTE refactor — persuasive teaching.
- **Gaps / issues**: CTE-vs-subquery performance neutrality (usually inlined) unstated; multiple references to one CTE not demonstrated; column-alias-list syntax (`WITH t(a, b) AS`) absent.
- **Suggestions**: (1) Add reuse-same-CTE-twice example. (2) One-line optimizer note. (3) Show the column-list form.

### 27-recursive-cte.html
- **Current state**: WITH RECURSIVE for org-chart traversal, anchor + recursive member. Good, correct treatment of a hard topic.
- **Strengths**: Level/depth column included; termination explained.
- **Gaps / issues**: Infinite-recursion risk (cyclic data) and dialect recursion limits absent; path-string building (materialized path) absent; UNION vs UNION ALL choice in the recursive member unexplained.
- **Suggestions**: (1) Add cycle warning + max-recursion note. (2) Add path concatenation example. (3) Explain the UNION ALL choice.

### 28-transactions.html
- **Current state**: BEGIN/COMMIT/ROLLBACK, ACID walkthrough, transfer example. Solid conceptual lesson.
- **Strengths**: The two-UPDATE money-transfer example is the right canonical case.
- **Gaps / issues**: Rename-damaged wording in notes; autocommit behavior absent; SAVEPOINT absent; isolation levels absent (acceptable scope cut, but deserves a "beyond this course" pointer); no failure demo (what actually happens mid-transaction on error).
- **Suggestions**: (1) Fix wording. (2) Add autocommit note per dialect. (3) Add SAVEPOINT example. (4) Show a forced-error rollback transcript.

### 29-normalization.html
- **Current state**: 1NF/2NF/3NF with stepwise decomposition, denormalization trade-offs. Good theory lesson.
- **Strengths**: Walks one messy table through all three forms — the right structure.
- **Gaps / issues**: Anomalies (insert/update/delete) named but not each demonstrated; functional-dependency notation may be too abstract without more examples; BCNF absent (fine) without a pointer; no tie-back to the hr schema ("which normal form is hr in?").
- **Suggestions**: (1) Demonstrate each anomaly on the denormalized table. (2) Add an "is hr.* 3NF?" closing exercise. (3) One-line BCNF pointer.

### 30-explain.html
- **Current state**: EXPLAIN output reading, seq-scan vs index-scan, optimization workflow. Good capstone.
- **Strengths**: Before/after index comparison; practical optimization checklist.
- **Gaps / issues**: Rename-damaged wording; EXPLAIN output shown for one dialect without saying which; EXPLAIN ANALYZE (actual vs estimated) distinction absent; join-order/row-estimate reading not taught; no closing "course complete" CTA.
- **Suggestions**: (1) Fix wording; state the dialect. (2) Add EXPLAIN vs EXPLAIN ANALYZE. (3) Add one join-plan reading example. (4) Add course-completion CTA.

---

## 8. Per-File Analysis — Assignments

### assignments/index.html
- **Current state**: Full catalog: 45 Python + 30 SQL rows, each with Tutorial + Assignment buttons, plus a notebook-layout preview. Complete and correctly linked.
- **Strengths**: Per-hour question counts shown; notebook preview sets expectations; tutorial back-links throughout.
- **Gaps / issues**: **Two orphaned files (`sql-filtering.html`, `sql-joins-report.html`) are not listed** — 32 SQL files exist, 30 linked; SQL rows say only "Topic N assignment" instead of question counts; no difficulty labels on Python rows; no anchor-link sub-navigation (Python vs SQL) at the top despite the page's length.
- **Suggestions**: (1) Link or delete the two orphans (see their entries below). (2) Add question counts to SQL rows. (3) Add jump links to #python/#sql sections.

### assignments/hour-01-python-introduction.html (spot check)
- **Current state**: 10 notebook-style questions on setup, Jupyter, print basics. Well-matched to the lesson.
- **Strengths**: Questions escalate sensibly; includes conceptual (markdown-cell) tasks; submission instructions.
- **Gaps / issues**: Q1 (screenshot) and Q2 (create notebook) can't be answered "in the cell" — the workspace hint `# Write your solution here` is misleading for them; no answers/self-check.
- **Suggestions**: (1) Mark non-code questions as such. (2) Add a collapsible hints or expected-output section per question.

### assignments/hour-09-string-methods.html (spot check)
- **Current state**: 20 well-crafted questions spanning case, strip, split/join, find vs index, cleanup. High quality.
- **Strengths**: Best assignment reviewed — includes discovery questions (endswith, isdigit, swapcase) and a realistic data-cleaning finale.
- **Gaps / issues**: The paired lesson doesn't teach ~half these methods (see hour-09 lesson entry) — difficulty cliff; no expected outputs.
- **Suggestions**: (1) Fix at the lesson side (teach the methods). (2) Add expected output per question.

### assignments/hour-30-exception-handling.html (spot check)
- **Current state**: 10 questions across ZeroDivisionError, ValueError, KeyError, IndexError, else/finally, raise. Good coverage.
- **Strengths**: Q10 (raise on negative age) pushes beyond the lesson appropriately.
- **Gaps / issues**: Q1 wording garbled: "a script that division-handles a ZeroDivisionError"; lesson barely covers `raise` (needed for Q10).
- **Suggestions**: (1) Fix Q1 wording. (2) Ensure lesson covers raise.

### assignments/hour-41-pandas-introduction.html (spot check)
- **Current state**: 10 questions from import to read_csv/shape. Tight lesson alignment.
- **Strengths**: Gradual ramp; references the hour-32 CSV to create continuity.
- **Gaps / issues**: Depends on `course_fees.csv` "created in Hour 32" — that dependency chain breaks for learners who skipped; no expected outputs.
- **Suggestions**: (1) Ship the CSV or include creation code inline. (2) Add expected outputs.

### assignments/hour-44-mini-project.html (spot check)
- **Current state**: 10 questions forming a mini ETL pipeline (read → clean → group → export → verify → report). Strong.
- **Strengths**: Question 9–10 verification/reporting steps model real practice.
- **Gaps / issues**: Same missing `course_fees.csv` dependency; no grading rubric despite being a project.
- **Suggestions**: (1) Provide the dataset. (2) Add a 5-point rubric.

### assignments/hour-45-final-assessment.html (spot check)
- **Current state**: 10 capstone questions spanning OOP, NumPy, Pandas, files, exceptions. Good synthesis.
- **Strengths**: Genuinely integrative; Q9 combines Pandas + FileNotFoundError.
- **Gaps / issues**: Requires `np.random` (never taught — see hour-39); Q10 ("submit your folder") isn't a code question but shares the code-cell hint.
- **Suggestions**: (1) Teach np.random in hour 39, or add a hint. (2) Restyle Q10 as a submission instruction.

### assignments/sql-basic-select.html (spot check — legacy #1)
- **Current state**: 4 requirements + starter code + expected output + 3 bonus questions on SELECT basics. Right format, damaged content.
- **Strengths**: Only assignment style with starter SQL and expected output blocks — the best template on the site.
- **Gaps / issues**: Garbled question text ("for every each employee row"); Q3 asks for distinct department names "represented in the table" but requires a join lesson 1 hasn't taught; **bonus Q1 asks to combine first and last name into a single `last_name` column** (should be `full_name`); not linked back from the lesson page.
- **Suggestions**: (1) Fix wording and the `full_name` alias. (2) Replace the join-dependent question with `SELECT DISTINCT department_id`. (3) Add tutorial back-link.

### assignments/sql-filtering.html (spot check — ORPHANED)
- **Current state**: Legacy WHERE/ORDER BY assignment, heavily rename-damaged, and **unreachable from any index**.
- **Strengths**: Underlying structure (requirements/starter/expected/bonus) is good.
- **Gaps / issues**: Nearly every question is corrupted: "Find the jobs table with a price greater than 50", "last names start with King" asked of a jobs table, expected output lists "Wireless HeadManagers 185000 / Desk Lamp 665000 / Notebook 12.00" — product-catalog data wearing an hr costume; starter comments contradict questions.
- **Suggestions**: (1) Either delete this file (topic 2's real assignment is `sql-where-practice.html`) or rewrite it fully against hr.employees and link it as extra practice. Deleting is simpler and safe since nothing links here.

### assignments/sql-joins-report.html (spot check — ORPHANED)
- **Current state**: Joins + aggregation report assignment with starter and expected output; **unreachable from any index**.
- **Strengths**: LEFT-JOIN-to-include-empty-departments requirement is exactly right; realistic starter query.
- **Gaps / issues**: **Q2 instructs computing total salary "using `department_id * salary`"** — multiplying an ID by salary is nonsense (rename damage from `quantity * price`); expected output shows Sales at 0.00 which conflicts with the site's own hr data implied elsewhere.
- **Suggestions**: (1) Fix Q2 to `SUM(salary)` per department. (2) Verify expected output against the seed data. (3) Link it from the index as bonus practice for topic 4/5, or delete.

### assignments/sql-06-dml.html (spot check — template stub)
- **Current state**: Four generic questions: review the tutorial, implement a solution, add comments, test 3 inputs. Near-zero practice value.
- **Strengths**: Correct chrome (breadcrumb, tutorial link, notebook styling).
- **Gaps / issues**: **No actual DML exercises** — no "insert this employee", "give department 50 a raise", "delete test rows" tasks; identical text to every other numbered SQL assignment.
- **Suggestions**: (1) Replace with 8–10 concrete tasks: multi-row INSERT into hr.employees, UPDATE with subquery condition, DELETE with a safety SELECT first, INSERT...SELECT archive into job_history.

### assignments/sql-23-window-row-number.html (spot check — template stub)
- **Current state**: Same four generic template questions as sql-06. No topic content.
- **Strengths**: Chrome only.
- **Gaps / issues**: A window-functions topic with zero window-function exercises; "test with 3 different inputs" doesn't even make sense for SELECT queries.
- **Suggestions**: (1) Replace with concrete tasks: number employees by salary within department; top-2 earners per department; dedupe job_history keeping latest row; paginate employees 10 at a time. **Apply this same rewrite to all of sql-06 … sql-30.**

---

## 9. Per-File Analysis — Blog

### blog/index.html
- **Current state**: Three-card blog listing with badges and dates. Clean and correct.
- **Strengths**: Consistent card layout; accurate links and dates.
- **Gaps / issues**: Only 3 posts for a "Tech Log" positioned prominently in the nav; no tag filtering (tags exist on posts but do nothing); no RSS; card badges use a generic style rather than tag-colored variants.
- **Suggestions**: (1) Add 2–3 posts matching course milestones (e.g. "What I learned finishing the loops block", "My first JOIN report"). (2) Make tags visually consistent between index and posts.

### blog/why-python-and-sql.html
- **Current state**: Short motivational post on learning Python + SQL together. Reads well.
- **Strengths**: Clear structure (Plan / Why Both / What's Next); links intent to the site's paths.
- **Gaps / issues**: Very thin (~150 words); "What's Next" promises follow-along logging that only 2 more posts deliver; no links to the actual learning paths inline; no prev/next between posts.
- **Suggestions**: (1) Add inline links to both path indexes. (2) Add post-to-post prev/next nav. (3) Expand with a concrete 4-week plan table.

### blog/day-1-setup.html
- **Current state**: Setup log: Python 3.12, VS Code, Git, SQLite, plus a first script with styled code block. Good.
- **Strengths**: Code block follows site styling with comment tokens; honest reflection section.
- **Gaps / issues**: Mentions VS Code while the Python course teaches Jupyter/Anaconda — setup narratives conflict; no verification commands (`python --version`, `sqlite3 --version`); no prev/next.
- **Suggestions**: (1) Reconcile with hour-01 (mention Jupyter install too). (2) Add verification command outputs. (3) Prev/next nav.

### blog/sql-breakthrough.html
- **Current state**: Reflection on the SELECT mental model with one query example. Charming and useful.
- **Strengths**: The plain-English→SQL mapping is a genuinely good pedagogical nugget; links to the SQL path.
- **Gaps / issues**: The example query is one long line (will overflow on mobile); post uses `hr.employees` while blog prose convention is generic; no prev/next.
- **Suggestions**: (1) Break the query across lines. (2) Add prev/next. (3) Consider promoting the "practice pattern" list into SQL lesson 1.

---

## 10. Summary Statistics

| Metric | Value |
|---|---|
| Files analyzed individually | 94 (45 + 30 lessons, 2 path indexes, assignments index + 12 assignment files, blog index + 3 posts, index.html, login.html) |
| Python lessons in newer high-quality format | 25 of 45 |
| Python lessons needing format upgrade | 20 (hours 6–25) — subset in flux |
| Python lessons with broken code examples | 7 (hours 13, 14, 26, 28, 29, 35, 36, 38) |
| SQL lessons with schema-drift or broken SQL | ≥12 (02, 07, 08, 09, 10, 12, 13, 14, 15, 18, 19 + others) |
| Files with confirmed corrupted rename tokens | 7 (sql 06, 10, 17, 20, 23, 24; sql-filtering assignment) |
| SQL assignments that are generic template stubs | 25 (sql-06 … sql-30) |
| Orphaned assignment files | 2 (sql-filtering.html, sql-joins-report.html) |
| SQL lessons missing nav + assignment links | 5 (lessons 01–05) |
| Pages with meta descriptions | 0 |

**Top 5 improvement themes:**
1. Replace the 25 template-stub SQL assignments with real topic-specific exercises.
2. Establish one canonical hr.* schema and fix every SQL example (duplicate columns, phantom columns, broken FKs, no-op ALTER) against it.
3. Upgrade Python hours 6–25 to the modern lesson format (styled code, outputs, no diagram stubs) and fix the 8 broken code examples.
4. Repair rename/encoding corruption site-wide ("payrollsible", "HeadManagers", mojibake) and the garbled legacy SQL assignments.
5. Close navigation and metadata gaps: SQL 01–05 nav/assignment links, orphaned files, meta descriptions, "Sql"→"SQL" titles.


