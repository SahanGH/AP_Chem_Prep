# Guided Notes

*Unit 9 • Thermodynamics and Electrochemistry*  
CED 9.1–9.11 • Zumdahl Ch 17–18 • 9 blocks

[← all lessons](../index.md)

---

> 📌 **One quantity, three languages**
>
> Everything in this unit is a consequence of a single number, $\Delta G^\circ$,
> and of the three equations that compute it or convert it:
> 
> | **Equation** | **Answers the question** | **From** |
> |---|---|---|
> | $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$ | is it favored, and at what $T$? | Unit 6 $+$ 9.1–9.2 |
> | $\Delta G^\circ = -RT\ln K$ | how far does it go? | Unit 7 |
> | $\Delta G^\circ = -nFE^\circ_{\text{cell}}$ | what voltage does it produce? | Unit 9 |

Read across the middle column and you have the whole course: Unit 6 measured
heat, Unit 7 measured extent, Unit 5 measured rate. $\Delta G^\circ$ is what
connects the first two — and topic 9.4 exists to insist that it says
nothing at all about the third.

Three signs travel together and are worth memorizing as one fact:

$$ \Delta G^\circ  1 \iff E^\circ_{\text{cell}} > 0 $$

> ⚠️ **The word the CED retired**
>
> The 2024 CED replaced “spontaneous” with
> **thermodynamically favored** throughout, because “spontaneous”
> misleads students into hearing “happens quickly, by itself.” A favored
> reaction may take geological time — diamond turning into graphite is
> favored and has not troubled anyone's jewellery.
> 
> Zumdahl's Chapter 17 is still titled “Spontaneity, Entropy, and Free
> Energy.” Read the chapter, write the CED's word.

## Entropy CED 9.1 • Zumdahl §17.1

> 📌 **By the end you can…**
>
> - State what entropy measures.
> - Predict the sign of $\Delta S^\circ$ from the change described.

**Read:** Zumdahl §17.1 • PDF pp. 835–841

#### INSTRUCTION A • What entropy actually measures 25 min

### Dispersal, not disorder `CED 9.1`

`SP 6`

Entropy, $S$, measures how many microscopic arrangements produce the
same macroscopic state — how dispersed the energy and
matter of a system are. More available arrangements means
higher entropy.

> ⚠️ **AP trap**
>
> “Disorder” is the usual shorthand and it is a poor one. A messy room has
> no more entropy than a tidy one, because nothing about the energy of its
> molecules has changed. Argue from **how many ways the particles and
> their energy can be arranged**, and from the volume available to them —
> that reasoning earns credit, and “it looks messier” does not.

### The four situations to recognize `CED 9.1`

Nearly every $\Delta S$ question on the exam is one of these:

1. **Phase change.**
   solid $ 📌 **The tie-breaker**
>
> When two of these compete, **gas wins**. In
> 2H₂(g) + O₂(g) → 2H₂O(l) three moles of gas become zero, so
> $\Delta S^\circ$ is strongly negative even though a liquid is arguably
> “more dispersed” than a crystal would be.

#### GUIDED PRACTICE • Predicting the sign 15 min

Predict the sign of $\Delta S^\circ$ and give the controlling reason.

1. H₂O(l) → H₂O(g) $+$; liquid becomes gas
2. 2NO₂(g) → N₂O₄(g) $-$; 2 mol gas to 1
3. NaCl(s) → Na+(aq) + Cl⁻(aq)
   $+$; crystal disperses
4. CaCO₃(s) → CaO(s) + CO₂(g)
   $+$; a gas appears
5. N₂(g) + 3H₂(g) → 2NH₃(g)
   $-$; 4 mol gas to 2

#### INSTRUCTION B • The second law 20 min

### The universe, not the system `CED 9.1`

`SP 6`

The second law of thermodynamics: for any thermodynamically favored
process,

$$ \Delta S_{\text{univ}} = \Delta S_{\text{sys}} + \Delta S_{\text{surr}}    > 0 $$

The system's entropy is allowed to *decrease* — water freezes, ice
crystals are more ordered than liquid — provided the surroundings gain
more than the system loses. Freezing releases heat to the surroundings, and
that heat raises their entropy.

> 📌 **Why this becomes Gibbs free energy**
>
> Tracking the surroundings is a nuisance. The next block folds them into a
> single system-only quantity, which is the entire reason $\Delta G$ is worth
> defining. If you understand $\Delta S_{\text{univ}} > 0$, you already
> understand $\Delta G^\circ  by $-T$.

#### APPLICATION • Reasoning with the second law 20 min

1. Water freezing at -10 °C is thermodynamically favored,
   yet the water's entropy decreases. Explain how both are true.
   
2. A student says a reaction with $\Delta S_{\text{sys}} 
3. Rank by absolute entropy at the same temperature: H₂O(s),
   H₂O(l), H₂O(g). H₂O(s) $ 📌 **Exit ticket**
>
> Predict the sign of $\Delta S^\circ$ for
> 2SO₂(g) + O₂(g) → 2SO₃(g) and justify in one sentence.

## Absolute Entropy and $\Delta S^\circ$ CED 9.2 • Zumdahl §17.2, §17.5–17.6

> 📌 **By the end you can…**
>
> - Explain why entropy has an absolute scale but enthalpy does not.
> - Calculate $\Delta S^\circ$ from tabulated absolute entropies.

**Read:** Zumdahl §17.2, §17.5–17.6 • PDF pp. 841–842, 848–853

> 📌 **Retrieval warm-up**
>
> 1. Sign of $\Delta S^\circ$ for 2NO₂(g) → N₂O₄(g):
>    negative
> 2. Which has more entropy, H₂O(l) or H₂O(g)?
>    H₂O(g)
> 3. $\Delta S_{\text{univ}}$ for a favored process:
>    $> 0$
> 4. The AP term replacing “spontaneous”:
>    thermodynamically favored

#### INSTRUCTION A • A real zero 25 min

### The third law `CED 9.2`

`SP 5`

The third law of thermodynamics says a perfect crystal at
0 K has entropy exactly zero. That gives
entropy a genuine origin, so every substance has a tabulated
absolute entropy $S^\circ$ — always a positive number.

> ⚠️ **AP trap**
>
> Contrast with enthalpy. There is no absolute $H$, so tables list
> $\Delta H_f^\circ$ and assign zero to elements in their standard states.
> 
> Entropy tables are different: **$S^\circ$ of an element is not zero.**
> O₂(g) has $S^\circ = 205\,\mathrm{J/K/mol}$. Setting
> element entropies to zero out of habit is a reliable way to lose a point.

$$ \boxed{\;\Delta S^\circ_{\text{rxn}} = \sum n S^\circ_{\text{products}}    - \sum n S^\circ_{\text{reactants}}\;} $$

Coefficients multiply, exactly as in Hess's law. And note the units:
$S^\circ$ is in joules while $\Delta H^\circ$ is in
kilojoules.

> 📘 **Worked example 1: decomposing limestone**
>
> CaCO₃(s) → CaO(s) + CO₂(g)
> $S^\circ$: CaCO₃ 93, CaO 40, CO₂ 214
> J/K/mol.
> 
> $$ \Delta S^\circ = (40 + 214) - 93 = \mathbf{+161}~\mathrm{J/K} $$
> 
> Positive, as predicted — a gas appeared where there was none.

> 📘 **Worked example 2: the Haber process**
>
> N₂(g) + 3H₂(g) → 2NH₃(g)
> $S^\circ$: N₂ 192, H₂ 131, NH₃ 193.
> 
> $$ \Delta S^\circ = 2(193) - [192 + 3(131)] = 386 - 585    = \mathbf{-199}~\mathrm{J/K} $$
> 
> Four moles of gas became two, so the sign had to be negative. Dropping the
> coefficient 3 on hydrogen gives $-68$ — wrong magnitude entirely.

#### GUIDED PRACTICE • Running the sums 15 min

$S^\circ$ (J/K/mol): H₂ 131, O₂ 205,
H₂O(l) 70, H₂O(g) 189, NO₂ 240, N₂O₄ 304.

1. 2H₂(g) + O₂(g) → 2H₂O(l): 
   *(working space)*
2. H₂O(l) → H₂O(g): $+119$ J/K
3. 2NO₂(g) → N₂O₄(g): $-176$ J/K

#### APPLICATION • Interpreting the numbers 20 min

1. Why is $S^\circ$ for H₂O(g) nearly triple that of
   H₂O(l), when it is the same substance?
   
2. A student computes the Haber $\Delta S^\circ$ as
   $193 - (192 + 131) = -130$ J/K. Find both errors.
   
3. For H₂O(l) → H₂O(g), $\Delta S^\circ = +119$ J/K and
   $\Delta H^\circ = +44$ kJ. Say what each sign contributes to
   favorability at 25 °C.
   

> 📌 **Exit ticket**
>
> Why can a table list an absolute $S^\circ$ for oxygen gas but not an
> absolute $H^\circ$?

## Gibbs Free Energy CED 9.3 • Zumdahl §17.3–17.4

> 📌 **By the end you can…**
>
> - Calculate $\Delta G^\circ$ from $\Delta H^\circ$ and
>    $\Delta S^\circ$.
> - Determine the temperature range over which a process is favored.

**Read:** Zumdahl §17.3–17.4 • PDF pp. 842–848

> 📌 **Retrieval warm-up**
>
> 1. $\Delta S^\circ$ for CaCO₃(s) → CaO(s) + CO₂(g):
>    $+161$ J/K
> 2. $\Delta S_{\text{univ}}$ must be what sign for a favored process?
>    positive
> 3. Units of $S^\circ$ versus $\Delta H^\circ$:
>    J/(K$\cdot$mol) versus kJ/mol
> 4. $S^\circ$ of an element in its standard state is:
>    not zero

#### INSTRUCTION A • One number that decides 25 min

### Folding the surroundings in `CED 9.3`

`SP 5`

Gibbs free energy removes the need to track the surroundings:

$$ G = H - TS \qquad\Longrightarrow\qquad    \boxed{\;\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ\;} $$

Dividing $\Delta G = \Delta H - T\Delta S$ by $-T$ returns exactly
$\Delta S_{\text{surr}} + \Delta S_{\text{sys}} = \Delta S_{\text{univ}}$.
So $\Delta G$ is the second law rewritten *entirely in terms of the
system*.

> 
$\Delta G^\circ  0$: not favored (the reverse is)   

$\Delta G^\circ = 0$: at equilibrium

The sign flip is worth stating aloud: $\Delta S_{\text{univ}}$ must be
positive, but $\Delta G^\circ$ must be
negative, because of the $-T$ used in the derivation.

> ⚠️ **AP trap**
>
> **Convert the entropy to kJ before subtracting.** $\Delta H^\circ$ is
> in kJ and $\Delta S^\circ$ in J/K. Forgetting the factor of 1000 is the
> single most common arithmetic error in this unit, and it produces answers
> wrong by roughly a factor of a thousand — large enough to spot if you
> sanity-check the magnitude.

#### INSTRUCTION B • When temperature decides 20 min

### The four cases `CED 9.3`

`SP 5`

Because $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$, the two signs
between them decide whether temperature matters at all:

| $\Delta H^\circ$ | $\Delta S^\circ$ | **Favored at** | **Comment** |
|---|---|---|---|
| $-$ | $+$ | **all temperatures** | both terms help; no calculation
  needed |
| $+$ | $-$ | **no temperature** | both terms oppose; never favored |
| $+$ | $+$ | **high $T$** | entropy wins once $T$ is large enough |
| $-$ | $-$ | **low $T$** | enthalpy wins while $T$ is small |

For the two mixed cases the crossover temperature, where
$\Delta G^\circ = 0$, is

$$ T = \frac{\Delta H^\circ}{\Delta S^\circ} $$

> 📘 **Worked example 3: why limestone needs a kiln**
>
> CaCO₃(s) → CaO(s) + CO₂(g): $\Delta H^\circ = +178.5$ kJ,
> $\Delta S^\circ = +161$ J/K. Both positive $\Rightarrow$ favored only at
> high temperature.
> 
> **At 298 K:**
> $\Delta G^\circ = 178.5 - 298(0.161) = +131$ kJ — not favored, which is
> why limestone buildings do not crumble into quicklime.
> 
> **Crossover:**
> 
> $$ T = \frac{178.5}{0.161} = \mathbf{1109}~\mathrm{K}    \quad (\approx 836\,\mathrm{{}^\circ C}) $$
> 
> Which is about the temperature at which lime kilns are operated.

#### APPLICATION • Predicting and calculating 20 min

1. For the Haber process $\Delta H^\circ = -92$ kJ and
   $\Delta S^\circ = -199$ J/K. Find $\Delta G^\circ$ at
   298 K and the crossover temperature.
   *(working space)*
2. For H₂O(l) → H₂O(g), $\Delta H^\circ = +44$ kJ and
   $\Delta S^\circ = +119$ J/K. Find the crossover temperature and say
   what it physically is.
   *(working space)*
3. Without calculating, say whether
   2H₂O₂(l) → 2H₂O(l) + O₂(g) ($\Delta H^\circ 

> 📌 **Exit ticket**
>
> A reaction has $\Delta H^\circ = +50$ kJ and $\Delta S^\circ = +100$ J/K.
> Is it favored at 298 K? Above what temperature does that change?

## Formation Free Energies and Kinetic Control CED 9.3, 9.4 • Zumdahl §17.4, §17.7

> 📌 **By the end you can…**
>
> - Calculate $\Delta G^\circ$ from free energies of formation.
> - Explain why a favored reaction may proceed immeasurably slowly.

**Read:** Zumdahl §17.4, §17.7 • PDF pp. 845–848, 853–859

> 📌 **Retrieval warm-up**
>
> 1. $\Delta G^\circ =$ $\Delta H^\circ -         T\Delta S^\circ$
> 2. Favored means $\Delta G^\circ$ is: negative
> 3. $\Delta H^\circ  0$: favored at
>    all temperatures
> 4. Crossover temperature $=$ $\Delta H^\circ /         \Delta S^\circ$

#### INSTRUCTION A • The second route to $\Delta G^\circ$ 25 min

### Free energies of formation `CED 9.3`

`SP 5`

Exactly as with enthalpy, $\Delta G^\circ$ can be assembled from tabulated
formation values:

$$ \Delta G^\circ_{\text{rxn}} = \sum n\Delta G_f^\circ{}_{\text{products}}    - \sum n\Delta G_f^\circ{}_{\text{reactants}} $$

and $\Delta G_f^\circ$ of an element in its standard state is
zero — unlike $S^\circ$.

> 📘 **Worked example 4: two routes, one answer**
>
> For 2H₂(g) + O₂(g) → 2H₂O(l):
> 
> **Route 1 — from $\Delta H^\circ$ and $\Delta S^\circ$.**
> $\Delta H^\circ = 2(-286) = -572$ kJ;
> $\Delta S^\circ = -327$ J/K $= -0.327$ kJ/K.
> 
> $$ \Delta G^\circ = -572 - 298(-0.327) = -572 + 97    = \mathbf{-475}~\text{kJ} $$
> 
> **Route 2 — from $\Delta G_f^\circ$.**
> $\Delta G^\circ = 2(-237) - 0 = \mathbf{-474}$ kJ.
> 
> The two agree to within table rounding. Note again that the entropy had to
> be converted from J/K to kJ/K first.

#### INSTRUCTION B • Favored is not the same as fast 20 min

### Thermodynamic versus kinetic control `CED 9.4`

`SP 6`

This is the point of topic 9.4, and it is the one place where this unit and
Unit 5 must be held apart:

> 
$\Delta G^\circ$ tells you **whether** and **how far**.   

$E_a$ tells you **how fast**.   

They are independent.

A reaction that is thermodynamically favored but has a large
activation energy proceeds too slowly to observe. It is
said to be under kinetic control.

- **Diamond to graphite.** $\Delta G^\circ$ is negative, so
   graphite is the favored form at room conditions. The rearrangement
   requires breaking a covalent network, so it does not measurably
   occur.
- **Petrol in air.** Combustion is strongly favored; a tank of
   fuel is stable because the reaction needs a spark to clear
   $E_a$.

> ⚠️ **AP trap**
>
> A **catalyst** lowers $E_a$ and speeds a reaction up. It does
> *not* change $\Delta G^\circ$, $\Delta H^\circ$, $\Delta S^\circ$, or
> $K$. A catalyst cannot make an unfavorable reaction
> favorable — it can only let an already-favored one arrive sooner.

#### APPLICATION • Thermodynamics versus kinetics 20 min

A reaction has $\Delta G^\circ = -150$ kJ but no measurable rate at
        room temperature. Is this a contradiction? Explain.
        

Give two ways to speed that reaction up, and state the effect of
        each on $K$. 

Explain why “spontaneous” is a poor word for $\Delta G^\circ 

> 📌 **Exit ticket**
>
> State one thing a catalyst changes and two things it does not.

## Free Energy and Equilibrium CED 9.5 • Zumdahl §17.9

> 📌 **By the end you can…**
>
> - Relate $\Delta G^\circ$ to $K$ and estimate one from the other.
> - Distinguish $\Delta G$ from $\Delta G^\circ$ using $Q$.

**Read:** Zumdahl §17.9 • PDF pp. 862–867

> 📌 **Retrieval warm-up**
>
> 1. If $K > 1$, which side is favored? products
> 2. $Q$ is calculated like $K$ but with:
>    non-equilibrium concentrations
> 3. What raises a rate without changing $K$?
>    a catalyst
> 4. $\Delta G^\circ$ for a favored process is:
>    negative

#### INSTRUCTION A • Two languages for one fact 25 min

### $\Delta G^\circ$ and $K$ `CED 9.5`

`SP 5`

You now have two ways of saying “products are favored”: $K > 1$ from
Unit 7, and $\Delta G^\circ  1$ | products favored at equilibrium |
| zero | $= 1$ | neither side favored |
| positive | $ 📌 **The MCQ half is no-calculator**
>
> You are not asked to evaluate logarithms by hand. You are asked to know
> which *way* the relationship runs: more negative $\Delta G^\circ$ means
> larger $K$, and the dependence is exponential — so a modest change in
> $\Delta G^\circ$ produces an enormous change in $K$. Reason with the sign
> and the direction, not with arithmetic.

#### INSTRUCTION B • $\Delta G$ versus $\Delta G^\circ$ 20 min

### Away from standard conditions `CED 9.5`

`SP 6`

$\Delta G^\circ$ is a fixed property of the reaction at a given temperature
— every species at standard conditions. $\Delta G$ is what the reaction
mixture *actually* has right now, and depends on the current
composition through $Q$:

$$ \Delta G = \Delta G^\circ + RT\ln Q $$

- $Q  K$: the mixture shifts reverse and
   $\Delta G > 0$.

> ⚠️ **AP trap**
>
> At equilibrium $\Delta G = 0$, **not** $\Delta G^\circ$. $\Delta G^\circ$
> is zero only in the special case $K = 1$. Writing “$\Delta G^\circ = 0$ at
> equilibrium” is a standard lost point — and setting $\Delta G = 0$ in
> $\Delta G = \Delta G^\circ + RT\ln Q$ is precisely how
> $\Delta G^\circ = -RT\ln K$ is derived.

#### APPLICATION • Connecting the two 20 min

Reaction A has $\Delta G^\circ = -5$ kJ, reaction B has
        $\Delta G^\circ = -50$ kJ. Compare their $K$ values qualitatively.
        

A reaction has $\Delta G^\circ = +20$ kJ. Can it ever proceed
        forward? 

At equilibrium, state the values of $\Delta G$ and of $Q$.
        $\Delta G = 0$ and $Q = K$

> 📌 **Exit ticket**
>
> A reaction has $K = 1$. What is $\Delta G^\circ$, and is the reaction
> favored?

## Dissolution and Coupled Reactions CED 9.6, 9.7 • Zumdahl §17.5, §17.10

> 📌 **By the end you can…**
>
> - Identify the enthalpy and entropy contributions to dissolution.
> - Explain how coupling or external energy drives an unfavorable
>    process.

**Read:** Zumdahl §17.5, §17.10 • PDF pp. 848–849, 867–869

> 📌 **Retrieval warm-up**
>
> 1. $\Delta G^\circ = -RT\ln K$; $R$ is in:
>    J/(mol$\cdot$K)
> 2. At equilibrium $\Delta G =$ 0
> 3. $\Delta S$ for dissolving a crystal is usually:
>    positive
> 4. A catalyst changes: $E_a$ only

#### INSTRUCTION A • Why some salts dissolve 25 min

### Three competing contributions `CED 9.6`

`SP 4`

Dissolving a salt is a free-energy balance with three parts:

**Breaking up the lattice.** $\Delta H$ strongly
        positive, $\Delta S$ positive.

**Reorganizing the solvent** around the ions. $\Delta S$
        negative — water becomes ordered in hydration
        shells.

**Ion–solvent attraction** (hydration). $\Delta H$
        negative.

> 📌 **Why the CED does not ask you to predict the total**
>
> The framework says outright that predicting the overall $\Delta G^\circ$ of
> dissolution is challenging because of the cancellations among these three
> factors. The enthalpy terms are large and opposite; so are the entropy
> terms. What remains is a small difference between big numbers.
> 
> You are expected to **identify the contributions and their signs**,
> not to predict solubility from scratch. Reasoning through the three factors
> earns credit even where the net direction is uncertain.

> 📘 **Worked example 5: dissolving that cools the beaker**
>
> NH₄NO₃ dissolves *endothermically* — the beaker gets cold, so
> $\Delta H^\circ > 0$. Yet it is very soluble. Why?
> 
> Because $\Delta S^\circ$ is strongly positive: an ordered crystal becomes
> freely moving hydrated ions dispersed through the solvent. At room
> temperature $T\Delta S^\circ$ exceeds $\Delta H^\circ$, so
> $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ  
> **Entropy is driving this one alone**, with the enthalpy term working
> against it — the case to remember whenever you are tempted to equate
> “exothermic” with “favored”.

#### INSTRUCTION B • Driving the unfavorable 20 min

### Coupling and external energy `CED 9.7`

`SP 4`

A process with $\Delta G^\circ > 0$ will not happen on its own. There are
two ways to make it happen anyway.

**1. Supply external energy.**

- **Electrical energy** driving an electrolytic cell or charging
   a battery — the subject of the next three blocks.
- **Light** driving photosynthesis, which builds glucose from
   CO₂ and water with a hugely positive $\Delta G^\circ$.

**2. Couple it to a favorable reaction.** Because free energies
add, an unfavorable step can be carried by a favorable
one — provided the two share a common intermediate
and the *sum* has $\Delta G^\circ  📘 **Worked example 6: how cells pay for chemistry**
>
> Phosphorylating glucose is unfavorable on its own:
> 
> $$ \text{glucose} + \text{Pi} \to \text{glucose-6-phosphate}    \qquad \Delta G^\circ = +13.8~\text{kJ/mol} $$
> 
> Hydrolysing ATP is strongly favorable:
> 
> $$ \text{ATP} + \text{H₂O} \to \text{ADP} + \text{Pi}    \qquad \Delta G^\circ = -30.5~\text{kJ/mol} $$
> 
> Coupled through the shared Pi:
> 
> $$ \Delta G^\circ = +13.8 + (-30.5) = \mathbf{-16.7}~\text{kJ/mol} $$
> 
> and therefore favored. This is what “ATP is the cell's energy currency”
> means — not that ATP contains energy, but that its hydrolysis is
> favorable enough to pay for reactions that are not.

#### APPLICATION • Putting free energy to work 20 min

NaCl dissolves with $\Delta H^\circ$ very slightly positive
        and still dissolves readily. Explain using the three contributions.
        

Reaction X has $\Delta G^\circ = +25$ kJ. It is coupled to
        reaction Y with $\Delta G^\circ = -40$ kJ. Is the coupled process
        favored, and what must the two share? 

*(working space)*

        

Name the external energy source that drives each: electrolysis of
        water; photosynthesis. electrical; light

> 📌 **Exit ticket**
>
> State the one condition that makes coupling chemically real rather than
> just an addition of two numbers.

## Galvanic and Electrolytic Cells CED 9.8 • Zumdahl §18.1, §18.7

> 📌 **By the end you can…**
>
> - Identify anode, cathode, and the direction of electron flow.
> - Distinguish galvanic from electrolytic cells.

**Read:** Zumdahl §18.1, §18.7 • PDF pp. 882–884, 906–911

> 📌 **Retrieval warm-up**
>
> 1. Oxidation is loss of: electrons
> 2. An unfavorable process has $\Delta G^\circ$:
>    positive
> 3. One way to drive an unfavorable reaction:
>    supply external energy
> 4. Oxidation number of Zn in Zn²⁺:
>    $+2$

#### INSTRUCTION A • Separating the half-reactions 25 min

### Why a wire is involved at all `CED 9.8`

`SP 1`

Drop zinc into copper sulfate and electrons pass directly from zinc to
Cu²⁺; the energy is released as heat. Separate
the two half-reactions into different compartments and the electrons must
travel through a wire instead — and along the way
they can do electrical work. That is the whole idea of a cell.

### The parts, and what each does `CED 9.8`

| **Part** | **Where** | **What happens** |
|---|---|---|
| Anode | one half-cell | oxidation; electrons leave |
| Cathode | the other half-cell | reduction; electrons arrive |
| Wire | between electrodes | carries electrons, anode $\to$ cathode |
| Salt bridge | joins the solutions | carries ions to keep both solutions neutral |

**An Ox and Red Cat** — **An**ode **Ox**idation,
**Red**uction **Cat**hode — holds in every cell, galvanic or
electrolytic. It is the one fact in this block that never changes.

> 📌 **What the CED excludes here**
>
> Topic 9.8 **excludes** assigning positive and negative labels to the
> electrodes. The signs actually reverse between galvanic and electrolytic
> cells, which is exactly why the framework leaves them out. Identify
> electrodes by *anode* and *cathode* and by what happens there;
> never by charge.

Without the salt bridge, oxidation at the anode would leave that solution
building up positive charge and the cathode solution
going negative. Charge separation halts electron flow almost immediately,
so the cell stops.

#### INSTRUCTION B • The same hardware, run backwards 20 min

### Galvanic against electrolytic `CED 9.8`

`SP 1`

|  | **Galvanic (voltaic)** | **Electrolytic** |
|---|---|---|
| $\Delta G^\circ$ | negative | positive |
| $E^\circ_{\text{cell}}$ | positive | negative |
| Drives itself? | yes — it is a battery | no — needs a power supply |
| Energy | chemical $\to$ electrical | electrical $\to$ chemical |
| Example | a AA cell discharging | electroplating; recharging |

An electrolytic cell is CED topic 9.7's “external energy source driving an
unfavorable process,” built in hardware.

#### APPLICATION • Describing cells 20 min

In a galvanic cell made from Zn/Zn²⁺ and
        Cu/Cu²⁺, zinc is oxidized. Name the anode, the cathode,
        and the direction of electron flow.
        

State what happens to the mass of each electrode as that cell runs.
        

A student labels the anode “negative” on an exam question about
        an electrolytic cell. Explain why the CED avoids this.
        

> 📌 **Exit ticket**
>
> Give the one statement about anode and cathode that is true in every cell,
> and one statement that is not.

## Cell Potential and Free Energy CED 9.9 • Zumdahl §18.2–18.3

> 📌 **By the end you can…**
>
> - Calculate $E^\circ_{\text{cell}}$ from standard reduction
>    potentials.
> - Relate $E^\circ_{\text{cell}}$ to $\Delta G^\circ$ and to $K$.

**Read:** Zumdahl §18.2–18.3 • PDF pp. 884–895

> 📌 **Retrieval warm-up**
>
> 1. Oxidation occurs at the: anode
> 2. Galvanic cells have $E^\circ_{\text{cell}}$:
>    positive
> 3. Electrons flow from anode to cathode
> 4. $\Delta G^\circ$ for a galvanic cell is:
>    negative

#### INSTRUCTION A • A scale built on an arbitrary zero 25 min

### Standard reduction potentials `CED 9.9`

`SP 5`

Only a *difference* in potential is measurable, so one half-reaction is
assigned a value by convention:

$$ \text{2H+(aq) + 2e⁻ → H₂(g)} \qquad E^\circ \equiv \mathbf{0.00}~\text{V} $$

Every other half-reaction is measured against this
standard hydrogen electrode. **Standard conditions** means all
solutes at 1 M, gases at 1 atm, and 25 °C.

> ⚠️ **AP trap**
>
> **Every table is written as reductions.** Reversing a half-reaction
> flips the sign of $E^\circ$. But multiplying a
> half-reaction by a coefficient does **not** change $E^\circ$ at all —
> potential is an intensive property, volts per unit charge, not volts
> per mole. Scaling a half-reaction to balance electrons is required; scaling
> its voltage is wrong.

$$ \boxed{\;E^\circ_{\text{cell}} = E^\circ_{\text{cathode}}    - E^\circ_{\text{anode}}\;} $$

with both values taken straight from the table as reductions. For a
galvanic cell you want $E^\circ_{\text{cell}} > 0$, so the species with the
more positive $E^\circ$ is the one reduced.

> 📘 **Worked example 7: the Daniell cell**
>
> Combine Zn²⁺/Zn ($-0.76$ V) and Cu²⁺/Cu ($+0.34$ V).
> Copper is more positive, so copper is reduced (cathode) and zinc oxidized
> (anode):
> 
> $$ \text{Zn + Cu²⁺ → Zn²⁺ + Cu} \qquad    E^\circ_{\text{cell}} = 0.34 - (-0.76) = \mathbf{+1.10}~\text{V} $$

> 📘 **Worked example 8: when the electrons do not balance**
>
> Combine Ag+/Ag ($+0.80$ V) and Cu²⁺/Cu ($+0.34$ V).
> Silver is reduced; balancing electrons needs *two* silver
> half-reactions:
> 
> $$ \text{Cu + 2Ag+ → Cu²⁺ + 2Ag} \qquad    E^\circ_{\text{cell}} = 0.80 - 0.34 = \mathbf{+0.46}~\text{V} $$
> 
> The silver half-reaction was doubled; its $E^\circ$ was not. Writing
> $2(0.80) - 0.34 = 1.26$ V is the classic error here.

#### GUIDED PRACTICE • Building cells from the table 15 min

$E^\circ$ (V): Ag+/Ag $+0.80$ • Cu²⁺/Cu
$+0.34$ • Pb²⁺/Pb $-0.13$ •\
Ni²⁺/Ni $-0.23$ • Fe²⁺/Fe $-0.44$
• Zn²⁺/Zn $-0.76$ • Mg²⁺/Mg
$-2.37$

Zn and Ag+: $+1.56$ V

Mg and Cu²⁺: $+2.71$ V

Zn and Ni²⁺: $+0.53$ V

Fe and Cu²⁺: $+0.78$ V

Pb and Ag+: $+0.93$ V

#### INSTRUCTION B • Volts into kilojoules, and on to $K$ 20 min

### $\Delta G^\circ = -nFE^\circ$ `CED 9.9`

`SP 5`

Electrical work is charge moved through a potential difference. With
Faraday's constant $F = 96485\,\mathrm{C/mol}$,

$$ \boxed{\;\Delta G^\circ = -nFE^\circ_{\text{cell}}\;} $$

> ⚠️ **AP trap**
>
> **Here is where $n$ finally matters.** Voltage does not depend on how
> many electrons are transferred; free energy does, because more electrons
> through the same potential means more energy. Two cells can share an
> $E^\circ$ and have very different $\Delta G^\circ$.
> 
> And $n$ comes from the **balanced overall equation**, not from either
> half-reaction alone.

> 📘 **Worked example 9: the Daniell cell in kilojoules**
>
> $E^\circ = +1.10$ V and $n = 2$:
> 
> $$ \Delta G^\circ = -(2)(96485)(1.10) = -212{,}267~\text{J}    = \mathbf{-212}~\text{kJ} $$
> 
> The answer arrives in **joules** — $F$ is coulombs per mole and a
> volt is a joule per coulomb — so convert to kJ.

Combining with $\Delta G^\circ = -RT\ln K$ gives the third link:

$$ nFE^\circ = RT\ln K \qquad\Longrightarrow\qquad    \ln K = \frac{nFE^\circ}{RT} $$

| $E^\circ_{\text{cell}}$ | $\Delta G^\circ$ | $K$ |  |
|---|---|---|---|
| $> 0$ | $ 1$ | favored; galvanic |
| $= 0$ | $= 0$ | $= 1$ | at equilibrium; a dead battery |
| $ 0$ | $

For Cu + 2Ag+ → Cu²⁺ + 2Ag, $E^\circ = +0.46$ V. Calculate
        $\Delta G^\circ$. 

*(working space)*

        

Two cells both have $E^\circ = +0.50$ V; one transfers 1 electron
        and the other 4. Compare their voltages and their $\Delta G^\circ$.
        

A battery is described as “dead”. Give $E_{\text{cell}}$,
        $\Delta G$, and the relationship between $Q$ and $K$.
        $E = 0$, $\Delta G = 0$, $Q = K$

> 📌 **Exit ticket**
>
> A student doubles a half-reaction to balance electrons and doubles its
> $E^\circ$ too. Explain why the second step is wrong.

## Nonstandard Conditions and Electrolysis CED 9.10, 9.11 • Zumdahl §18.4, §18.7

> 📌 **By the end you can…**
>
> - Predict qualitatively how concentration changes a cell potential.
> - Apply Faraday's law to an electrolysis calculation.

**Read:** Zumdahl §18.4, §18.7 • PDF pp. 895–900, 906–911

> 📌 **Retrieval warm-up**
>
> 1. $\Delta G^\circ =$ $-nFE^\circ$
> 2. $F =$ 96485 C/mol
> 3. $Q > K$ means the reaction shifts:
>    reverse
> 4. $E^\circ_{\text{cell}}$ for a dead battery:
>    0

#### INSTRUCTION A • Voltage as distance from equilibrium 25 min

### Changing the concentrations `CED 9.10`

`SP 6`

A cell's voltage measures how far the reaction is from equilibrium. As it
runs, reactants are consumed and products build up, so $Q$
rises toward $K$ and the voltage
falls. When $Q = K$ the cell is dead.

> 📌 **What CED 9.10 does and does not require**
>
> Topic 9.10 lists **no equation**. The Nernst equation is not required,
> and it does not appear on the AP equation sheet. What is required is the
> *direction* of the effect, argued from Le Ch\^atelier:
> 
> - Increase a **reactant** concentration $\Rightarrow$ $Q$
>    decreases $\Rightarrow$ the cell is further from equilibrium
>    $\Rightarrow$ voltage increases.
> - Increase a **product** concentration $\Rightarrow$ $Q$
>    increases $\Rightarrow$ voltage decreases.
> 
> Reason with $Q$ against $K$. That argument earns full credit and needs no
> logarithms.

A concentration cell has the *same* species in both half-cells
at different concentrations. $E^\circ_{\text{cell}} =$
0, since both electrodes are identical, yet the cell
still produces a voltage — the system moves to equalize the two
concentrations. The dilute half-cell is the anode
(metal dissolves, raising its concentration) and the concentrated one is
the cathode. The cell dies when the concentrations become equal.

#### INSTRUCTION B • Counting electrons with an ammeter 20 min

### Faraday's law `CED 9.11`

`SP 5`

Electrolysis is stoichiometry in which one reagent is
the electron. Current is how you count them:

$$ I = \frac{q}{t} \qquad\text{so}\qquad q = It $$

with $q$ in coulombs, $I$ in amperes, $t$ in
seconds. Then
$\text{mol e}^- = q/96485$.

> 
current & time $\to$ charge ($q = It$) $\to$ moles of electrons
($\div F$)   

$\to$ moles of substance ($\div n$ from the half-reaction) $\to$ grams
($\times$ molar mass)

> ⚠️ **AP trap**
>
> **The half-reaction supplies the electron ratio, and it is not always
> 2.** One mole of electrons deposits one mole of Ag, but only half a
> mole of Cu and a third of a mole of Al. Reading that number off
> the ion's charge is the step students skip.
> 
> Also: **time must be in seconds.** A problem stated in minutes or
> hours is stated that way on purpose.

> 📘 **Worked example 10: silver plating**
>
> 2.00 A for 30.0 min through AgNO₃.
> 
> $t = 30.0 \times 60 = 1800\,\mathrm{s}$;
> $q = (2.00)(1800) = 3600\,\mathrm{C}$;
> $\text{mol e}^- = 3600/96485 = 0.0373$.
> 
> Ag+ + e⁻ → Ag is one electron per atom, so
> $m = (0.0373)(107.87) = \mathbf{4.03}$ g.

> 📘 **Worked example 11: the same current, a different ion**
>
> 1.50 A for 1.00 h through CuSO₄.
> 
> $q = (1.50)(3600) = 5400\,\mathrm{C}$;
> $\text{mol e}^- = 5400/96485 = 0.0560$.
> 
> But Cu²⁺ + 2e⁻ → Cu needs *two* electrons per atom:
> 
> $$ \text{mol Cu} = \frac{0.0560}{2} = 0.0280 \qquad    m = (0.0280)(63.55) = \mathbf{1.78}~\text{g} $$
> 
> Forgetting to divide by 2 gives 3.56 g — exactly double, and a lost
> point.

#### APPLICATION • Predicting and scaling 20 min

For Zn + Cu²⁺ → Zn²⁺ + Cu, predict the effect on
        $E_{\text{cell}}$ of increasing $[\text{Cu²⁺}]$, and justify without
        calculating. 

How long, in hours, to deposit 5.00 g of copper at
        2.00 A? 

*(working space)*

        

A concentration cell is built from two Cu electrodes in
        0.10 M and 1.0 M Cu²⁺. Identify the
        anode and say when the cell stops.
        

> 📌 **Exit ticket**
>
> State the one question to ask before starting any calculation in this unit,
> and why it settles the method.

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
