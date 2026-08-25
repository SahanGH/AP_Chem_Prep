r"""Convert this project's Chapters\*.tex sources to student-edition HTML.

    python tools\tex2html.py                # all of Chapters\ -> Lessons\
    python tools\tex2html.py Chapters\chapter03-stoichiometry
    python tools\tex2html.py --no-figures   # skip TikZ rendering (faster)

Why a bespoke converter instead of latex2html / tex4ht / pandoc: the corpus
is machine-written against a closed vocabulary (apchem.sty + three classes,
about thirty constructs), so a translator that knows exactly those macros
produces clean semantic HTML, where generic tools choke on tcolorbox,
mhchem, and siunitx or emit unstylable tag soup.

Output:  Lessons\<chapter>\<stem>.html  (student edition: key-only content
removed, \selfcheck lines kept), plus Lessons\style.css and
Lessons\index.html. Chemistry and math render via MathJax + mhchem (CDN,
so pages need internet to display equations). TikZ figures are pre-rendered
to PNG through pdflatex + pdfcrop + MiKTeX Ghostscript (mgs).

A per-run report lands in Lessons\conversion-report.txt; any LaTeX command
the converter did not recognize is listed there. An empty report is the
done signal.
"""
import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Lessons"
OUT_MD = ROOT / "Lessons-md"

# Doc kinds that get answer-checking inputs and revealable explanations.
# Keyed on the stem suffix: "ch05-selfstudy" -> "selfstudy". Exams are
# deliberately absent -- self-grading defeats an assessment. Worksheets
# ("ws1".."ws4") are phase 2; adding them here is the whole switch.
EXPLAIN_KINDS = {"selfstudy", "selfstudy2"}
INTERACTIVE_KINDS = {"selfstudy", "selfstudy2"}

# Doc kinds whose scratch pads load the MathLive equation editor. It is
# ~1 MB, fetched lazily on the first focus of a pad, so a page nobody
# types maths into never pays for it. Keyed on kind rather than stem so
# new self-study files are covered without editing this.
MATHFIELD_KINDS = {"selfstudy", "selfstudy2"}


def _is_ws(kind: str) -> bool:
    return bool(re.fullmatch(r"ws\d+", kind))


# Notes and the examples sheet are fill-in documents too: their blanks
# carry real answers, they just group under headings rather than numbered
# problems. Exams stay out -- self-grading defeats an assessment.
FILLIN_KINDS = {"notes", "examples"}


def _is_fillin(kind: str) -> bool:
    return _is_ws(kind) or kind in FILLIN_KINDS


def wants(kind: str, base: set) -> bool:
    """Worksheets get the same treatment as self-study, matched by pattern
    rather than listed, so a future ws5 is not silently left out."""
    return kind in base or _is_fillin(kind)


def doc_kind(stem: str) -> str:
    return stem.split("-", 1)[1] if "-" in stem else stem


# ------------------------------------------------------------ tex utilities

def strip_comments(src: str) -> str:
    out = []
    for line in src.split("\n"):
        buf, i, saw_pct = [], 0, False
        while i < len(line):
            ch = line[i]
            if ch == "\\" and i + 1 < len(line):
                buf.append(line[i:i + 2]); i += 2; continue
            if ch == "%":
                saw_pct = True
                break
            buf.append(ch); i += 1
        text = "".join(buf)
        # A comment-only line contributes NOTHING in TeX -- the % eats the
        # newline too.  Emitting an empty line in its place turns a run of
        # comment lines into a \par, which is fatal inside a braced or
        # bracketed argument.  That is what killed fig-ch10-selfstudy-5:
        # its \begin{axis}[...] options carry a three-line comment, so the
        # figure silently vanished from the page instead of failing loudly.
        if saw_pct and not text.strip():
            continue
        out.append(text)
    return "\n".join(out)


def match_brace(src: str, i: int) -> int:
    """src[i] == '{'; return index just past the matching '}'."""
    depth, i0 = 0, i
    while i < len(src):
        ch = src[i]
        if ch == "\\":
            i += 2; continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError(f"unbalanced braces at {i0}: {src[i0:i0+60]!r}")


def match_bracket(src: str, i: int) -> int:
    """src[i] == '['; return index just past the matching ']' (skips {} groups)."""
    depth = 0
    while i < len(src):
        ch = src[i]
        if ch == "\\":
            i += 2; continue
        if ch == "{":
            i = match_brace(src, i); continue
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError("unbalanced brackets")


def take_args(src, i, n_opt=0, n_req=0):
    """Read up to n_opt [..] then n_req {..} starting at i. Returns (opts, reqs, i)."""
    opts, reqs = [], []
    for _ in range(n_opt):
        while i < len(src) and src[i] in " \n":
            i += 1
        if i < len(src) and src[i] == "[":
            j = match_bracket(src, i)
            opts.append(src[i + 1:j - 1]); i = j
        else:
            opts.append(None)
    for _ in range(n_req):
        while i < len(src) and src[i] in " \n":
            i += 1
        if i < len(src) and src[i] == "{":
            j = match_brace(src, i)
            reqs.append(src[i + 1:j - 1]); i = j
        else:
            reqs.append(""); break
    return opts, reqs, i


def sub_command(src, name, n_opt, n_req, fn):
    """Replace every \\name[opt]..{req}.. via fn(opts, reqs) -> str."""
    pat = re.compile(r"\\" + name + r"(?![a-zA-Z])")
    while True:
        m = pat.search(src)
        if not m:
            return src
        opts, reqs, end = take_args(src, m.end(), n_opt, n_req)
        src = src[:m.start()] + fn(opts, reqs) + src[end:]


def find_env(src, name):
    r"""Find the first \begin{name}..\end{name}, honouring NESTING of the same
    environment (enumerate inside enumerate is common here). Returns
    (start, end, opt, inner) or None."""
    b = re.search(r"\\begin\{" + re.escape(name) + r"\}", src)
    if not b:
        return None
    i = b.end()
    opt = None
    if i < len(src) and src[i] == "[":
        j = match_bracket(src, i)
        opt = src[i + 1:j - 1]; i = j
    inner_start = i
    depth = 1
    scan = re.compile(r"\\(begin|end)\{" + re.escape(name) + r"\}")
    while True:
        m = scan.search(src, i)
        if not m:
            raise ValueError(f"missing \\end{{{name}}}")
        depth += 1 if m.group(1) == "begin" else -1
        i = m.end()
        if depth == 0:
            return b.start(), m.end(), opt, src[inner_start:m.start()]


# ------------------------------------------------------------ siunitx units

UNIT = {
    "gram": "g", "mole": "mol", "litre": "L", "liter": "L", "second": "s",
    "kelvin": "K", "celsius": "&deg;C", "joule": "J", "Molar": "M",
    "atm": "atm", "torr": "torr", "mmHg": "mmHg", "pascal": "Pa",
    "meter": "m", "metre": "m", "minute": "min", "hour": "h",
    "ampere": "A", "coulomb": "C", "volt": "V", "electronvolt": "eV",
    "percent": "%", "u": "u", "atomicmassunit": "u",
    # \degree rendered as the literal word "degree" on every bond angle in
    # the corpus ("109.5 degree"); \molal is declared in shared/apchem.sty.
    "degree": "&deg;", "molal": "m",
}
PREFIX = {"kilo": "k", "milli": "m", "micro": "&micro;", "nano": "n",
          "centi": "c", "pico": "p"}
UNKNOWN_UNITS = set()


def expand_units(spec: str) -> str:
    r"""\gram\per\mole -> g/mol (HTML entities allowed)."""
    toks = re.findall(r"\\([a-zA-Z]+)|(squared|cubed)", spec)
    parts, per, prefix = [], False, ""
    for name, _ in toks:
        t = name or _
        if t == "per":
            per = True; continue
        if t in PREFIX:
            prefix = PREFIX[t]; continue
        if t == "squared":
            parts[-1] += "&sup2;"; continue
        if t == "cubed":
            parts[-1] += "&sup3;"; continue
        u = UNIT.get(t)
        if u is None:
            UNKNOWN_UNITS.add(t); u = t
        u = prefix + u
        prefix = ""
        parts.append(("/" if per else "") + u)
        per = False
    out = "".join(p if i == 0 else (p if p.startswith("/") else "&middot;" + p)
                  for i, p in enumerate(parts))
    return out


def convert_si(src: str, in_math: bool) -> str:
    def si(opts, reqs):
        val, spec = reqs
        u = expand_units(spec)
        if in_math:
            um = (u.replace("&deg;", r"{}^\circ ").replace("&micro;", r"\mu ")
                   .replace("&middot;", r"\cdot ").replace("&sup2;", "^2")
                   .replace("&sup3;", "^3").replace("%", r"\%"))
            return rf"{val}\,\mathrm{{{um}}}"
        return f"{val}&thinsp;{u}"

    def si1(opts, reqs):
        u = expand_units(reqs[0])
        if in_math:
            um = (u.replace("&deg;", r"{}^\circ ").replace("&micro;", r"\mu ")
                   .replace("&middot;", r"\cdot ").replace("&sup2;", "^2")
                   .replace("&sup3;", "^3").replace("%", r"\%"))
            return rf"\mathrm{{{um}}}"
        return u

    src = sub_command(src, "SI", 1, 2, si)
    src = sub_command(src, "si", 0, 1, si1)
    src = sub_command(src, "num", 0, 1, lambda o, r: r[0])
    return src


# ------------------------------------------------------------ figure render

# standalone crops to the drawing at the LaTeX level, so no pdfcrop (and no
# Perl, which this machine lacks) is needed. The tikz libraries must match
# shared\apchem.sty or positioning syntax like "above=of node" fails with a
# baffling "Unknown function `of'" from the PGF math parser.
FIGURE_PREAMBLE = r"""
\documentclass[border=4pt]{standalone}
\usepackage{tikz,pgfplots}
\usetikzlibrary{arrows.meta,positioning,patterns,calc}
\pgfplotsset{compat=1.18}
\usepackage{amsmath,amssymb}
\usepackage[version=4]{mhchem}
\usepackage{siunitx}
\usepackage{xcolor}
%s
\begin{document}
%s
\end{document}
"""


_MACROS = None


def project_macros() -> set:
    r"""Every macro name this project defines in shared\ -- \newcommand,
    \renewcommand, \DeclareRobustCommand, \newtcolorbox, \NewEnviron. These
    are exactly the names MathJax cannot know, so any of them surviving into
    a math span is a defect."""
    global _MACROS
    if _MACROS is None:
        _MACROS = set()
        for f in (ROOT / "shared").glob("*"):
            if f.suffix not in (".sty", ".cls"):
                continue
            txt = f.read_text(encoding="utf-8")
            _MACROS |= set(re.findall(
                r"\\(?:new|renew|provide)command\*?\{?\\([a-zA-Z@]+)", txt))
            _MACROS |= set(re.findall(r"\\DeclareRobustCommand\*?\{?\\([a-zA-Z@]+)",
                                      txt))
    return _MACROS


def palette_lines() -> str:
    """First (screen) palette block + any tikz/pgfplots styles from apchem.sty."""
    sty = (ROOT / "shared" / "apchem.sty").read_text(encoding="utf-8")
    lines, seen = [], set()
    for ln in sty.splitlines():
        s = ln.strip()
        m = re.match(r"\\definecolor\{(\w+)\}", s)
        if m and m.group(1) not in seen:
            seen.add(m.group(1))
            lines.append(re.sub(r"%.*", "", s))
        if re.match(r"\\(pgfplotsset|tikzset|pgfplotscreateplotcyclelist)", s):
            i = sty.find(ln)
            j = match_brace(sty, sty.index("{", i))
            lines.append(sty[i:j])
    return "\n".join(lines)


def render_figures(tex_path: Path, blocks, chapter_dir: Path, log):
    import shutil
    scratch = ROOT / "build" / "aux" / "tex2html"
    scratch.mkdir(parents=True, exist_ok=True)
    pal = palette_lines()
    names = []
    for k, block in enumerate(blocks, 1):
        name = f"fig-{tex_path.stem}-{k}"
        png = chapter_dir / f"{name}.png"
        names.append(png.name)
        if png.exists():
            continue
        job = scratch / f"{name}.tex"
        job.write_text(FIGURE_PREAMBLE % (pal, block), encoding="utf-8")
        pdf = scratch / f"{name}.pdf"
        if pdf.exists():
            pdf.unlink()
        # pdflatex exits nonzero on recoverable errors while still writing a
        # good PDF, so judge by the artifact, not the exit code.
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode",
                            f"-output-directory={scratch}", str(job)],
                           capture_output=True, cwd=scratch)
        if not pdf.exists():
            err = re.findall(r"^! .*", (r.stdout or b"").decode("utf8", "replace"),
                             re.M)
            log.append(f"  !! figure FAILED (pdflatex): {name}: "
                       f"{'; '.join(err[:2]) or 'no PDF produced'}")
            names[-1] = None
            continue
        r = subprocess.run(["mgs", "-q", "-dBATCH", "-dNOPAUSE", "-dSAFER",
                            "-sDEVICE=png16m", "-r200", "-dTextAlphaBits=4",
                            "-dGraphicsAlphaBits=4",
                            f"-sOutputFile={png}", str(pdf)],
                           capture_output=True, cwd=scratch)
        if not png.exists():
            log.append(f"  !! figure FAILED (ghostscript): {name}: "
                       f"{(r.stderr or b'')[-200:]}")
            names[-1] = None
            continue
        log.append(f"  figure rendered: {png.relative_to(OUT)}")
    return names


# ------------------------------------------------------------ the converter

MATH = []

# Commands that may sit INSIDE a math span but must become HTML, not math.
# \answerblank's argument is the answer, so the student edition discards it
# and emits an empty rule; \workspace and \answerlines are blank space by
# definition. Leaving any of these inside the stashed math is what makes
# MathJax print a red "\answerblank" -- the defect this exists to prevent.
# Blanks inside a math span are emitted here, not by the command table in
# convert_body, so this second implementation has to agree with it. It has
# no kind in scope, hence the module-level CURRENT_KIND -- the same pattern
# the MATH stash already uses. Getting this wrong left 54 blanks inert.
CURRENT_KIND = ""

ESCAPES = {
    "answerblank": (1, 1, lambda o, r: (
        f'<span class="blank" style="min-width:{o[0] or "4cm"}">'
        f'<span class="ansdata" hidden>{r[0]}</span></span>'
        if _is_fillin(CURRENT_KIND) else
        f'<span class="blank" style="min-width:{o[0] or "4cm"}"></span>')),
    "answerlines": (1, 1, lambda o, r:
                    '<div class="lines">' +
                    '<div class="rule"></div>' * (int(o[0]) if o[0] else 3) +
                    '</div>'),
    "workspace": (1, 0, lambda o, r:
                  f'<div class="workspace" style="height:{o[0] or "2cm"}"></div>'),
}
ESCAPE_RE = re.compile(r"\\(" + "|".join(ESCAPES) + r")(?![a-zA-Z])")


def stash_math(s: str) -> str:
    MATH.append(convert_si(s, in_math=True))
    return f"\x00M{len(MATH)-1}\x00"


def math_span(content: str, display: bool) -> str:
    r"""Turn one math span into HTML, splitting it around any embedded
    \answerblank / \workspace / \answerlines. A display span that contains a
    blank is emitted as inline pieces inside a centred div, so the line reads
    "M = ____" rather than breaking into two display blocks."""
    if not ESCAPE_RE.search(content):
        d = (r"\[", r"\]") if display else (r"\(", r"\)")
        return stash_math(d[0] + content + d[1])

    out, i = [], 0
    for m in ESCAPE_RE.finditer(content):
        if m.start() < i:
            continue
        name = m.group(1)
        n_opt, n_req, fn = ESCAPES[name]
        opts, reqs, end = take_args(content, m.end(), n_opt, n_req)
        chunk = content[i:m.start()].strip()
        if chunk:
            out.append(stash_math(r"\(" + chunk + r"\)"))
        out.append(fn(opts, reqs))
        i = end
    tail = content[i:].strip()
    if tail:
        out.append(stash_math(r"\(" + tail + r"\)"))
    html = " ".join(out)
    return f'<div class="center">{html}</div>' if display else html


def protect_math(src: str) -> str:
    while True:
        f = find_env(src, "align*")
        if not f:
            break
        a, b, _, inner = f
        src = (src[:a] +
               stash_math(r"\begin{align*}" + inner + r"\end{align*}") +
               src[b:])
    # The lookbehind matters: a line break with spacing, \\[0.3em], ends in a
    # "\[" that must NOT be read as display math -- doing so swallows
    # everything up to the next \], including \end{...} tokens.
    src = re.sub(r"(?<!\\)\\\[(.*?)\\\]",
                 lambda m: math_span(m.group(1), True), src, flags=re.S)
    src = re.sub(r"(?<!\\)\\\((.*?)\\\)",
                 lambda m: math_span(m.group(1), False), src, flags=re.S)
    src = re.sub(r"\$([^$]+)\$",
                 lambda m: math_span(m.group(1), False), src, flags=re.S)
    return src


def convert_ce(src: str) -> str:
    pat = re.compile(r"\\ce(?![a-zA-Z])")
    while True:
        m = pat.search(src)
        if not m:
            return src
        j = match_brace(src, src.index("{", m.end()))
        arg = src[src.index("{", m.end()) + 1:j - 1]
        src = src[:m.start()] + stash_math(rf"\(\ce{{{arg}}}\)") + src[j:]


def box(cls, title, inner):
    t = f'<div class="box-title">{title}</div>' if title else ""
    return f'\n<div class="box {cls}">{t}\n{inner}\n</div>\n'


def convert_tabular(inner: str) -> str:
    inner = re.sub(r"\\(toprule|bottomrule|midrule|hline)", "\x00RULE\x00", inner)
    rows_html, header_zone = [], True
    body = inner.strip()
    rows = re.split(r"\\\\", body)
    pending_rule = False
    first_rule_seen = False
    for row in rows:
        row = row.strip()
        has_rule = "\x00RULE\x00" in row
        row = row.replace("\x00RULE\x00", "").strip()
        if has_rule and rows_html:
            first_rule_seen = True
            header_zone = False
        if not row:
            continue
        cells = re.split(r"(?<!\\)&", row)
        tag = "th" if (header_zone and not first_rule_seen) else "td"
        tds = []
        for c in cells:
            c = c.strip()
            m = re.match(r"\\multicolumn\{(\d+)\}", c)
            span = ""
            if m:
                j = match_brace(c, c.index("{", m.end()))
                j2 = match_brace(c, c.index("{", j))
                span = f' colspan="{m.group(1)}"'
                c = c[c.index("{", j) + 1:j2 - 1]
            tds.append(f"<{tag}{span}>{c}</{tag}>")
        rows_html.append("<tr>" + "".join(tds) + "</tr>")
    return '\n<table>\n' + "\n".join(rows_html) + "\n</table>\n"


def convert_mcq(inner: str, n: int) -> str:
    i = inner.find(r"\choices")
    stem, rest = inner[:i], inner[i + len(r"\choices"):]
    items = []
    pat = re.compile(r"\\(choice|correct)(?![a-zA-Z])")
    while True:
        m = pat.search(rest)
        if not m:
            break
        j = match_brace(rest, rest.index("{", m.end()))
        items.append(rest[rest.index("{", m.end()) + 1:j - 1])
        rest = rest[j:]
    lis = "\n".join(f"<li>{c}</li>" for c in items)
    return (f'\n<div class="problem"><span class="qnum">{n}.</span> {stem}'
            f'\n<ol class="choices" type="A">\n{lis}\n</ol></div>\n')


def convert_body(body: str, meta: dict, fig_names, log, restore=True, kind=""):
    global CURRENT_KIND
    CURRENT_KIND = kind
    counters = {"problem": 0, "mcq": 0, "frq": 0, "fig": 0}

    # ---- drop key-only content ----
    while True:
        f = find_env(body, "rubric")
        if not f:
            break
        body = body[:f[0]] + body[f[1]:]
    drops = [("why", 0, 1), ("distractor", 0, 2),
             ("rpoint", 0, 2), ("examtotal", 0, 0)]
    if wants(kind, EXPLAIN_KINDS):
        # Keep the worked explanation; apcanswer (below) becomes the block
        # that add_interactivity() hides behind a button.
        body = sub_command(body, "keyonly", 0, 1, lambda o_, r_: r_[0])
    else:
        drops.insert(0, ("keyonly", 0, 1))
    for cmd, o, r in drops:
        body = sub_command(body, cmd, o, r, lambda o_, r_: "")

    # ---- math / chemistry / units ----
    body = protect_math(body)
    body = convert_ce(body)
    body = convert_si(body, in_math=False)

    # ---- figures ----
    def fig(o, r):
        counters["fig"] += 1
        name = fig_names[counters["fig"] - 1] if counters["fig"] <= len(fig_names) else None
        if name:
            return f'\n<figure><img src="{name}" alt="figure"></figure>\n'
        return '\n<p class="figure-missing">[figure — see the PDF edition]</p>\n'
    while True:
        f = find_env(body, "tikzpicture")
        if not f:
            break
        body = body[:f[0]] + fig(None, None) + body[f[1]:]

    # ---- mcq (before generic envs; owns its \choices) ----
    while True:
        f = find_env(body, "mcq")
        if not f:
            break
        counters["mcq"] += 1
        body = body[:f[0]] + convert_mcq(f[3], counters["mcq"]) + body[f[1]:]

    # ---- generic environments, innermost first ----
    ENV = {
        "apcanswer": lambda o, x: f'<div class="explain-body">{x}</div>',
        "workedexample": lambda o, x: box("we", o or "Worked example", x),
        "yourturn": lambda o, x: box("yt", o or "Your turn", x),
        "apcnote": lambda o, x: box("note", o or "Note", x),
        "apctrap": lambda o, x: box("trap", o or "AP trap", x),
        "warmup": lambda o, x: box("note", "Retrieval warm-up",
                                   f"<ol>{x}</ol>"),
        "exitticket": lambda o, x: box("note", "Exit ticket", x),
        "objectives": lambda o, x: box("note", "By the end you can\u2026",
                                       f"<ul>{x}</ul>"),
        "spiralstrip": lambda o, x: box("note", f"Spiral review \u2022 {o or ''}",
                                        f"<ol>{x}</ol>"),
        "parts": lambda o, x: f'<ol class="parts" type="a">{x}</ol>',
        "enumerate": lambda o, x: f"<ol>{x}</ol>",
        "itemize": lambda o, x: f"<ul>{x}</ul>",
        "center": lambda o, x: f'<div class="center">{x}</div>',
        "quote": lambda o, x: f"<blockquote>{x}</blockquote>",
        "tabular": lambda o, x: convert_tabular(x),
    }
    # spiralstrip/tabular take a {arg} not [opt]
    def env_pass(src):
        changed = False
        for name, fn in ENV.items():
            while True:
                f = find_env(src, name)
                if not f:
                    break
                a, b, opt, inner = f
                if name in ("spiralstrip", "tabular"):
                    inner2 = inner.lstrip()
                    if inner2.startswith("{"):
                        j = match_brace(inner2, 0)
                        opt, inner = inner2[1:j - 1], inner2[j:]
                if re.search(r"\\begin\{", inner) and name not in ("tabular",):
                    inner = env_pass(inner)
                src = src[:a] + fn(opt, inner) + src[b:]
                changed = True
        return src
    body = env_pass(body)

    # ---- commands ----
    def problem(o, r):
        counters["problem"] += 1
        return (f'\n<div class="problem"><span class="qnum">'
                f'{counters["problem"]}.</span> {r[0]}</div>\n')

    def frq(o, r):
        counters["frq"] += 1
        typ, pts = r[0], r[1]
        return (f'\n<h3 class="frq">Free-response {counters["frq"]} '
                f'\u2022 {typ} \u2022 {pts} points</h3>\n')

    def answerlines(o, r):
        n = int(o[0]) if o[0] else 3
        if _is_fillin(kind):
            # Ruled lines are for writing on paper. On screen they become a
            # real textarea, sized to the space the print version reserved.
            return (f'<textarea class="scratch" style="height:{n * 1.6:.1f}em"'
                    f' rows="{n}" spellcheck="false" aria-label="answer space"'
                    f' placeholder="your answer"></textarea>')
        return '<div class="lines">' + '<div class="rule"></div>' * n + '</div>'

    C = [
        ("problem", 1, 1, problem),
        ("answerblank", 1, 1,
         lambda o, r: (
             f'<span class="blank" style="min-width:{o[0] or "4cm"}">'
             f'<span class="ansdata" hidden>{r[0]}</span></span>'
             if _is_fillin(kind) else
             f'<span class="blank" style="min-width:{o[0] or "4cm"}"></span>')),
        ("answerlines", 1, 1, answerlines),
        ("workspace", 1, 0,
         lambda o, r: f'<div class="workspace" style="height:{o[0] or "2cm"}"></div>'),
        ("selfcheck", 0, 1,
         lambda o, r: f'<p class="selfcheck"><em>check:</em> {r[0]}</p>'),
        ("term", 0, 1, lambda o, r: f'<strong class="term">{r[0]}</strong>'),
        ("zsec", 0, 1, lambda o, r: f'<span class="badge">ZUM \u00a7{r[0]}</span>'),
        ("ced", 0, 1, lambda o, r: f'<span class="badge">CED {r[0]}</span>'),
        ("practice", 0, 1, lambda o, r: f'<span class="badge">SP {r[0]}</span>'),
        ("notesectionz", 0, 2,
         lambda o, r: f'<h3>{r[0]} <span class="badge">ZUM \u00a7{r[1]}</span></h3>'),
        ("notesection", 0, 2,
         lambda o, r: f'<h3>{r[0]} <span class="badge">CED {r[1]}</span></h3>'),
        ("notesub", 0, 1, lambda o, r: f"<h4>{r[0]}</h4>"),
        ("blocklesson", 0, 2,
         lambda o, r: f'<h2 class="block">{r[0]} <span class="sub">{r[1]}</span></h2>'),
        ("segment", 0, 3,
         lambda o, r: f'<h4 class="segment">{r[0]} \u2022 {r[2]} <span class="sub">{r[1]} min</span></h4>'),
        ("reading", 0, 2,
         lambda o, r: f'<p class="reading"><strong>Read:</strong> {r[0]} \u2022 PDF pp. {r[1]}</p>'),
        ("wsheader", 1, 0,
         lambda o, r: box("note", "Directions & data", o[0] or "")),
        ("apctitleblock", 0, 0, lambda o, r: ""),
        ("examsection", 0, 4,
         lambda o, r: f'<h2>Section {r[0]} \u2022 {r[1]} <span class="sub">{r[2]}</span></h2>'),
        ("frq", 0, 3, frq),
        ("nocalculator", 0, 0, lambda o, r: "NO CALCULATOR"),
        ("textbf", 0, 1, lambda o, r: f"<strong>{r[0]}</strong>"),
        ("textsc", 0, 1,
         lambda o, r: f'<span style="font-variant:small-caps">{r[0]}</span>'),
        ("emph", 0, 1, lambda o, r: f"<em>{r[0]}</em>"),
        ("textit", 0, 1, lambda o, r: f"<em>{r[0]}</em>"),
        ("texttt", 0, 1, lambda o, r: f"<code>{r[0]}</code>"),
        ("underline", 0, 1, lambda o, r: f"<u>{r[0]}</u>"),
        ("section", 0, 1, lambda o, r: f"<h2>{r[0]}</h2>"),
        ("subsection", 0, 1, lambda o, r: f"<h3>{r[0]}</h3>"),
        ("item", 1, 0, lambda o, r: "\n<li>" + (f"<strong>{o[0]}</strong> " if o[0] else "")),
        ("vspace", 1, 1, lambda o, r: ""),
        ("needspace", 0, 1, lambda o, r: ""),
        ("renewcommand", 0, 2, lambda o, r: ""),
        ("arraybackslash", 0, 0, lambda o, r: ""),
        ("raggedright", 0, 0, lambda o, r: ""),
        ("centerline", 0, 1, lambda o, r: f'<div class="center">{r[0]}</div>'),
    ]
    # \section*{..} -> strip the star first
    body = body.replace(r"\section*", r"\section")
    body = body.replace(r"\subsection*", r"\subsection")
    for name, no, nr, fn in C:
        body = sub_command(body, name, no, nr, fn)

    # \fbox{\parbox{w}{x}} -> callout
    def fbox(o, r):
        inner = r[0]
        m = re.match(r"\s*\\parbox\{[^}]*\}", inner)
        if m:
            j = match_brace(inner, inner.index("{", m.end()))
            inner = inner[inner.index("{", m.end()) + 1:j - 1]
        return f'<div class="fbox">{inner}</div>'
    body = sub_command(body, "fbox", 0, 1, fbox)

    # ---- simple textual replacements ----
    simple = [
        (r"\newline", "<br>"), (r"\checkmark", "\u2713"), (r"\hfill", " "),
        (r"\textbullet", "\u2022"), (r"\ldots", "\u2026"), (r"\dots", "\u2026"),
        (r"\%", "%"), (r"\&", "&amp;"), (r"\_", "_"), (r"\#", "#"),
        (r"\$", "$"), (r"\S", "\u00a7"), (r"\o ", "\u00f8"), (r"\o", "\u00f8"),
        (r"\,", "\u2009"), (r"\;", " "), (r"\!", ""), (r"\ ", " "),
        (r"\noindent", ""), (r"\centering", ""), (r"\sffamily", ""),
        (r"\footnotesize", ""), (r"\small", ""), (r"\itshape", ""),
        (r"\bfseries", ""), (r"\Large", ""), (r"\large", ""),
        (r"\clearpage", ""), (r"\newpage", ""), (r"\medskip", ""),
        (r"\smallskip", ""), (r"\bigskip", ""), (r"\quad", " &emsp; "),
        (r"\qquad", " &emsp;&emsp; "),
    ]
    for a, b in simple:
        body = body.replace(a, b)
    body = body.replace("---", "\u2014").replace("--", "\u2013")
    body = re.sub(r"``(.*?)''", "\u201c\\1\u201d", body, flags=re.S)
    body = body.replace("``", "\u201c").replace("''", "\u201d")
    body = re.sub(r"\\\\(\[[^\]]*\])?", "<br>", body)
    body = body.replace("~", "&nbsp;")

    # ---- audit ----
    # Outside math: anything still backslashed was not translated.
    for cmd in sorted(set(re.findall(r"\\[a-zA-Z]+", body))):
        log.append(f"  ?? unconverted: {cmd}")
    # Inside math: MathJax knows TeX and mhchem but nothing about THIS
    # project's macros, and renders an unknown one as red error text.
    # Auditing only outside math is how a red \answerblank reached 54 pages.
    # The watch list is read from shared\ so it can never drift out of date.
    for chunk in MATH:
        for cmd in sorted(set(re.findall(r"\\[a-zA-Z]+", chunk))):
            if cmd[1:] in project_macros():
                log.append(f"  ?? project macro inside math: {cmd}")

    # strip remaining lone braces
    body = re.sub(r"(?<!\\)[{}]", "", body)

    # ---- paragraphs ----
    BLOCK_TAGS = ("<div", "<ol", "<ul", "<table", "<h2", "<h3", "<h4",
                  "<figure", "<blockquote", "<li")
    blocks_out = []
    for chunk in re.split(r"\n\s*\n", body):
        c = chunk.strip()
        if not c:
            continue
        if c.startswith(("<", "\x00")) or any(t in c for t in BLOCK_TAGS):
            blocks_out.append(c)
        else:
            blocks_out.append(f"<p>{c}</p>")
    body = "\n\n".join(blocks_out)

    # ---- restore math (callers may defer, to render per output format) ----
    if restore:
        body = re.sub(r"\x00M(\d+)\x00", lambda m: MATH[int(m.group(1))], body)
    return body


# ------------------------------------------------- answer checking (HTML)
#
# Self-study ladders already print their answers in a gray \selfcheck line,
# so making them checkable exposes nothing new -- it just replaces an
# honour-system glance with a real self-test. The pairing rule: the N
# \workspace slots between one \selfcheck and the previous one are that
# ladder's N questions, matched in order to the (a)..(d) parts of the check
# line. If the counts disagree we leave the ladder alone and log it rather
# than guess -- a mispaired answer is worse than no answer.

# "950." is three significant figures, not "950" followed by a stray
# period -- the trailing point must be part of the number.
NUM = r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?"
SELFCHECK_RE = re.compile(r'<p class="selfcheck"><em>check:</em>(.*?)</p>', re.S)
WORKSPACE_RE = re.compile(r'<div class="workspace" style="height:([^"]*)"></div>')
PART_RE = re.compile(r"\(([a-h])\)")
ENTS = {"&thinsp;": " ", "&emsp;": " ", "&ensp;": " ", "&nbsp;": " ",
        "&times;": " x ", "&minus;": "-", "&deg;": " deg", "&amp;": "&",
        "&lt;": "<", "&gt;": ">", "&mdash;": "-", "&ndash;": "-"}


def clean_answer(h: str) -> str:
    """HTML fragment -> flat text suitable for parsing/compare."""
    h = re.sub(r"\\\((.*?)\\\)", r"\1", h, flags=re.S)   # inline math -> content
    h = re.sub(r"\\mathrm\{(.*?)\}", r"\1", h)
    h = re.sub(r"\\text\{(.*?)\}", r"\1", h)
    h = re.sub(r"<[^>]+>", "", h)
    for a, b in ENTS.items():
        h = h.replace(a, b)
    return re.sub(r"\s+", " ", h).strip()


def sigfigs(s: str) -> int:
    """Significant digits of a number as written. Trailing zeros with no
    decimal point are treated as not significant (1900 -> 2)."""
    s = s.strip().lstrip("+-")
    if "e" in s.lower():
        s = re.split(r"[eE]", s)[0]
    if "." in s:
        digits = s.replace(".", "").lstrip("0")
        return len(digits) if digits else 1
    digits = s.lstrip("0")
    return len(digits.rstrip("0")) or 1


# Unit symbols that may legitimately trail a numeric answer.  The old test
# was a permissive character class, which happily read the tail of an
# EXPRESSION as a unit: "4s^3" became value 4.0 unit "s^3", "3/2" became
# value 3.0 unit "/2", "10^5" became value 10.0 unit "^5".  Each of those
# published a checker that marks the correct answer wrong -- a student
# entering the real bond order 1.5 was told they were incorrect.  Anything
# not on this list now means "not a plain number", so the item falls back
# to Show-answer, which is this file's stated safe default.
UNIT_SYMBOLS = {
    "g", "kg", "mg", "ng", "m", "cm", "mm", "nm", "pm", "km",
    "L", "mL", "s", "ms", "min", "h", "mol", "mmol", "M", "K",
    "J", "kJ", "V", "A", "C", "atm", "torr", "Pa", "kPa", "mmHg",
    "u", "eV", "ppm", "particles", "particle", "mole", "moles",
    "%", "degC", "&deg;C", "°C", "&deg;", "°",
    "&micro;g", "&micro;m", "&micro;L",
}


def is_unit(unit: str) -> bool:
    """True if `unit` is a plausible unit rather than the tail of an
    expression.  Empty and "-" (dimensionless) count as units."""
    u = unit.strip()
    if u in ("", "-"):
        return True
    # An ASCII caret is always an exponent, never a unit: s^3, ^5, 2p^6.
    if "^" in u:
        return False
    for sup in ("&sup2;", "&sup3;", "²", "³"):
        u = u.replace(sup, "")
    parts = [p.strip() for p in re.split(r"[/·]|&middot;", u)]
    if not any(parts):
        return False
    return all(p in UNIT_SYMBOLS for p in parts if p)


def numeric_spec(text: str):
    """Return {value, unit, sig} if `text` is a number (optionally with a
    unit or written in scientific notation), else None."""
    t = text.strip().rstrip(".").strip()
    m = re.fullmatch(r"(" + NUM + r")\s*(?:\\times|x|\u00d7|\*)\s*10\^?\{?([-+]?\d+)\}?\s*(.*)",
                     t)
    if m:
        unit = m.group(3).strip()
        if is_unit(unit):
            return {"value": float(m.group(1)) * (10 ** int(m.group(2))),
                    "unit": unit, "sig": sigfigs(m.group(1))}
        return None
    m = re.fullmatch(r"(" + NUM + r")\s*(.*)", t)
    if m:
        unit = m.group(2).strip()
        if is_unit(unit):
            return {"value": float(m.group(1)), "unit": unit,
                    "sig": sigfigs(m.group(1))}
    return None


def parse_selfcheck(inner: str):
    """Check-line HTML -> [(label, display_html, spec_or_None)]."""
    # Only count (a),(b),(c)... running in sequence. Answers cross-reference
    # each other ("(d) only (a) is at STP"), and a naive split turns that
    # citation into a fifth part.
    marks = []
    for m in PART_RE.finditer(inner):
        if m.group(1) == chr(ord("a") + len(marks)):
            marks.append(m)
    chunks = []
    if marks:
        for k, m in enumerate(marks):
            end = marks[k + 1].start() if k + 1 < len(marks) else len(inner)
            chunks.append((m.group(1), inner[m.end():end]))
    else:
        chunks.append(("", inner))
    out = []
    for label, frag in chunks:
        # Trailing separators (\quad -> &emsp;) are layout, not answer. Strip
        # them as whole entities: a bare .strip(";") bites the semicolon off
        # "&emsp;" and leaves "&emsp" glued to the answer, which then fails
        # to parse as a number.
        frag = re.sub(r"(?:&(?:emsp|ensp|nbsp|thinsp|quad);|\s)+$", "", frag)
        disp = frag.strip().rstrip(",").strip()
        out.append((label, disp, numeric_spec(clean_answer(disp))))
    return out


def esc_attr(s: str) -> str:
    return (s.replace("&", "&amp;").replace('"', "&quot;")
             .replace("<", "&lt;").replace(">", "&gt;"))


def scratch(height: str) -> str:
    r"""\workspace is handwriting space in the PDF. On screen an empty dashed
    div is dead weight -- you cannot write in it -- so it becomes a real
    textarea. Scratch only: nothing reads it, and it clears on reload."""
    return (f'<textarea class="scratch" style="height:{height}" rows="2"'
            f' spellcheck="false" aria-label="working space"'
            f' placeholder="working (optional)"></textarea>')


def answer_row(label: str, disp: str, spec) -> str:
    # The (a)..(d) letters drive pairing with the check line, but the
    # questions are already numbered, so showing them again is duplicate
    # labelling. Keep them for screen readers only.
    n = ord(label) - ord("a") + 1 if label else 0
    aria = f"answer to question {n}" if n else "answer"
    if spec is not None:
        data = (f' data-check="num" data-val="{spec["value"]!r}"'
                f' data-sig="{spec["sig"]}"'
                f' data-unit="{esc_attr(spec["unit"])}"')
        btn = '<button class="anscheck" type="button">Check</button>'
        rev = ""
    else:
        # Prose, ratios, comparisons -- no reliable machine check. Offer the
        # answer, never a verdict: a wrong "incorrect" costs more than none.
        # It goes in the DOM rather than an attribute so MathJax typesets the
        # \ce{} formulas instead of showing raw LaTeX.
        data = ' data-check="none"'
        btn = '<button class="ansshow" type="button">Show answer</button>'
        rev = f'<span class="ansreveal" hidden>{disp}</span>'
    return (f'<div class="ansrow">'
            f'<input type="text" class="ansinput" autocomplete="off"'
            f' aria-label="{aria}" placeholder="your answer"{data}>'
            f'{btn}<span class="ansfeedback" role="status"></span>{rev}</div>')


def reveal(button: str, inner: str, cls: str) -> str:
    return (f'<div class="reveal"><button class="reveal-btn" type="button"'
            f' aria-expanded="false" data-show="Show {button}"'
            f' data-hide="Hide {button}">Show {button}</button>'
            f'<div class="reveal-body {cls}" hidden>{inner}</div></div>')


def find_div(s: str, start: int) -> int:
    """Index just past the </div> closing the <div ...> that starts at
    `start`. Counts nested divs."""
    i = s.index(">", start) + 1
    depth = 1
    while depth and i < len(s):
        nxt = s.find("<div", i)
        end = s.find("</div>", i)
        if end == -1:
            return len(s)
        if nxt != -1 and nxt < end:
            depth += 1
            i = nxt + 4
        else:
            depth -= 1
            i = end + 6
    return i


def wrap_explanations(body: str) -> str:
    """<div class="explain-body">X</div> -> collapsed reveal block."""
    while True:
        m = re.search(r'<div class="explain-body">', body)
        if not m:
            return body
        end = find_div(body, m.start())
        inner = body[m.end():end - 6]
        body = body[:m.start()] + reveal("explanation", inner, "explain") + body[end:]


# ---------------------------------------------- worksheets (HTML)
#
# Worksheets carry their answer inside \answerblank{...} itself, so unlike
# the self-study ladders there is nothing to pair -- each blank already
# knows what it is worth. The answer rides through conversion as a hidden
# span rather than an attribute, so math and \ce{} survive the restore
# pass intact and can be shown rendered rather than as raw LaTeX.
#
# Blanks check on Enter or on leaving the field; there is no button per
# blank, because 1044 of them would drown the page. Answers are revealed a
# problem at a time, matching the rhythm of working through a worksheet.

BLANK_RE = re.compile(
    r'<span class="blank" style="min-width:([^"]*)">'
    r'<span class="ansdata" hidden>(.*?)</span></span>', re.S)
PROBLEM_RE = re.compile(r'<div class="problem">')
# Notes have no numbered problems; their natural unit is the heading a
# group of blanks sits under (about two blanks each, close to the 2.6 a
# worksheet problem carries).
SECTION_RE = re.compile(r'<h[34][^>]*>')


def group_re(kind: str):
    return PROBLEM_RE if _is_ws(kind) else SECTION_RE


def blank_input(width: str, disp: str, grp: int) -> str:
    spec = numeric_spec(clean_answer(disp))
    if spec is not None:
        data = (f' data-check="num" data-val="{spec["value"]!r}"'
                f' data-sig="{spec["sig"]}"'
                f' data-unit="{esc_attr(spec["unit"])}"')
    else:
        data = ' data-check="none"'
    return (f'<span class="blankwrap">'
            f'<input type="text" class="ansinput blank-in"'
            f' style="width:{width}" autocomplete="off"'
            f' aria-label="answer"{data}>'
            f'<span class="ansfeedback" role="status"></span>'
            f'<span class="ansreveal" hidden data-grp="{grp}">{disp}</span>'
            f'</span>')


def reveal_blanks_button(grp: int) -> str:
    return ('<div class="reveal"><button class="reveal-btn revealblanks"'
            f' type="button" aria-expanded="false" data-grp="{grp}"'
            ' data-show="Show answers" data-hide="Hide answers">'
            'Show answers</button></div>')


def fillin_pass(body: str, kind: str) -> str:
    """Turn every \answerblank into a checkable field, grouped so answers
    reveal a problem (or a heading) at a time rather than all at once."""
    # Region boundaries INCLUDE the text before the first heading. Notes
    # open with blanks in a warm-up box above any h3, and treating that as
    # dead space left them inert with their answers still in the markup.
    bounds = [0] + [m.start() for m in group_re(kind).finditer(body)] + [len(body)]
    out, grp = [], 0
    for i in range(len(bounds) - 1):
        seg = body[bounds[i]:bounds[i + 1]]
        if not seg:
            continue
        grp += 1
        found = [0]

        def rep(m, grp=grp, found=found):
            found[0] += 1
            return blank_input(m.group(1), m.group(2), grp)

        seg = BLANK_RE.sub(rep, seg)
        if found[0]:
            seg += reveal_blanks_button(grp)
        out.append(seg)
    return "".join(out)


def number_pads(body: str, stem: str, math_on: bool) -> str:
    """Give every scratch pad a stable id so its contents can be restored on
    a later visit, and flag the ones that may upgrade to an equation editor.
    Runs last, in document order: the pairing loop rewrites regions back to
    front, so ids assigned there would come out reversed."""
    n = [0]

    def tag(m):
        n[0] += 1
        extra = f' data-pad="{stem}:{n[0]}"'
        if math_on:
            extra += ' data-math="1"'
        return m.group(0)[:-1] + extra + ">"

    return re.sub(r'<textarea class="scratch[^"]*"[^>]*>', tag, body)


def add_interactivity(body: str, kind: str, stem: str, log) -> str:
    if not wants(kind, INTERACTIVE_KINDS):
        return body
    out, pos, paired, skipped = [], 0, 0, 0
    for m in SELFCHECK_RE.finditer(body):
        region = body[pos:m.start()]
        answers = parse_selfcheck(m.group(1))
        slots = list(WORKSPACE_RE.finditer(region))
        if answers and len(slots) == len(answers):
            for k in range(len(slots) - 1, -1, -1):      # back to front
                sl = slots[k]
                label, disp, spec = answers[k]
                region = (region[:sl.start()] + scratch(sl.group(1))
                          + answer_row(label, disp, spec) + region[sl.end():])
            paired += len(answers)
        elif answers:
            skipped += 1
            log.append(f"  ?? check line with {len(answers)} parts but "
                       f"{len(slots)} workspace slots -- left non-interactive")
        out.append(region)
        out.append(reveal("answers", f'<p class="selfcheck">{m.group(1)}</p>',
                          "answers"))
        pos = m.end()
    out.append(body[pos:])
    # Ladders we declined to pair still get usable working space, so the
    # page does not mix live textareas with inert dashed boxes.
    body = WORKSPACE_RE.sub(lambda m: scratch(m.group(1)), "".join(out))
    if _is_fillin(kind):
        body = fillin_pass(body, kind)
    body = number_pads(body, stem, wants(kind, MATHFIELD_KINDS))
    return wrap_explanations(body)


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="../style.css?v={assetv}">
<script>
MathJax = {{ loader: {{ load: ['[tex]/mhchem'] }},
  tex: {{ packages: {{'[+]': ['mhchem']}},
         inlineMath: [['\\\\(', '\\\\)']] }} }};
</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
<script defer src="../lessons.js?v={assetv}"></script>
</head>
<body>
<header>
  <p class="crumb"><a href="../index.html">AP Chemistry lessons</a></p>
  <p class="unit">{unitword} {unit} \u2022 {unittitle}</p>
  <h1>{doctitle}</h1>
  <p class="subtitle">{subtitle}</p>
</header>
<main>
{body}
</main>
<footer><p>AP Chemistry course materials \u2022 student edition \u2022
CC BY-NC-SA 4.0</p></footer>
</body>
</html>
"""


def get_meta(src: str) -> dict:
    def grab(cmd, default=""):
        m = re.search(r"\\" + cmd + r"\{", src)
        if not m:
            return default
        j = match_brace(src, m.end() - 1)
        return src[m.end():j - 1]
    return {
        "unitword": grab("apcunitword", "Chapter"),
        "unit": grab("apcunit"),
        "unittitle": grab("apcunittitle"),
        "doctitle": grab("apcdoctitle"),
        "subtitle": grab("apcsubtitle"),
    }


def clean_meta(s: str) -> str:
    s = s.replace(r"\textbullet", "\u2022").replace(r"\S", "\u00a7")
    s = re.sub(r"\\ce\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    s = s.replace("\\ ", " ").replace("\\,", " ").replace("\\", "")
    s = s.replace("~", " ").replace("{", "").replace("}", "")
    s = s.replace("---", "\u2014").replace("--", "\u2013")
    return re.sub(r"\s+", " ", s).strip()


def convert_file(tex_path: Path, no_figures: bool, log, fmt="both"):
    global MATH
    MATH = []
    src = strip_comments(tex_path.read_text(encoding="utf-8"))
    meta = {k: clean_meta(v) for k, v in get_meta(src).items()}
    m = re.search(r"\\begin\{document\}(.*)\\end\{document\}", src, re.S)
    body = m.group(1)

    rel = tex_path.relative_to(ROOT / "Chapters")
    chapter_dir = OUT / rel.parts[0]
    chapter_dir.mkdir(parents=True, exist_ok=True)

    fig_blocks = []
    pos = 0
    probe = body
    while True:
        f = find_env(probe, "tikzpicture")
        if not f:
            break
        fig_blocks.append(r"\begin{tikzpicture}" + f[3] + r"\end{tikzpicture}")
        probe = probe[f[1]:]
    fig_names = []
    if fig_blocks and not no_figures:
        fig_names = render_figures(tex_path, fig_blocks, chapter_dir, log)
    elif fig_blocks:
        fig_names = [None] * len(fig_blocks)

    # convert_body leaves \x00Mn\x00 placeholders; render them per format.
    kind = doc_kind(tex_path.stem)
    raw = convert_body(body, meta, fig_names, log, restore=False, kind=kind)
    title = f"{meta['unitword']} {meta['unit']} \u2022 {meta['doctitle']}"
    stash = list(MATH)

    out = None
    if fmt in ("html", "both"):
        html_body = re.sub(r"\x00M(\d+)\x00",
                           lambda m: stash[int(m.group(1))], raw)
        html_body = add_interactivity(html_body, kind, tex_path.stem, log)
        out = chapter_dir / (tex_path.stem + ".html")
        out.write_text(PAGE.format(title=title, body=html_body, assetv=ASSET_V, **meta),
                       encoding="utf-8")
    if fmt in ("md", "both"):
        md_dir = OUT_MD / rel.parts[0]
        md_dir.mkdir(parents=True, exist_ok=True)
        html_for_md = re.sub(r"\x00M(\d+)\x00",
                             lambda m: math_to_md(stash[int(m.group(1))]), raw)
        page = PAGE.format(title=title, body=html_for_md, assetv=ASSET_V, **meta)
        md = html_to_md(page, meta)
        md_out = md_dir / (tex_path.stem + ".md")
        md_out.write_text(md, encoding="utf-8")
        for png in chapter_dir.glob("*.png"):
            tgt = md_dir / png.name
            if not tgt.exists() or tgt.stat().st_mtime < png.stat().st_mtime:
                tgt.write_bytes(png.read_bytes())
        out = out or md_out
    return out, meta


CSS = """
:root { --accent:#1F4E79; --ans:#9E2A2B; --gray:#5A5A5A; --light:#EEF3F8;
        --rule:#BFC9D4; --warn:#8A6D1F; --warnbg:#FDF6E3; }
* { box-sizing: border-box; }
body { font-family: Georgia, 'Times New Roman', serif; line-height: 1.75;
       margin: 0; color: #1a1a1a; background: #fff; }
header, main, footer { max-width: 52rem; margin: 0 auto; padding: 0 1.2rem; }
header { border-bottom: 3px solid var(--accent); padding-top: 1.2rem;
         padding-bottom: .8rem; }
header .crumb a { color: var(--gray); font-size: .85rem;
                  font-family: system-ui, sans-serif; text-decoration: none; }
header .unit { color: var(--accent); font-family: system-ui, sans-serif;
               font-weight: 600; margin: .4rem 0 0; }
header h1 { margin: .1rem 0; font-family: system-ui, sans-serif; }
header .subtitle { color: var(--gray); margin: 0 0 .4rem; }
main { padding-top: 1rem; padding-bottom: 3rem; }
h2 { font-family: system-ui, sans-serif; color: var(--accent);
     border-bottom: 1px solid var(--rule); padding-bottom: .2rem;
     margin-top: 2rem; }
h2.block { background: var(--accent); color: #fff; padding: .45rem .7rem;
           border-radius: 4px; border: none; }
h2 .sub, h3 .sub, h4 .sub { font-weight: 400; font-size: .8em;
           color: inherit; opacity: .85; }
h3, h4 { font-family: system-ui, sans-serif; margin-top: 1.4rem; }
h4.segment { background: var(--light); padding: .3rem .6rem;
             border-left: 4px solid var(--accent); }
.badge { font-family: system-ui, sans-serif; font-size: .72rem;
         background: var(--light); color: var(--accent);
         border: 1px solid var(--rule); border-radius: 999px;
         padding: .05rem .55rem; vertical-align: middle;
         white-space: nowrap; }
.box { border: 1px solid var(--rule); border-radius: 6px;
       margin: 1.1rem 0; padding: .2rem .9rem .6rem; }
.box-title { font-family: system-ui, sans-serif; font-weight: 700;
             font-size: .85rem; letter-spacing: .02em;
             margin: .5rem 0 .4rem; }
.box.we { border-color: var(--gray); }
.box.we .box-title { color: #fff; background: var(--gray);
     margin: .55rem -0.9rem .5rem; padding: .3rem .9rem;
     border-radius: 5px 5px 0 0; margin-top: -1px; }
.box.yt { border: 1.5px dashed var(--gray); }
.box.yt .box-title { color: var(--accent); }
.box.note { background: var(--light); border-color: var(--accent); }
.box.trap { background: var(--warnbg); border-color: var(--warn); }
.box.trap .box-title { color: var(--warn); }
.problem { margin: 1rem 0 .3rem; }
.qnum { font-weight: 700; font-family: system-ui, sans-serif; }
li { margin: .4rem 0; }
li > ol, li > ul { margin-top: .35rem; }
p { margin: .9rem 0; }
ol.parts { list-style-type: lower-alpha; }
ol.choices { list-style-type: upper-alpha; }
.blank { display: inline-block; border-bottom: 1px solid #333;
         min-height: 1.1em; vertical-align: bottom; }
.lines .rule { border-bottom: 1px solid #999; height: 1.7em; }
.workspace { border: 1px dashed var(--rule); border-radius: 4px;
             margin: .4rem 0; }
.selfcheck { color: var(--gray); font-size: .92rem; font-style: italic;
             border-top: 1px dotted var(--rule); padding-top: .3rem; }
.center { text-align: center; }
.fbox { border: 1.5px solid #333; padding: .5rem .9rem; margin: 1rem auto;
        max-width: 85%; text-align: center; }
table { border-collapse: collapse; margin: 1rem auto; }
th, td { padding: .3rem .7rem; text-align: left;
         border-bottom: 1px solid var(--rule); }
th { border-bottom: 2px solid var(--accent);
     font-family: system-ui, sans-serif; }
figure { text-align: center; margin: 1.2rem 0; }
figure img { max-width: 100%; height: auto; }
blockquote { border-left: 4px solid var(--rule); margin-left: 0;
             padding-left: 1rem; color: var(--gray); }
footer { border-top: 1px solid var(--rule); color: var(--gray);
         font-size: .85rem; font-family: system-ui, sans-serif; }
.figure-missing { color: var(--gray); font-style: italic; }
@media print { .selfcheck { display: none; } }

/* --- answer checking (screen only; print keeps the blank workspace) --- */
.scratch { display: block; width: 100%; box-sizing: border-box;
           margin: .3rem 0 .15rem; padding: .45rem .6rem;
           border: 1px dashed var(--rule); border-radius: 4px;
           font: inherit; font-size: .95rem; color: inherit; background: #fff;
           resize: vertical; min-height: 2.2rem; }
.scratch:focus { outline: 2px solid var(--accent); outline-offset: 1px;
                 border-style: solid; }
.scratch::placeholder { color: var(--gray); opacity: .55; }
math-field.mathfield { display: block; width: 100%; box-sizing: border-box;
    margin: .3rem 0 .15rem; padding: .35rem .5rem;
    border: 1px solid var(--accent); border-radius: 4px; background: #fff;
    font-size: 1.05rem; }
math-field.mathfield:focus { outline: 2px solid var(--accent);
    outline-offset: 1px; }
.ansrow { display: flex; flex-wrap: wrap; align-items: center; gap: .5rem;
          margin: .4rem 0 .9rem; font-family: system-ui, sans-serif; }
.ansinput { flex: 1 1 11rem; max-width: 16rem; padding: .35rem .5rem;
            border: 1px solid var(--rule); border-radius: 4px;
            font: inherit; font-size: 1rem; background: #fff; color: inherit; }
.ansinput:focus { outline: 2px solid var(--accent); outline-offset: 1px; }
.ansinput.ok { border-color: #2E7D32; background: #F1F8F2; }
.ansinput.no { border-color: var(--ans); background: #FDF3F3; }
.ansinput.warn { border-color: var(--warn); background: #FDF9EE; }
.anscheck, .ansshow, .reveal-btn {
    font-family: system-ui, sans-serif; font-size: .82rem;
    padding: .32rem .75rem; border: 1px solid var(--rule);
    border-radius: 999px; background: var(--light); color: var(--accent);
    cursor: pointer; }
.anscheck:hover, .ansshow:hover, .reveal-btn:hover { background: #E2EBF5; }
.anscheck:focus-visible, .ansshow:focus-visible, .reveal-btn:focus-visible {
    outline: 2px solid var(--accent); outline-offset: 2px; }
.blankwrap { display: inline-flex; align-items: baseline; gap: .3rem;
             flex-wrap: wrap; margin: .15rem 0; }
.blank-in { flex: none; min-width: 0; padding: .15rem .4rem;
            font-size: .95rem; }
.blankwrap .ansfeedback { font-size: .78rem; }
.ansfeedback { font-size: .85rem; font-family: system-ui, sans-serif; }
.ansfeedback.ok { color: #2E7D32; font-weight: 600; }
.ansfeedback.no { color: var(--ans); }
.ansfeedback.hint { color: var(--warn); }
.ansreveal { font-size: .9rem; color: var(--ans);
             font-family: system-ui, sans-serif; }
.reveal { margin: .6rem 0 1rem; }
.reveal-body { margin-top: .5rem; padding: .6rem .85rem;
               border-left: 3px solid var(--rule); background: var(--light);
               border-radius: 0 4px 4px 0; }
.reveal-body .selfcheck { display: block; margin: 0; }
@media print { .ansrow, .reveal-btn, .reveal-body { display: none; } }
"""


# ------------------------------------------------------- HTML -> Markdown
# Translating our own generated HTML is safe for the same reason the LaTeX
# converter is: the vocabulary is closed, because this file emitted it.

SUB = str.maketrans("0123456789", "\u2080\u2081\u2082\u2083\u2084\u2085"
                                  "\u2086\u2087\u2088\u2089")
SUP = str.maketrans("0123456789+-", "\u2070\u00b9\u00b2\u00b3\u2074\u2075"
                                    "\u2076\u2077\u2078\u2079\u207a\u207b")


LESSONS_JS = r"""/* Answer checking for the self-study ladders. Generated by
   tools/tex2html.py -- edit that, not this file.

   Deliberately forgiving: a student who has the chemistry right should not
   lose the exchange to formatting. Units are optional, commas and spaces in
   numbers are ignored, and scientific notation is accepted in three
   spellings. Significant figures never make an answer wrong -- they earn a
   nudge, because this is practice material, not the exam. */
(function () {
  "use strict";
  var TOL = 0.01;                       // 1% relative tolerance

  function sigfigs(s) {
    s = String(s).trim().replace(/^[+-]/, "");
    if (/e/i.test(s)) s = s.split(/e/i)[0];
    if (s.indexOf(".") >= 0) {
      return s.replace(".", "").replace(/^0+/, "").length || 1;
    }
    return s.replace(/^0+/, "").replace(/0+$/, "").length || 1;
  }

  /* First number in free text: "1900", "1,900 torr", "1.9e3", "1.2 x 10^24" */
  function parseEntry(raw) {
    var t = String(raw).trim().replace(/,/g, "");
    var m = t.match(/^([+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)\s*(?:x|X|\*|\u00d7)\s*10\s*\^?\s*\{?([+-]?\d+)\}?\s*(.*)$/);
    if (m) {
      return { value: parseFloat(m[1]) * Math.pow(10, parseInt(m[2], 10)),
               sig: sigfigs(m[1]), unit: m[3].trim() };
    }
    m = t.match(/^([+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)\s*(.*)$/);
    if (m) {
      return { value: parseFloat(m[1]), sig: sigfigs(m[1]), unit: m[2].trim() };
    }
    return null;
  }

  function normUnit(u) {
    return String(u).toLowerCase().replace(/[.\s]/g, "")
             .replace(/^degrees?/, "deg").replace(/celcius$/, "celsius");
  }

  function feedback(el, cls, msg) {
    el.className = "ansfeedback " + cls;
    el.textContent = msg;
  }

  function check(input) {
    var fb = input.parentNode.querySelector(".ansfeedback");
    var raw = input.value.trim();
    input.classList.remove("ok", "no", "warn");
    if (!raw) { feedback(fb, "", ""); return; }

    var got = parseEntry(raw);
    if (!got) { feedback(fb, "hint", "enter a number"); return; }

    var exp = parseFloat(input.getAttribute("data-val"));
    var expSig = parseInt(input.getAttribute("data-sig"), 10);
    var expUnit = (input.getAttribute("data-unit") || "").trim();
    var rel = Math.abs(got.value - exp) / Math.max(Math.abs(exp), 1e-12);

    if (rel > TOL) {
      input.classList.add("no");
      feedback(fb, "no", "not right \u2014 try again");
      return;
    }
    /* Right number, wrong unit is not "correct" -- but calling it wrong
       would punish a student who typed "atmospheres" for "atm". Third
       state: neither green nor red, and name the unit we wanted. */
    if (expUnit && got.unit && normUnit(got.unit) !== normUnit(expUnit)) {
      input.classList.add("warn");
      feedback(fb, "hint",
               "right number \u2014 check your units (expected " + expUnit + ")");
      return;
    }
    input.classList.add("ok");
    /* Sig figs nudge only when the value was ROUNDED differently. An exact
       match written to more places (1.90e3 for 1900) is not an error. */
    if (rel > 1e-9 && got.sig !== expSig) {
      feedback(fb, "hint", "correct \u2014 check your significant figures");
    } else {
      feedback(fb, "ok", "correct");
    }
  }

  function showAnswer(row) {
    var rev = row.querySelector(".ansreveal");
    if (rev) { rev.removeAttribute("hidden"); }
  }

  document.addEventListener("click", function (e) {
    var t = e.target;
    if (!t.classList) { return; }
    if (t.classList.contains("anscheck")) {
      check(t.parentNode.querySelector(".ansinput"));
    } else if (t.classList.contains("ansshow")) {
      showAnswer(t.parentNode);
    } else if (t.classList.contains("revealblanks")) {
      /* Worksheet answers are revealed a problem at a time. The button
         and its blanks share a group number assigned at build time, so
         nothing has to be inferred by walking the DOM. */
      var g = t.getAttribute("data-grp");
      var spans = document.querySelectorAll(
        '.ansreveal[data-grp="' + g + '"]');
      var showing = t.getAttribute("aria-expanded") !== "true";
      for (var j = 0; j < spans.length; j++) {
        if (showing) { spans[j].removeAttribute("hidden"); }
        else { spans[j].setAttribute("hidden", ""); }
      }
      t.setAttribute("aria-expanded", showing ? "true" : "false");
      t.textContent = showing ? t.getAttribute("data-hide")
                              : t.getAttribute("data-show");
    } else if (t.classList.contains("reveal-btn")) {
      var body = t.nextElementSibling;
      var opening = body.hasAttribute("hidden");
      if (opening) { body.removeAttribute("hidden"); }
      else { body.setAttribute("hidden", ""); }
      t.setAttribute("aria-expanded", opening ? "true" : "false");
      t.textContent = opening ? t.getAttribute("data-hide")
                              : t.getAttribute("data-show");
    }
  });

  document.addEventListener("keydown", function (e) {
    if (e.key !== "Enter" || !e.target.classList) { return; }
    if (!e.target.classList.contains("ansinput")) { return; }
    e.preventDefault();
    if (e.target.getAttribute("data-check") === "num") { check(e.target); }
    else { showAnswer(e.target.parentNode); }
  });

  /* ---- scratch pads: persistence, and an optional equation editor ----

     Saved per browser under a stable pad id, so a refresh mid-ladder does
     not lose a student's working. Never leaves their device.

     Pads flagged data-math upgrade to a MathLive <math-field> the first
     time they are focused. The library is ~1 MB, so it is fetched only on
     that first focus: a student who works on paper and just types answers
     downloads none of it. */

  var PAD_KEY = "apchem:scratch:";
  var MATHLIVE_URL =
    "https://cdn.jsdelivr.net/npm/mathlive@0.104.2/dist/mathlive.min.mjs";
  var mathlivePromise = null;

  function padKey(el) { return PAD_KEY + el.getAttribute("data-pad"); }

  function save(el) {
    var k = el.getAttribute("data-pad");
    if (!k) { return; }
    try {
      if (el.value) { localStorage.setItem(padKey(el), el.value); }
      else { localStorage.removeItem(padKey(el)); }
    } catch (e) { /* private mode, quota, storage disabled -- ignore */ }
  }

  function restore(el) {
    try {
      var v = localStorage.getItem(padKey(el));
      if (v) { el.value = v; }
    } catch (e) { /* ignore */ }
  }

  function loadMathLive() {
    if (!mathlivePromise) {
      mathlivePromise = import(MATHLIVE_URL).then(function (m) {
        /* Sounds are another ~227 KB and a keyclick in a quiet room is not
           what anyone wants. */
        if (m.MathfieldElement) { m.MathfieldElement.soundsDirectory = null; }
        return m;
      });
    }
    return mathlivePromise;
  }

  function upgrade(ta) {
    ta.setAttribute("data-upgrading", "1");
    loadMathLive().then(function () {
      var mf = document.createElement("math-field");
      mf.className = "scratch mathfield";
      mf.setAttribute("data-pad", ta.getAttribute("data-pad"));
      mf.setAttribute("aria-label", "working space");
      if (ta.style.height) { mf.style.minHeight = ta.style.height; }
      mf.value = ta.value || "";
      mf.addEventListener("input", function () { save(mf); });
      ta.parentNode.replaceChild(mf, ta);
      mf.focus();
    }).catch(function () {
      /* Offline, or a filter blocking the CDN. The textarea still works --
         leave it alone rather than break the pad. */
      ta.removeAttribute("data-math");
      ta.removeAttribute("data-upgrading");
    });
  }

  function initPads() {
    var pads = document.querySelectorAll("textarea.scratch[data-pad]");
    for (var i = 0; i < pads.length; i++) { restore(pads[i]); }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initPads);
  } else {
    initPads();
  }

  document.addEventListener("input", function (e) {
    if (e.target.classList && e.target.classList.contains("scratch")) {
      save(e.target);
    }
  });

  document.addEventListener("focusin", function (e) {
    var t = e.target;
    if (!t.classList || !t.classList.contains("scratch")) { return; }
    if (t.tagName !== "TEXTAREA") { return; }
    if (!t.getAttribute("data-math") || t.getAttribute("data-upgrading")) {
      return;
    }
    upgrade(t);
  });


  /* Inline worksheet blanks have no Check button -- 1044 of them would
     drown the page -- so they verify when you leave the field. Enter is
     handled by the shared keydown listener above. */
  document.addEventListener("focusout", function (e) {
    var t = e.target;
    if (!t.classList || !t.classList.contains("blank-in")) { return; }
    if (t.getAttribute("data-check") !== "num") { return; }
    if (!t.value.trim()) { return; }
    check(t);
  });

})();
"""


# The host serves css/js with max-age=31536000, so a plain style.css URL
# stays stale in a returning student's browser for a YEAR after any edit.
# Versioning the query string makes every change a new URL instead.
ASSET_V = hashlib.sha1((CSS + LESSONS_JS).encode("utf-8")).hexdigest()[:8]


def ce_to_unicode(f: str) -> str:
    r"""\ce{H2SO4} -> H₂SO₄, \ce{SO4^2-} -> SO₄²⁻. Markdown viewers cannot be
    relied on to load the mhchem extension, and Unicode reads correctly even
    in a plain-text editor."""
    f = f.replace("<=>", " \u21cc ").replace("->", " \u2192 ")
    f = f.replace("<-", " \u2190 ")
    out, i = [], 0
    while i < len(f):
        c = f[i]
        if c == "^":                      # charge / superscript
            j = i + 1
            if j < len(f) and f[j] == "{":
                k = f.index("}", j)
                out.append(f[j + 1:k].translate(SUP)); i = k + 1; continue
            while j < len(f) and f[j] in "0123456789+-":
                j += 1
            out.append(f[i + 1:j].translate(SUP)); i = j; continue
        if c == "_":
            j = i + 1
            if j < len(f) and f[j] == "{":
                k = f.index("}", j)
                out.append(f[j + 1:k].translate(SUB)); i = k + 1; continue
            out.append(f[j].translate(SUB)); i = j + 1; continue
        if c.isdigit() and out and (out[-1][-1:].isalpha() or out[-1][-1:] == ")"):
            j = i
            while j < len(f) and f[j].isdigit():
                j += 1
            out.append(f[i:j].translate(SUB)); i = j; continue
        if c in "$\\":                     # drop stray math markup
            i += 1; continue
        out.append(c); i += 1
    return "".join(out).replace("  ", " ").strip()


def math_to_md(m: str) -> str:
    """Stashed math -> Markdown. \\ce{} becomes Unicode; the rest stays TeX
    between $ delimiters, which GitHub renders."""
    disp = m.startswith(r"\[") or m.startswith(r"\begin{align")
    body = m
    for a, b in ((r"\[", ""), (r"\]", ""), (r"\(", ""), (r"\)", "")):
        body = body.replace(a, b)
    body = body.strip()
    only_ce = re.fullmatch(r"\\ce\{((?:[^{}]|\{[^{}]*\})*)\}", body)
    if only_ce:
        return ce_to_unicode(only_ce.group(1))
    body = re.sub(r"\\ce\{((?:[^{}]|\{[^{}]*\})*)\}",
                  lambda x: r"\text{" + ce_to_unicode(x.group(1)) + "}", body)
    body = body.replace("\n", " ").strip()
    return f"\n\n$$ {body} $$\n\n" if disp else f"${body}$"


def html_to_md(html: str, meta: dict) -> str:
    s = re.search(r"<main>(.*)</main>", html, re.S).group(1)

    # The Markdown mirror stays a plain student edition -- the revealable
    # explanations are a website affordance and have no button here.
    while True:
        m = re.search(r'<div class="explain-body">', s)
        if not m:
            break
        s = s[:m.start()] + s[find_div(s, m.start()):]

    s = re.sub(r'<figure><img src="([^"]+)"[^>]*></figure>',
               r"\n\n![figure](\1)\n\n", s)
    s = re.sub(r'<span class="badge">(.*?)</span>', r"`\1`", s, flags=re.S)
    s = re.sub(r'<span class="blank"[^>]*></span>', "**\\_\\_\\_\\_\\_\\_**", s)
    s = re.sub(r'<div class="lines">(?:<div class="rule"></div>)+</div>',
               "\n\n\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\n\n", s)
    s = re.sub(r'<div class="workspace"[^>]*></div>',
               "\n\n*(working space)*\n\n", s)
    s = re.sub(r'<p class="selfcheck"><em>check:</em>(.*?)</p>',
               r"\n\n> **check:**\1\n\n", s, flags=re.S)

    # boxes -> blockquotes with a bold title
    def box_md(m):
        cls, inner = m.group(1), m.group(2)
        t = re.search(r'<div class="box-title">(.*?)</div>', inner, re.S)
        title = t.group(1).strip() if t else ""
        inner = re.sub(r'<div class="box-title">.*?</div>', "", inner, flags=re.S)
        mark = {"we": "\U0001f4d8", "yt": "\u270f\ufe0f", "trap": "\u26a0\ufe0f"}.get(cls, "\U0001f4cc")
        head = f"**{mark} {title}**\n>\n" if title else ""
        body = "\n".join("> " + ln for ln in
                         html_to_md_inner(inner).strip().split("\n"))
        return f"\n\n> {head[2:] if head else ''}{body.lstrip('> ')}\n\n" \
            if False else f"\n\n> {mark} **{title}**\n>\n{body}\n\n"
    while True:
        m = re.search(r'<div class="box (\w+)">(.*?)</div>\s*(?=<|$)', s, re.S)
        prev = s
        s = re.sub(r'<div class="box (\w+)">(.*?)\n</div>', box_md, s,
                   count=1, flags=re.S)
        if s == prev:
            break

    s = html_to_md_inner(s)
    front = (f"# {meta['doctitle']}\n\n"
             f"*{meta['unitword']} {meta['unit']} \u2022 {meta['unittitle']}*  \n"
             f"{meta['subtitle']}\n\n[\u2190 all lessons](../index.md)\n\n---\n\n")
    tail = ("\n\n---\n\n*AP Chemistry course materials \u2022 student edition "
            "\u2022 CC BY-NC-SA 4.0*\n")
    return front + s.strip() + tail


def html_to_md_inner(s: str) -> str:
    def table_md(m):
        rows = re.findall(r"<tr>(.*?)</tr>", m.group(1), re.S)
        out, header_done = [], False
        for r in rows:
            cells = [re.sub(r"</?t[hd][^>]*>", "", c).strip()
                     for c in re.findall(r"<t[hd][^>]*>.*?</t[hd]>", r, re.S)]
            cells = [c.replace("|", "\\|") for c in cells]
            out.append("| " + " | ".join(cells) + " |")
            if not header_done:
                out.append("|" + "---|" * len(cells))
                header_done = True
        return "\n\n" + "\n".join(out) + "\n\n"
    s = re.sub(r"<table>(.*?)</table>", table_md, s, flags=re.S)

    def list_md(m, marker):
        items = re.split(r"<li>", m.group(1))[1:]
        out = []
        for k, it in enumerate(items, 1):
            it = re.sub(r"</li>", "", it).strip()
            bullet = f"{k}." if marker == "1" else "-"
            lines = it.split("\n")
            out.append(f"{bullet} " + lines[0])
            out += ["   " + ln.strip() for ln in lines[1:] if ln.strip()]
        return "\n\n" + "\n".join(out) + "\n\n"
    for _ in range(6):
        s = re.sub(r'<ol[^>]*>(.*?)</ol>', lambda m: list_md(m, "1"), s,
                   count=1, flags=re.S)
        s = re.sub(r"<ul>(.*?)</ul>", lambda m: list_md(m, "-"), s,
                   count=1, flags=re.S)

    s = re.sub(r'<h2[^>]*>(.*?)</h2>', r"\n\n## \1\n\n", s, flags=re.S)
    s = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n\n### \1\n\n", s, flags=re.S)
    s = re.sub(r"<h4[^>]*>(.*?)</h4>", r"\n\n#### \1\n\n", s, flags=re.S)
    s = re.sub(r"<strong>(.*?)</strong>", r"**\1**", s, flags=re.S)
    s = re.sub(r"<em>(.*?)</em>", r"*\1*", s, flags=re.S)
    s = re.sub(r"<u>(.*?)</u>", r"\1", s, flags=re.S)
    s = re.sub(r"<code>(.*?)</code>", r"`\1`", s, flags=re.S)
    s = re.sub(r'<span class="qnum">(.*?)</span>', r"**\1**", s, flags=re.S)
    s = re.sub(r"<blockquote>(.*?)</blockquote>",
               lambda m: "\n\n" + "\n".join("> " + l for l in
                                            m.group(1).strip().split("\n")) + "\n\n",
               s, flags=re.S)
    s = re.sub(r'<div class="fbox">(.*?)</div>', r"\n\n> \1\n\n", s, flags=re.S)
    s = re.sub(r"<br\s*/?>", "  \n", s)
    s = re.sub(r"</?(p|div|span|figure|header|main|footer)[^>]*>", "", s)
    s = re.sub(r"<[^>]+>", "", s)

    ent = {"&thinsp;": "\u2009", "&nbsp;": " ", "&middot;": "\u00b7",
           "&deg;": "\u00b0", "&micro;": "\u00b5", "&sup2;": "\u00b2",
           "&sup3;": "\u00b3", "&amp;": "&", "&emsp;": " ", "&lt;": "<",
           "&gt;": ">"}
    for a, b in ent.items():
        s = s.replace(a, b)
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = re.sub(r"^(#{2,4}) +", r"\1 ", s, flags=re.M)   # \sffamily left a gap
    return s


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("target", nargs="?", default="Chapters")
    ap.add_argument("--no-figures", action="store_true")
    ap.add_argument("--format", choices=["html", "md", "both"], default="both")
    args = ap.parse_args()

    target = ROOT / args.target
    files = sorted(target.rglob("*.tex")) if target.is_dir() else [target]
    if args.format in ("html", "both"):
        OUT.mkdir(exist_ok=True)
        (OUT / "style.css").write_text(CSS, encoding="utf-8")
        (OUT / "lessons.js").write_text(LESSONS_JS, encoding="utf-8")
    if args.format in ("md", "both"):
        OUT_MD.mkdir(exist_ok=True)

    log, index = [], {}
    for f in files:
        entry = []
        try:
            out, meta = convert_file(f, args.no_figures, entry, args.format)
            index.setdefault(f.relative_to(ROOT / "Chapters").parts[0], []).append(
                (out.name, meta))
            status = "ok" if not any("??" in e or "!!" in e for e in entry) else "WARN"
            print(f"  {status:<5} {f.name} -> {out.relative_to(ROOT)}")
        except Exception as e:
            entry.append(f"  !! FAILED: {e}")
            print(f"  FAIL  {f.name}: {e}")
        if entry:
            log.append(f.name)
            log.extend(entry)

    # index pages
    order = {"notes": 0, "examples": 1, "selfstudy": 2, "selfstudy2": 3,
             "ws": 4, "exam": 9}

    def key(t):
        stem = t[0].rsplit(".", 1)[0]
        suffix = stem.split("-", 1)[1] if "-" in stem else stem
        return (order.get(re.sub(r"\d+$", "", suffix), 5), suffix)

    items, md_items = [], [
        "# AP Chemistry \u2014 Lessons\n",
        "Student edition, generated from the LaTeX sources. "
        "The printable PDFs (with teacher keys) are built separately with "
        "`build.ps1`.\n",
    ]
    for chap in sorted(index):
        first_meta = index[chap][0][1]
        head = (f'{first_meta["unitword"]} {first_meta["unit"]} '
                f'\u2022 {first_meta["unittitle"]}')
        items.append(f"<h2>{head}</h2>\n<ul>")
        md_items.append(f"\n## {head}\n")
        for name, meta in sorted(index[chap], key=key):
            stem = name.rsplit(".", 1)[0]
            items.append(f'<li><a href="{chap}/{stem}.html">'
                         f'{meta["doctitle"]}</a></li>')
            md_items.append(f'- [{meta["doctitle"]}]({chap}/{stem}.md)')
        items.append("</ul>")
    if args.format in ("md", "both"):
        (OUT_MD / "index.md").write_text("\n".join(md_items) + "\n",
                                         encoding="utf-8")
    if args.format in ("html", "both"):
        idx = PAGE.format(assetv=ASSET_V, title="AP Chemistry \u2022 Lessons",
                          unitword="", unit="", unittitle="AP Chemistry",
                          doctitle="Lessons", subtitle="student edition \u2022 "
                          "HTML companions to the printable PDFs",
                          body="\n".join(items)).replace('href="../', 'href="').replace('src="../', 'src="')
        (OUT / "index.html").write_text(idx, encoding="utf-8")

    report = (OUT if args.format in ("html", "both") else OUT_MD) \
        / "conversion-report.txt"
    report.write_text("\n".join(log) + ("\n" if log else ""), encoding="utf-8")
    if UNKNOWN_UNITS:
        print(f"unknown units: {sorted(UNKNOWN_UNITS)}")
    print(f"\n{len(files)} file(s); report: {report.relative_to(ROOT)}"
          f" ({'empty -- clean' if not log else str(len(log)) + ' lines'})")


if __name__ == "__main__":
    main()
