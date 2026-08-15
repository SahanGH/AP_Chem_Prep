# Guided Notes

*Chapter 16 • Solubility Equilibria*  
Zumdahl §16.1 • PDF pp. 805–813 • 4 blocks

[← all lessons](../index.md)

---

> 📌 **How this chapter fits the AP course**
>
> **This short chapter completes the CED.** §16.1 alone carries the last
> three topics not covered anywhere else in these materials:
> **7.11** (solubility equilibria and $K_{sp}$), **7.12** (the
> common-ion effect applied to solubility) and **8.11** (pH and
> solubility).
> 
> **Skip the rest of the chapter.** §16.2 (precipitation and qualitative
> analysis) and §16.3 (complex ion equilibria) are not on the framework.
> A short treatment of $Q$ versus $K_{sp}$ closes Block 4 because the
> reasoning is Unit 7 material you already own — but it is flagged as
> enrichment, and the chapter test does not assess it.
> 
> **One CED boundary matters more than usual here.** Topic 8.11 carries
> an explicit *exclusion statement*: *computations of solubility as
> a function of pH will not be assessed*. So pH and solubility is taught
> **qualitatively**, by Le Ch\^atelier, and every quantitative
> common-ion problem in these materials uses an ion that is *not*
> pH-sensitive. That is a deliberate choice, not an omission.
> 
> Nothing here is a new kind of equilibrium. A saturated solution is a
> system at equilibrium with a solid, and $K_{sp}$ is its equilibrium
> constant with the solid left out — exactly the rule from Chapter 13.

## $K_{sp}$ and the Solubility Product Zumdahl §16.1

> 📌 **By the end you can…**
>
> - Write the $K_{sp}$ expression for any sparingly soluble salt.
> - Calculate $K_{sp}$ from a measured solubility.

**Read:** Zumdahl §16.1 • PDF pp. 805–810

> 📌 **Retrieval warm-up**
>
> 1. Species omitted from any $K$ expression:
>    **\_\_\_\_\_\_**
> 2. $K$ for 2A ⇌ B in terms of concentrations:
>    **\_\_\_\_\_\_**
> 3. Is AgCl soluble or insoluble by the Unit 4 rules?
>    **\_\_\_\_\_\_**
> 4. If $Q saturated — and that is a
**\_\_\_\_\_\_**, not a solution that has “stopped
dissolving.”

CaF₂(s) ⇌ Ca²⁺(aq) + 2F⁻(aq)

The equilibrium constant for this process is the solubility product,
$K_{sp}$:

$$ K_{sp} = [\text{Ca²⁺}][\text{F⁻}]^2 $$

Two features to notice, both of which are old rules reappearing:

- The solid does *not* appear — it is a
   **\_\_\_\_\_\_**, exactly as in Chapter 13.
- Each ion is raised to the power of its
   **\_\_\_\_\_\_**, so the 2 in 2F⁻ becomes an
   exponent.

> 📌 **Why more solid does not mean more dissolved**
>
> It seems as though a bigger pile of solid — more surface area — ought to
> give a more concentrated solution. Zumdahl's answer is worth keeping:
> doubling the surface area doubles the rate of dissolving, but it
> *equally* doubles the rate at which ions re-deposit on that surface.
> The two effects cancel and the equilibrium position does not move.
> 
> Grinding the solid or stirring the mixture makes equilibrium arrive
> *sooner*. Neither changes how much ends up dissolved.

> ⚠️ **AP trap**
>
> **$K_{sp}$ is an equilibrium constant; solubility is an equilibrium
> position.** This one sentence organizes the whole chapter.
> 
> $K_{sp}$ has a single value for a given solid at a given temperature.
> Solubility is how much actually dissolves, and it changes with what else is
> in the water — add a common ion and the solubility falls, while $K_{sp}$
> does not move at all. Students who treat the two words as synonyms get
> every common-ion question wrong.

#### GUIDED PRACTICE • Writing the expressions 15 min

1. AgCl: $K_{sp} =$
   **\_\_\_\_\_\_**
2. PbI₂: $K_{sp} =$
   **\_\_\_\_\_\_**
3. Ag₂CrO₄: $K_{sp} =$
   **\_\_\_\_\_\_**
4. Mg(OH)₂: $K_{sp} =$
   **\_\_\_\_\_\_**
5. Ca₃(PO₄)₂: $K_{sp} =$
   **\_\_\_\_\_\_**

#### INSTRUCTION B • From measured solubility to $K_{sp}$ 20 min

### The ICE table is trivial — the stoichiometry is not `ZUM §16.1`

`SP 5`

If $s$ moles of salt dissolve per litre, the ion concentrations follow
directly from the coefficients. That is the only step where mistakes
happen.

| **Type** | **Example** | **Ions at equilibrium** | **$K_{sp}$** |
|---|---|---|---|
| MX | AgCl | $s$, $s$ | $s^2$ |
| MX₂ | CaF₂ | $s$, $2s$ | $(s)(2s)^2 = 4s^3$ |
| M₂X | Ag₂CrO₄ | $2s$, $s$ | $(2s)^2(s) = 4s^3$ |
| M₃X | Ag₃PO₄ | $3s$, $s$ | $(3s)^3(s) = 27s^4$ |

Note that MX₂ and M₂X give the *same* formula, $4s^3$ —
which is why they can be compared with each other but not with an MX
salt.

> 📘 **Worked example 1: Zumdahl's copper(I) bromide**
>
> CuBr has a measured solubility of
> $2.0\times10^{-4}$ mol/L at 25 °C. Find $K_{sp}$.
> 
> $$ \text{CuBr(s) ⇌ Cu+(aq) + Br⁻(aq)} \qquad    K_{sp} = [\text{Cu+}][\text{Br-}] $$
> 
> Each formula unit gives one of each ion, so
> $[\text{Cu+}] = [\text{Br-}] = 2.0\times10^{-4}$:
> 
> $$ K_{sp} = (2.0\times10^{-4})(2.0\times10^{-4})    = \mathbf{4.0\times10^{-8}} $$
> 
> Units are conventionally omitted.

> 📘 **Worked example 2: a 1:2 salt, and grams to moles**
>
> Lead(II) iodide dissolves to the extent of 0.70 g/L at
> 25 °C. Find $K_{sp}$. ($M = 461.0\,\mathrm{g/mol}$)
> 
> **Convert first.** $s = 0.70/461.0 = 1.52\times10^{-3}$ mol/L.
> 
> **Then the stoichiometry.**
> PbI₂(s) ⇌ Pb²⁺(aq) + 2I⁻(aq), so $[\text{Pb²⁺}] = s$ and
> $[\text{I-}] = 2s = 3.04\times10^{-3}$:
> 
> $$ K_{sp} = (1.52\times10^{-3})(3.04\times10^{-3})^2    = \mathbf{1.4\times10^{-8}} $$
> 
> Forgetting to double the iodide gives $3.5\times10^{-9}$ — low by a
> factor of 4, and a guaranteed lost point.

#### APPLICATION • Calculating $K_{sp}$ 20 min

1. BaSO₄ dissolves to $9.0\times10^{-3}$ g/L
   ($M = 233.4\,\mathrm{g/mol}$). Find $K_{sp}$.
   *(working space)*
2. Ag₂CrO₄ has a solubility of $1.3\times10^{-4}$ M. Find
   $K_{sp}$.
   *(working space)*
3. A student computes $K_{sp}$ for CaF₂ as $(s)(s)^2$. What did
   they miss, and by what factor is the answer wrong?
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> 📌 **Exit ticket**
>
> A saturated solution of AgCl sits over a pile of undissolved
> AgCl. A student adds a second spoonful of solid AgCl. What
> happens to $[\text{Ag+}]$, and what happens to $K_{sp}$?

## Solubility from $K_{sp}$, and Comparing Salts Zumdahl §16.1

> 📌 **By the end you can…**
>
> - Calculate molar solubility from $K_{sp}$ for any stoichiometry.
> - Judge when $K_{sp}$ values may be compared directly and when they
>    may not.

**Read:** Zumdahl §16.1 (Relative Solubilities) • PDF pp. 808–811

> 📌 **Retrieval warm-up**
>
> 1. $K_{sp}$ for an MX salt in terms of $s$:
>    **\_\_\_\_\_\_**
> 2. $K_{sp}$ for an MX₂ salt in terms of $s$:
>    **\_\_\_\_\_\_**
> 3. $K_{sp}$ is a constant; solubility is a
>    **\_\_\_\_\_\_**

#### INSTRUCTION A • Running the calculation backwards 25 min

### Solving for $s$ `ZUM §16.1`

`SP 5`

Going from $K_{sp}$ to solubility is the same relationship read the other
way. Rearranged:

| **Type** | **Relation** | **Solubility** |
|---|---|---|
| MX | $K_{sp} = s^2$ | $s = \sqrt{K_{sp}}$ |
| MX₂ or M₂X | $K_{sp} = 4s^3$ | $s = \sqrt[3]{K_{sp}/4}$ |
| M₃X | $K_{sp} = 27s^4$ | $s = \sqrt[4]{K_{sp}/27}$ |

> 📘 **Worked example 3: two stoichiometries side by side**
>
> **AgCl**, $K_{sp} = 1.6\times10^{-10}$.
> Let $s = [\text{Ag+}] = [\text{Cl-}]$:
> 
> $$ 1.6\times10^{-10} = s^2 \;\Longrightarrow\;    s = \mathbf{1.3\times10^{-5}}~\text{M} $$
> 
> **CaF₂**, $K_{sp} = 4.0\times10^{-11}$.
> Here $[\text{Ca²⁺}] = s$ and $[\text{F-}] = 2s$:
> 
> $$ 4.0\times10^{-11} = (s)(2s)^2 = 4s^3    \;\Longrightarrow\; s^3 = 1.0\times10^{-11}    \;\Longrightarrow\; s = \mathbf{2.2\times10^{-4}}~\text{M} $$
> 
> Notice: CaF₂ has the *smaller* $K_{sp}$ but is over ten times
> *more* soluble. Hold that thought.

#### INSTRUCTION B • When you may compare $K_{sp}$ values 20 min

### The comparison trap `ZUM §16.1`

`SP 6`

> 
$K_{sp}$ values may be compared directly **only** for salts that
produce the **same total number of ions**.

**Same stoichiometry — comparison works.** All three of these are
MX salts, so $s = \sqrt{K_{sp}}$ for each and the order of $K_{sp}$ is
the order of solubility:

| **Salt** | $K_{sp}$ | **solubility (M)** |
|---|---|---|
| AgI | $1.5\times10^{-16}$ | $1.2\times10^{-8}$ |
| CuI | $5.0\times10^{-12}$ | $2.2\times10^{-6}$ |
| CaSO₄ | $6.1\times10^{-5}$ | $7.8\times10^{-3}$ |

**Different stoichiometry — the order can reverse outright.**
Zumdahl's example is worth memorizing because it is so extreme:

| **Salt** | **type** | $K_{sp}$ | **solubility (M)** |
|---|---|---|---|
| CuS | MX | $8.5\times10^{-45}$ | $9.2\times10^{-23}$ |
| Ag₂S | M₂X | $1.6\times10^{-49}$ | $3.4\times10^{-17}$ |
| Bi₂S₃ | M₂X₃ | $1.1\times10^{-73}$ | $1.0\times10^{-15}$ |

$K_{sp}$ order: CuS $>$ Ag₂S $>$ Bi₂S₃.   

Solubility order: **\_\_\_\_\_\_**
— **exactly reversed**.

> ⚠️ **AP trap**
>
> The reversal is not mysterious. Bi₂S₃ produces *five* ions per
> formula unit, so its $K_{sp}$ is a product of five concentration factors,
> each tiny. Multiplying five small numbers gives an absurdly small
> $K_{sp}$ even when a respectable amount of solid has dissolved.
> 
> The rule to carry into the exam: **if the formulas do not have the
> same ion count, you must calculate $s$ before you may rank them.**

### Connecting back to the Unit 4 solubility rules `ZUM §16.1`

The solubility rules you memorized in Unit 4 are the qualitative version of
this same idea. The CED makes the link explicit: a salt with
$K_{sp} > 1$ is what those rules call
**\_\_\_\_\_\_**, and the very small $K_{sp}$ values in the
table belong to the salts the rules call
**\_\_\_\_\_\_**. “Insoluble” never meant zero — it meant
an equilibrium lying far to the left.

#### APPLICATION • Ranking and calculating 20 min

1. Calculate the molar solubility of Mg(OH)₂,
   $K_{sp} = 8.9\times10^{-12}$.
   *(working space)*
2. Rank BaSO₄ ($1.5\times10^{-9}$), SrSO₄
   ($3.2\times10^{-7}$) and PbSO₄ ($1.3\times10^{-8}$) by
   increasing solubility, and say why no calculation is needed.
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
3. CaF₂ ($K_{sp} = 4.0\times10^{-11}$) and BaCrO₄
   ($K_{sp} = 8.5\times10^{-11}$). Which is more soluble?
   *(working space)*

> 📌 **Exit ticket**
>
> Salt A has a larger $K_{sp}$ than salt B. A student concludes A is more
> soluble. Under what condition are they right, and under what condition
> could they be badly wrong?

## The Common-Ion Effect on Solubility Zumdahl §16.1

> 📌 **By the end you can…**
>
> - Predict qualitatively how a common ion changes solubility.
> - Calculate solubility in a solution already containing a common ion.

**Read:** Zumdahl §16.1 (Common Ion Effect) • PDF pp. 811–812

> 📌 **Retrieval warm-up**
>
> 1. Molar solubility of AgCl in pure water
>    ($K_{sp} = 1.6\times10^{-10}$):
>    **\_\_\_\_\_\_**
> 2. Adding a product shifts an equilibrium:
>    **\_\_\_\_\_\_**
> 3. A common ion is one that is:
>    **\_\_\_\_\_\_**
> 4. Does adding a common ion change $K_{sp}$?
>    **\_\_\_\_\_\_**

#### INSTRUCTION A • Le Ch\^atelier, one more time 25 min

### Why solubility falls `ZUM §16.1`

`SP 6`

CaF₂(s) ⇌ Ca²⁺(aq) + 2F⁻(aq)

Dissolve the salt in a solution that already contains F- — from
NaF, say — and you have added a **\_\_\_\_\_\_**. The
equilibrium shifts **\_\_\_\_\_\_**, so *less* CaF₂
dissolves.

This is the identical mechanism you met in Chapter 15, where NaF
suppressed the ionization of HF. Only the equilibrium has changed.

> ⚠️ **AP trap**
>
> Say precisely what moved. The *solubility* decreased; $K_{sp}$ did
> **not** change — it cannot, because nothing about the temperature
> changed. The product $[\text{Ca²⁺}][\text{F-}]^2$ still equals
> $4.0\times10^{-11}$; the two concentrations have simply redistributed, with
> much more fluoride and much less calcium.
> 
> “The common ion lowers $K_{sp}$” is marked wrong every time.

> 📘 **Worked example 4: Zumdahl's calcium fluoride**
>
> Find the solubility of CaF₂ ($K_{sp} = 4.0\times10^{-11}$) in
> 0.025 M NaF, and compare with pure water.
> 
> Let $s$ be the moles of CaF₂ that dissolve per litre.
> 
> |  | $[\text{Ca²⁺}]$ | $[\text{F-}]$ |
> |---|---|---|
> | initial | 0 | 0.025 |
> | change | $+s$ | $+2s$ |
> | equilibrium | $s$ | $0.025 + 2s$ |

$$ 4.0\times10^{-11} = (s)(0.025 + 2s)^2 \approx (s)(0.025)^2 $$

because $K_{sp}$ is tiny, so $2s$ is negligible beside 0.025. Then

$$ s = \frac{4.0\times10^{-11}}{6.25\times10^{-4}}      = \mathbf{6.4\times10^{-8}}~\text{M} $$

In pure water the solubility was $2.2\times10^{-4}$ M. The fluoride already
present cut it by a factor of about **3400**.

#### GUIDED PRACTICE • Which ion, and which power 15 min

The size of the effect depends on *which* ion you add, because the two
ions enter the expression with different exponents.

1. AgCl in 0.10 M NaCl: $s = K_{sp}/[\text{Cl-}] =$
   **\_\_\_\_\_\_**
2. AgCl in 0.020 M AgNO₃:
   **\_\_\_\_\_\_**
3. BaSO₄ ($1.5\times10^{-9}$) in 0.010 M
   Na₂SO₄: **\_\_\_\_\_\_**
4. Would NaNO₃ change the solubility of AgCl? Why?
   **\_\_\_\_\_\_**

#### INSTRUCTION B • Adding the cation instead 20 min

### The exponent decides the sensitivity `ZUM §16.1`

`SP 5`

For CaF₂, adding F- is far more effective than adding
Ca²⁺, because fluoride is **\_\_\_\_\_\_** in the
expression while calcium is not.

> 📘 **Worked example 5: the same salt, the other ion**
>
> Find the solubility of CaF₂ in 0.10 M Ca(NO₃)₂.
> 
> Now the *calcium* is pre-loaded: $[\text{Ca²⁺}] = 0.10 + s \approx 0.10$
> and $[\text{F-}] = 2s$.
> 
> $$ 4.0\times10^{-11} = (0.10)(2s)^2 = 0.40s^2    \;\Longrightarrow\; s^2 = 1.0\times10^{-10}    \;\Longrightarrow\; s = \mathbf{1.0\times10^{-5}}~\text{M} $$
> 
> Note that the *fluoride is still doubled* even though calcium is the
> ion you added — the $(2s)^2$ contributes a factor of 4. Writing
> $(0.10)(s)^2$ here is the commonest slip in the whole chapter.
> 
> **Compare the three cases:**
> 
> | **Solvent** | **solubility (M)** | **fall** |
> |---|---|---|
> | pure water | $2.2\times10^{-4}$ | — |
> | 0.10 | thinsp;M Ca(NO₃)₂ | $1.0\times10^{-5}$ | $\times 22$ |
> | 0.10 | thinsp;M NaF | $4.0\times10^{-9}$ | $\times 54{,}000$ |

Same concentration of common ion, wildly different effect — because the
fluoride is squared.

#### APPLICATION • Common-ion calculations 20 min

1. Calculate the solubility of PbI₂
   ($K_{sp} = 1.4\times10^{-8}$) in 0.10 M NaI.
   *(working space)*
2. Explain, without calculating, why BaSO₄ is used as an X-ray
   contrast agent despite barium ions being toxic.
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
3. A student says a common ion works by “using up” the solid.
   Correct them.
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> 📌 **Exit ticket**
>
> CaF₂ is dissolved to saturation in 0.10 M NaF. State
> what happens to each of: the solubility of CaF₂, $[\text{F-}]$,
> $[\text{Ca²⁺}]$, and $K_{sp}$ — compared with pure water.

## pH and Solubility Zumdahl §16.1–16.2

> 📌 **By the end you can…**
>
> - Predict qualitatively how pH changes the solubility of a salt.
> - Use $Q$ against $K_{sp}$ to predict precipitation *(enrichment)*.

**Read:** Zumdahl §16.1 (pH and Solubility) • PDF pp. 812–813

> 📌 **Retrieval warm-up**
>
> 1. Common ion added $\Rightarrow$ solubility:
>    **\_\_\_\_\_\_**
> 2. Conjugate base of a *weak* acid is a:
>    **\_\_\_\_\_\_**
> 3. Conjugate base of a *strong* acid is a:
>    **\_\_\_\_\_\_**

> 📌 **Read this before Block 4**
>
> CED topic 8.11 carries an **exclusion statement**:
> *computations of solubility as a function of pH will not be assessed on
> the AP Exam.* Everything in this block is therefore **qualitative** —
> predict the direction and justify it with Le Ch\^atelier. If a question ever
> asks you to *calculate* a solubility at a given pH, it is not an AP
> question.

#### INSTRUCTION A • When does pH matter? 25 min

### Only if the anion is a base `ZUM §16.1`

`SP 6`

Mg(OH)₂(s) ⇌ Mg²⁺(aq) + 2OH⁻(aq)

Add acid. The H+ reacts with OH- and removes it from solution.
That is removing a **\_\_\_\_\_\_**, so the equilibrium shifts
**\_\_\_\_\_\_** and *more* solid dissolves.

This is why milk of magnesia — a suspension of solid Mg(OH)₂ —
dissolves in the stomach exactly as fast as it is needed to neutralize
excess acid.

Now the general principle. Adding acid can only pull an anion out of
solution if that anion actually reacts with H+ — that is, if it is a
meaningful base, which happens when its conjugate acid HX is
**\_\_\_\_\_\_**.

| **Anion** | **Conjugate acid** | **Solubility in acid** |
|---|---|---|
| OH-, S²⁻, CO₃²⁻, C₂O₄²⁻, CrO₄²⁻,
  PO₄³⁻, F- | *weak* — H₂O, H₂S, H₂CO₃, HF | **increases**: the anion is consumed |
| [0.7em]
Cl-, Br-, I-, NO₃-, ClO₄- | *strong* — HCl, HNO₃ | **unchanged**: the anion does not react |

> 📘 **Worked example 6: three salts, three answers**
>
> **Ag₃PO₄ in acid — more soluble.** PO₄³⁻ is a strong
> enough base to take a proton:
> H+(aq) + PO₄³⁻(aq) → HPO₄²⁻(aq)
> That lowers $[\text{PO₄³⁻}]$, so
> Ag₃PO₄(s) ⇌ 3Ag+(aq) + PO₄³⁻(aq) shifts right.
> 
> **AgCl in acid — unchanged.** Cl- is the conjugate base of
> HCl, a strong acid, so it has essentially no affinity for protons. No
> HCl molecules form, $[\text{Cl-}]$ is untouched, and the equilibrium does
> not move.
> 
> **Mg(OH)₂ in *base* — less soluble.** Raising the pH adds
> OH-, which is a product. This is the ordinary common-ion effect, and
> the solubility falls.

> ⚠️ **AP trap**
>
> “Acids are reactive, so everything dissolves better in acid” is false, and
> Zumdahl asks you to refute it directly. AgCl is the counterexample:
> its solubility in 1 M HNO₃ is the same as in pure water.
> The test is never how strong the acid is — it is whether the
> *anion* is a base.

#### GUIDED PRACTICE • More soluble in acid? 15 min

For each salt, write **yes** or **no** and name the anion's
conjugate acid:

1. CaCO₃: **\_\_\_\_\_\_**
2. AgBr: **\_\_\_\_\_\_**
3. CaF₂: **\_\_\_\_\_\_**
4. Fe(OH)₃: **\_\_\_\_\_\_**
5. PbI₂: **\_\_\_\_\_\_**

### Where limestone caves come from `ZUM §16.1`

Rainwater dissolves atmospheric CO₂, which makes it slightly acidic.
That acid attacks limestone:
CaCO₃(s) + H+(aq) → Ca²⁺(aq) + HCO₃⁻(aq)
Over long times this hollows out caverns. Where the water drips into open
air, dissolved CO₂ escapes, the pH rises, and the reverse happens —
CaCO₃ precipitates as stalactites and stalagmites. The same
equilibrium, run in both directions by nothing more than a change in pH.

#### APPLICATION • Predicting and justifying 20 min

Predict the effect of lowering the pH on the solubility of
        ZnS, and justify with an equation.
        

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

A solution is saturated with Mg(OH)₂. NaOH is added.
        State the effect on solubility, on $[\text{Mg²⁺}]$, and on
        $K_{sp}$. 

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Two beakers hold saturated AgCl and saturated CaCO₃.
        Nitric acid is added to both. Describe and explain what differs.
        

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

#### INSTRUCTION B • $Q$ versus $K_{sp}$ *(enrichment)* 20 min

> 📌 **Enrichment — not on the chapter test**
>
> Predicting precipitation is Zumdahl §16.2, which is off the CED as a topic.
> It is included here because the reasoning is nothing new: it is the
> $Q$-versus-$K$ comparison from Unit 7, applied to a dissolution.

Compute the ion product $Q$ using the concentrations *as mixed*,
before any reaction, then compare:

| $Q > K_{sp}$ | a precipitate forms, until the ions satisfy $K_{sp}$ |
|---|---|
| $Q = K_{sp}$ | exactly saturated; no change |
| $Q  📘 **Worked example 7: does a precipitate form?**
>
> 50.0 mL of 0.0020 M AgNO₃ is mixed with
> 50.0 mL of 0.0020 M NaCl.
> $K_{sp}(\text{AgCl}) = 1.6\times10^{-10}$.
> 
> **Dilution first** — the total volume is now
> 100.0 mL, so each concentration is halved:
> $[\text{Ag+}]_0 = [\text{Cl-}]_0 = 1.0\times10^{-3}$ M.
> 
> $$ Q = (1.0\times10^{-3})(1.0\times10^{-3}) = 1.0\times10^{-6} $$
> 
> $Q = 1.0\times10^{-6}$ is far greater than
> $K_{sp} = 1.6\times10^{-10}$, so **a precipitate forms**.
> 
> Skipping the dilution step is the usual error — and it changes $Q$ by a
> factor of 4 here.

> 📌 **Exit ticket**
>
> Give the single test that decides whether a salt's solubility depends on
> pH, and apply it to BaSO₄ and to BaCO₃.

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
