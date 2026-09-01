# Guided Notes

*Chapter 11 • Properties of Solutions*  
Zumdahl §11.1–11.3 (CED) + §11.4–11.7 (enrichment) • PDF pp. 551–581 • 4 blocks

[← all lessons](../index.md)

---

> 📌 **Read this first — about half the chapter is off-syllabus**
>
> **Examinable: §11.1–11.3.** Solution composition, the energetics of
> dissolving, and the factors that affect solubility — CED 3.7 and 3.10,
> taught in Unit 3.
> 
> **Not examinable: §11.4–11.8.** Vapour pressure lowering,
> boiling-point elevation, freezing-point depression, osmotic pressure, and
> colloids. Collectively the *colligative properties*, all dropped from
> the AP framework in the 2019 redesign. They appear here as
> **one clearly marked enrichment block**, included because freezing-point
> depression is the reason salt is spread on icy roads and osmosis is the
> reason cells burst in pure water — worth an hour, worth zero exam points.
> 
> Note that **molality** exists almost entirely to serve colligative
> calculations. It is defined in Block 1 for completeness and because
> distinguishing it from molarity sharpens what molarity actually means.

## Solution Composition Zumdahl §11.1

> 📌 **By the end you can…**
>
> - Compute molarity, molality, mass percent, and mole fraction.
> - Explain why molarity is temperature-dependent and molality is not.

**Read:** Zumdahl §11.1 • PDF pp. 552–555

> 📌 **Retrieval warm-up**
>
> 1. Moles in 58.44 g NaCl:
>    1.000 mol
> 2. $[\text{Cl-}]$ in 0.20 M CaCl₂:
>    0.40 M
> 3. Mole fraction of A if $n_A = 0.25$, $n_{\text{tot}} = 1.00$:
>    0.25

#### INSTRUCTION A • Four ways to state a concentration 25 min

### The definitions `ZUM §11.1`

`SP 5`

| **Measure** | **Definition** | **Note** |
|---|---|---|
| Molarity ($M$) | $\dfrac{\text{mol solute}}{\text{L solution}}$ | the working unit of AP chemistry |
| Molality ($m$) | $\dfrac{\text{mol solute}}{\text{kg solvent}}$ | used for colligative work |
| Mass percent | $\dfrac{\text{mass solute}}{\text{mass solution}}\times100\%$ | common in industry and medicine |
| Mole fraction ($\chi$) | $\dfrac{n_A}{n_{\text{total}}}$ | used for gas partial pressures |

> ⚠️ **AP trap**
>
> Two denominators, two different things. Molarity uses litres of
> *solution*; molality uses kilograms of *solvent*. Dissolving a
> solid changes the volume but not the mass of solvent — which is exactly
> why these are different numbers, and why you cannot convert between them
> without knowing the density.

#### Why molality is temperature-independent

Volume expands when a solution is warmed, so molarity
decreases even though nothing was added or removed. Mass
does not change with temperature, so molality stays
constant. That is the only reason molality exists.

> 📘 **Worked example: one solution, four numbers**
>
> Dissolve 5.00 g of NaCl ($M = 58.44$) in 100.0 g of
> water. The resulting solution has a volume of 102 mL.
> 
> $$ \begin{align*}   n(\text{NaCl}) &= \frac{5.00}{58.44} = 0.0856\,\mathrm{mol}\\   \text{molarity} &= \frac{0.0856}{0.102} = 0.839\,\mathrm{M}\\   \text{molality} &= \frac{0.0856}{0.1000} = 0.856\,\mathrm{mol/kg}\\   \text{mass \%} &= \frac{5.00}{105.0}\times100 = 4.76\%\\   n(\text{H₂O}) &= \frac{100.0}{18.02} = 5.549\,\mathrm{mol},\quad   \chi(\text{NaCl}) = \frac{0.0856}{5.635} = 0.0152 \end{align*} $$
> 
> Four correct descriptions of the same bottle. Molarity and molality are
> close here only because the solution is dilute and aqueous — do not assume
> that in general.

#### GUIDED PRACTICE • Composition drill 15 min

A solution contains 12.0 g of NaOH ($M = 40.00$) dissolved in
250.0 g of water; the solution volume is 255 mL.

1. Moles of NaOH: 0.300 mol
2. Molarity: 1.18 M
3. Molality: 1.20 mol/kg
4. Mass percent: 4.58%

#### INSTRUCTION B • Choosing the right measure 20 min

### Which one, and when `ZUM §11.1`

`SP 4`

- **Molarity** for anything involving reaction stoichiometry —
   you measure out a volume and need moles.
- **Mole fraction** for gas mixtures — it converts directly to
   partial pressure via
   $P_A = \chi_A P_{\text{total}}$.
- **Mass percent** when the solute's identity or molar mass is
   unknown, or irrelevant.
- **Molality** essentially only for colligative properties.

#### APPLICATION • Composition reasoning 20 min

1. A solution is prepared and then warmed from 20 °C to
   60 °C. State what happens to its molarity, its molality,
   and its mass percent. 
2. A student prepares a solution by adding 0.100 mol of solute
   to exactly 1.000 L of water and labels it
   0.100 M. Identify the error and state whether the true
   molarity is higher or lower. 

> 📌 **Exit ticket**
>
> Why can you not convert molarity to molality without knowing the solution's
> density?

## The Energetics of Dissolving Zumdahl §11.2

> 📌 **By the end you can…**
>
> - Break dissolving into three energy steps and predict the sign of
>    each.
> - Use $\Delta H_{\text{soln}}$ to explain why some things dissolve and
>    others do not.

**Read:** Zumdahl §11.2 • PDF pp. 555–559

> 📌 **Retrieval warm-up**
>
> 1. Molality of 0.50 mol in 500 g solvent:
>    1.0 mol/kg
> 2. Which measure is temperature-independent?
>    molality
> 3. Strongest IMF in water: hydrogen bonding

#### INSTRUCTION A • Three steps 25 min

### Zumdahl's model of solution formation `ZUM §11.2`

`SP 5`

Dissolving is treated as three imaginary steps. They are not a mechanism —
they are an energy accounting scheme, exactly like Hess's law.

| **Step** | **What happens** | **Sign of $\Delta H$** |
|---|---|---|
| 1 | Separate the solute into its components | endothermic — forces must be overcome |
| 2 | Expand the solvent to make room | endothermic — same reason |
| 3 | Let solute and solvent interact | exothermic — new attractions form |

$\Delta H_{\text{soln}} =$ $\Delta H_1 + \Delta H_2 + \Delta H_3$

The overall sign can go either way, and small differences between large
numbers decide it.

> 📌 **Note**
>
> For an ionic solute the accounting has familiar names: Step 1 is the
> lattice energy (large and endothermic to overcome), and Step 3 is the
> hydration energy (large and exothermic). Dissolving happens when
> hydration nearly pays for the lattice. NaCl is a near-tie:
> $\Delta H_{\text{soln}} = +3.9\,\mathrm{kJ/mol}$, barely
> endothermic — which is why table salt dissolves readily but the water gets
> very slightly cooler.

#### GUIDED PRACTICE • Predict the thermal effect 15 min

1. NH₄NO₃ has $\Delta H_{\text{soln}} =         +25.7\,\mathrm{kJ/mol}$. What do you feel when it
   dissolves? the container gets cold
2. CaCl₂ has $\Delta H_{\text{soln}} =         -82.8\,\mathrm{kJ/mol}$. What do you feel?
   the container gets hot
3. Which of the two would you put in an instant cold pack?
   NH₄NO₃

#### INSTRUCTION B • Why oil and water do not mix 20 min

### The energetic explanation of “like dissolves like” `ZUM §11.2`

`SP 6`

> 📘 **Worked example: Zumdahl's oil slick**
>
> Why is oil insoluble in water? Work through the three steps.
> 
> **Step 1** (expand the oil): oil molecules are held only by dispersion
> forces — but they are large molecules, so this is
> *moderately* endothermic.
> 
> **Step 2** (expand the water): this requires breaking water's
> hydrogen bonds, which is *strongly* endothermic
> — the largest term in the accounting.
> 
> **Step 3** (let them interact): a polar water molecule can induce a
> dipole in a nonpolar oil molecule, so this is exothermic — but a
> dipole–induced dipole attraction is much
> weaker than the hydrogen bonds that were sacrificed in
> Step 2.
> 
> The exothermic Step 3 cannot pay for the endothermic Step 2, so
> $\Delta H_{\text{soln}}$ is strongly positive and the two liquids stay
> separate.

> 📌 **Note**
>
> This is what “like dissolves like” actually *means*. It is not a
> rule to memorize — it is the observation that Step 3 can only repay Step 2
> when the new solute–solvent attractions are of the same kind and strength
> as the solvent–solvent attractions being broken.

#### APPLICATION • Energetic reasoning 20 min

1. Explain, using the three-step model, why NaCl dissolves in
   water but not in hexane. 
2. Ethanol is miscible with water in all proportions. Explain in terms
   of the three steps. 

> 📌 **Exit ticket**
>
> A solute dissolves even though $\Delta H_{\text{soln}}$ is positive. What
> does that tell you about the process?

## Factors Affecting Solubility Zumdahl §11.3

> 📌 **By the end you can…**
>
> - Predict solubility from molecular structure.
> - State how pressure and temperature affect solid and gas solubility.

**Read:** Zumdahl §11.3 • PDF pp. 559–563

> 📌 **Retrieval warm-up**
>
> 1. Sign of $\Delta H$ for Step 2 (expanding solvent):
>    positive
> 2. Cold pack salt: NH₄NO₃
> 3. Which dissolves I₂ better, water or CCl₄?
>    CCl₄

#### INSTRUCTION A • Structure effects 25 min

### Hydrophobic and hydrophilic `ZUM §11.3`

`SP 6`

> 📘 **Worked example: two vitamins**
>
> Zumdahl contrasts vitamins A and C.
> 
> **Vitamin A** is built almost entirely from carbon and hydrogen, whose
> electronegativities are similar — so the molecule is essentially
> nonpolar, or hydrophobic. It dissolves in body
> fat but not in water.
> 
> **Vitamin C** carries many polar O–H and C–O bonds, making it
> polar, or hydrophilic, and water-soluble.
> 
> The consequence is medical: fat-soluble vitamins (A, D, E, K)
> accumulate in fatty tissue, so excess intake can cause
> hypervitaminosis. Water-soluble vitamins are
> excreted and must be consumed regularly — which is
> why sailors developed scurvy without fresh food.

#### The chain-length effect

For alcohols, water solubility falls as the carbon
chain grows: methanol and ethanol are miscible, but 1-octanol is nearly
insoluble. The polar –OH group stays the same size while the nonpolar
hydrocarbon portion grows, so the molecule becomes progressively more
hydrophobic overall.

#### GUIDED PRACTICE • Predict solubility 15 min

More soluble in water? Give the structural reason.

1. CH₃OH or C₆H₁₄:
   CH₃OH — H-bonds with water
2. NaCl or I₂:
   NaCl — ion–dipole
3. C₂H₅OH or C₈H₁₇OH:
   C₂H₅OH — shorter nonpolar chain

#### INSTRUCTION B • Pressure and temperature 20 min

### What changes solubility `ZUM §11.3`

`SP 4`

|  | **Solids in water** | **Gases in water** |
|---|---|---|
| Pressure | essentially no effect | solubility increases with pressure |
| Temperature | *usually* increases, but
  not always | solubility decreases with temperature |

> 📘 **Worked example: why soda goes flat**
>
> A sealed bottle is pressurized with CO₂ at 5.0 atm. Using
> Zumdahl's Henry's law constant $k = 3.1e-2\,\mathrm{mol/L/atm}$:
> 
> $$ \begin{align*}   \text{sealed:}\quad C &= (3.1\times10^{-2})(5.0) = 0.16\,\mathrm{mol/L}\\   \text{opened:}\quad C &= (3.1\times10^{-2})(4.0\times10^{-4}) = 1.2e-5\,\mathrm{mol/L} \end{align*} $$
> 
> Once opened, the CO₂ equilibrates with the atmosphere, where its
> partial pressure is only $4.0\times10^{-4}$ atm. The dissolved concentration
> falls by a factor of more than ten thousand — which is precisely what
> “going flat” means.

> 📌 **Note**
>
> AP expects the *relationships* — gas solubility rises with pressure
> and falls with temperature — not the Henry's law constant calculation. The
> qualitative reasoning is what gets tested: warm soda goes flat faster, and
> warm river water holds less dissolved oxygen, which is why thermal pollution
> harms fish.

> ⚠️ **AP trap**
>
> “Solids always dissolve better when hot” is false, and Zumdahl says so
> explicitly. Most solids do, but sodium sulfate and cerium sulfate become
> *less* soluble as temperature rises. Also distinguish two different
> claims: heating always makes dissolving *faster*, but it does not
> always increase *how much* will dissolve.

#### APPLICATION • Solubility reasoning 20 min

1. Explain why a warm carbonated drink fizzes more violently when
   opened than a cold one. 
2. A power plant returns warmed water to a river. Explain the effect on
   dissolved oxygen and why it matters.
   
3. A student says “heating always dissolves more solute.” Give a
   precise correction. 

> 📌 **Exit ticket**
>
> Divers breathing compressed air at depth must ascend slowly. Connect this to
> gas solubility.

## ENRICHMENT: Colligative Properties Zumdahl §11.4–11.7 — NOT on the CED

> 📌 **This block is optional**
>
> Nothing here is assessed on the AP exam — colligative properties were
> dropped in the 2019 redesign. It is included because these effects explain
> several everyday phenomena, and because the central idea (a property that
> depends only on how many particles are present, not what they are) is
> elegant. Skip it entirely without penalty.

> 📌 **By the end you can…**
>
> - Define a colligative property.
> - Describe vapour pressure lowering, boiling-point elevation,
>    freezing-point depression, and osmotic pressure.

**Read:** Zumdahl §11.4–11.7 • PDF pp. 563–579

#### INSTRUCTION A • Counting particles, not identifying them 25 min

### What colligative means `ZUM §11.4`

`SP 1`

A colligative property depends only on the
number of solute particles in solution — not on their
chemical identity. One mole of dissolved sugar and one mole of dissolved
neon would behave identically.

| **Property** | **Effect of solute** | **Everyday example** |
|---|---|---|
| Vapour pressure | lowered | — |
| Boiling point | raised | salted cooking water |
| Freezing point | lowered | salt on icy roads;
  antifreeze |
| Osmotic pressure | develops across a membrane | cells swell in pure water |

#### Why electrolytes count double (or triple)

Because these properties count *particles*, a mole of NaCl
produces 2 moles of particles and a mole of CaCl₂
produces 3. That is why salt is far more effective per
gram at melting ice than sugar would be.

#### GUIDED PRACTICE • Particle counting 15 min

Rank by freezing-point depression, greatest first, at equal molality:
glucose, NaCl, CaCl₂.
CaCl₂ $>$ NaCl $>$ glucose (3, 2, 1 particles)

#### INSTRUCTION B • Osmosis 20 min

### Water moving through a membrane `ZUM §11.6`

`SP 6`

A semipermeable membrane lets solvent through but blocks solute.
Water moves from the more dilute side toward the
more concentrated side. The pressure needed to stop
that flow is the osmotic pressure.

> 📌 **Note**
>
> Consequences worth knowing: a red blood cell placed in pure water swells and
> bursts, because water floods in toward the higher solute concentration
> inside. Placed in concentrated brine it shrivels, as water leaves. This is
> why intravenous fluids must be *isotonic* with blood — and why
> saltwater is undrinkable.

#### APPLICATION • Explaining familiar effects 20 min

Explain why spreading salt on an icy road melts the ice.
        

Explain why a cucumber shrivels into a pickle in brine.
        

> 📌 **Exit ticket**
>
> Why is CaCl₂ preferred over NaCl for de-icing at very low
> temperatures?

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
