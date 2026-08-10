# AP® Chemistry Course Materials

A complete, print-ready course pack for a full year of AP® Chemistry —
guided notes, worksheets, unit exams, and review sheets — written in LaTeX
and aligned to the College Board's 2024 Course and Exam Description.

![LaTeX](https://img.shields.io/badge/built%20with-LaTeX-008080)
![CED](https://img.shields.io/badge/aligned%20to-2024%20CED-1f6feb)
![Variants](https://img.shields.io/badge/every%20document-4%20variants-6f42c1)
![Format](https://img.shields.io/badge/designed%20for-90--min%20blocks-2da44e)

Every document compiles from a single source into **four variants** —
student and teacher-key editions, each in a print layout and an LMS
(screen) layout. Answers, rationales, and scoring rubrics live inline next
to their questions and appear only in the key builds, so the two editions
can never drift apart.

---

## What's inside

| | |
|---|---|
| **9 CED units** | The exam-prep track, in College Board sequence (`Units/`). Each unit: a one-page map, block-by-block guided notes, 4–5 worksheets, a review sheet, and a unit exam with scoring rubrics. |
| **18 textbook chapters** | The reading track, in Zumdahl's sequence (`Chapters/`). Notes, worksheets, and a chapter test each. |
| **168 LaTeX sources** | ≈ 670 finished PDFs after a full build. |
| **A real exam blueprint** | Every exam mirrors AP weighting: 1-point MCQs, 10-point long FRQs, 4-point short FRQs, no-calculator multiple choice throughout. |

Designed for a **MWF × 90-minute block schedule** (a co-op / homeschool
year), but the documents themselves are schedule-agnostic — each notes
"block" is a self-contained 90-minute lesson with warm-up, two instruction
segments, guided practice, application, and an exit ticket.

### Design commitments

- **Every item is CED-tagged.** Each question carries its topic code
  (`3.11`) and, where relevant, a science-practice tag — so coverage is
  auditable, not aspirational.
- **Original items only.** Released College Board FRQs are referenced by
  year and number, never reproduced.
- **Grayscale by design.** Everything prints correctly on a black-and-white
  copier; nothing is distinguished by hue alone.
- **Spiral review everywhere.** Worksheets close with a five-item strip
  reaching back through earlier blocks; unit exams assume retention.
- **Self-verifying exams.** Every exam ends with a macro that recounts its
  own questions and points and prints the total — a mis-sized exam
  announces itself.

---

## Repository layout

```
AP_Chem_Prep/
├── build.ps1            # the build system — one script, four variants per source
├── PLAN.md              # year calendar, block budget, exam blueprint
├── TEXTBOOK-MAP.md      # every CED topic → exact textbook page range
├── shared/              # apchem.sty + the notes / worksheet / exam classes
├── Units/               # CED track: unit01-atomic-structure … unit09-…
│   └── unitNN-topic/    #   uNN-map, uNN-notes, worksheets/, uNN-review, exam/
├── Chapters/            # textbook track: chapter01 … chapter18
├── Reference/           # periodic table handout
├── tools/               # build utilities + smoke-test documents
└── build/               # all output lands here (generated — not committed)
```

---

## Quick start

### 1 · Clone

```bash
git clone https://github.com/SahanGH/AP_Chem_Prep.git
cd AP_Chem_Prep
```

### 2 · Install prerequisites

All you need is a LaTeX distribution — building requires nothing else.

<details>
<summary><strong>Windows</strong> (the tested platform)</summary>

1. **[MiKTeX](https://miktex.org/download)** — during setup, set *"Install
   missing packages on-the-fly"* to **Yes**. The first build will download
   the packages it needs (mhchem, siunitx, tcolorbox, pgfplots, chemfig,
   and friends); after that, builds are fast.
2. PowerShell ships with Windows — nothing to install.

</details>

<details>
<summary><strong>macOS</strong></summary>

**[MacTeX](https://www.tug.org/mactex/)** — the full distribution includes
every package used here:

```bash
brew install --cask mactex
```

Build manually (see below) — or install PowerShell
(`brew install powershell`) with the caveat noted there.

</details>

<details>
<summary><strong>Linux</strong></summary>

**TeX Live** — simplest is the full scheme:

```bash
sudo apt install texlive-full          # Debian/Ubuntu
```

or, for a leaner install, the collections that cover this repo:

```bash
sudo apt install texlive-latex-extra texlive-science \
                 texlive-pictures texlive-fonts-recommended
```

</details>

### 3 · Build

**On Windows**, from the repo root:

```powershell
.\build.ps1 -All                                    # everything (~40 min first time)
.\build.ps1 Units\unit01-atomic-structure           # one unit, all variants
.\build.ps1 Chapters\chapter14-acids-bases          # one chapter
.\build.ps1 Units\unit05-kinetics\u05-notes.tex -Variant key-print
.\build.ps1 -Clean                                  # drop the aux directory
```

Output mirrors the source tree under `build/`. Compile errors surface
directly in the console with the offending log lines.

**On macOS / Linux**, `build.ps1` is untested (it assumes Windows path and
`TEXINPUTS` conventions), so compile directly — from the document's own
folder, with `shared/` on the search path:

```bash
cd Units/unit01-atomic-structure
export TEXINPUTS=".:../../shared:"

# student print edition — run twice; the layout stabilises on the second pass
pdflatex -jobname u01-notes-student-print "\input{u01-notes.tex}"
pdflatex -jobname u01-notes-student-print "\input{u01-notes.tex}"

# teacher key:  \def\ISKEY{1}     LMS layout:  \def\ISLMS{1}     both: chain them
pdflatex -jobname u01-notes-key-print "\def\ISKEY{1}\input{u01-notes.tex}"
pdflatex -jobname u01-notes-key-print "\def\ISKEY{1}\input{u01-notes.tex}"
```

---

## The four variants

| Variant | Toggle(s) | What it is |
|---|---|---|
| `student-print` | — | handout: blank answer rules, workspace, print margins |
| `student-lms` | `\ISLMS` | the same, laid out for on-screen posting |
| `key-print` | `\ISKEY` | teacher key: answers in bold, rubrics, marginal notes |
| `key-lms` | `\ISKEY` + `\ISLMS` | key, screen layout |

The toggles are injected by the build system — they are never hardcoded in
a source file. Answer blanks reserve **identical space** in both editions,
so the student and key builds paginate the same and can be marked side by
side.

---

## The two tracks

**`Units/`** follows the CED unit sequence and is what exam preparation is
built on — this is where the unit exams, review sheets, and AP-style FRQs
live.

**`Chapters/`** follows the textbook's own chapter order and provides the
reading-companion material: chapter notes keyed to section numbers, plus
worksheets and chapter tests. The two tracks cross-reference each other
through [TEXTBOOK-MAP.md](TEXTBOOK-MAP.md), which maps every CED topic to
exact page ranges.

Page references are keyed to **Zumdahl, Zumdahl & DeCoste,
*Chemistry* (AP Edition), 10th ed.** The textbook itself is copyrighted
and is **not in this repository** — you'll need your own copy for the
reading assignments, but nothing in the build depends on it.

---

## A note for teachers using this publicly

Answer keys are not separate files — every answer and rubric lives in the
`.tex` source, revealed by a build-time toggle. That is the feature that
keeps keys and questions synchronized, but it also means **anyone who can
read this repository can read the answers**, including a student who finds
it. Treat the exams as a bank to draw from and modify, not as secure
instruments, or keep your own fork private.

---

## Tools

Building the PDFs needs neither of these — they are authoring aids.

| Tool | What it does |
|---|---|
| `tools/fix_blank_widths.py` | reads TeX's own measurements from the build logs and widens any answer blank narrower than its answer (Python 3, standard library only) |
| `tools/smoke/` | minimal test documents for the three classes — build these first after touching `shared/` |

---

## License & attribution

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey)](LICENSE)

This work is licensed under
**[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)**
(see [LICENSE](LICENSE)). In plain terms:

- **Use it freely.** Teach from it, print it, post it to your LMS, adapt
  it to your own schedule — no permission needed.
- **Non-commercial.** Don't sell it or bundle it into a paid product.
- **Share-alike.** If you publish a modified version, license it the same
  way.
- **Attribution.** Keep a pointer back to this repository in anything you
  redistribute.

The teaching materials are original work by the author. No textbook
content is reproduced; released College Board exam questions are cited by
year and number only.

AP® is a trademark registered by the College Board, which is not
affiliated with, and does not endorse, this repository.
