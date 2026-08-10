# AP Chemistry — Materials Game Plan

**Status:** DRAFT v3 — for review before execution
**Course:** AP Chemistry, co-op year → AP Exam early May 2027
**Schedule:** **MWF × 90 min**, first day **Mon Aug 10, 2026**, 30 instructional weeks = **90 blocks**
**Textbook:** Zumdahl, Zumdahl & DeCoste, *Chemistry* (AP Edition), 10th ed.
**Labs:** taught in a separate session — **out of scope** for these materials (see §7)
**Output:** LaTeX → PDF (MiKTeX confirmed: `pdflatex`, `xelatex`, `latexmk`)
**Notes model:** Guided (skeleton) student version + complete teacher key
**Assessment model:** AP-mirror unit exams (MCQ + FRQ + scoring rubric)

---

## 1. Source of truth

Content is keyed to the current **AP Chemistry Course and Exam Description** (Course at a Glance, © 2024 College Board, V.1), verified 2026-08-08. Every notes section, worksheet, and exam item carries its CED topic code (e.g. `3.11`), its science practice (SP 1–6), and its Zumdahl section.

### Unit structure, converted to your blocks

1 block = 90 min = 2 CED periods.

| Unit | Title | CED Topics | CED Periods | **Blocks** | AP Weight |
|:----:|-------|:----------:|:-----------:|:----------:|:---------:|
| 1 | Atomic Structure and Properties | 1.1–1.8 | ~9–10 | 5 | 7–9% |
| 2 | Compound Structure and Properties | 2.1–2.7 | ~12–13 | 6 | 7–9% |
| 3 | **Properties of Substances and Mixtures** | 3.1–3.13 | ~14–15 | 9 | **18–22%** |
| 4 | Chemical Reactions | 4.1–4.9 | ~14–15 | 7 | 7–9% |
| 5 | Kinetics | 5.1–5.11 | ~13–14 | 7 | 7–9% |
| 6 | Thermochemistry | 6.1–6.9 | ~10–11 | 5 | 7–9% |
| 7 | Equilibrium | 7.1–7.12 | ~13–15 | 8 | 7–9% |
| 8 | **Acids and Bases** | 8.1–8.11 | ~14–16 | 9 | **11–15%** |
| 9 | Thermodynamics and Electrochemistry | 9.1–9.11 | ~10–13 | 9 | 7–9% |
|  | | **Total** | ~116 | **65** | 100% |

### Year budget — 35 weeks to the exam, labs excluded

The exam is **Thu May 6, 2027**. With the co-op's four break weeks, that
leaves **35 instructional weeks = 104 blocks** between Aug 10 and the exam,
not the 30 weeks originally assumed. See §6 for the full re-cut.

| Category | Blocks |
|----------|:------:|
| Content instruction | 65 |
| Course launch + math/sig-fig diagnostic | 1 |
| Unit exams (9 × 1) | 9 |
| Benchmarks A & B + results review | 4 |
| Full mock AP (2) + results review (1) | 3 |
| Targeted pre-AP review + FRQ clinics | 12 |
| Course wrap + semester wrap + exam logistics | 3 |
| **Committed** | **97** |
| Float — named reteach block per unit, sick days, drift | **7** |
| **Total** | **104** |

**The year fits with real margin — because labs moved out and the exam is
later than assumed.** Content instruction grew from 59 blocks to 65, with
the extra six going to Units 3, 7, 8 and 9 (the two heaviest-weighted units
and the two hardest). Review roughly doubled and now sits adjacent to the
exam rather than ten weeks before it.

### Exam format being mirrored

- **Section I:** 60 MCQ, 90 min, 50% of score. **No calculator.**
- **Section II:** 7 FRQ, 105 min, 50% — 3 long (10 pts) + 4 short (4 pts). Calculator permitted.
- Equations & Constants sheet + periodic table provided for both sections.
- Derived pacing used for sizing: **~1.5 min/MCQ, ~22 min/long FRQ, ~9 min/short FRQ.**

---

## 2. Zumdahl 10e ↔ CED mapping

Unit maps and worksheets will cite these. Note that CED unit order ≠ Zumdahl chapter order — you are **not** teaching straight through the book, and several units pull from chapters far apart.

| Unit | Primary Zumdahl chapters | Notes |
|:----:|--------------------------|-------|
| 1 | Ch 3 (Stoichiometry — moles, molar mass, % composition); Ch 7.11–7.13 (electron config, periodic trends); Ch 2 | |
| 2 | Ch 8 (Bonding: General Concepts); Ch 9 (Covalent Bonding: Orbitals); Ch 10 (ionic solids, metals/alloys) | |
| 3 | Ch 10 (Liquids and Solids — IMFs); Ch 5 (Gases, KMT, deviations); Ch 11 (Properties of Solutions); Ch 4.1–4.3 (concentration); Ch 7.1–7.2 (EM radiation, photons) | Widest spread in the book |
| 4 | Ch 3 (stoichiometry); Ch 4 (Types of Chemical Reactions and Solution Stoichiometry — net ionic, titration, redox) | |
| 5 | Ch 12 (Chemical Kinetics) | Clean 1:1 |
| 6 | Ch 6 (Thermochemistry) | Clean 1:1 |
| 7 | Ch 13 (Chemical Equilibrium); Ch 16.1–16.2 (Ksp); Ch 15.1 (common-ion effect) | |
| 8 | Ch 14 (Acids and Bases); Ch 15 (Acid-Base Equilibria — buffers, titrations, H–H); Ch 16.3 (pH and solubility) | |
| 9 | Ch 17 (Spontaneity, Entropy, Free Energy); Ch 18 (Electrochemistry) | |

### Textbook coverage — verified against the PDF, not assumed

The book PDF is in `Textbook/` (1,219 pp.). I extracted its section-level outline and searched the full text. **A full topic-by-topic page map lives in [TEXTBOOK-MAP.md](TEXTBOOK-MAP.md)** — that file, not this one, is what the unit maps cite.

Correcting v3: I had flagged four CED topics as textbook gaps. **All four are in fact covered.**

| CED Topic | v3 claim | Verified reality |
|-----------|----------|------------------|
| **1.6** Photoelectron Spectroscopy | "Essentially absent" | **Fully covered**, pp. 368–369 — $E = h\nu - KE$, He 58.4 nm source, Fig. 7.33, B/F overlay |
| **1.2** Mass Spectra | "Thin" | **Properly covered**, §3.2 — Ne spectrum, Cu worked average-mass example |
| **3.13** Beer–Lambert Law | "Thin" | Covered in **Appendix 3**, p. 1142 |
| **3.9** Separation of Mixtures | "Barely covered" | Covered in **§1.10**, p. 53 |

**The real problem is dislocation, not absence.** Unit 3 pulls from Chapters 1, 4, 5, 7, 10, 11, *and* Appendix 3 — seven locations. "Read Chapter 10" gets a student a fraction of the unit. Every unit map therefore carries **exact page ranges**, never chapter numbers.

**Net effect: the build got cheaper.** Original content is now needed only for particulate-representation practice, PES and Beer–Lambert problem sets (exposition exists, exercises don't), Unit 3's connective narrative, and AP-format FRQs throughout.

### ~300 pages to skip

Zumdahl carries substantial content the CED dropped in 2019: **MO theory (§9.2–9.5), colligative properties (§11.4–11.7), phase diagrams (§10.9), and Chapters 19–22** (nuclear, representative elements, transition metals, organic). Full list in [TEXTBOOK-MAP.md](TEXTBOOK-MAP.md). At 90 blocks, none of it fits.

---

## 3. What MWF × 90 min drives

### 3.1 Notes are organized by *block*, not by topic

Nobody absorbs 90 minutes of chemistry lecture. Each unit's guided notes are chunked into **block lessons** with a fixed rhythm, printed into the student packet as timing cues:

| Segment | Time | What |
|---------|:----:|------|
| Retrieval warm-up | 5 min | 3 spiral questions from prior units |
| **Instruction A** | 25 min | Guided notes, blanks, worked example |
| Guided practice | 15 min | Embedded worksheet strip — you circulate |
| **Instruction B** | 20 min | Second topic or deeper layer |
| Application | 20 min | FRQ task or particulate-drawing task |
| Exit ticket | 5 min | One question, collected — tells you what to reteach Wednesday |

So `u01-notes.tex` contains 5 block lessons, not 8 topic sections. Worksheets are sized to the 15-minute in-class window rather than being monolithic take-homes.

### 3.2 MWF gaps are 2 / 2 / 3 days — manageable, but the weekend still bites

Even gaps are the good case; you dodged the Tue/Wed/Thu dead zone. Still, Monday opens after 3 days cold. Built into every artifact:

- **Every block opens with a 5-minute retrieval warm-up** — 3 questions, none from the previous block, drawn from 2+ weeks back. Pre-written into the packet; you don't invent them Monday morning. **Monday warm-ups run 4 questions instead of 3.**
- **Homework is spaced, not massed.** Every worksheet's back page carries a "spiral strip" of 5 problems from earlier units. A Unit 7 worksheet still drills Unit 3 IMFs.

With 4-day-a-week gaps between contact, retrieval practice buys you more than an extra content block would.

---

## 4. Per-unit deliverable set

Five artifacts per unit, identical every time. Students learn the format once.

| # | Artifact | Pages | Description |
|:-:|----------|:-----:|-------------|
| 1 | **Unit map** | 1 | CED topics, Zumdahl reading assignments, block-by-block calendar, exam date, objectives in student language |
| 2 | **Guided notes** | 10–16 | Block lessons per §3.1 with timing cues, blanks, particulate space, worked-example frames. **+ teacher key** |
| 3 | **Worksheets** | 3–5 sets | Sized to the 15-min in-class window; each with spiral strip + full solution key |
| 4 | **Unit exam** | 5–9 | AP-mirror MCQ + FRQ, one block. **+ answer key + point-by-point rubric** |
| 5 | **Review sheet** | 2 | Student one-pager (equations, traps, decision trees) + cumulative spiral MCQ set |

### Worksheet types (each unit gets a mix)

- **Type A — Skill drill.** Computational fluency: stoichiometry, pH, rate laws, ICE tables. Answer-only key.
- **Type B — Conceptual / particulate.** Draw-and-explain, particulate diagrams, graph interpretation, "which is larger and why." Where AP points are actually lost — and where Zumdahl helps least.
- **Type C — AP-style FRQ practice.** Full FRQs in College Board voice with real rubric language ("1 point for…"). Students self-score against the rubric.

**Copyright note:** all items are **original**, written in AP style. Released College Board FRQs are copyrighted; I'll reference them by year/number as supplemental assignments rather than reproducing them.

---

## 5. Exam blueprint

Every unit exam fits one block and lands near real Progress Check size. Scaled to the AP's 50/50 MCQ–FRQ split.

Points: 1 per MCQ, 10 per long FRQ, 4 per short FRQ (matching real AP
scoring). `\examtotal` prints the true count on every built exam — check it
against this table after any edit.

| Unit | MCQ | FRQ | Est. Time | Points |
|:----:|:---:|-----|:---------:|:------:|
| 1 | 20 | 2 short | 48 min | 28 |
| 2 | 20 | 1 long | 52 min | 30 |
| 3 | 30 | 1 long + 1 short | 76 min | 44 |
| 4 | 20 | 1 long | 52 min | 30 |
| 5 | 25 | 1 short + 1 long | 69 min | 39 |
| 6 | 20 | 2 short | 48 min | 28 |
| 7 | 30 | 1 short + 1 long | 76 min | 44 |
| 8 | 30 | 1 long + 1 short | 76 min | 44 |
| 9 | 25 | 1 short + 1 long | 69 min | 39 |

Lighter units leave 30–40 min of the block to review the exam or launch the next unit. Every exam is **no-calculator on the MCQ half** — students need that habit from Unit 1, not from April.

### Cumulative assessments

- **Benchmark A** — after Unit 3 (covers 1–3): 30 MCQ + 2 FRQ, one block.
- **Benchmark B** — after Unit 6 (covers 1–6): 30 MCQ + 2 FRQ, one block.
- **Full mock exam** — complete 60 MCQ + 7 FRQ under real timing. 195 min = **2 blocks** (Section I Monday, Section II Wednesday) + 1 block for results.

---

## 6. Calendar — dated, MWF from Mon Aug 10, 2026

**AP Chemistry Exam: Thursday, May 6, 2027, afternoon session.**
Confirmed against the College Board 2027 schedule, not assumed.

Dated against the co-op break calendar (Thanksgiving, Christmas, Easter).
Break weeks are shown in place so the row numbers stay honest.

| Wk | Week of | Mon | Wed | Fri |
|:--:|:-------:|-----|-----|-----|
| 1 | **Aug 10** | Launch + diagnostic | U1 · Block 1 | U1 · Block 2 |
| 2 | **Aug 17** | U1 · Block 3 | U1 · Block 4 | U1 · Block 5 |
| 3 | **Aug 24** | **U1 EXAM** | U2 · Block 1 | U2 · Block 2 |
| 4 | **Aug 31** | U2 · Block 3 | U2 · Block 4 | U2 · Block 5 |
| 5 | **Sep 7** | U2 · Block 6 | **U2 EXAM** | U3 · Block 1 |
| 6 | **Sep 14** | U3 · Block 2 | U3 · Block 3 | U3 · Block 4 |
| 7 | **Sep 21** | U3 · Block 5 | U3 · Block 6 | U3 · Block 7 |
| 8 | **Sep 28** | U3 · Block 8 | U3 · Block 9 | U3 reteach *(float)* |
| 9 | **Oct 5** | **U3 EXAM** | **BENCHMARK A** | BM-A results review |
| 10 | **Oct 12** | U4 · Block 1 | U4 · Block 2 | U4 · Block 3 |
| 11 | **Oct 19** | U4 · Block 4 | U4 · Block 5 | U4 · Block 6 |
| 12 | **Oct 26** | U4 · Block 7 | U4 reteach *(float)* | **U4 EXAM** |
| 13 | **Nov 2** | U5 · Block 1 | U5 · Block 2 | U5 · Block 3 |
| 14 | **Nov 9** | U5 · Block 4 | U5 · Block 5 | U5 · Block 6 |
| 15 | **Nov 16** | U5 · Block 7 | U5 reteach *(float)* | **U5 EXAM** |
| — | *Nov 23* | — | *THANKSGIVING* | — |
| 16 | **Nov 30** | U6 · Block 1 | U6 · Block 2 | U6 · Block 3 |
| 17 | **Dec 7** | U6 · Block 4 | U6 · Block 5 | **U6 EXAM** |
| 18 | **Dec 14** | **BENCHMARK B** | BM-B results review | **Semester wrap** |
| — | *Dec 21* | — | *CHRISTMAS BREAK* | — |
| — | *Dec 28* | — | *CHRISTMAS BREAK* | — |
| 19 | **Jan 4** | U7 · Block 1 | U7 · Block 2 | U7 · Block 3 |
| 20 | **Jan 11** | U7 · Block 4 | U7 · Block 5 | U7 · Block 6 |
| 21 | **Jan 18** | U7 · Block 7 | U7 · Block 8 *(Ksp)* | U7 reteach *(float)* |
| 22 | **Jan 25** | **U7 EXAM** | U8 · Block 1 | U8 · Block 2 |
| 23 | **Feb 1** | U8 · Block 3 | U8 · Block 4 | U8 · Block 5 |
| 24 | **Feb 8** | U8 · Block 6 | U8 · Block 7 | U8 · Block 8 |
| 25 | **Feb 15** | U8 · Block 9 | U8 reteach *(float)* | **U8 EXAM** |
| 26 | **Feb 22** | U9 · Block 1 | U9 · Block 2 | U9 · Block 3 |
| 27 | **Mar 1** | U9 · Block 4 | U9 · Block 5 | U9 · Block 6 |
| 28 | **Mar 8** | U9 · Block 7 | U9 · Block 8 | U9 · Block 9 |
| 29 | **Mar 15** | U9 reteach *(float)* | U9 review | **U9 EXAM** |
| — | *Mar 22* | — | *EASTER / HOLY WEEK* | — |
| 30 | **Mar 29** | Course wrap | Review: Unit 3 | Review: Unit 8 |
| 31 | **Apr 5** | Review: equilibrium arc (U7) | Review: Unit 9 | FRQ clinic |
| 32 | **Apr 12** | **MOCK — Section I** | **MOCK — Section II** | Mock results review |
| 33 | **Apr 19** | Targeted review (mock-driven) | Targeted review | FRQ clinic |
| 34 | **Apr 26** | Targeted review | FRQ clinic | Weakest-topic clinic |
| 35 | **May 3** | Final FRQ clinic | Exam logistics + Q&A *(Wed May 5)* | — |
| | | | | 🎯 **AP EXAM Thu May 6, PM** |

**35 instructional weeks · 104 blocks.** Content runs weeks 1–29 (87
blocks); review runs weeks 30–35 (17 blocks).

### What changed when the dates went in, and why

Pinning real dates and confirming the exam date exposed that the original
30-week plan finished **five weeks early**. Three changes followed.

**1. The mock moved from February to April (wk 32, Apr 12).** This was the
main reason to re-cut. A full mock ten weeks out mostly measures what
students have forgotten since Unit 3. At three weeks out it measures what
they will actually score — and weeks 33–35 are deliberately left as
*targeted* review so the mock results can direct them. Do not pre-plan those
rows; fill them in from the mock.

**2. Content decompressed by 12 blocks rather than adding more review.**
Ten weeks of review would be too much and students disengage. The slack went
to the units that carry the most exam weight or the most conceptual load:

| Unit | Was | Now | Why |
|---|:--:|:--:|---|
| 3 Properties of Substances | 8 | **9** | heaviest unit, 18–22% |
| 7 Equilibrium | 7 | **8** | +1 for Ksp, which Ch 13 did not cover |
| 8 Acids and Bases | 8 | **9** | 11–15%, spans two Zumdahl chapters |
| 9 Thermo + Electrochem | 6 | **9** | 11 CED topics, two chapters, all new |

Every unit also gained a named **reteach/float** block. Those are real, not
padding — the first year of any course overruns, and a float block per unit
is what keeps the calendar from sliding.

**3. The semester wrap moved to wk 18 (Dec 18), the Friday before
Christmas break** — where a semester actually ends. It was sitting at
Nov 16, which the week numbers had hidden.

Benchmark B moved with it, to the Monday of that same week, so the
half-year assessment and the wrap sit together.

### Latest safe dates

If the schedule slips, these are the dates that matter:

- **U9 EXAM by Fri Mar 19** — anything later eats the review runway.
- **Mock by Fri Apr 16** — later than this and there is no time to act on it.
- **Wed May 5** is the last contact before the exam.

---

## 7. Labs — out of scope, but they still have to line up

You said labs run separately, so I'm not writing lab handouts. Two things still matter:

1. **AP expects ~25% of instructional time on hands-on lab, across 16 guided-inquiry investigations.** That obligation now lives entirely with the separate lab session. Worth confirming it's actually covering that load — it's the part of the audit syllabus most often under-served.
2. **Sync matters.** A solubility lab is worth far more during Unit 7 than three weeks after it.

**Optional cheap add-on:** a one-page **lab alignment map** — which AP investigation pairs with which unit, and the week it should run to match this calendar. One page total, not per unit. Useful to hand the lab instructor. Say the word and I'll include it in Phase 1.

---

## 8. Technical build

### 8.1 Textbook access — plain text cache, not a vector DB

Phase 0 extracts all 1,219 pages to per-page plain text (~4 MB) under `Textbook/cache/`, plus a JSON index of the section outline with page anchors.

**Why not a vector database:** the PDF ships a complete section-level outline with exact page anchors, already converted into [TEXTBOOK-MAP.md](TEXTBOOK-MAP.md). The task is "read pp. 493–498 and write notes," not "find something about IMFs" — exact ranges beat semantic approximation, and keyword search over the cache returns in seconds. Embeddings would add an inference dependency, a store, and chunking decisions to search *one* book that already has a clean table of contents. Revisit if the corpus grows to multiple textbooks or a released-exam archive.

### Repository layout

```
D:\AP_Chem_Prep\
├─ PLAN.md
├─ TEXTBOOK-MAP.md               # CED topic → Zumdahl page ranges
├─ Textbook\
│   ├─ Chemistry 10e Zumdahl, DeCoste.pdf
│   └─ cache\                    # per-page .txt + outline.json (Phase 0)
├─ build.ps1                     # build all / one unit / one file
├─ shared\
│   ├─ apchem.sty                # macros, chem shortcuts, boxes, blanks
│   ├─ apchem-notes.cls          # block-lesson layout w/ timing cues
│   ├─ apchem-worksheet.cls      # incl. spiral-strip environment
│   ├─ apchem-exam.cls           # MCQ engine, FRQ rubric blocks
│   └─ assets\                   # shared image/data includes
├─ Reference\                    # student reference sheets (periodic table,
│                                #   equations & constants) -- NOT under
│                                #   shared\, which build.ps1 -All skips
├─ Units\                        # CED-sequence materials (exam prep)
│   ├─ unit01-atomic-structure\
│   │   ├─ u01-map.tex
│   │   ├─ u01-notes.tex         # ONE source → student PDF + key PDF
│   │   ├─ worksheets\ u01-ws1.tex … u01-ws4.tex
│   │   ├─ exam\ u01-exam.tex
│   │   └─ u01-review.tex
│   └─ unit02-…  …  unit09-…
├─ Chapters\                     # Zumdahl-sequence materials (foundation)
│   ├─ README.md
│   └─ chapter02-atoms-molecules-ions\
├─ cumulative\                   # benchmarks, mock exam
├─ warmups\                      # spiral retrieval bank, tagged by unit
└─ build\                        # all generated PDFs
```

### The one design decision that matters: single-source key generation

Student version and teacher key compile from **the same `.tex` file**, switched by a boolean:

```latex
\answerblank[3cm]{$K_a = \dfrac{[\ce{H+}][\ce{A-}]}{[\ce{HA}]}$}
```

renders as a ruled blank in the student PDF and the filled-in answer (boxed, colored) in the key. Build:

```powershell
latexmk -pdf -jobname=u01-notes-student u01-notes.tex
latexmk -pdf -jobname=u01-notes-key "\def\ISKEY{1}\input{u01-notes.tex}"
```

**Why this matters:** with two separate files, the key drifts from the student copy the first time you fix a typo — and you find out during class. One source makes drift structurally impossible. Exams use the same mechanism: MCQ answers, distractor rationales, and FRQ rubric points are written inline next to the question and appear only in the key.

### LaTeX stack

| Package | Use |
|---------|-----|
| `mhchem` | `\ce{H2SO4}`, `\ce{Cu^2+ + 2e- -> Cu}` — all formulas and equations |
| `siunitx` | units, sig figs, uncertainty, scientific notation |
| `chemfig` | Lewis structures, VSEPR, organic skeletons |
| `pgfplots` | titration curves, PES spectra, energy profiles, Maxwell–Boltzmann |
| `tikz` | particulate diagrams, orbital boxes, galvanic cells |

MiKTeX auto-installs on demand — Phase 0 runs a smoke test to confirm before any real content is written.

---

## 9. Execution sequence

Vertical slice first. I build **Unit 1 completely** so you review the real look and feel before nine units are locked to a format you dislike.

| Phase | Work | Gate |
|:-----:|------|------|
| **0** | Infrastructure: `.sty`/`.cls`, key toggle, block-lesson layout, build script, smoke test, **textbook text cache** (§8.1) | PDFs compile |
| **1** | **Unit 1 complete** — map, 5 block lessons + key, 4 worksheets + keys, exam + rubric, review sheet | **← YOU REVIEW HERE.** Format locked after your notes |
| **2** | Units 2–3 (Unit 3 is the big one — build early, revise most) + warm-up bank seeded | Review |
| **3** | Units 4–5, Benchmark A | Review |
| **4** | Units 6–9 | Review |
| **5** | Benchmark B, full mock exam, pre-AP review packets | Complete |

**Timing pressure is real but manageable:** Unit 1 starts Wed Aug 12 — two days out. Phase 0 + Phase 1 need to land first. Everything after that stays comfortably ahead of the calendar.

---

## 10. Recommendations

- **Build Unit 3 second.** 18–22% of the exam, conceptually the widest, spread across four separate Zumdahl chapters, and the unit most likely to need a revision pass. Build it early so there's time for that pass.
- **Budget original content for PES (1.6).** Zumdahl 10e effectively doesn't cover it and it shows up on nearly every AP exam. This is the single largest textbook gap.
- **Take the 5-minute spiral warm-up seriously.** Pre-written into every packet, so it costs you nothing to run, and it's the highest-leverage response to MWF gaps.
- **Rubric-visible FRQ practice.** Hand students the rubric with the worksheet and make them self-score. AP points are awarded for specific stated things; students who've never seen a rubric write essays instead of earning points.
- **No-calculator MCQ from Unit 1.** A year of calculator-assisted MCQs produces a May disaster.

---

## 11. Still open

1. **Co-op break calendar** — needed to pin real dates to §6.
2. **Print or LMS?** Defaulting to print-friendly (generous blanks, high-contrast, duplex-aware). One-line switch to change.
3. **Lab alignment map** — want the optional one-pager from §7?
