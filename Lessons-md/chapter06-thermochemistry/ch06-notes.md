# Guided Notes

*Chapter 6 • Thermochemistry*  
Zumdahl §6.1–6.4 • PDF pp. 282–308 • 4 blocks

[← all lessons](../index.md)

---

> 📌 **How this chapter fits the AP course**
>
> This is the **cleanest chapter-to-unit match in the book**. Sections
> 6.1–6.4 are essentially all of CED Unit 6, in the textbook's own order —
> you can read straight through without untangling anything.
> 
> Unit 6 adds only two topics from elsewhere, and you have already met both:
> **energy of phase changes** (CED 6.5, Zumdahl §10.8) came up in Unit 3
> Block 2, and **bond enthalpies** (CED 6.7, Zumdahl §8.8) in Unit 2
> Block 1. Treat those as callbacks to your own notes.
> 
> §6.5–6.6 (present and new energy sources) are skipped — off-syllabus.

## The Nature of Energy Zumdahl §6.1

> 📌 **By the end you can…**
>
> - Define system and surroundings, and apply the sign conventions for
>    heat and work.
> - Use the first law, $\Delta E = q + w$, including $w = -P\Delta V$.
> - Explain what makes a quantity a state function.

**Read:** Zumdahl §6.1 • PDF pp. 283–290

> 📌 **Retrieval warm-up**
>
> 1. Convert 25 °C to kelvin: 298 K
> 2. KMT: temperature measures what?
>    average kinetic energy
> 3. Moles in 16.04 g CH₄: 1.000 mol

#### INSTRUCTION A • Energy, heat, and work 25 min

### Defining the boundary `ZUM §6.1`

`SP 1`

Before any energy bookkeeping, you must decide what you are keeping books
*on*:

- The system is the part of the universe you are studying —
   usually the reaction itself.
- The surroundings are everything else —
   the solvent, the container, the room.

Energy crosses that boundary in exactly two ways:

|  | **Definition** | **Sign convention (system's view)** |
|---|---|---|
| Heat ($q$) | transfer driven by a
  temperature difference | $q > 0$: heat flows into the system (endothermic)  

  $q Work ($w$) | transfer by force acting through a distance | $w > 0$: work done on the system  

  $w  📌 **Note**
>
> Every sign is written from the *system's* point of view — treat the
> system as an account and ask whether energy is being deposited or withdrawn.
> Heat flowing out of a reaction is negative for the reaction even though the
> room got warmer. Students who reason from the surroundings invert every
> sign.

#### How heat transfer actually happens

Zumdahl's picture: two gas samples at different temperatures separated by a
thin membrane. Temperature measures average kinetic energy, so the
fast-moving particles on the hot side transfer energy through collisions to
the slower particles on the cold side. Energy always flows from
hot to cold, until both reach the
same intermediate temperature.

#### GUIDED PRACTICE • Assign the signs 15 min

1. A reaction warms the beaker it is in.
   exothermic, $q  0$ for the pack
3. A gas is compressed by a piston.
   $w > 0$ (work done on the gas)
4. A gas expands and pushes the piston out.
   $w internal energy — the total kinetic and
potential energy of everything in the system. The first law says energy is
neither created nor destroyed; it only moves or changes form.

#### Pressure–volume work

When a gas expands against a constant external pressure:
$w =$ $-P\Delta V$

The minus sign is not decoration. If the gas *expands*, $\Delta V$ is
positive, so $w$ is negative — the system spent
energy pushing the surroundings back. If it is compressed, $\Delta V  0$.

> 📘 **Worked example 1: combining heat and work**
>
> A gas absorbs 450 J of heat and expands, doing 120 J
> of work on its surroundings.
> 
> $$ \Delta E = q + w = (+450) + (-120) = +330\,\mathrm{J} $$
> 
> The system gained 450 J but spent 120 J pushing outward, so its internal
> energy rose by only 330 J.

> 📘 **Worked example 2: $P\Delta V$ with units**
>
> A gas expands from 2.0 L to 5.0 L against a constant
> 1.5 atm.
> 
> $$ w = -P\Delta V = -(1.5)(5.0-2.0) = -4.5\,\mathrm{L\cdot atm} $$
> 
> Converting with 1 L·atm $=$ 101.3 J:
> $w = -456\,\mathrm{J}$. Negative, as expected for expansion.

#### APPLICATION • State functions 20 min

### Path independence `ZUM §6.1`

`SP 6`

A state function depends only on the current state, not on how you
got there. Energy ($E$) and enthalpy ($H$) are state functions;
$q$ and $w$ individually are not.

> 📌 **Note**
>
> Altitude is a state function; distance walked is not. Two hikers reaching
> the same summit have identical altitude change but may have walked wildly
> different distances. Likewise, two routes from the same reactants to the
> same products give identical $\Delta E$ — even though the heat and work
> split differently along the way. Block 3 turns this fact into a calculation
> tool.

1. A system releases 200 J of heat while
   75 J of work is done on it. Find $\Delta E$.
   $-125$ J
2. Explain why $\Delta E$ for converting graphite to diamond is the
   same whether done in one step or ten.
   

> 📌 **Exit ticket**
>
> A reaction in a beaker makes the beaker feel cold. State the sign of $q$ for
> the reaction and name the process.

## Enthalpy and Calorimetry Zumdahl §6.2

> 📌 **By the end you can…**
>
> - Relate enthalpy change to heat at constant pressure.
> - Use $q = mc\Delta T$ and interpret calorimetry data.

**Read:** Zumdahl §6.2 • PDF pp. 290–297

> 📌 **Retrieval warm-up**
>
> 1. Sign of $q$ for an exothermic reaction:
>    negative
> 2. First law equation: $\Delta E = q + w$
> 3. $w$ when a gas expands: negative
> 4. Is enthalpy a state function? yes

#### INSTRUCTION A • Enthalpy 25 min

### Why chemists use $H$ instead of $E$ `ZUM §6.2`

`SP 5`

Enthalpy is defined as $H = E + PV$. Its value comes from one consequence:
at *constant pressure* — which is how nearly every reaction in an
open beaker runs —
$\Delta H =$ $q_P$

So the heat you measure in an open container *is* the enthalpy change.
That is the whole reason enthalpy exists as a bookkeeping quantity.

|  | **$\Delta H$ sign** | **Surroundings** |
|---|---|---|
| Exothermic | negative | get warmer |
| Endothermic | positive | get cooler |

#### $\Delta H$ scales with amount

A thermochemical equation's $\Delta H$ belongs to the coefficients as
written:

$$ \text{CH₄(g) + 2 O₂(g) → CO₂(g) + 2 H₂O(l)} \qquad \Delta H = -890\,\mathrm{kJ} $$

> 📘 **Worked example 1: scaling**
>
> How much heat is released when 5.8 g of CH₄ burns at constant
> pressure?
> 
> $$ \begin{align*}   n &= \frac{5.8}{16.04} = 0.36\,\mathrm{mol}\\   \Delta H &= 0.36 \times (-890) = -320\,\mathrm{kJ} \end{align*} $$
> 
> *Reality check:* less than one mole burned, so less than 890 kJ should
> be released. It is.

#### GUIDED PRACTICE • Enthalpy scaling 15 min

Using $\Delta H = -890\,\mathrm{kJ}$ per mole of CH₄:

1. Heat from 2.00 mol CH₄:
   -1780 kJ
2. Heat from 32.08 g CH₄:
   -1780 kJ
3. $\Delta H$ for the *reverse* reaction:
   +890 kJ

#### INSTRUCTION B • Calorimetry 20 min

### Measuring heat by measuring temperature `ZUM §6.2`

`SP 4`

A calorimeter determines heat by watching a temperature change. The
central equation:
$q =$ $mc\Delta T$ $\qquad \Delta T = T_{\text{final}} - T_{\text{initial}}$

The specific heat capacity $c$ is the energy needed to raise
1 g by 1 °C. For water,
$c =$ 4.184 J/g/°C — unusually
large, which is why water moderates temperature so effectively.

> ⚠️ **AP trap**
>
> The heat absorbed by the *solution* and the heat released by the
> *reaction* are equal in magnitude and opposite in sign:
> $q_{\text{rxn}} = -q_{\text{solution}}$. Students routinely report an
> exothermic reaction with a positive $\Delta H$ because they forgot to flip
> the sign after computing $mc\Delta T$ for the water.

> 📘 **Worked example 2: neutralization in a coffee cup**
>
> 50.0 mL of 1.00 M HCl and
> 50.0 mL of 1.00 M NaOH, both at
> 25.0 °C, are mixed. The temperature rises to
> 31.9 °C. Assume the solution has the density and specific heat
> of water.
> 
> $$ \begin{align*}   m &= 100.0\,\mathrm{g}, \qquad \Delta T = 6.9\,\mathrm{{}^\circ C}\\   q_{\text{soln}} &= (100.0)(4.184)(6.9) = 2887\,\mathrm{J} = 2.89\,\mathrm{kJ}\\   q_{\text{rxn}} &= -2.89\,\mathrm{kJ}\\   n &= (0.0500)(1.00) = 0.0500\,\mathrm{mol}\\   \Delta H &= \frac{-2.89}{0.0500} = -57.8\,\mathrm{kJ/mol} \end{align*} $$
> 
> The accepted value is about -57.3 kJ/mol — close, with
> the difference explained by heat lost to the cup and thermometer.

#### APPLICATION • Determining a specific heat 20 min

A 55.0 g piece of metal is heated to 99.0 °C and
dropped into 100.0 g of water at 21.0 °C. The final
temperature is 24.8 °C.

1. Heat gained by the water: 
   *(working space)*
2. Specific heat of the metal: 
   *(working space)*
3. Suggest the metal's identity.
   copper ($c \approx 0.385$)
4. Why does the water's temperature rise far less than the metal's
   falls? 

> 📌 **Exit ticket**
>
> A student computes $q_{\text{solution}} = +3.2\,\mathrm{kJ}$ for a
> reaction and reports $\Delta H = +3.2\,\mathrm{kJ}$. What did they get
> wrong?

## Hess's Law Zumdahl §6.3

> 📌 **By the end you can…**
>
> - State Hess's law and explain why it follows from $H$ being a state
>    function.
> - Combine thermochemical equations to obtain an unknown $\Delta H$.

**Read:** Zumdahl §6.3 • PDF pp. 297–301

> 📌 **Retrieval warm-up**
>
> 1. $\Delta H$ equals $q$ under what condition?
>    constant pressure
> 2. $q$ for 25.0 g water warmed 10.0 °C:
>    1046 J
> 3. Sign of $\Delta H$ for an endothermic process:
>    positive

#### INSTRUCTION A • The law and why it must be true 25 min

### Hess's law `ZUM §6.3`

`SP 5`

> 📌 **Note**
>
> **Hess's law:** if a reaction is carried out in a series of steps,
> $\Delta H$ for the overall reaction equals the sum of the
> $\Delta H$ values for the individual steps.
> 
> This is not a separate discovery — it is a direct consequence of enthalpy
> being a state function. If $\Delta H$ depended on the
> route, you could build a machine that created energy by going one way and
> returning another.

> 📘 **Worked example 1: Zumdahl's nitrogen oxides**
>
> The direct reaction:
> 
> $$ \text{N₂(g) + 2 O₂(g) → 2 NO₂(g)} \qquad \Delta H_1 = 68\,\mathrm{kJ} $$
> 
> The same change in two steps:
> 
> $$ \begin{align*}   \text{N₂(g) + O₂(g) & → 2 NO(g)}   &\Delta H_2 &= 180\,\mathrm{kJ}\\   \text{2 NO(g) + O₂(g) & → 2 NO₂(g)} &\Delta H_3 &= -112\,\mathrm{kJ} \end{align*} $$
> 
> Adding the steps cancels the 2 NO and reproduces the overall equation,
> and indeed $180 + (-112) = 68\,\mathrm{kJ} = \Delta H_1$.

#### The two manipulation rules

1. Reverse a reaction $\Rightarrow$ reverse the sign
   of $\Delta H$.
2. Multiply the coefficients by a factor $\Rightarrow$
   multiply $\Delta H$ by the same factor.

Rule 1 follows because $\Delta H$'s sign records the direction of heat flow;
run the change backwards and the flow reverses. Rule 2 follows because
enthalpy is extensive — twice the reaction releases twice the heat.

#### GUIDED PRACTICE • Manipulate 15 min

Given 2 H₂(g) + O₂(g) → 2 H₂O(l), $\Delta H = -572\,\mathrm{kJ}$:

1. $\Delta H$ for H₂(g) + 1/2 O₂(g) → H₂O(l):
   -286 kJ
2. $\Delta H$ for 2 H₂O(l) → 2 H₂(g) + O₂(g):
   +572 kJ
3. $\Delta H$ for 4 H₂(g) + 2 O₂(g) → 4 H₂O(l):
   -1144 kJ

#### INSTRUCTION B • The working method 20 min

### A reliable procedure `ZUM §6.3`

`SP 5`

Write the target equation first.

Find a substance that appears in only *one* given equation and
        place it correctly — reverse or scale that equation as needed.

Repeat for the next such substance.

Add everything; confirm the intermediates
        cancel.

Sum the adjusted $\Delta H$ values.

> 📘 **Worked example 2: a two-step target**
>
> Target: C(s) + 1/2 O₂(g) → CO(g), given
> 
> $$ \begin{align*}   \text{(i)}\ \text{C(s) + O₂(g) & → CO₂(g)} &\Delta H &= -393.5\,\mathrm{kJ}\\   \text{(ii)}\ \text{2 CO(g) + O₂(g) & → 2 CO₂(g)} &\Delta H &= -566.0\,\mathrm{kJ} \end{align*} $$
> 
> CO appears only in (ii), but on the wrong side and with the wrong
> coefficient. Reverse (ii) and halve it:
> 
> $$ \text{CO₂(g) → CO(g) + 1/2 O₂(g)} \qquad \Delta H = +283.0\,\mathrm{kJ} $$
> 
> Add to (i): the CO₂ cancels, giving the target with
> 
> $$ \Delta H = -393.5 + 283.0 = -110.5\,\mathrm{kJ} $$

#### APPLICATION • Build it yourself 20 min

Determine $\Delta H$ for 2 C(s) + H₂(g) → C₂H₂(g) given:

$$ \begin{align*}   \text{(i)}\ \text{C₂H₂(g) + 5/2 O₂(g) & → 2 CO₂(g) + H₂O(l)} &\Delta H &= -1300.\,\mathrm{kJ}\\   \text{(ii)}\ \text{C(s) + O₂(g) & → CO₂(g)} &\Delta H &= -393.5\,\mathrm{kJ}\\   \text{(iii)}\ \text{H₂(g) + 1/2 O₂(g) & → H₂O(l)} &\Delta H &= -286\,\mathrm{kJ} \end{align*} $$

*(working space)*

> 📌 **Exit ticket**
>
> Why does reversing a reaction reverse the sign of $\Delta H$?

## Standard Enthalpies of Formation Zumdahl §6.4

> 📌 **By the end you can…**
>
> - Define $\Delta H^\circ_f$ and standard state.
> - Compute $\Delta H^\circ_{\text{rxn}}$ from tabulated formation
>    enthalpies.

**Read:** Zumdahl §6.4 • PDF pp. 301–308

> 📌 **Retrieval warm-up**
>
> 1. Hess's law depends on $H$ being a what?
>    state function
> 2. Reverse a reaction: $\Delta H$ does what?
>    changes sign
> 3. Halve the coefficients: $\Delta H$ does what?
>    halves
> 4. $q$ for 50.0 g water cooled 4.00 °C:
>    -837 J

#### INSTRUCTION A • A universal reference point 25 min

### Standard enthalpy of formation `ZUM §6.4`

`SP 5`

The standard enthalpy of formation $\Delta H^\circ_f$ is the enthalpy
change when 1 mole of a compound forms from its
elements, with everything in its
standard state.

Standard state means the substance's most stable form at
1 atm and (conventionally) 25 °C — so
O₂(g), Br₂(l), C(graphite).

> 📌 **Note**
>
> It follows directly from the definition that
> $\Delta H^\circ_f$ of an *element in its standard state* is
> 0 — forming an element from itself is no change at
> all. That is why O₂(g) contributes nothing to a calculation while
> O₃(g) (not the standard form) contributes $+143$ kJ/mol.

#### Why the tables exist

Some enthalpy changes cannot be measured directly. Zumdahl's example:
converting graphite to diamond is far too slow for a calorimeter. But if
every compound's formation enthalpy is tabulated once, any reaction's
$\Delta H$ can be assembled from them — Hess's law industrialized.

#### GUIDED PRACTICE • Writing formation equations 15 min

Write the formation equation (1 mol of product, elements in standard states):

NH₃(g):
        1/2 N₂(g) + 3/2 H₂(g) → NH₃(g)

CO₂(g):
        C(graphite) + O₂(g) → CO₂(g)

$\Delta H^\circ_f$ of N₂(g): 0

#### INSTRUCTION B • The master equation 20 min

### Computing $\Delta H^\circ_{\text{rxn}}$ `ZUM §6.4`

`SP 5`

$\Delta H^\circ_{\text{rxn}} =$ $\sum n\,\Delta H^\circ_f(\text{products}) - \sum n\,\Delta H^\circ_f(\text{reactants})$

Note the two easy losses: multiply each value by its
coefficient, and subtract in the right order —
products minus reactants.

> 📘 **Worked example 1: methane combustion**
>
> CH₄(g) + 2 O₂(g) → CO₂(g) + 2 H₂O(l)
> Using $\Delta H^\circ_f$: CH₄ $-74.8$, O₂ $0$, CO₂ $-393.5$,
> H₂O(l) $-285.8$ kJ/mol.
> 
> $$ \begin{align*}   \Delta H^\circ &= [(-393.5) + 2(-285.8)] - [(-74.8) + 2(0)]\\   &= (-965.1) - (-74.8) = -890.3\,\mathrm{kJ} \end{align*} $$
> 
> This matches the experimental $-890$ kJ used in Block 2 — a good check
> that the method and the table agree.

> ⚠️ **AP trap**
>
> Watch the physical state. $\Delta H^\circ_f$ for H₂O(l) is $-285.8$ but
> for H₂O(g) it is $-241.8$ — a 44 kJ/mol difference, exactly the heat
> of vaporization. Using the wrong state is worth 88 kJ of error in the
> example above.

#### APPLICATION • Full calculations 20 min

Compute $\Delta H^\circ$ for
        2 NH₃(g) → N₂(g) + 3 H₂(g), given
        $\Delta H^\circ_f(\text{NH₃}) = -46.1\,\mathrm{kJ/mol}$.
        

*(working space)*

        

Compute $\Delta H^\circ$ for the thermite reaction
        2 Al(s) + Fe₂O₃(s) → Al₂O₃(s) + 2 Fe(s), given
        $\Delta H^\circ_f$: Fe₂O₃ $-826$, Al₂O₃ $-1676$
        kJ/mol. 

*(working space)*

        

In problem 2, why do Al(s) and Fe(s) contribute nothing?
        

> 📌 **Exit ticket**
>
> A reaction has $\Delta H^\circ = -1250\,\mathrm{kJ}$. State whether it
> is exothermic or endothermic, and what happens to the temperature of the
> surroundings.

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
