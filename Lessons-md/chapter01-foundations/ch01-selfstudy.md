# Self-Study • Chapter 1, I do / You do

*Chapter 1 • Chemical Foundations*  
Zumdahl §1.1–1.10 • PDF pp. 31–57 • four YOUR TURN questions per ladder

[← all lessons](../index.md)

---

> 📌 **How to use these notes — read this first**
>
> Each skill is a **ladder**: a fully worked example in the
> solid-framed box, then **four** YOUR TURN questions in the dashed
> box — same skill, new numbers, no help.
> 
> 1. **Work all four** before checking anything.
> 2. Check against the gray *check:* line. All four right on the
>    first try earns the tick on the tracker (last page).
> 3. Any misses: re-read the worked example, then redo the missed ones
>    from a blank page.
> 
> **Why this chapter deserves real effort.** Nothing here is
> difficult, and that is exactly the trap: these are the habits every later
> chapter assumes. A stoichiometry answer with the wrong number of
> significant figures, or a gas law worked in °C, loses the mark
> no matter how good the chemistry was. Get these seven skills automatic
> now and they cost you nothing for the rest of the year.

## Ladder 1 • Units, prefixes, and scientific
notation

`ZUM §1.3`

SI gives each quantity one base unit; prefixes scale it by powers of ten.

| **Prefix** | **Symbol** | **Factor** | **Example** |
|---|---|---|---|
| kilo | k | $10^{3}$ | 1 | thinsp;kg $= 1000\,\mathrm{g}$ |
| centi | c | $10^{-2}$ | 1 | thinsp;cm $= 0.01\,\mathrm{m}$ |
| milli | m | $10^{-3}$ | 1 | thinsp;mL $= 0.001\,\mathrm{L}$ |
| micro | $\mu$ | $10^{-6}$ |  | micro;L |
| nano | n | $10^{-9}$ | — |

Volume has a useful identity worth memorizing outright:

$$ 1\,\mathrm{mL} = 1\,\mathrm{cm^3} $$

> 📘 **I do: moving between prefixes**
>
> **(a) Convert 4.50 kg to milligrams.** Go through the
> base unit rather than guessing an exponent:
> 
> $$ 4.50~\text{kg} \times \frac{1000~\text{g}}{1~\text{kg}}    \times \frac{1000~\text{mg}}{1~\text{g}}    = \mathbf{4.50\times10^{6}~mg} $$
> 
> **(b) Convert 250 nm to metres.**
> 
> $$ 250 \times 10^{-9} = \mathbf{2.50\times10^{-7}~m} $$
> 
> **(c) Express 0.0000345 L in scientific notation and
> in microlitres.** Move the point until one non-zero digit sits to its
> left:
> 
> $$ 3.45\times10^{-5}~\text{L}    = 3.45\times10^{-5} \times 10^{6}~\mathrm{\mu L}    = \mathbf{34.5}~\mathrm{\mu L} $$
> 
> **The check that catches sign errors:** a *smaller* unit must
> give a *bigger* number. Milligrams are tiny, so (a) had to grow;
> metres are large, so (b) had to shrink.

> ✏️ **YOUR TURN 1 — four questions**
>
> 1. 3.20 cm in metres: 
>    *(working space)*
> 2. 75 mL in litres, and in cm³:
>    *(working space)*
> 3. 0.00845 g in scientific notation, and in milligrams:
>    *(working space)*
> 4. 2.6 km in centimetres: 
>    *(working space)*
> 
> > **check:** (a) 0.0320 m     (b) 0.075 L $=$
> 75 cm³     (c) $8.45\times10^{-3}$ g $=$
> 8.45 mg     (d) $2.6\times10^{5}$ cm

## Ladder 2 • Precision, accuracy, and
uncertainty

`ZUM §1.4`

Two words that are not synonyms:

|  | **Definition** | **Poor when** |
|---|---|---|
| **Accuracy** | closeness to the *true* value | there is a systematic error |
| **Precision** | closeness of repeats to *each other* | there is random scatter |

A miscalibrated balance gives readings that agree beautifully with each
other and are all wrong: **precise but inaccurate**. That
combination is the signature of systematic error, and no amount of
repeating fixes it — only recalibration does.

Every measurement carries one **estimated** final digit. Reading a
burette marked every 0.1 mL, you record
23.46 mL: three certain digits and one estimated.

> 📘 **I do: judging a data set**
>
> Three students each mass the same object four times. The true mass is
> 4.000 g.
> 
> | **Student** | **Readings (g)** | **Mean** | **Verdict** |
> |---|---|---|---|
> | A | 3.998, 4.001, 3.999, 4.002 | 4.000 | accurate *and* precise |
> | B | 4.512, 4.510, 4.511, 4.513 | 4.512 | precise, not accurate |
> | C | 3.85, 4.15, 3.92, 4.08 | 4.00 | accurate on average, not precise |

**Student B** is the instructive case: the readings agree to
0.001 g, so the technique is excellent, but every one is high
by about 0.51 g. That is a systematic error — a balance that
was not zeroed. Repeating the measurement a hundred times would not
reveal it; only checking against a known standard would.

**Student C** shows why a good mean is not proof of a good
experiment: the average lands on 4.00 by luck of cancellation, while no
individual reading is close.

> ✏️ **YOUR TURN 2 — four questions**
>
> 1. A thermometer reads 2.0 °C too high every time. Which
>    is affected, accuracy or precision?
>    *(working space)*
> 2. Readings 25.1, 25.9, 24.8, 25.6 with a true value of
>    25.4 °C: describe both qualities.
>    *(working space)*
> 3. A burette is marked every 0.1 mL. How many
>    decimal places should you record, and why?
>    *(working space)*
> 4. Which type of error can be reduced by averaging more trials, and
>    which cannot?
>    *(working space)*
> 
> > **check:** (a) accuracy only     (b) accurate on average, imprecise
>     (c) two — estimate one digit past the smallest marking    
> (d) random can be averaged down; systematic cannot

## Ladder 3 • Counting significant figures

`ZUM §1.5`

1. Non-zero digits always count.
2. Zeros *between* non-zeros count (captive): 1005 has 4.
3. Leading zeros never count — they only place the decimal:
   0.0042 has 2.
4. Trailing zeros count **only if a decimal point is
   present**: 100 has 1, but 100. has 3 and 100.0 has 4.
5. **Exact numbers** — counted objects and definitions — have
   infinite significant figures and never limit an answer.

> 📘 **I do: counting, including the awkward cases**
>
> | **Number** | **Sig figs** | **Why** |
> |---|---|---|
> | 0.00560 | 3 | leading zeros place only; the trailing 0 counts |
> | 9004 | 4 | captive zeros count |
> | 2500 | 2 | no decimal point, so trailing zeros do not count |
> | 2500. | 4 | the decimal point makes them count |
> | $2.50\times10^{3}$ | 3 | scientific notation removes all ambiguity |
> | 12 eggs | exact | counted, not measured |
> | 1 | thinsp;kg $=$ 1000 | thinsp;g | exact | a definition |

**The lesson in rows 3–5:** “2500” is genuinely ambiguous in
ordinary writing. Scientific notation is not decoration — it is how you
say precisely how many digits you mean.

> ✏️ **YOUR TURN 3 — four questions**
>
> Give the number of significant figures:
> 
> 1. 0.03080     and     40.0 
>    *(working space)*
> 2. 6000     and     6000. 
>    *(working space)*
> 3. $7.20\times10^{-4}$     and     1.0090 
>    *(working space)*
> 4. How many significant figures does the “60” carry in
>    “1 min $=$ 60 s”? Explain.
>    *(working space)*
> 
> > **check:** (a) 4 and 3     (b) 1 and 4     (c) 3 and 5    
> (d) exact — infinite, because it is a definition

## Ladder 4 • Calculating with significant
figures

`ZUM §1.5`

Two rules, and they are different. Mixing them is the single commonest
error in this chapter.

> 
**Multiply / divide** $\Rightarrow$ count **significant
figures**; the answer takes the fewest.  

**Add / subtract** $\Rightarrow$ count **decimal places**; the
answer takes the fewest.

And one procedural rule: in a multi-step calculation, **round only
at the end**. Rounding intermediates lets error accumulate.

> 📘 **I do: both rules, and a subtraction that surprises**
>
> **(a) $6.221 \times 5.2$.** Multiplication, so count sig figs:
> 4 and 2, fewest is 2.
> 
> $$ 6.221 \times 5.2 = 32.3492 \to \mathbf{32} $$
> 
> **(b) $18.7 + 2.34 + 0.891$.** Addition, so count *decimal
> places*: 1, 2, 3 — fewest is 1.
> 
> $$ 18.7 + 2.34 + 0.891 = 21.931 \to \mathbf{21.9} $$
> 
> Note the answer has 3 sig figs while one input had only 3 and another had
> 4 — with addition, sig figs are not what governs.
> 
> **(c) $8.55 - 8.32$.** Both inputs have 3 sig figs, but subtraction
> counts decimal places (2 each):
> 
> $$ 8.55 - 8.32 = \mathbf{0.23} $$
> 
> The answer has only **2** significant figures. Subtracting nearby
> numbers destroys precision — which is why a titration's
> *difference* of two burette readings is the weak link in the
> measurement.

> ✏️ **YOUR TURN 4 — four questions**
>
> 1. $4.12 \times 0.20$ 
>    *(working space)*
> 2. $105.6 + 3.27$ 
>    *(working space)*
> 3. $\dfrac{27.9}{1.3}$ 
>    *(working space)*
> 4. $12.00 - 11.61$ — give the answer and say how many significant
>    figures survived.
>    *(working space)*
> 
> > **check:** (a) 0.82     (b) 108.9     (c) 21     (d) 0.39, only
> 2 sig figs

## Ladder 5 • Dimensional analysis

`ZUM §1.6–1.7`

Write every conversion as a fraction, arranged so the unit you have
cancels. If the units come out right, the arithmetic is almost certainly
right too — and if they do not, no amount of correct arithmetic will
save the answer.

> 📘 **I do: a two-step conversion, units first**
>
> A car's fuel use is 7.60 L per 100 km. How many
> litres for a 450 km trip? Then: how many millilitres per
> kilometre?
> 
> **Set up so kilometres cancel:**
> 
> $$ 450~\text{km} \times \frac{7.60~\text{L}}{100~\text{km}}    = \mathbf{34.2~L} $$
> 
> The kilometres cancel top and bottom, leaving litres — which is what
> was asked, so the setup is right.
> 
> **Second part, chaining two factors:**
> 
> $$ \frac{7.60~\text{L}}{100~\text{km}}    \times \frac{1000~\text{mL}}{1~\text{L}}    = \mathbf{76.0~mL/km} $$
> 
> **Sense check:** 450 km is 4.5 times the 100 km reference, and
> $4.5 \times 7.60 = 34.2$. The dimensional setup and the mental estimate
> agree.

> ✏️ **YOUR TURN 5 — four questions**
>
> Use 1 inch $=$ 2.54 cm (exact) where needed.
> 
> 1. Convert 12.0 inches to centimetres: 
>    *(working space)*
> 2. Convert 5.00 m to inches: 
>    *(working space)*
> 3. A tap fills 2.5 L in 40 s. How long to
>    fill 15 L?
>    *(working space)*
> 4. In question (b), which unit had to cancel, and where did you
>    place it to make that happen?
>    *(working space)*
> 
> > **check:** (a) 30.5 cm     (b) 197 in    
> (c) 240 s (4.0 min)     (d) centimetres, placed in the
> denominator

## Ladder 6 • Temperature and density

`ZUM §1.8–1.9`

$$ T_{\text{K}} = T_{^\circ\text{C}} + 273.15 \qquad    T_{^\circ\text{C}} = \frac{5}{9}\left(T_{^\circ\text{F}} - 32\right)    \qquad d = \frac{m}{V} $$

Celsius and Kelvin degrees are the *same size* — only the zero
moves — so a temperature *difference* is numerically identical in
both. Fahrenheit degrees are a different size, which is why its
conversion needs both a factor and an offset.

Density is a conversion factor between mass and volume, usable in either
direction. Water is 1.00 g/mL, which makes it the
reference for whether something floats.

> 📘 **I do: temperature, then density both ways**
>
> **(a) Convert -40 °C to kelvin and to Fahrenheit.**
> 
> $$ T_{\text{K}} = -40 + 273.15 = \mathbf{233~K} $$
> 
> $$ T_{^\circ\text{F}} = \frac{9}{5}(-40) + 32 = -72 + 32 =    \mathbf{-40~^\circ F} $$
> 
> The famous coincidence: $-40$ is the one temperature where the two
> scales read alike.
> 
> **(b) A metal cube of side 2.00 cm has a mass of
> 86.4 g. Find its density.**
> 
> $$ V = (2.00)^3 = 8.00\,\mathrm{cm^3} \qquad    d = \frac{86.4}{8.00} = \mathbf{10.8~g/cm^3} $$
> 
> **(c) What volume would 250. g of that metal occupy?**
> Run the density backward:
> 
> $$ V = \frac{m}{d} = \frac{250.}{10.8} = \mathbf{23.1~cm^3} $$

> ✏️ **YOUR TURN 6 — four questions**
>
> 1. Convert 25 °C to kelvin, and 350 K to
>    °C:
>    *(working space)*
> 2. A liquid has mass 45.0 g and volume
>    57.0 mL. Find its density, and say whether it
>    floats on water.
>    *(working space)*
> 3. Find the mass of 125 mL of ethanol
>    ($d = 0.789\,\mathrm{g/mL}$):
>    *(working space)*
> 4. A reaction warms a solution by 12 °C. By how many
>    kelvin did it warm? Explain in one line.
>    *(working space)*
> 
> > **check:** (a) 298 K; 77 °C     (b)
> 0.789 g/mL, floats     (c) 98.6 g
>     (d) 12 K — the degrees are the same size

## Ladder 7 • Classifying matter

`ZUM §1.10`

> 
matter $\to$ **pure substance** (element or compound)
    or     **mixture** (homogeneous or heterogeneous)

The dividing question is whether the sample has **fixed
composition**. A compound always has it; a mixture does not — brass can
be any proportion of copper and zinc.

A homogeneous mixture (a solution) is uniform throughout;
a heterogeneous one has visibly distinct regions. And the way you
separate them tells you which you had: mixtures come apart by
**physical** means (filtration, distillation, chromatography),
compounds only by **chemical** means.

> 📘 **I do: classify, then justify by separation**
>
> **Air** — a homogeneous *mixture*. Its composition varies
> with place and altitude, and it separates by fractional distillation,
> which is physical.
> 
> **Water** — a *compound*. Always 11.2% hydrogen by mass
> wherever it comes from, and splitting it needs electrolysis, which is
> chemical.
> 
> **Sand in water** — a heterogeneous *mixture*: the regions
> are visible, and filtration separates them.
> 
> **Copper wire** — an *element*: it cannot be broken into
> anything simpler by any means.
> 
> **The reasoning to imitate:** name the category, then justify it
> twice — once by composition, once by how it separates.

> ✏️ **YOUR TURN 7 — four questions**
>
> Classify each and give the separation method or reason:
> 
> 1. table salt, NaCl 
>    *(working space)*
> 2. Italian salad dressing 
>    *(working space)*
> 3. filtered seawater 
>    *(working space)*
> 4. Is dissolving sugar in water a physical or chemical change?
>    Justify.
>    *(working space)*
> 
> > **check:** (a) compound     (b) heterogeneous mixture    
> (c) homogeneous mixture — separate by distillation    
> (d) physical — the sugar is unchanged and recoverable

## Mastery tracker

Tick a row only if **all four** YOUR TURN questions were right on
the first attempt.

| **First try?** | **Skill** | **Ladder** | **If not, re-read…** |
|---|---|---|---|
| $\square$ | units, prefixes, scientific notation | 1 | smaller unit,
  bigger number |
| $\square$ | precision vs. accuracy | 2 | the systematic-error case |
| $\square$ | counting significant figures | 3 | the trailing-zero rule |
| $\square$ | calculating with sig figs | 4 | sig figs vs. decimal
  places |
| $\square$ | dimensional analysis | 5 | arrange so units cancel |
| $\square$ | temperature and density | 6 | differences vs. values |
| $\square$ | classifying matter | 7 | fixed composition? |

> 📌 **Scoring yourself honestly**
>
> 7/7: you are ready for Chapter 2 — and, more usefully, for every
> calculation in the course. 5–6: redo the missed ladders tomorrow, not
> today. 4 or fewer: the misses are almost certainly in Ladders 3–4,
> which is worth knowing, because significant figures cost marks in every
> later chapter and are the cheapest marks in the course to secure. Redo
> those two before anything else.

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
