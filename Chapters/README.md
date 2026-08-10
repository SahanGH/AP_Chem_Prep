# Chapters — textbook-track materials

Materials that follow **Zumdahl's chapter sequence** rather than the CED unit
sequence. Same build system, same four variants, same conventions as the
unit folders — only the header word changes (`\apcunitword{Chapter}`).

## Why this track exists

The CED and the textbook disagree about order. Unit 1 alone pulls from
Zumdahl §3.2–3.7 and §7.5–7.12; Unit 3 draws on seven separate locations.
That's correct for AP exam preparation, but it means the book can't be read
straight through alongside the units.

These chapter materials cover a chapter on its own terms — useful for:

- assigning a chapter as coherent reading before the units that fracture it,
- foundation content the CED assumes but never tests directly
  (nomenclature is the big one),
- students who want the book's own narrative.

**They do not replace the unit materials.** Exam preparation follows the
units; see [PLAN.md](../PLAN.md).

## Built so far

| Folder | Zumdahl | PDF pp. | Contents |
|---|---|:---:|---|
| `chapter01-foundations` | §1.3–1.5, 1.7–1.10 | 27–68 | notes (**1 block**), scored diagnostic, remediation sheet — **no test** |
| `chapter02-atoms-molecules-ions` | §2.1–2.8 | 69–109 | notes (3 blocks), 2 worksheets, chapter test |
| `chapter03-stoichiometry` | §3.1–3.11 | 110–167 | notes (4 blocks), 3 worksheets, chapter test |
| `chapter04-reactions-solution-stoich` | §4.1–4.11 | 168–225 | **elaborated** notes (5 blocks), 4 worksheets, chapter test |
| `chapter05-gases` | §5.1–5.9 | 226–281 | **elaborated** notes (5 blocks), 3 worksheets, chapter test |
| `chapter06-thermochemistry` | §6.1–6.4 | 282–308 | **elaborated** notes (4 blocks), 3 worksheets, chapter test |
| `chapter07-atomic-structure` | §7.1–7.2, 7.5, 7.8–7.9, 7.11–7.12 | 331–389 | **elaborated** notes (4 blocks), 3 worksheets, chapter test |
| `chapter08-bonding` | §8.1–8.13 | 390–453 | **elaborated** notes (5 blocks), 3 worksheets, chapter test |
| `chapter09-covalent-orbitals` | §9.1 (CED) + §9.2–9.3 (enrichment) | 454–490 | notes (2 CED blocks + 1 enrichment), 2 worksheets, **short** chapter test |
| `chapter10-liquids-solids` | §10.1–10.8 | 491–530 | **elaborated** notes (5 blocks), 3 worksheets, chapter test |
| `chapter11-solutions` | §11.1–11.3 (CED) + §11.4–11.7 (enrichment) | 551–581 | notes (3 CED blocks + 1 enrichment), 3 worksheets, chapter test |
| `chapter12-kinetics` | §12.1–12.7 | 593–632 | **elaborated** notes (5 blocks), 3 worksheets, chapter test |
| `chapter13-equilibrium` | §13.1–13.7 | 650–695 | **elaborated** notes (5 blocks), 3 worksheets, chapter test |
| `chapter14-acids-bases` | §14.1–14.9 (CED) + §14.10–14.11 (enrichment) | 696–754 | **elaborated** notes (5 blocks), 3 worksheets, chapter test |
| `chapter15-acid-base-equilibria` | §15.1–15.5 (CED) + §15.6 (shape only) | 755–803 | **elaborated** notes (5 blocks), 3 worksheets, **long-FRQ** chapter test |
| `chapter16-solubility-equilibria` | §16.1 only (§16.2–16.3 skipped) | 805–813 | **elaborated** notes (4 blocks), **4 worksheets**, chapter test |
| `chapter17-thermodynamics` | §17.1–17.10 | 834–880 | **elaborated** notes (5 blocks), **4 worksheets**, **long-FRQ** chapter test |
| `chapter18-electrochemistry` | §18.1–18.4, 18.7–18.8 (§18.5–18.6 skipped) | 881–930 | **elaborated** notes (5 blocks), **4 worksheets**, **long-FRQ** chapter test |

## Coverage note for Chapter 1

**The Day 1 launch block.** Deliberately the smallest set in the corpus:
one notes block, a scored diagnostic, and a remediation sheet. **No chapter
test** — this is a placement instrument, not assessed content.

**Nothing here is a CED topic; all of it is assumed on every CED topic.**
Significant figures, dimensional analysis and density never appear as
learning objectives, and they appear in nearly every FRQ. AP readers deduct
for sig-fig errors on calculated answers — one of the few places a student
can reason perfectly and still lose the point. That mismatch is the entire
justification for the chapter.

`ch01-ws1` is the **scored 25-mark diagnostic** named in the PLAN.md
calendar (week 1, Monday). It carries a teacher scoring guide mapping score
bands to actions, and — more usefully — tells you to **read the pattern, not
the total**: a student who scores well but drops both marks on the
addition/subtraction items has one specific fixable misconception rather
than a general weakness. `ch01-ws2` is the remediation sheet you assign
based on that result.

**Skipped:** §1.1–1.2 (overview, scientific method) and §1.6 (a
problem-solving essay). Nothing is examined from them.

The one idea worth the block: **multiply/divide counts significant figures,
add/subtract counts decimal places, and they are different rules.**
`100.0 + 0.005 = 100.0` (four sig figs from a term with one) is the example
that makes the distinction impossible to fudge, and it is the exit ticket.

## Coverage note for Chapter 3

The front half (§3.1–3.7) overlaps CED Unit 1; the back half (§3.8–3.11) is
**Unit 4 content** — balancing, mass-to-mass calculations, limiting reactant,
percent yield — which students otherwise wouldn't meet until well into the
year. Teaching the whole chapter early front-loads the most reusable skill in
the course. Block 4 uses Zumdahl's own **BCA (Before/Change/After) tables**
(p. 146), which stay useful all the way through equilibrium in Unit 7.

## Coverage note for Chapter 2

Sections 2.1–2.5 (history, mass laws, early experiments) are **background**:
AP assesses the reasoning, not the names and dates. Sections 2.6–2.8 (ions,
formulas, nomenclature) are **prerequisite skills** — the CED never lists
them as topics but assumes them everywhere from Unit 4 onward. Naming is
worth drilling to fluency here; `ch02-ws2` is built for exactly that and is
designed to be done twice, timed on the second pass.

## Build

```powershell
.\build.ps1 Chapters\chapter02-atoms-molecules-ions
```

## Coverage note for Chapter 4

The single richest chapter in the book for AP purposes: nearly all of **CED
Unit 4 (Chemical Reactions)** lives here, and §4.1–4.3 backfill the solution
and molarity content of **Unit 3.7–3.8**. Three skills introduced here run
through the rest of the course — net ionic equations, oxidation states, and
solution stoichiometry (which becomes titration math in Unit 8).

These notes are written **elaborated**: fuller exposition and two or more
worked examples per idea, rather than the tighter style of Chapters 2–3.

§4.10's full half-reaction balancing in acidic/basic solution is marked
**ENRICHMENT** in Block 5 — the current CED asks students to *identify*
redox and balance simple cases, not to run H+/OH−/H2O bookkeeping. Useful
groundwork for Unit 9 electrochemistry, but not exam-tested.

## Coverage note for Chapter 5

Mostly **review** — §5.2–5.3, 5.5, 5.6 and 5.8 are CED topics 3.4–3.6,
already taught in Unit 3. Work this chapter for the two things Unit 3 does
not cover:

1. **§5.4 gas stoichiometry** — closes the loop between Chapter 3's mole
   ratios and gas volumes. The main reason to teach the chapter.
2. **Collecting a gas over water** (§5.5) — a standard lab technique that
   appears on the AP exam and is covered nowhere else in these materials.
   `P_gas = P_total − P_H2O`, with a vapour-pressure table in the notes.

**§5.7 Graham's law of effusion** is marked ENRICHMENT — not a current CED
topic, though the underlying "lighter means faster" idea certainly is.
**§5.10 atmospheric chemistry** is skipped entirely.

## Coverage note for Chapter 6

**The cleanest chapter-to-unit match in the book.** §6.1–6.4 is essentially
all of CED Unit 6, in the textbook's own order — no untangling required.
This is the one chapter that can genuinely serve as the unit.

Unit 6 adds only two topics from elsewhere, and both are callbacks to
material already taught: **energy of phase changes** (CED 6.5, §10.8) from
Unit 3 Block 2, and **bond enthalpies** (CED 6.7, §8.8) from Unit 2 Block 1.

§6.5–6.6 (present and new energy sources) are skipped — off-syllabus.

## Coverage note for Chapter 7

**The most scattered chapter, and the one with the most off-syllabus
content — roughly a third.** It splits across two CED units, so the notes
open with an explicit map rather than letting a student read straight
through:

- **§7.1–7.2** → Unit 3.11–3.12 (spectroscopy, photons)
- **§7.5, 7.8–7.9, 7.11** → Unit 1.5 (electron configuration)
- **§7.12** → Unit 1.6–1.7 (PES and periodic trends)

**Skip:** §7.3 (hydrogen line spectrum), §7.4 (Bohr model), §7.6 (quantum
numbers), §7.7 (orbital shapes in detail), §7.10 (periodic table history),
§7.13 (alkali metals). All were dropped in the 2019 redesign. The chapter
test states its scope explicitly so students know none of it is examined.

The notes build one deliberate through-line: the **photoelectric effect**
(Block 1) becomes the measuring principle for **PES** (Block 4), and the
**penetration argument** for why 2s lies below 2p (Block 2) is exactly what
PES peak positions confirm experimentally.

## Coverage note for Chapter 8

High value: nearly all of **CED Unit 2** lives here, and the chapter also
supplies two topics belonging to other units — **§8.4** (ions and ionic
radii) is CED 1.8, and **§8.8** (bond energies) is CED 6.7, the
bond-enthalpy topic Unit 6 borrows from this chapter.

For a student who has done Unit 2, Blocks 4–5 (Lewis structures, resonance,
VSEPR) are consolidation. The genuinely new material is **lattice energy**
(Block 2) and **computing ΔH from bond energies** (Block 3).

The bond-energy block is worth teaching carefully for one reason: its sign
convention is **broken − formed**, the reverse of Chapter 6's
products − reactants. Students who have just finished thermochemistry
reliably invert it, so the notes flag the reversal explicitly and give a
sanity check.

§8.6 (partial ionic character) is background reading only.

## Coverage note for Chapter 9

**The thinnest chapter in the book for AP purposes — only §9.1 is
examinable** (hybridization and σ/π bonding, CED 2.7). §9.2–9.5 develop
molecular orbital theory, which is entirely off the current CED.

This set is deliberately sized to match, rather than padded to look like the
others:

- Notes are **2 examinable blocks + 1 clearly marked enrichment block**.
  The enrichment block states on its face that skipping it costs nothing.
- The chapter test is **15 MCQ + 1 FRQ (25 pts, 35 min)** instead of the
  usual 20 + 2, and carries a scope note explaining why.
- `ch09-ws2` problem 3 is labelled OPTIONAL.

The enrichment block is included for one reason worth an hour: **MO theory
answers a question the Lewis model gets flatly wrong.** O₂'s Lewis structure
shows all electrons paired and predicts diamagnetism; liquid oxygen sticks
to a magnet. Seeing a model fail is worth more than another correct
prediction.

Zumdahl's own caution about dsp³ is quoted in Block 1 — he writes that the
model "does not give an accurate picture" and that newer work does not use
*d* orbitals at all. That is exactly why the CED stops at sp³.

## Coverage note for Chapter 10

Feeds **three** CED units, more than any other chapter:
§10.1 → Unit 3.1 (IMFs) · §10.2–10.3, 10.6–10.7 → Unit 3.2–3.3 (solids,
liquids, phases) · §10.4 → Unit 2.4 (metals and alloys) · §10.7 → Unit 2.3
(ionic solids) · **§10.8 → Unit 6.5**, the energy-of-phase-changes topic
Unit 6 borrows from here.

Two enrichment asides are marked inline: **unit-cell counting and density
calculations** (§10.3–10.4) and the **Clausius–Clapeyron equation**
(§10.8). Both are off the current CED — students are responsible for the
qualitative structures and for reading a heating curve, not for computing a
density from a unit-cell edge. The chapter test carries a scope note saying
so.

§10.9 (phase diagrams) is optional; a short treatment closes Block 5 because
it makes vapour pressure easier to picture, but it is not tested.

## Coverage note for Chapter 11

About **half the chapter is off-syllabus**. §11.1–11.3 (solution
composition, energetics of dissolving, factors affecting solubility) are
CED 3.7 and 3.10. §11.4–11.8 — vapour pressure lowering, boiling-point
elevation, freezing-point depression, osmotic pressure, colloids — are the
**colligative properties**, all dropped in the 2019 redesign.

Handled the same way as Chapter 9: three examinable blocks plus **one
clearly marked enrichment block**, with the chapter test scoped to
§11.1–11.3 and carrying a note saying so. `ch11-ws3` problem 6 is labelled
OPTIONAL.

**Molality** is defined in Block 1 even though it exists almost entirely to
serve colligative calculations — distinguishing it from molarity is what
sharpens the point that molarity uses *litres of solution*, which is a real
source of student error.

The most valuable examinable content is §11.2's **three-step energy model**.
It converts "like dissolves like" from a slogan into an argument: step 3 can
only repay step 2 when the new solute–solvent attractions match the
solvent–solvent attractions being broken. Zumdahl's oil-slick analysis is
worked through in full.

## Coverage note for Chapter 12

**Nothing here is off-syllabus.** Chapter 12 maps onto CED Unit 5 section by
section, in the textbook's own order — the cleanest one-to-one match in the
book alongside Chapter 6. You can assign "read Chapter 12" and mean it.

§12.1 → 5.1 · §12.2–12.3 → 5.2 · §12.4 → 5.3 · §12.5 → 5.4, 5.7–5.9 ·
§12.6 → 5.5, 5.6, 5.10 · §12.7 → 5.11.

One idea governs the chapter and the notes state it on page one:
**everything about a rate must be determined experimentally.** Orders cannot
be read off a balanced equation — Zumdahl's own `2 N2O5 → 4 NO2 + O2` has a
coefficient of 2 and is first order. The single exception is an *elementary
step*, where molecularity does give the order, and knowing which case you
are in is the whole skill.

## Coverage note for Chapter 13

Covers **CED 7.1–7.10** in the textbook's own order, with nothing
off-syllabus — about 80% of Unit 7.

**The gap:** Unit 7's last two topics, **7.11 solubility equilibria (Ksp)**
and **7.12 the common-ion effect**, are not in this chapter. They live in
§16.1 and §15.1 and must be picked up separately.

Two connections the notes make explicitly:

- **ICE tables are BCA tables from Chapter 3 with new labels.**
  Before/Change/After becomes Initial/Change/Equilibrium, the change row is
  still driven by coefficient ratios, and the only new idea is that the
  reaction stops partway so the change is an unknown *x*.
- **Coefficients become exponents in a K expression but never in a rate
  law.** Students meet both rules within two chapters, so the notes state
  the distinction directly: *K* describes a thermodynamic end state fixed by
  the overall equation; a rate law describes a mechanism.

## Coverage note for Chapter 14

The core of **CED Unit 8 (Acids and Bases, 11–15%)** — the second-heaviest
unit in the course. §14.1–14.9 are all examinable and map cleanly:
§14.1–14.2 → 8.1 · §14.3–14.4 → 8.1–8.2 · §14.5 → 8.3 · §14.6–14.7 → 8.4 ·
§14.8–14.9 → 8.5 and 8.10.

**Enrichment (marked inline, off the test):** §14.10 (acid–base properties
of oxides) and §14.11 (the Lewis model). The CED defines acids and bases
Brønsted–Lowry only; the Lewis model does not appear until coordination
chemistry, which is not on the framework at all.

**The gap:** Unit 8's back half — buffers (8.7–8.9), titration curves
(8.6), and indicators — is Chapter 15, not this chapter. Chapter 14 is the
prerequisite half.

Three things the notes work hard on because they are the reliable failure
points:

- **Strong is not concentrated.** Made numerical rather than asserted:
  0.10 M HCl gives pH 1.00, 0.10 M acetic acid gives pH 2.87, same
  concentration.
- **For a weak base, ICE `x` is [OH⁻], not [H⁺].** Reporting −log *x* as
  the pH turns a strongly basic answer into a strongly acidic one. Both
  `ch14-ws2` and the chapter test carry an error-analysis item on exactly
  this, and the rubrics award zero for it.
- **Dilution raises percent dissociation while also raising pH.** Students
  read these as contradictory; *x* falls as √C₀ while C₀ falls linearly, so
  the fraction grows even as the absolute [H⁺] shrinks.

Neutrality is defined throughout as **[H⁺] = [OH⁻]**, never as "pH 7" —
pure water at 50 °C has a pH below 7 and is still neutral, and both the
worksheet and the test ask for it.

## Coverage note for Chapter 15

**The chapter that finishes Unit 8**, and the natural sequel to Chapter 14:
§15.2 → CED 8.4 and 8.8–8.9 · §15.3 → 8.10 · §15.4–15.5 → 8.5.

**It also closes half of the gap left open by Chapter 13.** Unit 7's last
two topics were missing from the equilibrium chapter; **§15.1 supplies 7.12,
the common-ion effect**. **7.11 (Ksp)** and **8.11 (pH and solubility)**
both live in §16.1 — see Chapter 16 below, which closes them.

**§15.6 (polyprotic titrations)** is marked enrichment and scoped to shape
only: students should read a polyprotic curve and count the acidic protons
from the evenly spaced equivalence points, but multi-equivalence-point
calculations are off the framework.

The chapter test **deviates from the usual 20 MCQ + 2 short FRQ**: it
carries **20 MCQ + 1 long (10 pt) + 1 short (4 pt), 34 points in 60
minutes**. A complete titration is the canonical AP long-response topic and
cannot be assessed in four points. The scope note on the test says so.

One idea organizes the whole chapter, and the notes open with it: **a buffer
is a weak-acid equilibrium with the conjugate base already present, and a
titration is a stoichiometry problem followed by whatever equilibrium is
left over.** The skill is deciding which of the two you are in — which is
why the weak-acid titration is taught as a table of *four regions, four
different methods* rather than as one procedure.

Three deliberate teaching choices:

- **Stoichiometry first, then equilibrium**, stated as a numbered method and
  reinforced by an AP-trap box. Putting added strong base into an ICE table
  is the single most reliable way to lose every point on a buffer question,
  and both `ch15-ws2` and the test carry an error-analysis item on it.
- **The titration-curve figure is computed, not sketched.** Both curves come
  from an exact charge-balance solve, overlaid on one set of axes so the
  contrast is visible: same equivalence *volume*, different equivalence
  *pH* (7.00 against 8.72), and convergence afterwards once only excess
  \ce{NaOH} matters.
- **Rounding is addressed head-on.** Ammonium's p$K_a$ is 9.25 by one route
  and 9.26 by another, purely from rounding in the tabulated constants. The
  notes say so explicitly and tell students to pick a route and stay
  consistent rather than chase the last digit.

## Coverage note for Chapter 16

**The chapter that completes the CED.** §16.1 alone carries the last three
topics not sourced anywhere else: **7.11** (solubility equilibria and Ksp),
**7.12** (common-ion effect applied to solubility) and **8.11** (pH and
solubility). With this chapter built, every CED topic in Units 1–8 has
source material.

**Two-thirds of the chapter is skipped.** §16.2 (precipitation, selective
precipitation, qualitative analysis) and §16.3 (complex ion equilibria) are
off the framework entirely. A short $Q$-versus-$K_{sp}$ treatment closes
Block 4 because the reasoning is Unit 7 material students already own, but
it is marked enrichment and the chapter test does not assess it.

**One CED boundary drove real design decisions.** Topic 8.11 carries an
explicit **exclusion statement** — *computations of solubility as a function
of pH will not be assessed*. So pH-and-solubility is taught qualitatively
throughout, and every quantitative common-ion problem deliberately uses an
ion that is not pH-sensitive (F⁻, Cl⁻, SO₄²⁻, I⁻ — never a hydroxide in a
buffer). Reading the exclusion before writing killed one planned worked
example that would have taught an untested skill.

The set is **4 blocks and 4 worksheets** — more practice than usual against
less content, because Ksp is unusually calculational for its size and the
error modes are mechanical rather than conceptual.

The organizing sentence is Zumdahl's own: **"Ksp is an equilibrium constant;
solubility is an equilibrium position."** Students who treat the two words
as synonyms get every common-ion question wrong, so the distinction is
stated in Block 1, tested in an exit ticket, and revisited in every later
block.

Three mechanical traps the materials attack directly:

- **The coefficient is both a multiplier and an exponent.** For an MX₂ salt
  $K_{sp} = (s)(2s)^2 = 4s^3$; writing $s^3$ is wrong by a factor of 4.
  Worksheet 1 makes students find and quantify exactly that error.
- **Ksp values may be compared only at matching ion counts.** Zumdahl's
  CuS / Ag₂S / Bi₂S₃ example is used because the Ksp order is *exactly
  reversed* from the solubility order.
- **Adding the cation still leaves the anion doubled.** In CaF₂ with excess
  Ca²⁺, the $(2s)^2$ contributes a factor of 4 that students routinely drop
  — flagged inline as "the commonest slip in the whole chapter."

## Coverage note for Chapter 17

**The front half of Unit 9**, the last unit of the course: §17.1–17.2 →
CED 9.1 · §17.6 → 9.2 · §17.3–17.4, 17.7 → 9.3 · §17.9 → 9.5 · §17.5 →
9.6 · §17.10 → 9.7. Chapter 18 supplies electrochemistry (9.8–9.11).

**This chapter carries the sharpest textbook-vs-CED conflict in the
course, and the notes open with it.** Zumdahl's chapter is titled
"Spontaneity, Entropy, and Free Energy" and uses **spontaneous** on nearly
every page. The 2024 CED explicitly retires the word in favour of
**thermodynamically favored**, to stop students reading it as "suddenly" or
"without cause". The CED text is quoted directly in an AP-trap box on page
one, because a student following the textbook faithfully will otherwise
write the deprecated term on the exam. Every worksheet header repeats the
reminder.

**CED 9.4 (kinetic control) has no Zumdahl section at all.** Block 4 builds
it as a deliberate callback to Chapter 12 — which is the payoff for having
taught kinetics on the chapter track long before Unit 9. The CED's own
warning is made explicit: *a process that is not proceeding is not
necessarily at equilibrium*; if it is favored and nothing is happening, the
answer wanted is kinetic control.

**§17.8** (pressure dependence of *G*) and the derivations in **§17.10**
go beyond the framework; the examinable parts are folded into Blocks 4–5.

All thermodynamic data comes from **Zumdahl Appendix 4** (pp. 1145–1146),
not from memory, so students can look every value up in their own book.
Because the appendix rounds to whole kJ and whole J, the two routes to
ΔG° (ΔH° − TΔS° versus Σ ΔG*f*°) disagree by a kJ or two. Rather than hide
that, `ch17-ws2` problem 5 makes students compute both, notice the gap, and
explain it — and the exam FRQ awards a point for attributing it to rounding
rather than to an error.

Three things the materials attack directly:

- **Units.** ΔH° is in kJ and S° in J/K. Forgetting to convert inflates the
  TΔS° term a thousandfold, and there is a dedicated error-analysis item
  plus an exam MCQ on exactly that factor of 1000.
- **S° for an element is not zero.** Students carry the enthalpy convention
  across by habit. The third law gives entropy a true zero, so absolute
  entropies are tabulated — O₂(g) is 205 J/(K·mol), not 0.
- **Favored ≠ fast, and favored ≠ complete.** Both errors get their own
  worksheet item; the exam FRQ uses CO persisting in the atmosphere despite
  ΔG° = −514 kJ.

Water's crossover temperature works out to 370 K against a real boiling
point of 373 K. The notes use it as a landmark result and explain the 3 K
gap as table rounding rather than quietly adjusting the number.

The chapter test is **20 MCQ + 1 long (10 pt) + 1 short (4 pt), 34 points
in 60 minutes** — the same deviation as Chapter 15, for the same reason: a
full thermodynamic analysis (ΔS°, ΔG° two ways, crossover T, K) is a
standard AP long-response task and does not fit in four points.

## Coverage note for Chapter 18

**The last chapter of the course.** §18.1 → CED 9.8 · §18.2–18.3 → 9.9 ·
§18.4 → 9.10 · §18.7–18.8 → 9.11. With Chapter 17 it finishes Unit 9 — and
with it, **every topic in the CED now has source material.**

**Skip §18.5 (batteries) and §18.6 (corrosion)** — applications, not
framework topics.

**Two CED boundaries cut real material out of this chapter, and both are
stated on page one:**

1. **Never label an electrode positive or negative.** Topic 9.8 carries an
   explicit exclusion. The sign convention reverses between galvanic and
   electrolytic cells, so the exam avoids it entirely. Anode and cathode
   are taught instead, and `ch18-ws1` problem 7 makes students explain why
   "the anode is the negative electrode" should not appear on an AP answer.
2. **The Nernst equation is not required.** Topic 9.10 lists *no equation* —
   it asks for reasoning about how far the cell sits from equilibrium.
   Zumdahl §18.4 works the full Nernst calculation; that is enrichment.
   Block 4 teaches the Q-versus-K reasoning the CED actually assesses, and
   the test does not calculate a nonstandard potential.

**The most surprising CED statement in the whole framework lives here:**
*equilibrium arguments such as Le Châtelier's principle do not apply to
electrochemical systems, because the systems are not in equilibrium.*
Students arrive from Unit 7 with Le Châtelier as a reflex, and it is the
wrong tool — a running cell is held **away** from equilibrium, and that is
exactly where its voltage comes from. Both `ch18-ws3` and an exam distractor
target this directly.

Electrochemistry is where three earlier units converge: redox bookkeeping
from **Unit 4**, Q versus K from **Unit 7**, ΔG° from **Chapter 17**. An
electrolytic cell is literally CED 9.7's "external energy source driving an
unfavorable process," built in hardware.

Three mechanical traps the materials attack:

- **Scaling a half-reaction does not scale its voltage.** Doubling a
  half-reaction to balance electrons and doubling E° is the classic error;
  potential is intensive. Only *n* changes, and it enters later through
  ΔG° = −nFE°.
- **n comes from the balanced overall equation**, not from either
  half-reaction alone — and it is where two cells with identical voltages
  end up with very different ΔG°.
- **The electron ratio in Faraday problems is not always 2.** Ag⁺ needs
  one, Cu²⁺ two, Al³⁺ three. `ch18-ws4` makes students quantify the error
  from skipping the division.

All potentials come from **Zumdahl Table 18.1** (p. 887). The Daniell cell
works out to exactly the 1.10 V Zumdahl reports measuring, which the notes
use as a confidence check on the whole method.
