# Self-Study • §3.1–3.6, I do / You do

*Chapter 3 • Stoichiometry*  
Zumdahl §3.1–3.6 • PDF pp. 111–124 • work every YOUR TURN before moving on

[← all lessons](../index.md)

---

> 📌 **How to use these notes — read this first**
>
> Each skill comes as a **ladder** with two rungs. The solid-framed box
> is the **worked example**: read it slowly, with a pencil, reproducing
> each step. The dashed box is **YOUR TURN**: the same problem with new
> numbers, and no help.
> 
> 1. **Attempt the YOUR TURN completely** before looking at
>    anything. Write real work in the workspace, not fragments.
> 2. Check your result against the small gray *check:* line. Right
>    first try? Tick it on the tracker (last page) and climb on.
> 3. Wrong? **Re-read the worked example, then redo** — do not
>    stare at your first attempt. Full solutions are in the teacher key
>    if you are stuck after two tries.
> 
> These six sections build one idea: the **mole** is how chemists count
> particles by weighing — and everything else in Chapter 3 stands on it.

## Ladder 1 • Counting by weighing; average
atomic mass

`ZUM §3.1–3.2`

You cannot count atoms one at a time, but you can *weigh* them in
bulk — and if you know the average mass of one unit, a mass *is* a
count. That is the whole trick of the chapter. For atoms the “average
mass of one unit” is the tabulated atomic mass: a
**weighted average** over the natural isotopes,

$$ \bar m = \sum (\text{fractional abundance} \times \text{isotope mass}), $$

measured by a mass spectrometer, where **peak height gives
abundance**. No single atom has the average mass — there is no chlorine
atom weighing 35.45 u.

> 📘 **I do: the atomic mass of silver**
>
> Natural silver is 51.839% ¹⁰⁷Ag (106.905 u) and 48.161%
> ¹⁰⁹Ag (108.905 u). Compute the tabulated atomic mass.
> 
> $$ \bar m = (0.51839)(106.905) + (0.48161)(108.905) $$
> 
> $$ \phantom{\bar m} = 55.418 + 52.450 = \mathbf{107.87~u} $$
> 
> **Sanity checks, always both:** the result lies *between* the
> two isotope masses, and it leans toward ¹⁰⁷Ag — the more
> abundant isotope. An answer outside 106.905–108.905 means an abundance
> was dropped; an answer leaning the wrong way means the abundances were
> swapped.

> ✏️ **YOUR TURN 1**
>
> Natural gallium is 60.108% ⁶⁹Ga (68.926 u) and 39.892%
> ⁷¹Ga (70.925 u). Compute the atomic mass, and state both sanity
> checks. 
> 
> *(working space)*
> 
> > **check:** 69.72  — between the isotope masses, leaning toward
> ⁶⁹Ga

## Ladder 2 • Working backward to an
abundance

`ZUM §3.2`

Given the average and the isotope masses, the abundances follow from one
equation: if $x$ is the fraction of the lighter isotope, the fractions
must sum to 1, so the heavier one is $(1-x)$.

> 📘 **I do: the isotopes of boron**
>
> Boron has two isotopes, ¹⁰B (10.013 u) and ¹¹B
> (11.009 u), and a tabulated mass of 10.81 u. Find the percent abundances.
> 
> **Set up** with $x$ = fraction of ¹⁰B:
> 
> $$ x(10.013) + (1 - x)(11.009) = 10.81 $$
> 
> **Solve:**
> 
> $$ 11.009 - 0.996\,x = 10.81 \quad\Longrightarrow\quad    x = \frac{11.009 - 10.81}{11.009 - 10.013} = \frac{0.199}{0.996}    = 0.200 $$
> 
> So boron is **20.0% ¹⁰B and 80.0% ¹¹B**.
> 
> **Sanity check:** 10.81 sits much closer to 11.009 than to 10.013,
> so the heavy isotope had to dominate — and it does, four to one.

> ✏️ **YOUR TURN 2**
>
> Rubidium has two isotopes, ⁸⁵Rb (84.912 u) and ⁸⁷Rb
> (86.909 u), and a tabulated mass of 85.47 u. Find both percent
> abundances. 
> 
> *(working space)*
> 
> > **check:** 72.1% ⁸⁵Rb, 27.9% ⁸⁷Rb

## Ladder 3 • The mole

`ZUM §3.3`

One mole is $6.022\times10^{23}$ of anything — chosen so that one mole
of an element has a mass in grams numerically equal to its atomic mass in
u. Two conversions, and only two:

$$ \text{grams} \xrightarrow{\;\div M\;} \text{moles}    \xrightarrow{\;\times N_A\;} \text{particles} $$

and each arrow reverses ($\times M$; $\div N_A$) to run the other way.
Avogadro's number converts **moles to particles**, never grams to
particles directly.

> 📘 **I do: atoms in a foil strip**
>
> How many aluminum atoms are in a 10.0 g strip of foil
> ($M_{\text{Al}} = 26.98\,\mathrm{g/mol}$)?
> 
> **Grams to moles first:**
> 
> $$ \frac{10.0}{26.98} = 0.371\,\mathrm{mol}~\text{Al} $$
> 
> **Then moles to atoms:**
> 
> $$ 0.371 \times 6.022\times10^{23} = \mathbf{2.23\times10^{23}~atoms} $$
> 
> **Sense check:** a hand-sized object should hold a substantial
> fraction of a mole — $10^{23}$ is the right neighbourhood. An answer
> like $10^{2}$ or $10^{46}$ means a conversion was skipped or doubled.

> ✏️ **YOUR TURN 3**
>
> What is the mass of a sample containing $1.00\times10^{22}$ copper atoms
> ($M_{\text{Cu}} = 63.55\,\mathrm{g/mol}$)? 
> 
> *(working space)*
> 
> > **check:** 1.06 g

## Ladder 4 • Molar mass of a compound

`ZUM §3.4`

A compound's molar mass is the sum over the formula, *every
subscript honoured* — and once you have moles of the compound, the
subscripts also convert to moles of each element inside it.

> 📘 **I do: aluminum sulfate, down to the atoms**
>
> For Al₂(SO₄)₃: (a) the molar mass, (b) the moles in
> 10.0 g, (c) the number of oxygen *atoms* in that sample.
> 
> **(a)** The parentheses multiply everything inside:
> 
> $$ M = 2(26.98) + 3(32.07) + 12(16.00)      = 53.96 + 96.21 + 192.0 = 342.2\,\mathrm{g/mol} $$
> 
> (12 oxygens — $4 \times 3$ — not 4. Mis-reading parentheses is the
> single commonest molar-mass error.)
> 
> **(b)** $\dfrac{10.0}{342.2} = 0.0292\,\mathrm{mol}$
> 
> **(c)** Each formula unit carries 12 O atoms:
> 
> $$ 0.0292 \times 12 = 0.351\,\mathrm{mol}~\text{O}    \;\Rightarrow\; 0.351 \times 6.022\times10^{23}    = \mathbf{2.11\times10^{23}~atoms} $$

> ✏️ **YOUR TURN 4**
>
> For K₂Cr₂O₇ ($M_{\text{K}} = 39.10$, $M_{\text{Cr}} = 52.00$):
> (a) the molar mass, (b) the moles in 5.00 g, (c) the number of
> oxygen atoms in that sample. 
> 
> *(working space)*
> 
> > **check:** (a) 294.2 g/mol     (b) 0.0170 mol
>     (c) $7.16\times10^{22}$ O atoms

## Ladder 5 • Zumdahl's three questions

`ZUM §3.5`

Section 3.5 teaches no chemistry — it teaches the *approach* that
every multi-step problem in this book expects:

> 
**Where am I going?**     **What do I know?**    
**Does my answer make sense?**

Plan the route *before* touching the calculator, and check the
result *after*. The middle — arithmetic — is the easy part.

> 📘 **I do: the three questions, worked visibly**
>
> How many hydrogen atoms are in 8.52 g of ammonia, NH₃?
> 
> **Where am I going?** From grams of a compound to *atoms of one
> element inside it*. Route: grams $\to$ mol NH₃ $\to$ mol H (via the
> subscript) $\to$ atoms (via $N_A$). Three hops, planned before any
> arithmetic.
> 
> **What do I know?** $M_{\text{NH₃}} = 14.01 + 3(1.008) = 17.03\,\mathrm{g/mol}$; each NH₃ carries 3 H.
> 
> **Execute the plan:**
> 
> $$ \frac{8.52}{17.03} = 0.500\,\mathrm{mol}~\text{NH₃}    \;\xrightarrow{\times 3}\; 1.50\,\mathrm{mol}~\text{H}    \;\xrightarrow{\times N_A}\; \mathbf{9.04\times10^{23}~atoms} $$
> 
> **Does it make sense?** Half a mole of molecules, three H each —
> about 1.5 moles of H, so a bit more than $N_A$ atoms. Yes.

> ✏️ **YOUR TURN 5**
>
> What mass of oxygen is contained in 0.750 mol of CO₂?
> **First write the route as arrows** (no numbers), then execute, then
> state why the size of the answer is reasonable. 
> 
> *(working space)*
> 
> > **check:** route: mol CO₂ $\to$ mol O $\to$ g O; answer
> 24.0 g

## Ladder 6 • Percent composition

`ZUM §3.6`

Each element's mass percent is its share of the molar mass:

$$ \%~\text{element} =    \frac{n \times M_{\text{element}}}{M_{\text{compound}}} \times 100 $$

where $n$ is the subscript. The percents must total 100 (within
rounding) — that check is free, so always run it.

> 📘 **I do: aspirin, and a real tablet**
>
> Aspirin is C₉H₈O₄. Find the mass percent of each element, then the
> mass of carbon in one 500.0 mg tablet.
> 
> **Molar mass:**
> $M = 9(12.01) + 8(1.008) + 4(16.00) = 108.09 + 8.064 + 64.00 = 180.15\,\mathrm{g/mol}$
> 
> **Each element's share:**
> 
> $$ \%\text{C} = \frac{108.09}{180.15} \times 100 = 60.00\% \qquad    \%\text{H} = \frac{8.064}{180.15} \times 100 = 4.48\% $$
> 
> $$ \%\text{O} = \frac{64.00}{180.15} \times 100 = 35.53\% $$
> 
> **Total check:** $60.00 + 4.48 + 35.53 = 100.01$ — within rounding
> of 100 (each percent was rounded to two decimals). A total off by more
> than about $\pm 0.05$ is not rounding; it is an arithmetic slip.
> 
> **The tablet:** percent composition is a recipe for *any*
> sample size:
> 
> $$ m_{\text{C}} = 0.5000 \times 0.6000 = 0.300\,\mathrm{g}~\text{of carbon} $$

> ✏️ **YOUR TURN 6**
>
> Ammonium nitrate fertilizer is NH₄NO₃
> ($M = 80.05\,\mathrm{g/mol}$). Find the mass percent of each
> element (run the total check), then the mass of nitrogen in a
> 25.0 g scoop. 
> 
> *(working space)*
> 
> > **check:** 35.00% N, 5.04% H, 59.96% O (total 100.00); N in the scoop
> 8.75 g

## Mastery tracker

Tick a row only if your YOUR TURN was right on the *first* attempt.
Any unticked row: re-study that ladder's worked example before the next
session, then redo the problem from a blank page.

| **First try?** | **Skill** | **Ladder** | **If not, re-read…** |
|---|---|---|---|
| $\square$ | weighted-average atomic mass | 1 | silver; both sanity checks |
| $\square$ | abundances from the average | 2 | boron; the $(1-x)$ setup |
| $\square$ | grams–moles–particles | 3 | the two-conversion chain |
| $\square$ | molar mass; atoms inside a sample | 4 | the parentheses rule |
| $\square$ | planning before calculating | 5 | the three questions |
| $\square$ | percent composition | 6 | aspirin; the total check |

> 📌 **Scoring yourself honestly**
>
> 6/6 first-try: go straight on to the §3.7–3.11 self-study — these six
> skills are exactly what it assumes. 4–5: solid; redo the missed ladders
> tomorrow, not today. 3 or fewer: the gap is usually one of three habits
> — (1) grams never convert to particles directly, only through moles;
> (2) subscripts multiply, including through parentheses; (3) every answer
> gets a does-it-make-sense pass before you write it down. Fix the habit
> and the ladders fall together.

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
