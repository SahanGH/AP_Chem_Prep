# Self-Study • CED 5.1–5.11, I do / You do

*Unit 5 • Kinetics*  
Twelve ladders • four YOUR TURN questions each • work alone, check after all four

[← all lessons](../index.md)

---

> 📌 **How to use these notes — read this first**
>
> Each skill is a **ladder**: a worked example, then **four**
> YOUR TURN questions — same skill, new numbers, no help. Work all four
> before checking anything.
> 
> **The one idea this whole unit turns on.** Kinetics is about
> *how fast*, thermodynamics is about *how far*. They are
> independent. A reaction can be enormously favourable and still take
> centuries; diamond turning to graphite is the standard example. Never
> answer a rate question with an argument about stability.
> 
> **The habit that decides this unit.** Reaction orders are
> **experimental**. They come from data, or from the slow step of a
> mechanism — never from the coefficients of the overall equation. Reading
> orders off a balanced equation is the single most common way to lose marks
> here.
> 
> **One scope note.** The CED excludes **Arrhenius equation
> calculations**: you will not be asked to extract an activation energy from
> two rate constants or from a plot of $\ln k$ against $1/T$. Reading an
> energy profile and reasoning about temperature and catalysts qualitatively
> both remain fully examinable.

## Ladder 1 • Expressing reaction rate

`CED 5.1`

Rate is a change in concentration per unit time. Divide each species'
rate by its coefficient and every species gives the *same* number —
one rate for the reaction.

> 📘 **I do: relating species**
>
> For 2N₂O₅ → 4NO₂ + O₂, oxygen appears at
> 0.0125 M/s. Find the rates for the other two.
> 
> **Scale by the coefficients.** Relative to O₂ (coefficient 1):
> 
> NO₂ has coefficient 4, so it forms at
> $4 \times 0.0125 = \mathbf{0.0500}$ M/s.
> 
> N₂O₅ has coefficient 2, so it is *consumed* at
> $2 \times 0.0125 = \mathbf{0.0250}$ M/s. As a rate of change,
> $\Delta[\text{N₂O₅}]/\Delta t = -0.0250$ M/s — negative, because it is
> disappearing.
> 
> **The single reaction rate:**
> 
> $$ -\tfrac{1}{2}\frac{\Delta[\text{N₂O₅}]}{\Delta t}    = \tfrac{1}{4}\frac{\Delta[\text{NO₂}]}{\Delta t}    = \frac{\Delta[\text{O₂}]}{\Delta t} = 0.0125\,\mathrm{M/s} $$

> ✏️ **YOUR TURN 1 — four questions**
>
> 1. For N₂ + 3H₂ → 2NH₃, if N₂ is consumed at
>    0.020 M/s, how fast is H₂ consumed?
>    *(working space)*
> 2. How fast is NH₃ formed in (a)? 
>    *(working space)*
> 3. Why is the rate of change of a reactant negative?
>    *(working space)*
> 4. Why divide each rate by its coefficient? 
>    *(working space)*
> 
> > **check:** (a) 0.060 M/s    
> (b) 0.040 M/s     (c) its concentration falls    
> (d) to get one rate independent of the species watched

## Ladder 2 • Rate law from initial rates

`CED 5.2`

Compare two experiments in which *one* concentration changes and the
others are held constant. The factor the rate changes by tells you the
order.

> 📘 **I do: reading a rate table**
>
> For A + 2B → C:
> 
> | **Exp** | $[\text{A}]_0$ | $[\text{B}]_0$ | **rate** (M/s) |
> |---|---|---|---|
> | 1 | 0.050 | 0.10 | $1.2\times10^{-3}$ |
> | 2 | 0.100 | 0.10 | $4.8\times10^{-3}$ |
> | 3 | 0.050 | 0.20 | $2.4\times10^{-3}$ |

**Order in A:** compare 1 and 2, where $[\text{B}]$ is constant.
$[\text{A}]$ doubles and the rate goes up by
$4.8/1.2 = 4$. Since $2^n = 4$, $n = \mathbf{2}$.

**Order in B:** compare 1 and 3, where $[\text{A}]$ is constant.
$[\text{B}]$ doubles and the rate doubles, so $n = \mathbf{1}$.

$$ \text{rate} = k[\text{A}]^2[\text{B}] \qquad    \text{overall order } 2 + 1 = \mathbf{3} $$

**Note what the equation would have suggested:** a coefficient of 2
on B, hence perhaps second order in B. The data say first. Orders are
experimental.

> ✏️ **YOUR TURN 2 — four questions**
>
> 1. If tripling a reactant's concentration multiplies the rate by 9,
>    what is the order?
>    *(working space)*
> 2. If doubling a concentration leaves the rate unchanged, what is the
>    order?
>    *(working space)*
> 3. If doubling a concentration multiplies the rate by 8, what is the
>    order?
>    *(working space)*
> 4. Why must the other concentrations be held constant?
>    *(working space)*
> 
> > **check:** (a) second     (b) zero     (c) third     (d) otherwise
> you cannot attribute the change to one reactant

## Ladder 3 • The rate constant and its units

`CED 5.2`

$k$ is found by substituting one experiment back into the rate law. Its
*units* are whatever makes the equation dimensionally consistent, and
they depend on the overall order.

> 📘 **I do: value and units together**
>
> From experiment 1 above, find $k$ with units.
> 
> $$ k = \frac{\text{rate}}{[\text{A}]^2[\text{B}]}      = \frac{1.2\times10^{-3}}{(0.050)^2(0.10)}      = \frac{1.2\times10^{-3}}{2.5\times10^{-4}} = \mathbf{4.8} $$
> 
> **Units:** rate is M/s and
> $[\text{A}]^2[\text{B}]$ is M³, so $k$ carries
> /M²/s — that is,
> M\textsuperscript-2 s\textsuperscript-1.
> 
> **Check with another experiment:**
> $4.8(0.100)^2(0.10) = 4.8\times10^{-3}$, matching experiment 2.
> ✓ A rate constant that fails this check means the orders are
> wrong.
> 
> **The pattern:** overall order 0 gives M/s; order
> 1 gives /s; order 2 gives
> /M/s; order 3 gives
> /M²/s.

> ✏️ **YOUR TURN 3 — four questions**
>
> 1. Units of $k$ for a first-order reaction: 
>    *(working space)*
> 2. Units of $k$ for a second-order reaction: 
>    *(working space)*
> 3. A reaction has rate $= k[\text{A}][\text{B}]$ with rate
>    6.0e-4 M/s when both are
>    0.20 M. Find $k$.
>    *(working space)*
> 4. Why do the units of $k$ differ between orders?
>    *(working space)*
> 
> > **check:** (a) /s     (b) /M/s    
> (c) 1.5e-2 /M/s     (d) they must make the
> equation dimensionally consistent

## Ladder 4 • Integrated rate laws: which plot is straight?

`CED 5.3`

Given concentration-versus-time data, the order is identified by which
plot comes out linear.

> 📘 **I do: the three tests**
>
> State which plot is linear for each order, and what the slope gives.
> 
> **Zero order:** $[\text{A}]$ against $t$ is linear. Slope $= -k$.
> The concentration falls by equal *amounts* in equal times.
> 
> **First order:** $\ln[\text{A}]$ against $t$ is linear. Slope
> $= -k$. The concentration falls by equal *fractions* in equal times
> — which is what a constant half-life means.
> 
> **Second order:** $1/[\text{A}]$ against $t$ is linear. Slope
> $= +k$, positive because the reciprocal grows.
> 
> **How to use it:** plot all three from the same data. Exactly one
> comes out straight, and that identifies the order. The slope then gives
> $k$ directly — and note the sign: negative for zero and first order,
> positive for second.

> ✏️ **YOUR TURN 4 — four questions**
>
> 1. A plot of $\ln[\text{A}]$ against time is a straight line. What
>    order?
>    *(working space)*
> 2. A plot of $1/[\text{A}]$ against time is straight with slope
>    $+0.25$. Give the order and $k$.
>    *(working space)*
> 3. For a zero-order reaction, what does a graph of $[\text{A}]$ against
>    $t$ look like?
>    *(working space)*
> 4. Which order has a half-life independent of concentration?
>    *(working space)*
> 
> > **check:** (a) first     (b) second, $k = 0.25$
> /M/s     (c) a straight line of negative slope
>     (d) first

## Ladder 5 • Half-life

`CED 5.3`

For a first-order reaction, $t_{1/2} = 0.693/k$ — constant, whatever the
concentration. Every half-life removes half of whatever remains.

> 📘 **I do: half-life and successive halvings**
>
> A first-order reaction has $k = 0.0300\,\mathrm{/s}$ and starts at
> 0.800 M. Find the half-life and the concentration after three
> half-lives.
> 
> $$ t_{1/2} = \frac{0.693}{0.0300} = \mathbf{23.1~s} $$
> 
> **Three half-lives:**
> $0.800 \to 0.400 \to 0.200 \to \mathbf{0.100~M}$, taking
> $3 \times 23.1 = 69.3\,\mathrm{s}$.
> 
> **Why the half-life does not drift.** As the concentration falls, the
> rate falls in exact proportion — that is what first order means. Half of
> a smaller amount takes exactly as long to disappear as half of a larger
> one did.
> 
> **Contrast:** for a *second*-order reaction the half-life
> *doubles* each time, because the rate falls faster than the
> concentration does.

> ✏️ **YOUR TURN 5 — four questions**
>
> 1. Half-life when $k = 2.5e-4\,\mathrm{/s}$:
>    *(working space)*
> 2. Fraction remaining after four half-lives: 
>    *(working space)*
> 3. Starting at 0.600 M, concentration after four
>    half-lives:
>    *(working space)*
> 4. Does a first-order half-life depend on the starting
>    concentration? Explain.
>    *(working space)*
> 
> > **check:** (a) 2.8e3 s     (b) $1/16$    
> (c) 0.0375 M     (d) no — $t_{1/2} = 0.693/k$ only

## Ladder 6 • Elementary reactions

`CED 5.4`

An elementary step describes an actual molecular event. For an elementary
step *only*, the coefficients may be used as the orders.

> 📘 **I do: when coefficients are allowed**
>
> For the elementary step 2NO₂ → NO₃ + NO, write the rate law. Then
> explain why the same cannot be done for the overall equation
> 2NO₂ + F₂ → 2NO₂F.
> 
> **Elementary step:** the event is two NO₂ molecules colliding,
> so
> 
> $$ \text{rate} = k[\text{NO₂}]^2 $$
> 
> This is legitimate *because* the step is elementary — the equation
> describes the collision itself.
> 
> **Overall equation:** it is a summary of the net change, not a
> description of any single event. It says nothing about how many molecules
> actually meet in the slow step. Writing
> $\text{rate} = k[\text{NO₂}]^2[\text{F₂}]$ from it would be a guess, and
> experiment shows the true law is $k[\text{NO₂}][\text{F₂}]$.
> 
> **Molecularity:** one molecule is unimolecular, two bimolecular.
> Termolecular steps — three particles meeting at once — are very rare,
> which is why proposed mechanisms almost never contain them.

> ✏️ **YOUR TURN 6 — four questions**
>
> 1. Rate law for the elementary step A + B → C:
>    *(working space)*
> 2. Rate law for the elementary step 2A → B:
>    *(working space)*
> 3. What is the molecularity of O₃ → O₂ + O?
>    *(working space)*
> 4. Why are termolecular steps rare? 
>    *(working space)*
> 
> > **check:** (a) $k[\text{A}][\text{B}]$     (b) $k[\text{A}]^2$    
> (c) unimolecular     (d) three particles colliding simultaneously is
> very improbable

## Ladder 7 • The collision model

`CED 5.5`

A collision produces reaction only if it carries at least the activation
energy *and* the molecules are correctly oriented. Everything that
changes a rate changes one of those two.

> 📘 **I do: why a small warming does so much**
>
> A rise of 10 °C can roughly double a rate, though it raises
> the average speed only a few percent. Explain.
> 
> **What actually matters** is the *fraction* of collisions
> carrying at least $E_a$, and that fraction lies far out in the
> high-energy tail of the distribution of molecular energies.
> 
> **Warming shifts and broadens the whole distribution.** Near the
> average that is a small change. Out in the tail, where the threshold sits,
> the population rises steeply — easily doubling.
> 
> **Collision frequency rises too, but only slightly** — a few
> percent, in line with the speed. Essentially all of the rate increase
> comes from the energy distribution, not from more collisions.
> 
> **The answer that earns half marks:** “molecules move faster and
> collide more often”. True, but it is the smaller effect; the marks are
> for the fraction above $E_a$.

> ✏️ **YOUR TURN 7 — four questions**
>
> 1. State the two requirements for a successful collision.
>    *(working space)*
> 2. Why does increasing concentration increase the rate?
>    *(working space)*
> 3. Why does powdering a solid reactant speed up its reaction?
>    *(working space)*
> 4. Which effect of warming matters more: more collisions, or more
>    energetic ones?
>    *(working space)*
> 
> > **check:** (a) enough energy, correct orientation     (b) more frequent
> collisions     (c) more exposed surface area     (d) more energetic
> ones, by far

## Ladder 8 • Reading an energy profile

`CED 5.6` `CED 5.10`

The vertical axis is potential energy. The peak is the transition state;
the climb from reactants to peak is $E_a$; the difference between the two
ends is $\Delta H$.

> 📘 **I do: everything on one diagram**
>
> A profile rises from reactants at 50 kJ to a peak at
> 170 kJ, then falls to products at 20 kJ.
> Find $E_a$ forward, $E_a$ reverse and $\Delta H$, and say whether it is
> exothermic.
> 
> **Forward $E_a$:** $170 - 50 = \mathbf{120~kJ}$ — reactants up to
> the peak.
> 
> **Reverse $E_a$:** $170 - 20 = \mathbf{150~kJ}$ — products up to
> the same peak.
> 
> **$\Delta H$:** $20 - 50 = \mathbf{-30~kJ}$, products minus
> reactants. Negative, so **exothermic** — and the products sit lower
> than the reactants, which is the visual signature.
> 
> **The relationship worth remembering:**
> $\Delta H = E_{a,\text{forward}} - E_{a,\text{reverse}} = 120 - 150 = -30$ kJ. ✓
> 
> **A multi-step profile** has one peak per step, with shallow minima
> between them where intermediates sit. The *highest* peak is the
> rate-determining step.

> ✏️ **YOUR TURN 8 — four questions**
>
> 1. Reactants 30 kJ, peak 110 kJ,
>    products 75 kJ. Forward $E_a$?
>    *(working space)*
> 2. $\Delta H$ for that reaction, and is it endo- or exothermic?
>    *(working space)*
> 3. On a two-step profile, how do you identify the rate-determining
>    step?
>    *(working space)*
> 4. What sits in the shallow minimum between two peaks?
>    *(working space)*
> 
> > **check:** (a) 80 kJ     (b) $+45$ kJ, endothermic    
> (c) the step with the highest peak     (d) an intermediate

## Ladder 9 • Mechanisms and the rate-determining step

`CED 5.7` `CED 5.8` `CED 5.9`

A mechanism is valid only if its steps add to the overall equation
*and* its slow step predicts the observed rate law.

> 📘 **I do: testing a mechanism**
>
> Test this mechanism for NO₂ + CO → NO + CO₂, whose observed rate law
> is $k[\text{NO₂}]^2$:
> 
> $$ \begin{align*} \text{Step 1:}\quad & \text{NO₂ + NO₂ → NO₃ + NO} \qquad \text{(slow)}\\ \text{Step 2:}\quad & \text{NO₃ + CO → NO₂ + CO₂} \qquad \text{(fast)} \end{align*} $$
> 
> **Do the steps add?** Summing:
> 2NO₂ + NO₃ + CO → NO₃ + NO + NO₂ + CO₂. Cancel NO₃ from both
> sides and one NO₂:
> NO₂ + CO → NO + CO₂. ✓
> 
> **Does the slow step give the observed law?** Step 1 is elementary
> and bimolecular in NO₂, so
> $\text{rate} = k[\text{NO₂}]^2$. ✓
> 
> **The striking prediction:** CO does not appear in the rate law
> at all, even though it is a reactant. It enters only in the *fast*
> step, after the bottleneck — so adding more of it does not speed the
> reaction up. That is exactly what the experiment finds, and it is strong
> evidence for this mechanism.

> ✏️ **YOUR TURN 9 — four questions**
>
> 1. In the mechanism above, identify the intermediate.
>    *(working space)*
> 2. Which step determines the rate, and why? 
>    *(working space)*
> 3. Why does CO not appear in the rate law? 
>    *(working space)*
> 4. What two tests must any proposed mechanism pass?
>    *(working space)*
> 
> > **check:** (a) NO₃     (b) step 1, the slow one     (c) it
> appears only after the slow step     (d) steps sum to the overall
> equation; slow step gives the observed rate law

## Ladder 10 • Intermediates versus catalysts

`CED 5.7` `CED 5.11`

Both appear inside a mechanism and neither appears in the overall
equation — but they are opposites. An intermediate is
*made then used*; a catalyst is *used then remade*.

> 📘 **I do: telling them apart**
>
> In this mechanism, identify the catalyst and the intermediate:
> 
> $$ \begin{align*} \text{Step 1:}\quad & \text{X + A → XA} \\ \text{Step 2:}\quad & \text{XA + B → C + X} \end{align*} $$
> 
> **X is the catalyst.** It is *consumed* in step 1 and
> *regenerated* in step 2 — present at the start, present at the end,
> unchanged overall.
> 
> **XA is the intermediate.** It is *produced* in step 1 and
> *consumed* in step 2 — absent at the start, absent at the end.
> 
> **The test is the order of events.** Consumed first, then produced:
> catalyst. Produced first, then consumed: intermediate.
> 
> **Overall:** A + B → C, with X appearing nowhere —
> which is why a catalyst is never written into the equation, only above the
> arrow.

> ✏️ **YOUR TURN 10 — four questions**
>
> 1. A species is produced in step 1 and consumed in step 3. What is
>    it?
>    *(working space)*
> 2. A species is consumed in step 1 and regenerated in step 3. What is
>    it?
>    *(working space)*
> 3. Why does neither appear in the overall equation?
>    *(working space)*
> 4. Can a catalyst appear in the rate law? 
>    *(working space)*
> 
> > **check:** (a) an intermediate     (b) a catalyst     (c) both cancel
> when the steps are added     (d) yes, if it acts at or before the slow
> step

## Ladder 11 • How a catalyst works

`CED 5.11`

A catalyst provides an *alternative pathway* with a lower activation
energy. It does not push the old reaction harder — it opens a new route.

> 📘 **I do: what changes and what does not**
>
> State precisely what a catalyst changes and what it leaves alone.
> 
> **Changes: the activation energy.** The new pathway has a lower
> barrier, so at any given temperature a larger fraction of collisions
> carries enough energy. The rate rises, often by orders of magnitude.
> 
> **Does *not* change $\Delta H$.** Reactants and products sit at
> exactly the same energies as before. Only the height of the hill between
> them is reduced — the two ends are untouched.
> 
> **Does *not* change the equilibrium position or $K$.** The
> forward and reverse barriers are lowered by the *same* amount, so
> both rates rise in the same proportion. Equilibrium arrives sooner, in
> exactly the same place.
> 
> **Two answers that earn zero:** “it lowers the energy of the
> reactants” and “it shifts the equilibrium toward products”. Both
> describe things a catalyst cannot do.

> ✏️ **YOUR TURN 11 — four questions**
>
> 1. What does a catalyst do to the activation energy?
>    *(working space)*
> 2. What does it do to $\Delta H$? 
>    *(working space)*
> 3. What does it do to the yield at equilibrium?
>    *(working space)*
> 4. Explain why a catalyst speeds the reverse reaction too.
>    *(working space)*
> 
> > **check:** (a) lowers it, via a new pathway     (b) nothing    
> (c) nothing     (d) the same lowered barrier is crossed either way

## Ladder 12 • Kinetics versus thermodynamics

`CED 5.5` `CED 5.6`

Two independent questions: *does it want to happen* (thermodynamics)
and *will it happen quickly* (kinetics). The answers need not agree.

> 📘 **I do: favourable but immeasurably slow**
>
> Diamond converting to graphite has
> $\Delta G^\circ = -2.9\,\mathrm{kJ/mol}$ — thermodynamically
> favourable at room temperature. Explain why diamonds do not visibly
> change.
> 
> **Thermodynamics says it should happen.** A negative $\Delta G$ means
> graphite is the more stable form, and the conversion would release energy.
> 
> **Kinetics says it will not, on any human timescale.** Rearranging
> diamond's covalent network requires breaking very strong C-C bonds —
> an enormous activation energy. At room temperature essentially no atom has
> that much energy, so the rate is indistinguishable from zero.
> 
> **The general statement:** $\Delta G$ tells you about the
> *destination*; $E_a$ tells you about the *journey*. A large
> negative $\Delta G$ with a large $E_a$ describes a reaction that is
> strongly favourable and completely stuck — which is why fuels can sit
> safely in a tank in air.

> ✏️ **YOUR TURN 12 — four questions**
>
> 1. Petrol and oxygen do not react at room temperature although the
>    reaction is highly favourable. Why?
>    *(working space)*
> 2. What does a spark supply? 
>    *(working space)*
> 3. Does a large equilibrium constant mean a fast reaction?
>    *(working space)*
> 4. Name two ways to speed a reaction without changing $\Delta H$.
>    *(working space)*
> 
> > **check:** (a) high activation energy     (b) energy to surmount $E_a$
>     (c) no     (d) raise the temperature; add a catalyst

## Where you stand

Tick a ladder only if all four YOUR TURN questions were right first time.

| **First try?** | **Skill** | **Ladder** | **If not, re-read…** |
|---|---|---|---|
| $\square$ | expressing rate | 1 | divide by coefficients |
| $\square$ | rate law from data | 2 | hold the others constant |
| $\square$ | $k$ and its units | 3 | units follow the order |
| $\square$ | which plot is straight | 4 | $\ln$ first, $1/[\text{A}]$ second |
| $\square$ | half-life | 5 | first order: independent of $c$ |
| $\square$ | elementary steps | 6 | coefficients allowed only here |
| $\square$ | collision model | 7 | the tail above $E_a$ |
| $\square$ | energy profiles | 8 | peak minus start |
| $\square$ | mechanisms | 9 | sum, then slow step |
| $\square$ | intermediate vs catalyst | 10 | which comes first |
| $\square$ | how catalysts work | 11 | new path, same $\Delta H$ |
| $\square$ | kinetics vs thermodynamics | 12 | how fast vs how far |

> 📌 **Scoring yourself honestly**
>
> 12/12: move on to the unit worksheets and the free-response set.
> 9–11: solid — redo the missed ladders tomorrow from a blank page.
> 8 or fewer: the recurring root causes here are exactly three —
> (1) reading reaction orders off the balanced equation instead of from
> data or the slow step, (2) quoting a rate constant with no units, and
> (3) answering a rate question with a stability argument. Fix those three
> and most of these ladders fall together.

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
