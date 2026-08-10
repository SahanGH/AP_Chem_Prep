r"""Widen \answerblank rules using the widths TeX actually measured.

The key build sets each answer in a fixed-width \makebox. An answer wider than
its box does not fail the build -- it silently spills out and overprints
whatever follows. \answerblank now measures its own content and logs

    Package apchem Warning: answerblank OVERFLOW by 47.0pt (declared 3.4cm)
                            on input line 454.

This reads those warnings back out of build\aux and rewrites each offending
blank to the width it actually needs. Run a key build first so the warnings
are current:

    .\build.ps1 -All -Variant key-print
    python tools\fix_blank_widths.py            # then rebuild

    python tools\fix_blank_widths.py --dry      # report without editing

This supersedes widen_blanks.py, which estimated the rendered width from a
character count because measuring was assumed to need a LaTeX pass per blank.
The build measures every blank in one ordinary pass, so estimation -- and its
habit of being wrong in both directions at once -- is no longer necessary.
"""
import argparse
import math
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PT_PER_CM = 28.4527
PAD_CM = 0.25          # breathing room past the measured width
DEFAULT_WIDTH = "4cm"  # \answerblank's own default, for calls with no [width]

WARNING = re.compile(
    r"answerblank OVERFLOW by ([\d.]+)pt \(declared ([\d.]+)cm\) on input line (\d+)"
)


def read_warnings():
    """{(doc, line, declared_cm): [overflow_cm, ...]} from the key-print logs."""
    found = defaultdict(list)
    for log in (ROOT / "build" / "aux").glob("*-key-print.log"):
        doc = log.name[: -len("-key-print.log")]
        # LaTeX hard-wraps log lines mid-message, so unwrap before matching.
        text = log.read_text(encoding="utf-8", errors="replace").replace("\n", "")
        for m in WARNING.finditer(text):
            over, declared, line = m.groups()
            found[(doc, int(line), float(declared))].append(float(over) / PT_PER_CM)
    return found


def find_source(doc):
    for base in ("Units", "Chapters", "tools"):
        hits = list((ROOT / base).rglob(f"{doc}.tex"))
        if hits:
            return hits[0]
    return None


def scan_blanks(src):
    r"""Every \answerblank in src, as (declared_cm, end_line, spans).

    spans locate the optional argument so it can be rewritten in place. The end
    line is where the closing brace of the answer sits -- that is the line TeX
    reports, because the warning is issued once the whole argument has been
    read.
    """
    out = []
    for m in re.finditer(r"\\answerblank\s*(\[([^\]]*)\])?\s*\{", src):
        opt = m.group(2)
        declared = opt if opt is not None else DEFAULT_WIDTH
        if not declared.endswith("cm"):
            continue
        # Walk the answer argument, honouring nested braces.
        depth, i = 1, m.end()
        while i < len(src) and depth:
            if src[i] == "\\":
                i += 2
                continue
            depth += (src[i] == "{") - (src[i] == "}")
            i += 1
        out.append({
            "declared": float(declared[:-2]),
            "end_line": src.count("\n", 0, i) + 1,
            "opt_span": (m.start(1), m.end(1)) if opt is not None
                        else (m.end(0) - 1, m.end(0) - 1),
            "start": m.start(),
        })
    return out


def process(doc, warnings, dry):
    path = find_source(doc)
    if path is None:
        print(f"  !! no source found for {doc}")
        return 0
    src = path.read_text(encoding="utf-8")
    blanks = scan_blanks(src)

    edits = []
    for (line, declared), overflows in sorted(warnings.items()):
        matches = [b for b in blanks
                   if b["end_line"] == line and abs(b["declared"] - declared) < 1e-6]
        if len(matches) < len(overflows):
            print(f"  !! {doc} line {line}: {len(overflows)} warning(s) but "
                  f"{len(matches)} matching blank(s) -- skipped")
            continue
        for blank, over in zip(matches, overflows):
            need = math.ceil((declared + over + PAD_CM) * 10) / 10
            edits.append((blank["opt_span"], need, declared, line))

    if not edits:
        return 0
    for (start, end), need, _, _ in sorted(edits, key=lambda e: -e[0][0]):
        src = f"{src[:start]}[{need}cm]{src[end:]}"
    if not dry:
        path.write_text(src, encoding="utf-8")
    widest = max(e[1] for e in edits)
    print(f"  {doc:<14} {len(edits):>3} blank(s), widest now {widest:.1f}cm")
    return len(edits)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true", help="report without editing")
    args = ap.parse_args()

    raw = read_warnings()
    if not raw:
        print("no overflow warnings found -- run a key-print build first")
        return
    by_doc = defaultdict(dict)
    for (doc, line, declared), overs in raw.items():
        by_doc[doc][(line, declared)] = overs

    total = sum(process(doc, w, args.dry) for doc, w in sorted(by_doc.items()))
    verb = "would widen" if args.dry else "widened"
    print(f"\n{verb} {total} blank(s) across {len(by_doc)} document(s)")


if __name__ == "__main__":
    main()
