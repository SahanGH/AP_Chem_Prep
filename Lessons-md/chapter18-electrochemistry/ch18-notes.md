# Guided Notes

*Chapter 18 • Electrochemistry*  
Zumdahl §18.1–18.4, 18.7–18.8 • PDF pp. 881–930 • 5 blocks

[← all lessons](../index.md)

---

> 📌 **How this chapter fits the AP course**
>
> **This is the last chapter of the course, and it completes the CED.**
> §18.1 $\to$ CED 9.8, §18.2–18.3 $\to$ 9.9, §18.4 $\to$ 9.10,
> §18.7–18.8 $\to$ 9.11. With Chapter 17 it finishes Unit 9, and with it the
> entire framework.
> 
> **Skip:** §18.5 (batteries) and §18.6 (corrosion) are applications,
> not framework topics — interesting, and referenced in passing, but not
> examined.
> 
> Electrochemistry is where three earlier units meet. Redox bookkeeping comes
> from **Unit 4**, the $Q$-versus-$K$ argument from **Unit 7**, and
> $\Delta G^\circ$ from **Chapter 17**. The single new idea is that a
> favored redox reaction can be made to push electrons through a wire, and
> that the push is measurable as a voltage.

> ⚠️ **AP trap**
>
> **Two CED boundaries that change what you should study.**
> 
> **1. Do not label electrodes “positive” or “negative.”** Topic 9.8
> carries an explicit exclusion: *labeling an electrode as positive or
> negative will not be assessed on the AP Exam.* The sign convention differs
> between galvanic and electrolytic cells and is a reliable source of
> confusion, so the exam simply avoids it. Learn **anode** and
> **cathode** instead — those never change meaning.
> 
> **2. The Nernst equation is not required.** Topic 9.10 asks you to
> *reason* about how a cell potential changes when conditions move away
> from standard — using $Q$ against $K$ — and it lists no equation.
> Zumdahl §18.4 works through the full Nernst calculation; that is beyond the
> framework. Block 4 teaches the reasoning the CED actually asks for, and
> flags the algebra as enrichment.

## Galvanic Cells: How They Work Zumdahl §18.1

> 📌 **By the end you can…**
>
> - Identify each component of an electrochemical cell and its role.
> - Determine the direction of electron and ion flow.

**Read:** Zumdahl §18.1 • PDF pp. 882–886

> 📌 **Retrieval warm-up**
>
> 1. Oxidation is the loss of electrons.
> 2. Reduction is the gain of electrons.
> 3. Oxidation number of Zn in Zn(s):
>    0
> 4. A reaction with $\Delta G^\circ     thermodynamically favored

#### INSTRUCTION A • Separating the half-reactions 25 min

### Why a wire is involved at all `ZUM §18.1`

`SP 2`

Drop zinc metal into copper(II) sulfate and the reaction
Zn(s) + Cu²⁺(aq) → Zn²⁺(aq) + Cu(s)
happens immediately, releasing energy as heat. The
electrons pass directly from zinc atoms to copper ions at the point of
contact, and nothing useful is captured.

A galvanic cell (also called a voltaic cell) does the same chemistry
with the two halves **physically separated**, so the electrons are
forced to travel through an external wire to get from one to the other.
That flow is an electric current, and it can do work.

### The parts, and what each one does `ZUM §18.1`

| **Component** | **Role** |
|---|---|
| Anode | where **oxidation** happens; electrons are released here |
| Cathode | where **reduction** happens; electrons are consumed here |
| Salt bridge | lets ions migrate to keep each half-cell electrically
  neutral; without it the cell stops almost immediately |
| External wire | carries electrons from anode to cathode |
| Voltmeter | measures the potential difference driving that flow |

> 
**An Ox** — **An**ode, **Ox**idation   

**Red Cat** — **Red**uction, **Cat**hode   

True in *every* cell, galvanic and electrolytic alike.

Electrons always flow from anode to
cathode through the wire — alphabetical order, which
is worth noticing because it never changes.

> 📌 **What the salt bridge is actually for**
>
> As the cell runs, the anode compartment accumulates positive ions
> (Zn²⁺ entering solution) and the cathode compartment loses them
> (Cu²⁺ plating out). Charge would build up on both sides within
> moments and the electron flow would stop.
> 
> The salt bridge prevents that by letting spectator ions migrate: anions move
> *toward the anode* and cations *toward the cathode*, cancelling
> the charge imbalance. It completes the circuit without letting the two
> solutions mix.

#### GUIDED PRACTICE • Reading a cell 15 min

For Zn(s) + Cu²⁺(aq) → Zn²⁺(aq) + Cu(s) run as a galvanic cell:

1. Oxidation half-reaction:
   Zn → Zn²⁺ + 2e⁻
2. Reduction half-reaction:
   Cu²⁺ + 2e⁻ → Cu
3. The anode is made of: zinc
4. The cathode is made of: copper
5. Electrons flow from the zinc to the copper
6. The zinc electrode's mass decreases; the
   copper electrode's mass increases
7. Anions in the salt bridge move toward:
   the anode (zinc)

#### INSTRUCTION B • Galvanic against electrolytic 20 min

### The same hardware, run backwards `ZUM §18.7`

`SP 2`

|  | **Galvanic (voltaic)** | **Electrolytic** |
|---|---|---|
| Reaction | thermodynamically **favored** | thermodynamically
  **unfavored** |
| $E^\circ_{\text{cell}}$ | positive | negative |
| $\Delta G^\circ$ | negative | positive |
| Energy | *produces* electrical energy | *consumes* it from an
  external source |
| Anode | oxidation | oxidation |
| Cathode | reduction | reduction |

The bottom two rows are the point of the table: **anode and cathode
mean the same thing in both**. What reverses is which direction the reaction
is being pushed, and whether energy comes out or must be put in.

> ⚠️ **AP trap**
>
> This is exactly Chapter 17's “driving an unfavorable process with an
> external energy source,” in hardware. An electrolytic cell is CED topic
> 9.7 made physical — and it is why electrolysis was one of the CED's two
> named examples of external energy.

#### APPLICATION • Describing cells 20 min

1. A student builds a cell and finds the silver electrode gains mass
   while the copper electrode dissolves. Identify the anode, the
   cathode, and the direction of electron flow.
   
2. Why does a galvanic cell stop working if the salt bridge is
   removed? 
3. A cell has $E^\circ_{\text{cell}} = -0.46$ V. Is it galvanic or
   electrolytic, and what must be supplied?
   

> 📌 **Exit ticket**
>
> State the one rule about anodes and cathodes that is true in every
> electrochemical cell, and one thing the exam will *not* ask you to
> label.

## Standard Reduction Potentials Zumdahl §18.2

> 📌 **By the end you can…**
>
> - Calculate $E^\circ_{\text{cell}}$ from standard reduction
>    potentials.
> - Predict which species is oxidized and which is reduced.

**Read:** Zumdahl §18.2 • PDF pp. 886–892

> 📌 **Retrieval warm-up**
>
> 1. Oxidation occurs at the: anode
> 2. Electrons flow from anode to:
>    cathode
> 3. A favored reaction has $E^\circ_{\text{cell}}$:
>    positive

#### INSTRUCTION A • A scale built on an arbitrary zero 25 min

### The standard hydrogen electrode `ZUM §18.2`

`SP 5`

Only a *difference* in potential can be measured — there is no way to
measure one half-cell alone. So one half-reaction is assigned a value by
convention:

$$ \text{2H+(aq) + 2e⁻ → H₂(g)} \qquad E^\circ \equiv    \mathbf{0.00}~\text{V} $$

Every other half-reaction is then measured against this
standard hydrogen electrode. Zumdahl's zinc cell reads 0.76 V against
it, so Zn²⁺ + 2e⁻ → Zn is assigned $E^\circ = -0.76$ V.

**Standard conditions** means all solutes at 1 M, all gases
at 1 atm, and 25 °C.

> ⚠️ **AP trap**
>
> **Every table is written as reductions.** That is a universal
> convention, and it means the table does not tell you which way a reaction
> runs — you decide that.
> 
> Reversing a half-reaction **flips the sign** of $E^\circ$. But
> multiplying a half-reaction by a coefficient does **not** change
> $E^\circ$ at all. Potential is an intensive property — volts per charge,
> not volts per mole. Scaling a half-reaction to balance electrons is
> required, and scaling its voltage is wrong.

### Computing the cell potential `ZUM §18.2`

$$ \boxed{\;E^\circ_{\text{cell}} = E^\circ_{\text{cathode}}    - E^\circ_{\text{anode}}\;} $$

where both values are taken *straight from the table as reductions* —
no sign flipping needed if you use this form.

For a **galvanic** cell you want $E^\circ_{\text{cell}} > 0$, so the
species with the more positive $E^\circ$ is reduced (it
is the cathode) and the other is oxidized.

> 📘 **Worked example 1: the Daniell cell**
>
> Combine Zn²⁺/Zn ($-0.76$ V) and Cu²⁺/Cu ($+0.34$ V).
> 
> Copper has the more positive reduction potential, so **copper is
> reduced** (cathode) and **zinc is oxidized** (anode):
> 
> $$ \begin{align*}   \text{cathode:} &\quad \text{Cu²⁺ + 2e⁻ → Cu} \\   \text{anode:}   &\quad \text{Zn → Zn²⁺ + 2e⁻} \\   \text{overall:} &\quad \text{Zn + Cu²⁺ → Zn²⁺ + Cu} \end{align*} $$
> 
> $$ E^\circ_{\text{cell}} = 0.34 - (-0.76) = \mathbf{+1.10}~\text{V} $$
> 
> Positive, so the cell is galvanic — and 1.10 V is exactly what a
> voltmeter reads on this cell.

> 📘 **Worked example 2: when the electrons do not balance**
>
> Combine Ag+/Ag ($+0.80$ V) and Cu²⁺/Cu ($+0.34$ V).
> 
> Silver is more positive, so silver is reduced and copper oxidized. Balancing
> electrons requires *two* silver half-reactions:
> 
> $$ \begin{align*}   \text{cathode:} &\quad \text{2Ag+ + 2e⁻ → 2Ag} \\   \text{anode:}   &\quad \text{Cu → Cu²⁺ + 2e⁻} \\   \text{overall:} &\quad \text{Cu + 2Ag+ → Cu²⁺ + 2Ag} \end{align*} $$
> 
> $$ E^\circ_{\text{cell}} = 0.80 - 0.34 = \mathbf{+0.46}~\text{V} $$
> 
> **Note what did not happen:** the silver half-reaction was doubled, but
> its $E^\circ$ was *not*. Writing $2(0.80) - 0.34 = 1.26$ V is the
> classic error in this chapter.

#### GUIDED PRACTICE • Building cells from the table 15 min

$E^\circ$ (V): Ag+/Ag $+0.80$ • Cu²⁺/Cu $+0.34$
• Pb²⁺/Pb $-0.13$ • Ni²⁺/Ni $-0.23$
• Fe²⁺/Fe $-0.44$ • Zn²⁺/Zn $-0.76$
• Mg²⁺/Mg $-2.37$

1. Zn and Ag+: $E^\circ_{\text{cell}} =$
   $+1.56$ V
2. Mg and Cu²⁺: $E^\circ_{\text{cell}} =$
   $+2.71$ V
3. Zn and Ni²⁺: $E^\circ_{\text{cell}} =$
   $+0.53$ V
4. Fe and Cu²⁺: $E^\circ_{\text{cell}} =$
   $+0.78$ V
5. Pb and Ag+: $E^\circ_{\text{cell}} =$
   $+0.93$ V

#### APPLICATION • Reading the table as a ranking 20 min

1. Which is the stronger oxidizing agent, Ag+ or Zn²⁺?
   Justify. 
2. Which is the stronger reducing agent, Mg or Cu?
   
3. Will Cu(s) react with 1 M HCl? Support your
   answer with a cell potential.
   *(working space)*

> 📌 **Exit ticket**
>
> A student doubles a half-reaction to balance electrons and doubles its
> $E^\circ$ as well. Explain why the second step is wrong.

## Cell Potential, Free Energy, and $K$ Zumdahl §18.3

> 📌 **By the end you can…**
>
> - Relate $E^\circ_{\text{cell}}$ to $\Delta G^\circ$ and to $K$.
> - Explain why $n$ matters for free energy but not for voltage.

**Read:** Zumdahl §18.3 • PDF pp. 892–895

> 📌 **Retrieval warm-up**
>
> 1. $E^\circ_{\text{cell}} =$
>    $E^\circ_{\text{cathode}} -         E^\circ_{\text{anode}}$
> 2. Reversing a half-reaction does what to $E^\circ$?
>    flips its sign
> 3. Doubling a half-reaction does what to $E^\circ$?
>    nothing

#### INSTRUCTION A • Connecting volts to kilojoules 25 min

### $\Delta G^\circ = -nFE^\circ$ `ZUM §18.3`

`SP 5`

Electrical work is charge moved through a potential difference. For $n$
moles of electrons carrying Faraday's constant
$F = 96485\,\mathrm{C/mol}$ of charge each,

$$ \boxed{\;\Delta G^\circ = -nFE^\circ_{\text{cell}}\;} $$

Read off the consequences:

- $E^\circ > 0 \Rightarrow \Delta G^\circ$
   negative $\Rightarrow$ favored, galvanic.
- $E^\circ  ⚠️ **AP trap**
>
> **Here is where $n$ finally matters.** Voltage does not depend on how
> many electrons are transferred, but free energy does — because
> $\Delta G^\circ$ is an amount of energy, and more electrons moving through
> the same potential means more energy.
> 
> So two cells can have the same $E^\circ$ and very different
> $\Delta G^\circ$. Getting $n$ wrong is the most common way to lose a point
> on this calculation, and $n$ comes from the *balanced overall
> equation*, not from either half-reaction alone.

> 📘 **Worked example 3: the Daniell cell in kilojoules**
>
> $E^\circ = +1.10$ V and $n = 2$ (two electrons per zinc atom):
> 
> $$ \Delta G^\circ = -(2)(96485)(1.10) = -212{,}267~\text{J}    = \mathbf{-212}~\text{kJ} $$
> 
> Strongly favored, as the positive voltage already told us. Note the answer
> comes out in **joules** — $F$ is in coulombs per mole and volts are
> joules per coulomb — so it must be converted to kJ.

#### INSTRUCTION B • And on to the equilibrium constant 20 min

### Three descriptions of one thing `ZUM §18.3`

`SP 5`

Combining $\Delta G^\circ = -nFE^\circ$ with Chapter 17's
$\Delta G^\circ = -RT\ln K$:

$$ nFE^\circ = RT\ln K \qquad\Longrightarrow\qquad    \ln K = \frac{nFE^\circ}{RT} $$

You now have *three* equivalent ways to say “products are favored”:

| $E^\circ_{\text{cell}}$ | $\Delta G^\circ$ | $K$ |  |
|---|---|---|---|
| $> 0$ | $ 1$ | favored; galvanic |
| $= 0$ | $= 0$ | $= 1$ | at equilibrium; a dead battery |
| $ 0$ | $ 📘 **Worked example 4: how far does the Daniell cell go?**
>
> With $E^\circ = 1.10$ V and $n = 2$:
> 
> $$ \ln K = \frac{(2)(96485)(1.10)}{(8.314)(298)} = 85.7    \qquad K = e^{85.7} \approx \mathbf{2\times10^{37}} $$
> 
> Effectively complete. A modest-looking 1.10 V corresponds to an equilibrium
> constant of $10^{37}$ — because $E^\circ$ is multiplied by $nF$, a very
> large number, before it enters an exponential.

#### APPLICATION • Moving between the three 20 min

1. For Cu + 2Ag+ → Cu²⁺ + 2Ag, $E^\circ = +0.46$ V.
   Calculate $\Delta G^\circ$.
   *(working space)*
2. A cell has $E^\circ = -1.10$ V with $n = 2$. Find
   $\Delta G^\circ$ and state what it means practically.
   *(working space)*
3. Two cells both have $E^\circ = +0.50$ V, but one transfers 1
   electron and the other 4. Compare their voltages and their
   $\Delta G^\circ$ values. 

> 📌 **Exit ticket**
>
> A battery is described as “dead.” Give the value of $E_{\text{cell}}$, of
> $\Delta G$, and the relationship between $Q$ and $K$ at that moment.

## Nonstandard Conditions Zumdahl §18.4

> 📌 **By the end you can…**
>
> - Predict how a change in concentration changes the cell potential.
> - Explain how a concentration cell produces a voltage.

**Read:** Zumdahl §18.4 • PDF pp. 895–901

> 📌 **Retrieval warm-up**
>
> 1. $\Delta G^\circ =$ $-nFE^\circ$
> 2. $Q = K$ means the system is at:
>    equilibrium
> 3. Faraday's constant: 96,485 C/mol

> 📌 **What the CED asks for here**
>
> Topic 9.10 lists **no equation**. It asks you to *reason* about
> how the cell potential responds when conditions leave standard state, using
> the distance from equilibrium. The Nernst equation in Zumdahl §18.4 is
> **enrichment** — useful, but not required, and not on this chapter's
> test.

#### INSTRUCTION A • Voltage as distance from equilibrium 25 min

### The one idea in this block `ZUM §18.4`

`SP 6`

> 
The cell potential is a **driving force toward equilibrium**.   

The further the cell is from equilibrium, the **larger** $|E|$.   

At equilibrium, $Q = K$ and $E = \mathbf{0}$.

Standard conditions correspond to $Q =$ 1, which is
where $E = E^\circ$. So to decide whether a change raises or lowers the
voltage, ask one question: **does the change move $Q$ further from
$K$, or closer to it?**

| Change takes the cell *further* from equilibrium | $\|E\|$
  **increases** |
|---|---|
| Change takes the cell *closer* to equilibrium | $\|E\|$
  **decreases** |

For a favored cell, $K$ is large, so $Q$ starts below it. Then:
*increasing reactant* concentration lowers $Q$, moving it
further from $K$, so the voltage
rises. *Increasing product* concentration raises
$Q$, moving it closer to $K$, so the voltage
falls.

> ⚠️ **AP trap**
>
> **Do not invoke Le Ch\^atelier here.** The CED says so outright:
> equilibrium arguments such as Le Ch\^atelier's principle *do not apply
> to electrochemical systems, because the systems are not at equilibrium*.
> 
> A running cell is deliberately held away from equilibrium — that is where
> its voltage comes from. Reason with $Q$ against $K$ and with distance from
> equilibrium, not with “the equilibrium shifts.”

> 📘 **Worked example 5: which way does the voltage move?**
>
> For the Daniell cell,
> Zn(s) + Cu²⁺(aq) → Zn²⁺(aq) + Cu(s), so
> $Q = [\text{Zn²⁺}]/[\text{Cu²⁺}]$.
> 
> **Raise $[\text{Cu²⁺}]$.** $Q$ gets *smaller*, so the cell is
> further from equilibrium and $E$ **increases** above 1.10 V.
> 
> **Raise $[\text{Zn²⁺}]$.** $Q$ gets *larger*, closer to $K$, so
> $E$ **decreases**.
> 
> **Add more zinc metal.** No change at all — Zn(s) is a pure
> solid and does not appear in $Q$.

#### INSTRUCTION B • Concentration cells 20 min

### A voltage from nothing but a difference `ZUM §18.4`

`SP 6`

A concentration cell has the *same* half-reaction on both sides,
differing only in concentration. Since both electrodes are identical,

$$ E^\circ_{\text{cell}} = 0.34 - 0.34 = \mathbf{0}~\text{V} $$

and yet the cell produces a measurable voltage. The reason is that it is not
at equilibrium: equilibrium here means **equal concentrations**.

> 📘 **Worked example 6: reasoning out the direction**
>
> $$ \text{Cu} \mid \text{Cu²⁺}~(0.010\,\mathrm{M}) \parallel    \text{Cu²⁺}~(1.0\,\mathrm{M}) \mid \text{Cu} $$
> 
> Ask what has to happen for the two sides to become equal:
> 
> - The **dilute** side must become more concentrated, so
>    Cu²⁺ must be *produced* there:
>    Cu → Cu²⁺ + 2e⁻. That is oxidation, so the dilute side is
>    the **anode**.
> - The **concentrated** side must become more dilute, so
>    Cu²⁺ must be *consumed*:
>    Cu²⁺ + 2e⁻ → Cu. Reduction — the **cathode**.
> 
> Electrons therefore flow from the dilute half-cell to the concentrated one.
> The voltage is small but positive, and it falls to **zero** once the
> two concentrations match.

#### APPLICATION • Predicting the response 20 min

1. For Zn + Cu²⁺ → Zn²⁺ + Cu, state and justify the effect
   on $E$ of (i) diluting the Cu²⁺ solution, (ii) adding
   Na₂S to the cathode compartment to precipitate CuS.
   
2. A concentration cell is built from Ag electrodes in
   0.10 M and 2.0 M AgNO₃. Identify the
   anode and predict what happens to $E$ over time.
   
3. Explain why a student who answers “by Le Ch\^atelier's principle,
   the equilibrium shifts right” would not receive credit here.
   

> 📌 **Exit ticket**
>
> A cell's voltage has fallen to zero. State what is true of $Q$, of $K$, and
> of $\Delta G$, and whether any reactant remains.

## Electrolysis and Faraday's Law Zumdahl §18.7–18.8

> 📌 **By the end you can…**
>
> - Relate current, time, charge and moles of electrons.
> - Calculate the mass deposited or dissolved at an electrode.

**Read:** Zumdahl §18.7–18.8 • PDF pp. 913–925

> 📌 **Retrieval warm-up**
>
> 1. Electrolytic cells have $E^\circ$:
>    negative
> 2. Faraday's constant: 96,485 C/mol e$^-$
> 3. Reduction still occurs at the:
>    cathode

#### INSTRUCTION A • Counting electrons with an ammeter 25 min

### The bridge from electricity to moles `ZUM §18.8`

`SP 5`

Electrolysis is stoichiometry in which one of the reagents is
the electron. The whole calculation rests on being able
to count electrons, and current is how you do it:

$$ \boxed{\;I = \frac{q}{t}\;} \qquad\text{so}\qquad    q = It $$

with $q$ in coulombs, $I$ in amperes and $t$ in
seconds. Then Faraday's constant converts charge to
moles of electrons:

$$ \text{mol e}^- = \frac{q}{96485} $$

The full chain, worth memorizing as a sequence:

> 
current & time $\to$ charge ($q = It$) $\to$ moles of electrons
($\div F$)   

$\to$ moles of substance ($\div n$ from the half-reaction) $\to$ grams
($\times$ molar mass)

> ⚠️ **AP trap**
>
> **The half-reaction supplies the electron ratio, and it is not always
> 2.** Depositing one mole of metal takes one mole of electrons for
> Ag+, two for Cu²⁺, three for Al³⁺. Reading that number off
> the charge of the ion is the step students skip.
> 
> Also: **time must be in seconds**. A problem stated in minutes or hours
> is stated that way on purpose.

> 📘 **Worked example 7: silver plating**
>
> A current of 2.00 A runs for 30.0 min through a
> solution of AgNO₃. What mass of silver plates out?
> 
> **Charge:** $t = 30.0 \times 60 = 1800\,\mathrm{s}$, so
> $q = (2.00)(1800) = 3600\,\mathrm{C}$.
> 
> **Moles of electrons:**
> $3600 / 96485 = 0.0373\,\mathrm{mol}$.
> 
> **Moles of silver:** the half-reaction is
> Ag+ + e⁻ → Ag, one electron per atom, so
> $0.0373\,\mathrm{mol}$ of Ag.
> 
> **Mass:** $(0.0373)(107.87) = \mathbf{4.03}~\text{g}$

> 📘 **Worked example 8: the same current, a different ion**
>
> Now 1.50 A for 1.00 h through CuSO₄.
> 
> $q = (1.50)(3600) = 5400\,\mathrm{C}$;
> $\text{mol e}^- = 5400/96485 = 0.0560$.
> 
> But Cu²⁺ + 2e⁻ → Cu needs *two* electrons per atom:
> 
> $$ \text{mol Cu} = \frac{0.0560}{2} = 0.0280    \qquad m = (0.0280)(63.55) = \mathbf{1.78}~\text{g} $$
> 
> Forgetting to divide by 2 gives 3.56 g — exactly double, and a lost point.

#### GUIDED PRACTICE • Running the chain 15 min

How long, in hours, to deposit 5.00 g of copper at
        2.00 A? 

*(working space)*

        

What current deposits 10.0 g of silver in
        1.00 h? 

*(working space)*

        

#### INSTRUCTION B • Where this is used 20 min

### Electrolysis in industry `ZUM §18.8`

`SP 2`

- **Producing aluminium** (the Hall–H\'eroult process).
   Al³⁺ needs three electrons per atom, and aluminium sits at
   $-1.66$ V, so the process is enormously energy-hungry — which is
   why aluminium smelters are built next to power stations and why
   recycling aluminium saves so much energy.
- **Electroplating** — depositing a thin layer of one metal
   onto another, controlled precisely by current and time.
- **Electrorefining** — purifying copper by dissolving the
   impure metal at the anode and depositing pure metal at the cathode.
- **Electrolysis of water**, which has
   $E^\circ = -1.23$ V and so requires an applied potential. This was
   Chapter 17's “external energy source driving an unfavorable
   process,” realized in hardware.

#### APPLICATION • Scaling up 20 min

Chromium is plated from Cr³⁺ at 5.00 A for
        2.00 h. Find the mass deposited. 

*(working space)*

        

How much charge is needed to produce 1.00 kg of
        aluminium? 

*(working space)*

        

Two cells are wired in series so the same current passes through
        both: one plates Ag from Ag+, the other Cu from
        Cu²⁺. After the same time, which has more *moles* of
        metal deposited, and why? 

> 📌 **Exit ticket**
>
> List the four conversion steps between a measured current and a mass of
> plated metal, in order.

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
