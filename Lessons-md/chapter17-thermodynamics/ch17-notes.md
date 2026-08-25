# Guided Notes

*Chapter 17 • Entropy and Free Energy*  
Zumdahl §17.1–17.10 • PDF pp. 834–880 • 5 blocks

[← all lessons](../index.md)

---

> 📌 **How this chapter fits the AP course**
>
> This is the **front half of Unit 9**, the last unit of the course:
> §17.1–17.2 $\to$ CED 9.1, §17.6 $\to$ 9.2, §17.3–17.4 and 17.7
> $\to$ 9.3, §17.9 $\to$ 9.5, §17.5 $\to$ 9.6, §17.10 $\to$ 9.7.
> Chapter 18 supplies the electrochemistry half (9.8–9.11).
> 
> Kinetic control (**9.4**) has no Zumdahl section of its own — it is a
> deliberate callback to Chapter 12, and Block 4 makes it.
> 
> §17.8 (pressure dependence of $G$) and the derivations in §17.10 go
> beyond the framework; the parts you need are folded into Blocks 4 and 5.
> 
> **This chapter answers a question Chapter 12 could not.** Kinetics told
> you *how fast*; equilibrium told you *how far*. Neither told you
> *why* a reaction runs one way at all. That is what free energy is for.

> ⚠️ **AP trap**
>
> **Read this before anything else: the textbook and the exam use
> different words.**
> 
> Zumdahl's chapter is titled “Spontaneity, Entropy, and Free Energy” and
> uses spontaneous on nearly every page. The 2024 CED explicitly
> retires that word:
> 
> > “Historically, the term *spontaneous* has been used to describe
> > processes for which $\Delta G^\circ  favored* is preferred instead, so that common misunderstandings (equating
> > `spontaneous' with `suddenly' or `without cause') can be avoided.”
> 
> Read “spontaneous” in the textbook; write **“thermodynamically
> favored”** on the exam. They mean the same thing — $\Delta G^\circ  — and neither means fast, sudden, or uncaused. A thermodynamically favored
> reaction may take a million years.

## Entropy and the Second Law Zumdahl §17.1–17.2

> 📌 **By the end you can…**
>
> - Identify the sign and relative magnitude of an entropy change.
> - State the second law and explain what it predicts.

**Read:** Zumdahl §17.1–17.2 • PDF pp. 835–843

> 📌 **Retrieval warm-up**
>
> 1. Sign of $\Delta H$ for an exothermic reaction:
>    negative
> 2. Which phase has the most freedom of motion?
>    gas
> 3. At constant $P$, $q$ equals: $\Delta H$
> 4. Raising the temperature of a gas does what to the spread of
>    molecular speeds? broadens it

#### INSTRUCTION A • What entropy actually measures 25 min

### Dispersal, not disorder `ZUM §17.1`

`SP 6`

Entropy ($S$) measures how **dispersed** the matter and energy
of a system are — how many microscopic arrangements produce the same
macroscopic state. The more ways there are, the higher the entropy.

“Disorder” is the usual shorthand and it is a poor one: a messy bedroom is
not a thermodynamic state. Think *spread out*, in two senses the CED
names separately:

- **Matter disperses.** Particles occupy a larger volume or move
   more freely.
- **Energy disperses.** At higher temperature the distribution of
   molecular kinetic energies broadens, so the
   energy is spread over more states.

### The four situations you must recognize `ZUM §17.1`

| **Change** | **$\Delta S$** | **Why** |
|---|---|---|
| solid $\to$ liquid $\to$ gas | **positive** | particles freer, larger
  volume |
| gas expands (constant $T$) | **positive** | same particles, more space |
| temperature rises | **positive** | energy spread over more states |
| moles of gas increase | **positive** | the dominant term in a
  reaction |

> ⚠️ **AP trap**
>
> **For a reaction, count moles of gas first.** Gases carry far more
> entropy than liquids or solids, so $\Delta n_{\text{gas}}$ almost always
> decides the sign. Compare the standard entropies:
> H₂O(l) is 70 J/K/mol but H₂O(g) is
> 189 J/K/mol — the same substance, nearly triple.
> 
> Only when $\Delta n_{\text{gas}} = 0$ do you look at anything else.

#### GUIDED PRACTICE • Predicting the sign 15 min

Give the sign of $\Delta S^\circ$ and the reason:

1. CaCO₃(s) → CaO(s) + CO₂(g)
   positive — 0 to 1 mol gas
2. N₂(g) + 3H₂(g) → 2NH₃(g)
   negative — 4 to 2 mol gas
3. 2H₂(g) + O₂(g) → 2H₂O(l)
   negative — 3 mol gas to 0
4. H₂O(s) → H₂O(l)
   positive — solid to liquid
5. 2NO₂(g) → N₂O₄(g)
   negative — 2 to 1 mol gas

#### INSTRUCTION B • The second law 20 min

### The universe, not the system `ZUM §17.2`

`SP 6`

> 
**Second law of thermodynamics:** in any thermodynamically favored
process, the entropy of the *universe* increases.   

$\Delta S_{\text{univ}} = \Delta S_{\text{sys}} + \Delta S_{\text{surr}} > 0$

The system's entropy is allowed to decrease — water
freezes, ammonia forms, life builds ordered structures — provided the
surroundings gain more than the system loses.

The surroundings gain entropy when the system releases heat to them, and how
much they gain depends on temperature:

$$ \Delta S_{\text{surr}} = -\frac{\Delta H}{T} $$

> 📌 **Why the same heat matters more when it is cold**
>
> The $T$ in the denominator is doing real work. Dumping
> 1 kJ into cold surroundings is a large fractional increase in
> their energy dispersal; the same kilojoule into hot surroundings barely
> registers.
> 
> That is why **exothermicity is a strong driving force at low
> temperature and a weak one at high temperature** — and it is the reason
> water freezes below 0 °C but melts above it, with no change in
> $\Delta H$ or $\Delta S$ at all.

#### APPLICATION • Reasoning with the second law 20 min

1. Water freezing has $\Delta S_{\text{sys}} 
2. A living organism builds highly ordered molecules from simple ones.
   Does this violate the second law? 

> 📌 **Exit ticket**
>
> State the sign of $\Delta S_{\text{sys}}$, of $\Delta S_{\text{surr}}$, and
> of $\Delta S_{\text{univ}}$ for the combustion of methane at room
> temperature.

## Calculating Entropy Changes Zumdahl §17.6

> 📌 **By the end you can…**
>
> - Calculate $\Delta S^\circ$ from absolute (standard molar) entropies.
> - Explain why absolute entropies exist but absolute enthalpies do not.

**Read:** Zumdahl §17.6 • PDF pp. 851–855

> 📌 **Retrieval warm-up**
>
> 1. Sign of $\Delta S^\circ$ when moles of gas increase:
>    positive
> 2. $\Delta S_{\text{surr}} =$ $-\Delta H/T$
> 3. Units of $S^\circ$: J/(K$\cdot$mol)

#### INSTRUCTION A • Absolute entropies 25 min

### The third law makes a real zero possible `ZUM §17.6`

`SP 5`

The third law of thermodynamics says a perfect crystal at
0 K has an entropy of exactly zero. That
gives entropy a genuine origin, so every substance has an
absolute entropy $S^\circ$ — a positive number, tabulated
directly.

> ⚠️ **AP trap**
>
> Contrast this with enthalpy. There is no absolute $H$, so tables list
> $\Delta H_f^\circ$, the enthalpy *of formation*, and elements in their
> standard states are assigned zero by convention.
> 
> Entropy tables are different: **$S^\circ$ for an element is not zero**.
> O₂(g) has $S^\circ = 205\,\mathrm{J/K/mol}$. Setting
> element entropies to zero out of habit is a reliable way to lose a point.

$$ \boxed{\;\Delta S^\circ_{\text{reaction}} = \sum n S^\circ_{\text{products}}    - \sum n S^\circ_{\text{reactants}}\;} $$

Note the coefficients multiply, exactly as in Hess's law — and note the
units: $S^\circ$ is in **joules** while $\Delta H^\circ$ is in
**kilojoules**. Mixing them is the single most common arithmetic error
in this unit.

> 📘 **Worked example 1: decomposing limestone**
>
> CaCO₃(s) → CaO(s) + CO₂(g)
> $S^\circ$: CaCO₃ 93, CaO 40, CO₂ 214
> J/K/mol.
> 
> $$ \Delta S^\circ = (40 + 214) - (93) = \mathbf{+161}~    \mathrm{J/K} $$
> 
> Positive, as predicted — a gas appeared where there was none.

> 📘 **Worked example 2: the Haber process**
>
> N₂(g) + 3H₂(g) → 2NH₃(g)
> $S^\circ$: N₂ 192, H₂ 131, NH₃ 193.
> 
> $$ \Delta S^\circ = 2(193) - [192 + 3(131)]    = 386 - 585 = \mathbf{-199}~\mathrm{J/K} $$
> 
> Four moles of gas became two, so the sign had to be negative. Notice the
> coefficient of 3 on hydrogen — dropping it gives $-68$ and the wrong
> magnitude entirely.

#### GUIDED PRACTICE • Running the sums 15 min

$S^\circ$ values (J/K/mol): H₂ 131,
O₂ 205, H₂O(l) 70, H₂O(g) 189, NO₂ 240,
N₂O₄ 304.

1. 2H₂(g) + O₂(g) → 2H₂O(l): 
   *(working space)*
2. H₂O(l) → H₂O(g): $+119$ J/K
3. 2NO₂(g) → N₂O₄(g): $-176$ J/K

#### APPLICATION • Interpreting the numbers 20 min

1. For H₂O(l) → H₂O(g), $\Delta S^\circ = +119$ J/K while
   $\Delta H^\circ = +44$ kJ. Explain what each sign says about
   whether the process is favored at 25 °C.
   
2. Why is $S^\circ$ for H₂O(g) nearly triple that for
   H₂O(l), when it is the same substance?
   
3. A student computes $\Delta S^\circ$ for the Haber process as
   $193 - (192 + 131) = -130$ J/K. Find both errors.
   

> 📌 **Exit ticket**
>
> Why can a table list an absolute $S^\circ$ for oxygen gas but not an
> absolute $H^\circ$?

## Gibbs Free Energy Zumdahl §17.3–17.4, 17.7

> 📌 **By the end you can…**
>
> - Calculate $\Delta G^\circ$ two ways and judge thermodynamic
>    favorability.
> - Predict the temperature conditions under which a process is favored.

**Read:** Zumdahl §17.3–17.4, 17.7 • PDF pp. 843–851, 855–860

> 📌 **Retrieval warm-up**
>
> 1. $\Delta S^\circ$ for CaCO₃(s) → CaO(s) + CO₂(g):
>    $+161$ J/K
> 2. $\Delta S_{\text{univ}}$ must be what sign for a favored process?
>    positive
> 3. Units of $S^\circ$ versus $\Delta H^\circ$:
>    J/(K$\cdot$mol) versus kJ/mol
> 4. The AP term replacing “spontaneous”:
>    thermodynamically favored

#### INSTRUCTION A • One number that decides 25 min

### Folding the surroundings into the system `ZUM §17.4`

`SP 5`

Judging favorability from $\Delta S_{\text{univ}}$ means tracking the
surroundings, which is a nuisance. Gibbs free energy removes the
need:

$$ G = H - TS \qquad\Longrightarrow\qquad    \boxed{\;\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ\;} $$

Dividing $\Delta G = \Delta H - T\Delta S$ by $-T$ gives exactly
$\Delta S_{\text{surr}} + \Delta S_{\text{sys}} = \Delta S_{\text{univ}}$.
So $\Delta G$ is the second law rewritten *entirely in terms of the
system* — which is why it is worth having.

> 
$\Delta G^\circ  0$: not favored (the reverse is)   

$\Delta G^\circ = 0$: at equilibrium

The sign flip is worth stating: $\Delta S_{\text{univ}}$ must be
positive, but $\Delta G^\circ$ must be
negative, because of the $-T$ used in the derivation.

### The second route: free energies of formation `ZUM §17.7`

Exactly as with enthalpy, $\Delta G^\circ$ can be assembled from tabulated
formation values:

$$ \Delta G^\circ_{\text{reaction}} =    \sum n\Delta G_f^\circ{}_{\text{products}}    - \sum n\Delta G_f^\circ{}_{\text{reactants}} $$

> 📘 **Worked example 3: two routes, one answer**
>
> For 2H₂(g) + O₂(g) → 2H₂O(l):
> 
> **Route 1 — from $\Delta H^\circ$ and $\Delta S^\circ$.**
> $\Delta H^\circ = 2(-286) = -572$ kJ;
> $\Delta S^\circ = -327$ J/K $= -0.327$ kJ/K.
> 
> $$ \Delta G^\circ = -572 - (298)(-0.327) = -572 + 97 = \mathbf{-475}~    \text{kJ} $$
> 
> **Route 2 — from $\Delta G_f^\circ$.**
> $\Delta G^\circ = 2(-237) - 0 = \mathbf{-474}$ kJ.
> 
> The two agree to within rounding in the table. **Watch the units** —
> the entropy had to be converted from J/K to kJ/K before it could be
> subtracted from a value in kJ.

#### INSTRUCTION B • When temperature decides 20 min

### The four cases `ZUM §17.3`

`SP 5`

Because $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$, the signs of
$\Delta H^\circ$ and $\Delta S^\circ$ between them determine whether
temperature matters at all:

| $\Delta H^\circ$ | $\Delta S^\circ$ | **Favored at** | **Comment** |
|---|---|---|---|
| $-$ | $+$ | **all temperatures** | both terms help; no calculation
  needed |
| $+$ | $-$ | **no temperature** | both terms oppose; never favored |
| $+$ | $+$ | **high $T$** | entropy wins once $T$ is large enough |
| $-$ | $-$ | **low $T$** | enthalpy wins while $T$ is small |

For the two mixed cases, the crossover temperature — where
$\Delta G^\circ = 0$ and the behaviour switches — is

$$ T = \frac{\Delta H^\circ}{\Delta S^\circ} $$

> 📘 **Worked example 4: why limestone needs a kiln**
>
> CaCO₃(s) → CaO(s) + CO₂(g):
> $\Delta H^\circ = +178.5$ kJ, $\Delta S^\circ = +161$ J/K.
> 
> Both positive $\Rightarrow$ favored only at high temperature.
> 
> **At 298 K:**
> $\Delta G^\circ = 178.5 - 298(0.161) = +131$ kJ — *not* favored, which
> is why limestone buildings do not crumble into quicklime.
> 
> **Crossover:**
> 
> $$ T = \frac{178.5}{0.161} = \mathbf{1109}~\mathrm{K}    \quad (\approx 836\,\mathrm{{}^\circ C}) $$
> 
> Above about 1100 K the decomposition becomes favored — which is
> exactly the temperature at which lime kilns are operated.

#### APPLICATION • Predicting and calculating 20 min

1. For the Haber process, $\Delta H^\circ = -92$ kJ and
   $\Delta S^\circ = -199$ J/K. Find $\Delta G^\circ$ at
   298 K and the crossover temperature.
   *(working space)*
2. For H₂O(l) → H₂O(g), $\Delta H^\circ = +44$ kJ and
   $\Delta S^\circ = +119$ J/K. Find the crossover temperature and
   say what it physically is.
   *(working space)*
3. Without calculating, say whether
   2H₂O₂(l) → 2H₂O(l) + O₂(g) ($\Delta H^\circ 

> 📌 **Exit ticket**
>
> A reaction has $\Delta H^\circ = +50$ kJ and $\Delta S^\circ = +100$ J/K.
> Is it favored at 298 K? Above what temperature does that change?

## Free Energy, Equilibrium, and Kinetic Control Zumdahl §17.9

> 📌 **By the end you can…**
>
> - Relate $\Delta G^\circ$ to $K$ and estimate one from the other.
> - Explain why a favored reaction may not occur at a measurable rate.

**Read:** Zumdahl §17.9 • PDF pp. 863–869

> 📌 **Retrieval warm-up**
>
> 1. $\Delta G^\circ =$ $\Delta H^\circ -         T\Delta S^\circ$
> 2. Favored means $\Delta G^\circ$ is: negative
> 3. If $K > 1$, which side is favored?
>    products
> 4. What raises a rate without changing $K$?
>    a catalyst

#### INSTRUCTION A • Two languages for the same fact 25 min

### $\Delta G^\circ$ and $K$ `ZUM §17.9`

`SP 5`

You now have two ways of saying “products are favored”: $K > 1$ from
Unit 7, and $\Delta G^\circ  1$ | products favored at equilibrium |
| zero | $= 1$ | neither side favored |
| positive | $ 📌 **Estimating without a calculator**
>
> The CED asks you to connect $K$ and $\Delta G^\circ$ *qualitatively by
> estimation*, so learn the scale rather than only the formula. The quantity
> to compare against is $RT$, which at 298 K is about
> 2.5 kJ/mol.
> 
> | $\Delta G^\circ \approx 0$ | $K$ close to 1 |
> |---|---|
> | $\Delta G^\circ = -10$ kJ | $K \approx 60$ |
> | $\Delta G^\circ = -50$ kJ | $K \approx 6\times10^{8}$ |
> | $\Delta G^\circ = +50$ kJ | $K \approx 2\times10^{-9}$ |

The lesson: because $\Delta G^\circ$ sits inside an exponential, a modest
free-energy change produces an enormous swing in $K$.

> 📘 **Worked example 5: limestone again, as an equilibrium**
>
> At 298 K the decomposition of CaCO₃ has
> $\Delta G^\circ = +131$ kJ. Find $K$.
> 
> $$ \ln K = -\frac{\Delta G^\circ}{RT}    = -\frac{131{,}000}{(8.314)(298)} = -52.9 $$
> 
> $$ K = e^{-52.9} = \mathbf{1\times10^{-23}} $$
> 
> Essentially no CO₂ above limestone at room temperature — which is
> what “not favored” looks like quantitatively.

#### INSTRUCTION B • Favored is not the same as fast 20 min

### Kinetic control `ZUM §17.4 (CED)`

`SP 6`

This is CED topic **9.4**, and it is the payoff for having taught
kinetics first.

A thermodynamically favored reaction tells you *where* the system would
end up. It says nothing about *how long* that takes. When a favored
reaction proceeds too slowly to observe, it is under
kinetic control, and the usual cause is a high
activation energy.

> ⚠️ **AP trap**
>
> **A reaction that is not proceeding is not necessarily at
> equilibrium.** Diamond converting to graphite has $\Delta G^\circ  room temperature — it is favored — yet diamonds persist indefinitely
> because the activation barrier is enormous.
> 
> If you are told a process is favored but nothing appears to happen, the
> conclusion the CED wants is **kinetic control**, not equilibrium.
> 
> Note what a catalyst does and does not do: it lowers $E_a$ and so raises the
> rate, but it cannot change $\Delta G^\circ$ or $K$. Catalysts move a system
> to equilibrium faster; they never move the equilibrium.

#### APPLICATION • Thermodynamics versus kinetics 20 min

1. A reaction has $\Delta G^\circ = -33$ kJ at 298 K.
   Calculate $K$.
   *(working space)*
2. A mixture of H₂ and O₂ can sit in a flask for years
   without reacting, yet the combustion has
   $\Delta G^\circ = -474$ kJ. Explain, and say what a spark does.
   
3. A student says “$\Delta G^\circ$ is negative, so the reaction will
   be fast.” Correct them in one sentence.
   

> 📌 **Exit ticket**
>
> Give one reaction that is thermodynamically favored but does not visibly
> occur, and name what is preventing it.

## Dissolution and Coupled Reactions Zumdahl §17.5, 17.10

> 📌 **By the end you can…**
>
> - Explain solubility in terms of the enthalpy and entropy of
>    dissolution.
> - Explain how an unfavorable process can be driven by coupling or an
>    external energy source.

**Read:** Zumdahl §17.5, 17.10 • PDF pp. 850–851, 869–873

> 📌 **Retrieval warm-up**
>
> 1. $\Delta G^\circ = -RT\ln K$; if $\Delta G^\circ     greater than 1
> 2. A favored but immeasurably slow reaction is under:
>    kinetic control
> 3. Adding two reactions adds their:
>    $\Delta G^\circ$ values

#### INSTRUCTION A • Why some salts dissolve and others do not 25 min

### Three competing contributions `ZUM §17.5`

`SP 4`

This is CED **9.6**. Dissolving a salt is a free-energy balance with
three parts:

**Breaking up the solid** — overcoming the lattice.
        $\Delta H$ strongly positive,
        $\Delta S$ positive.

**Reorganizing the solvent** around the ions.
        $\Delta S$ negative — water molecules become
        ordered in hydration shells.

**Ion–solvent attraction** (hydration).
        $\Delta H$ negative.

> 📌 **Why the CED does not ask you to predict the total**
>
> The framework says outright that predicting the overall $\Delta G^\circ$ of
> dissolution “can be challenging due to the cancellations among” these
> three factors. The enthalpy terms are large and opposite; the entropy terms
> likewise. What is left over is a small difference between big numbers.
> 
> So you are expected to **identify the contributions and their signs**,
> not to predict solubility from scratch. An answer that reasons through the
> three factors earns credit even if the final direction is uncertain.

> 📘 **Worked example 6: dissolving that cools the beaker**
>
> NH₄NO₃ dissolves *endothermically* — the beaker gets cold, so
> $\Delta H^\circ > 0$. Yet it is very soluble. Why?
> 
> Because $\Delta S^\circ$ is strongly positive: an ordered crystal becomes
> freely moving hydrated ions dispersed through the solvent. At room
> temperature $T\Delta S^\circ$ exceeds $\Delta H^\circ$, so
> $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ  
> **Entropy is driving this one on its own** — the enthalpy term is
> working against it. This is precisely the case the CED flags in 9.3.A.4,
> where you must consider both terms rather than assuming exothermic means
> favored.

#### INSTRUCTION B • Driving the unfavorable 20 min

### Coupling, and external energy `ZUM §17.10`

`SP 4`

A process with $\Delta G^\circ > 0$ will not happen on its own. There are
two ways to make it happen anyway — CED topic **9.7**.

**1. Supply external energy.** Examples the CED names:

- **Electrical energy** driving an electrolytic cell or charging
   a battery — the whole subject of Chapter 18.
- **Light** driving photosynthesis, which converts CO₂ and
   water into glucose with a hugely positive $\Delta G^\circ$.

**2. Couple it to a favorable reaction.** Because free energies
add, an unfavorable step can be carried by a favorable
one, provided the two share a common intermediate and
the *sum* has $\Delta G^\circ  📘 **Worked example 7: how cells pay for chemistry**
>
> Phosphorylating glucose is unfavorable on its own:
> 
> $$ \text{glucose} + \text{Pi} \to \text{glucose-6-phosphate}    \qquad \Delta G^\circ = +13.8~\text{kJ/mol} $$
> 
> Hydrolysing ATP is strongly favorable:
> 
> $$ \text{ATP} + \text{H₂O} \to \text{ADP} + \text{Pi}    \qquad \Delta G^\circ = -30.5~\text{kJ/mol} $$
> 
> Coupled through the shared Pi, the overall process is
> 
> $$ \Delta G^\circ = +13.8 + (-30.5) = \mathbf{-16.7}~\text{kJ/mol} $$
> 
> and therefore favored. This is what “ATP is the cell's energy currency”
> actually means — not that ATP contains energy, but that its hydrolysis is
> favorable enough to pay for reactions that are not.

#### APPLICATION • Putting the unit together 20 min

Photosynthesis has $\Delta G^\circ \approx +2870$ kJ/mol of
        glucose. Explain how it occurs at all.
        

Reaction X has $\Delta G^\circ = +25$ kJ. It is coupled to
        reaction Y with $\Delta G^\circ = -60$ kJ. Is the coupled process
        favored, and what must the two reactions share?
        yes, $-35$ kJ; a common intermediate

NaCl dissolves with $\Delta H^\circ$ very close to zero.
        Explain what must be driving it. 

> 📌 **Exit ticket**
>
> A classmate says “an unfavorable reaction can never happen.” Give the two
> ways it can, with one example each.

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
