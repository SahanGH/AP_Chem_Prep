"""CI checks for the course sources and the published site.

    python tools/ci_check.py sources    # silent-failure patterns in the .tex
    python tools/ci_check.py site       # regenerate Lessons/, diff the result

Every check here is a defect class that once shipped with a clean build and
was only caught by reading the output (CLAUDE.md, "LaTeX gotchas"). Portable
on purpose: runs on the Ubuntu CI runner and on the Windows build machine.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIRS = ("Units", "Chapters")
SITE_DIRS = ("Lessons", "Lessons-md")
BASELINE = ROOT / "tools" / "ci" / "conversion-baseline.txt"
REPORT = ROOT / "Lessons" / "conversion-report.txt"


def strip_comments(src: str) -> str:
    # An unescaped % starts a comment; \% is a literal percent sign.
    return re.sub(r"(?<!\\)%.*", "", src)


def line_of(src: str, pos: int) -> int:
    return src.count("\n", 0, pos) + 1


def match_brace(s: str, open_pos: int) -> int:
    depth, i = 0, open_pos
    while i < len(s):
        if s[i] == "\\":
            i += 2
            continue
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return len(s)


def ce_spans(src: str):
    for m in re.finditer(r"\\ce\{", src):
        yield m.start(), match_brace(src, m.end() - 1)


def blank_out(src: str, spans) -> str:
    """Replace spans with spaces, keeping offsets (and line numbers) intact."""
    chars = list(src)
    for a, b in spans:
        for i in range(a, b):
            if chars[i] != "\n":
                chars[i] = " "
    return "".join(chars)


# ------------------------------------------------------------------ checks
# Each returns a list of (line, message).

def check_display_math(src, path):
    # "\\[0.3em]" is a line break with spacing, not display maths.
    tokens = sorted([(m.start(), +1) for m in re.finditer(r"(?<!\\)\\\[", src)] +
                    [(m.start(), -1) for m in re.finditer(r"(?<!\\)\\\]", src)])
    out, depth = [], 0
    for pos, step in tokens:
        depth += step
        if depth > 1:
            out.append((line_of(src, pos), r"\[ opened inside another \[ -- "
                        "a \\] is missing before here"))
            depth = 1
        elif depth < 0:
            out.append((line_of(src, pos), r"\] with no matching \["))
            depth = 0
    if depth:
        out.append((line_of(src, tokens[-1][0]), r"unclosed \[ at end of file"))
    return out


def check_bare_arrows(src, path):
    """A reaction split across two \\ce{} calls leaves its arrow in plain
    maths, where "->" renders as a minus sign and a greater-than."""
    masked = blank_out(src, ce_spans(src))
    # TikZ draws arrows with [->], [<->], (a) -> (b) etc.; not chemistry.
    for env in ("tikzpicture", "axis"):
        spans = [(m.start(), m.end()) for m in re.finditer(
            r"\\begin\{" + env + r"\}.*?\\end\{" + env + r"\}", masked, re.S)]
        masked = blank_out(masked, spans)
    masked = re.sub(r"\[[^\]\n]*->[^\]\n]*\]", lambda m: " " * len(m.group()), masked)
    return [(line_of(masked, m.start()), "bare '->' outside \\ce{} "
             "(split reaction?)") for m in re.finditer(r"<?->", masked)]


def check_ce_plus(src, path):
    """\\ce{H+F2} parses "H+" as a cation. A charge is followed by a space,
    a brace or the end; a joining plus is followed by the next species."""
    out = []
    for a, b in ce_spans(src):
        inner = src[a:b]
        for m in re.finditer(r"[A-Za-z0-9)\]]\+(?=[A-Za-z\[]|\((?!(aq|s|l|g)\)))", inner):
            out.append((line_of(src, a + m.start()),
                        f"unspaced '+' inside {inner[:60]!r}"))
    return out


def check_rubric_totals(src, path):
    """Every \\frq{type}{points} must equal its own rubric's \\rpoint sum."""
    out = []
    frqs = [(m.start(), int(m.group(1)))
            for m in re.finditer(r"\\frq\{[a-z]+\}\{(\d+)\}", src)]
    rubrics = [(m.start(), m.group(1)) for m in re.finditer(
        r"\\begin\{rubric\}(.*?)\\end\{rubric\}", src, re.S)]
    for i, (pos, pts) in enumerate(frqs):
        nxt = frqs[i + 1][0] if i + 1 < len(frqs) else len(src)
        mine = [body for rpos, body in rubrics if pos < rpos < nxt]
        if not mine:
            continue  # a free-response item without a rubric is allowed
        got = sum(int(x) for body in mine
                  for x in re.findall(r"\\rpoint\{(\d+)\}", body))
        if got != pts:
            out.append((line_of(src, pos),
                        f"\\frq declares {pts} points, its rubric sums to {got}"))
    return out


def check_examtotal(src, path):
    if not re.search(r"\\documentclass(\[[^\]]*\])?\{apchem-exam\}", src):
        return []
    n = len(re.findall(r"\\examtotal\b", src))
    return [] if n == 1 else [(1, f"exam has {n} \\examtotal (must be exactly 1)")]


def check_test_full_answerlines(src, path):
    """\\answerlines drops its answer on the web for every non-fill-in kind,
    and a comprehensive test is all answers. Bitten twice."""
    if not path.stem.endswith("test-full"):
        return []
    return [(line_of(src, m.start()), "\\answerlines in a test-full file -- "
             "use \\workspace + \\keyonly{apcanswer}")
            for m in re.finditer(r"\\answerlines\b", src)]


# Units that are not declared SI units. \psi is the worst kind: it exists as
# the Greek letter, so it typesets as a psi instead of failing the build.
BAD_UNITS = ("psi", "pound", "gallon", "hectare", "inch")


def check_bad_units(src, path):
    out = []
    for m in re.finditer(r"\\(SI|si)\{", src):
        a = match_brace(src, m.end() - 1)
        units = src[a:match_brace(src, a)] if m.group(1) == "SI" else \
            src[m.end() - 1:a]
        for name in BAD_UNITS:
            if re.search(r"\\" + name + r"(?![a-zA-Z])", units):
                out.append((line_of(src, m.start()),
                            f"\\{name} is not an SI unit here -- write it as text"))
    return out


CHECKS = [check_display_math, check_bare_arrows, check_ce_plus,
          check_rubric_totals, check_examtotal, check_test_full_answerlines,
          check_bad_units]


def sources() -> int:
    files = sorted(p for d in CONTENT_DIRS for p in (ROOT / d).rglob("*.tex"))
    failures = 0
    for path in files:
        src = strip_comments(path.read_text(encoding="utf-8"))
        rel = path.relative_to(ROOT).as_posix()
        for check in CHECKS:
            for line, msg in check(src, path):
                failures += 1
                # GitHub turns this into an annotation on the PR's diff.
                print(f"::error file={rel},line={line}::{check.__name__}: {msg}")
    print(f"{len(files)} source files, {len(CHECKS)} checks, "
          f"{failures} problem(s)")
    return 1 if failures else 0


# -------------------------------------------------------------------- site

def normalise(text: str, suffix: str) -> str:
    """Figures need MiKTeX's Ghostscript, so CI regenerates without them.
    Drop figure markup from both sides before comparing."""
    text = text.replace("\r\n", "\n")
    if suffix == ".html":
        text = re.sub(r"<figure>.*?</figure>", "", text, flags=re.S)
        text = re.sub(r'<p class="figure-missing">.*?</p>', "", text, flags=re.S)
    else:
        text = re.sub(r"^!\[[^\]]*\]\([^)]*\)\s*$", "", text, flags=re.M)
        text = re.sub(r"^\[figure \u2014 see the PDF edition\]\s*$", "", text,
                      flags=re.M)
    return text


def git(*args) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, check=True,
                          capture_output=True, text=True,
                          encoding="utf-8").stdout


def site() -> int:
    run = subprocess.run([sys.executable, str(ROOT / "tools" / "tex2html.py"),
                          "--no-figures"], cwd=ROOT, capture_output=True,
                         text=True, encoding="utf-8")
    print(run.stdout[-600:])
    failures = 0
    if run.returncode != 0:
        print(f"::error::tex2html.py exited {run.returncode}\n{run.stderr}")
        return 1
    for line in run.stdout.splitlines():
        if line.lstrip().startswith("FAIL") or line.startswith("unknown units"):
            print(f"::error::{line.strip()}")
            failures += 1

    # The converter's own warnings: anything not already known is new.
    known = set(BASELINE.read_text(encoding="utf-8").splitlines())
    report = REPORT.read_text(encoding="utf-8").splitlines()
    current_file = ""
    for line in report:
        if not line.startswith(" "):
            current_file = line
            continue
        if f"{current_file}\t{line.strip()}" not in known:
            print(f"::error::new conversion warning in {current_file}: "
                  f"{line.strip()}")
            failures += 1

    # The deploy ships the COMMITTED Lessons/, so it must match the sources.
    changed = git("diff", "--name-only", "--", *SITE_DIRS).split()
    untracked = git("ls-files", "--others", "--exclude-standard", "--",
                    *SITE_DIRS).split()
    stale = []
    for rel in changed:
        if rel.endswith("conversion-report.txt") or rel.endswith(".png"):
            continue
        old = git("show", f"HEAD:{rel}")
        new = (ROOT / rel).read_text(encoding="utf-8")
        if normalise(old, Path(rel).suffix) != normalise(new, Path(rel).suffix):
            stale.append(rel)
    for rel in untracked:
        if not rel.endswith(".png"):
            stale.append(rel + " (not committed)")
    for rel in stale:
        print(f"::error file={rel}::committed page is out of date with its "
              ".tex source -- run python tools/tex2html.py and commit Lessons/")
    failures += len(stale)
    print(f"site: {len(stale)} stale page(s), {failures} problem(s) in total")
    return 1 if failures else 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "sources":
        sys.exit(sources())
    if cmd == "site":
        sys.exit(site())
    sys.exit("usage: python tools/ci_check.py sources|site")
