"""Widen \answerblank rules whose bold key text would overrun them.

The key build sets the answer in bold inside a fixed-width \makebox. If the
text is wider than the rule, it spills past it -- and where prose follows on
the same line, it collides. This estimates the rendered width and rewrites
any blank that is too narrow.

    python tools\\widen_blanks.py Units\\unit06-thermochemistry
    python tools\\widen_blanks.py Chapters\\chapter18-electrochemistry --dry

Estimating rather than measuring is deliberate: a real measurement needs a
LaTeX pass per blank. The constant below is calibrated against built PDFs
and errs toward slightly-too-wide, which is harmless -- a rule longer than
its answer looks normal, a rule shorter than its answer does not.
"""
import argparse
import glob
import os
import re

CM_PER_CHAR = 0.18   # bold 10pt, averaged over mixed-case prose
SLACK = 1.12         # rule this much longer than the estimated text
PAD = 0.2            # plus a fixed pad, cm

TEX_CMD = re.compile(r"\\[a-zA-Z]+\s?")
PUNCT = re.compile(r"[{}$^_\\]")
BLANK = re.compile(r"\\answerblank\[([0-9.]+)cm\]\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")


def visible_width(answer: str) -> float:
    """Rough rendered width in cm, ignoring LaTeX markup."""
    plain = PUNCT.sub("", TEX_CMD.sub("", answer))
    return len(plain) * CM_PER_CHAR


def process(path: str, dry: bool) -> int:
    src = open(path, encoding="utf-8").read()
    out, last, n = [], 0, 0
    for m in BLANK.finditer(src):
        width = float(m.group(1))
        answer = m.group(2)
        need = round(visible_width(answer) * SLACK + PAD, 1)
        if need > width:
            out.append(src[last:m.start()])
            out.append(f"\\answerblank[{need}cm]{{{answer}}}")
            last = m.end()
            n += 1
            flat = " ".join(answer.split())
            print(f"  {os.path.basename(path):<16} {width}cm -> {need}cm   {flat[:46]}")
    if last and not dry:
        out.append(src[last:])
        open(path, "w", encoding="utf-8").write("".join(out))
    return n


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", help="directory or .tex file to process")
    ap.add_argument("--dry", action="store_true", help="report without editing")
    args = ap.parse_args()

    files = ([args.path] if args.path.endswith(".tex")
             else sorted(glob.glob(os.path.join(args.path, "**", "*.tex"),
                                   recursive=True)))
    total = sum(process(f, args.dry) for f in files)
    verb = "would widen" if args.dry else "widened"
    print(f"\n{verb} {total} blank(s) across {len(files)} file(s)")


if __name__ == "__main__":
    main()
