# Guided Notes

*Chapter 1 • Chemical Foundations*  
Zumdahl §1.3–1.5, 1.7–1.10 • PDF pp. 27–68 • 1 block (Day 1)

[← all lessons](../index.md)

---

> 📌 **Why this chapter exists, and why it is only one block**
>
> **None of this is a CED topic. All of it is assumed on every CED
> topic.** Significant figures, dimensional analysis and density never appear
> in the framework as learning objectives — and they appear in almost every
> free-response question you will ever write.
> 
> That is why this is the **Day 1 launch block** rather than a unit:
> one block to establish the conventions, a scored diagnostic to find out who
> actually has them, and a remediation sheet for whoever needs it. There is no
> chapter test.
> 
> **Skipped:** §1.1–1.2 (overview and the scientific method) and
> §1.6 (a general problem-solving essay). Read them if you like; nothing
> is examined from them.
> 
> **Where this bites on the real exam:** AP readers deduct for
> significant-figure errors on calculated FRQ answers. It is one of the few
> places you can reason perfectly and still lose the point.

## Measurement, Uncertainty, and Units Zumdahl §1.3–1.5, 1.7–1.10

> 📌 **By the end you can…**
>
> - Count significant figures and apply them to calculations.
> - Convert units by dimensional analysis and use density as a
>    conversion factor.

**Read:** Zumdahl §1.3–1.5, 1.7–1.10 • PDF pp. 35–56

> 📌 **Retrieval warm-up**
>
> 1. How many significant figures in $0.0025$?
>    2
> 2. How many in $1.008$? 4
> 3. $25\,\mathrm{{}^\circ C}$ in kelvin: 298 K
> 4. Density $=$ mass $\div$ volume

#### INSTRUCTION A • Every measurement carries uncertainty 25 min

### Precision is not accuracy `ZUM §1.4`

`SP 2`

- Accuracy is how close a measurement is to the
   true value.
- Precision is how close repeated measurements are to
   one another.

> 📌 **Zumdahl's graduated cylinder**
>
> A student fills a cylinder to its 25-mL mark five times and measures what
> was actually delivered with a buret: 26.54, 26.51, 26.60, 26.49,
> 26.57 mL. Average: 26.54 mL.
> 
> The five readings agree closely — **excellent precision**, good
> technique. But every one is about 1.5 mL above 25, so the
> cylinder is **not accurate**. That constant offset is a
> systematic error.
> 
> **Precision indicates accuracy only when there is no systematic
> error.** A well-behaved set of repeated results can be reliably, repeatably
> wrong — which is why calibration matters and why AP asks about it in
> experimental-design questions.

### Counting significant figures `ZUM §1.5`

`SP 5`

Zumdahl's rules, which are the ones AP uses:

1. **Nonzero digits** always count.
2. **Leading zeros** (before all nonzero digits) are
   never significant — they only place the
   decimal. $0.0025$ has 2.
3. **Captive zeros** (between nonzero digits) are
   always significant. $1.008$ has
   4.
4. **Trailing zeros** are significant *only if there is a
   decimal point*. $100$ has 1;
   $100.$ has 3; $1.00\times10^{2}$ has
   3.
5. **Exact numbers** — from counting (8 molecules) or from
   definitions ($1~\text{in} \equiv 2.54~\text{cm}$) — have
   infinite significant figures and never limit a
   result.

> ⚠️ **AP trap**
>
> **Scientific notation removes the ambiguity, so use it.** Written as
> $2500$, the number could mean two, three or four significant figures and
> the reader cannot tell. Written as $2.5\times10^{3}$, $2.50\times10^{3}$ or
> $2.500\times10^{3}$, it is unambiguous.
> 
> When a question gives you a bare number like $100$, take it at the rules'
> word: one significant figure.

#### GUIDED PRACTICE • Counting 15 min

Give the number of significant figures:

1. $0.0105$ 3
2. $0.050080$ 5
3. $8.050\times10^{-3}$ 4
4. $45.20$ 4
5. $1200$ 2
6. $1.20\times10^{3}$ 3
7. $0.00300$ 3
8. $6.0\times10^{-5}$ 2

#### INSTRUCTION B • Significant figures in calculations 20 min

### Two different rules — do not mix them `ZUM §1.5`

`SP 5`

> 
**Multiply or divide:** the result keeps the fewest
**significant figures** of any factor.   

**Add or subtract:** the result keeps the fewest
**decimal places** of any term.

These are genuinely different rules, and using the multiplication rule on a
sum is the most common significant-figure error there is.

> 📘 **Worked example 1: the two rules side by side**
>
> **Multiplication.** $4.56 \times 1.4 = 6.384$. The limiting factor
> $1.4$ has two significant figures, so the answer is $\mathbf{6.4}$.
> 
> **Addition.** $12.11 + 18.0 + 1.013 = 31.123$. The limiting term
> $18.0$ has one decimal place, so the answer is $\mathbf{31.1}$ — which
> still has three significant figures. *Counting significant figures
> here would have given the wrong answer.*
> 
> **Subtraction, where it gets dramatic.**
> $25.64 - 25.6 = 0.04$. One decimal place, so the answer is
> $\mathbf{0.0}$. Two four-figure measurements produced a result with
> essentially no significant figures at all — subtracting nearly equal
> numbers destroys precision, which is exactly why titration and
> calorimetry procedures are designed to avoid it.

### Dimensional analysis `ZUM §1.7`

`SP 5`

Multiply by conversion factors arranged so unwanted units
cancel. The factor you need is whichever way up makes
that happen.

> 📘 **Worked example 2: a multi-step conversion**
>
> Convert 5.00 miles to kilometres, given
> $1~\text{mi} = 5280~\text{ft}$, $1~\text{ft} = 12~\text{in}$,
> $1~\text{in} = 2.54~\text{cm}$.
> 
> $$ 5.00~\text{mi} \times    \frac{5280~\text{ft}}{1~\text{mi}} \times    \frac{12~\text{in}}{1~\text{ft}} \times    \frac{2.54~\text{cm}}{1~\text{in}} \times    \frac{1~\text{m}}{100~\text{cm}} \times    \frac{1~\text{km}}{1000~\text{m}} = 8.0467\ldots $$
> 
> Track the cancellation by reading down the fractions: **mi** on top
> meets mi on the bottom, then ft meets ft, in meets in, cm meets cm, m meets
> m — each unit appears once above the line and once below, so all of them
> divide out and only **km** survives. If a unit does not appear on both
> sides, the factor is upside down.
> 
> Every conversion factor here is a *definition*, so all are exact and
> none limits the answer. Only the measured $5.00$ does, giving three
> significant figures: $\mathbf{8.05}~\text{km}$.

#### APPLICATION • Density, temperature, and matter 20 min

### Density is a conversion factor `ZUM §1.9`

`SP 5`

$$ d = \frac{m}{V} $$

Treat it as a conversion factor between mass and volume, not as a formula to
memorize — that is how it is used in every real problem.

1. Aluminium has $d = 2.70\,\mathrm{g/cm^3}$. Find
   the mass of 15.0 cm³.
   *(working space)*
2. A metal sample has mass 45.2 g. Dropped into a cylinder,
   the water level rises from 25.0 mL to
   41.7 mL. Find the density.
   *(working space)*

### Temperature and classification `ZUM §1.8, 1.10`

$$ K = {}^\circ\text{C} + 273.15 $$

Kelvin is the scale that matters: it appears in the gas laws, in
$\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$, and in every
equilibrium expression. 25 °C, the standard temperature, is
298 K.

| **Matter** |  |
|---|---|
|    Pure substances | **elements** (one kind of atom) and
  **compounds** (fixed ratio) |
|    Mixtures | **homogeneous** (uniform; a solution) and
  **heterogeneous** (visibly non-uniform) |

A physical change alters form but not identity (melting, dissolving);
a chemical change produces a
new substance.

> 📌 **Exit ticket**
>
> A student computes $100.0 + 0.005$ and reports $1\times10^{2}$, reasoning
> that “$0.005$ has only one significant figure, so the answer gets one.”
> Identify the error and give the correct answer.

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
