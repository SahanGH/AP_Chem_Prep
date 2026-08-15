# Self-Study • §5.1–5.10, I do / You do

*Chapter 5 • Gases*  
Zumdahl §5.1–5.10 • PDF pp. 227–268 • four YOUR TURN questions per ladder

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
> **Two rules that prevent most lost marks in this chapter.**
> Temperature in any gas calculation is **always in kelvin** —
> $T(\mathrm{K}) = T(^\circ\mathrm{C}) + 273.15$. And the value of $R$ you
> choose dictates every other unit: with
> $R = 0.08206\,\mathrm{L\cdot atm/mol/K}$, pressure must be atm
> and volume litres.

## Ladder 1 • Pressure and its units

`ZUM §5.1`

Pressure is force per unit area. A barometer balances the atmosphere
against a mercury column, so pressure is quoted as the height that column
supports:

$$ 1\,\mathrm{atm} = 760\,\mathrm{mmHg} = 760\,\mathrm{torr}    = 101325\,\mathrm{Pa} = 101.325\,\mathrm{kPa} $$

> 📘 **I do: one reading, four units**
>
> A weather station reports 745 torr. Express it in atm, kPa, and
> mmHg.
> 
> **To atm** — divide by the number of torr in an atm:
> 
> $$ \frac{745}{760} = \mathbf{0.980~atm} $$
> 
> **To kPa** — go through atm, or use the direct ratio:
> 
> $$ 0.980 \times 101.325 = \mathbf{99.3~kPa} $$
> 
> **To mmHg** — no work at all: the torr and the mmHg are the
> *same size*, so 745 torr $= \mathbf{745~mmHg}$.
> 
> **Sense check:** the reading is slightly below one atmosphere, so
> every converted value should sit slightly below its 1-atm counterpart
> (1 atm, 101.3 kPa, 760 mmHg). All three do.

> ✏️ **YOUR TURN 1 — four questions**
>
> 1. 2.50 atm in torr: 
>    *(working space)*
> 2. 88.0 kPa in atm: 
>    *(working space)*
> 3. 0.335 atm in mmHg: 
>    *(working space)*
> 4. A gauge reads 950 torr. Is the gas above or below
>    atmospheric pressure, and by what factor?
>    *(working space)*
> 
> > **check:** (a) 1900 torr     (b) 0.868 atm    
> (c) 255 mmHg     (d) above; $950/760 = 1.25$ times

## Ladder 2 • The combined gas law

`ZUM §5.2`

Boyle ($P_1V_1 = P_2V_2$), Charles ($V_1/T_1 = V_2/T_2$), and
Gay-Lussac ($P_1/T_1 = P_2/T_2$) are all one relationship with the
unchanged variables cancelled:

$$ \boxed{\;\frac{P_1V_1}{T_1} = \frac{P_2V_2}{T_2}\;} $$

Learn this one and delete anything held constant — there is no need to
memorize four separate laws.

> 📘 **I do: a weather balloon rising**
>
> A balloon holds 4.50 L at 1.00 atm and
> 22 °C. It rises to where the pressure is 0.450 atm and
> the temperature -25 °C. Find the new volume.
> 
> **Kelvin first — always:**
> 
> $$ T_1 = 22 + 273 = 295\,\mathrm{K} \qquad    T_2 = -25 + 273 = 248\,\mathrm{K} $$
> 
> **Rearrange for $V_2$:**
> 
> $$ V_2 = V_1 \times \frac{P_1}{P_2} \times \frac{T_2}{T_1}        = 4.50 \times \frac{1.00}{0.450} \times \frac{248}{295}        = \mathbf{8.41~L} $$
> 
> **Sense check, factor by factor:** the pressure fell to less than
> half, which should roughly double the volume; the temperature dropped,
> which should shrink it a little. Up by $2.22$, down by $0.841$ —
> net roughly $\times 1.87$. The balloon expands, as balloons do at
> altitude.

> ✏️ **YOUR TURN 2 — four questions**
>
> 1. 2.00 L at 1.50 atm is compressed to
>    0.750 L at constant $T$. New pressure?
>    *(working space)*
> 2. 500. mL at 27 °C is warmed to
>    127 °C at constant $P$. New volume?
>    *(working space)*
> 3. A rigid can at 1.00 atm and 20 °C is heated to
>    300 °C. New pressure?
>    *(working space)*
> 4. 6.00 L at 2.00 atm and 300 K moves
>    to 1.50 atm and 400 K. New volume?
>    *(working space)*
> 
> > **check:** (a) 4.00 atm     (b) 667 mL    
> (c) 1.96 atm     (d) 10.7 L

## Ladder 3 • The ideal gas law

`ZUM §5.3`

$$ \boxed{\;PV = nRT\;} \qquad    R = 0.08206\,\mathrm{L\cdot atm/mol/K} $$

Use $PV = nRT$ for **one state** of a gas; use the combined law when
a sample *changes* from one state to another. Choosing between them
is most of the skill.

> 📘 **I do: moles, then mass**
>
> What mass of oxygen occupies 7.50 L at 1.20 atm and
> 35 °C?
> 
> **Kelvin:** $35 + 273 = 308\,\mathrm{K}$
> 
> **Solve for $n$:**
> 
> $$ n = \frac{PV}{RT} = \frac{(1.20)(7.50)}{(0.08206)(308)}      = \frac{9.00}{25.27} = 0.356\,\mathrm{mol} $$
> 
> **Moles to grams:** $0.356 \times 32.00 = \mathbf{11.4~g}$
> 
> **Sense check:** at room conditions a mole of gas fills about 24 L,
> so 7.5 L should be roughly a third of a mole. It is.

> ✏️ **YOUR TURN 3 — four questions**
>
> 1. Moles of gas in 10.0 L at 2.00 atm and
>    273 K:
>    *(working space)*
> 2. Pressure of 0.500 mol of gas in 5.00 L at
>    25 °C:
>    *(working space)*
> 3. Volume of 16.04 g of CH₄
>    ($M = 16.04\,\mathrm{g/mol}$) at 1.00 atm and
>    0 °C:
>    *(working space)*
> 4. A 2.00 L flask holds 0.150 mol at
>    1.85 atm. Find the temperature in °C.
>    *(working space)*
> 
> > **check:** (a) 0.893 mol     (b) 2.45 atm    
> (c) 22.4 L     (d) 28 °C

## Ladder 4 • Molar mass and density

`ZUM §5.3`

Substituting $n = m/M$ into $PV = nRT$ gives the two most useful
rearrangements in the chapter:

$$ M = \frac{mRT}{PV} = \frac{dRT}{P} \qquad\text{and}\qquad    d = \frac{PM}{RT} $$

Read the second one: at fixed $P$ and $T$, **density is
proportional to molar mass** — which is why a balloon of He rises
and one of CO₂ sinks.

> 📘 **I do: identifying an unknown gas**
>
> A 0.582 g sample of an unknown gas occupies
> 0.500 L at 1.00 atm and 100 °C. What is it?
> 
> **Kelvin:** $100 + 273 = 373\,\mathrm{K}$
> 
> $$ M = \frac{mRT}{PV} = \frac{(0.582)(0.08206)(373)}{(1.00)(0.500)}      = \frac{17.81}{0.500} = \mathbf{35.6~g/mol} $$
> 
> **Identify:** Cl₂ is 70.90, HCl is 36.46, O₂ is
> 32.00. The value points to **HCl** — and note the
> *measurement* decides, not a guess; 35.6 against 36.46 is within
> ordinary experimental error, while the alternatives are far off.

> ✏️ **YOUR TURN 4 — four questions**
>
> 1. Density of CO₂ ($M = 44.01$) at 1.00 atm and
>    0 °C:
>    *(working space)*
> 2. A gas has density 1.34 g/L at
>    1.00 atm and 25 °C. Find $M$.
>    *(working space)*
> 3. 1.25 g of a gas fills 1.00 L at
>    0.980 atm and 20 °C. Find $M$.
>    *(working space)*
> 4. Without calculating: at the same $P$ and $T$, which is denser,
>    N₂ or Ar? Why?
>    *(working space)*
> 
> > **check:** (a) 1.96 g/L     (b)
> 32.8 g/mol     (c) 30.7 g/mol    
> (d) Ar — larger molar mass at the same $P$, $T$

## Ladder 5 • Gas stoichiometry

`ZUM §5.4`

Chapter 3's spine gains a gas entrance and a gas exit:

> 
$P$, $V$, $T$ $\to$ moles (via $PV=nRT$) $\to$ mole ratio $\to$ moles
$\to$ $P$, $V$, $T$ or grams

At **STP** (0 °C, 1 atm) only, one mole of any
gas occupies 22.4 L — a shortcut that is wrong at every
other condition.

> 📘 **I do: hydrogen from a metal and acid**
>
> What volume of H₂, collected at 25 °C and
> 1.00 atm, forms when 5.00 g of zinc
> ($M = 65.38\,\mathrm{g/mol}$) reacts completely?
> Zn(s) + 2HCl(aq) → ZnCl₂(aq) + H₂(g)
> 
> **Grams to moles:**
> $\dfrac{5.00}{65.38} = 0.0765\,\mathrm{mol}~\text{Zn}$
> 
> **Mole ratio** (1:1): $0.0765\,\mathrm{mol}~\text{H₂}$
> 
> **Moles to volume, at the stated conditions — not STP:**
> 
> $$ V = \frac{nRT}{P} = \frac{(0.0765)(0.08206)(298)}{1.00}      = \mathbf{1.87~L} $$
> 
> Using 22.4 L/mol here would give 1.71 L, which is wrong by 9%: the gas
> is at 25 °C, not 0 °C.

> ✏️ **YOUR TURN 5 — four questions**
>
> 1. Volume of CO₂ at STP from decomposing 25.0 g of
>    CaCO₃ ($M = 100.09$): CaCO₃ → CaO + CO₂
>    *(working space)*
> 2. Volume of O₂ at 1.00 atm, 25 °C from
>    0.500 mol of KClO₃:
>    2KClO₃ → 2KCl + 3O₂
>    *(working space)*
> 3. Mass of NH₃ formed from 5.00 L of N₂ at
>    2.00 atm and 300 K with excess H₂:
>    N₂ + 3H₂ → 2NH₃
>    *(working space)*
> 4. Why is 22.4 L/mol usable in (a) but not in (b)?
>    *(working space)*
> 
> > **check:** (a) 5.60 L     (b) 18.3 L    
> (c) 13.8 g     (d) only (a) is at STP

## Ladder 6 • Partial pressures

`ZUM §5.5`

In a mixture each gas behaves as if alone:

$$ P_{\text{total}} = P_1 + P_2 + \cdots \qquad    P_i = X_i P_{\text{total}}, \quad    X_i = \frac{n_i}{n_{\text{total}}} $$

Mole fractions are dimensionless and sum to 1. A gas
**collected over water** is wet, so
$P_{\text{gas}} = P_{\text{total}} - P_{\text{H₂O}}$.

> 📘 **I do: a three-gas mixture, then a wet gas**
>
> **(a)** A vessel holds 0.200 mol N₂,
> 0.300 mol O₂, and 0.500 mol He at a total
> pressure of 2.40 atm. Find each partial pressure.
> 
> $n_{\text{total}} = 1.000$ mol, so the mole fractions are 0.200, 0.300,
> 0.500, and
> 
> $$ P_{\text{N₂}} = 0.200(2.40) = \mathbf{0.480~atm} \quad    P_{\text{O₂}} = \mathbf{0.720~atm} \quad    P_{\text{He}} = \mathbf{1.20~atm} $$
> 
> They sum to 2.40 atm — always check that.
> 
> **(b)** Hydrogen collected over water at 25 °C has a
> total pressure of 755 torr. The vapour pressure of water at
> 25 °C is 23.8 torr. The dry hydrogen pressure is
> 
> $$ 755 - 23.8 = \mathbf{731~torr} $$
> 
> Forgetting to subtract the water overstates the gas by about 3%.

> ✏️ **YOUR TURN 6 — four questions**
>
> 1. A mixture is 1.00 mol N₂ and 3.00 mol
>    H₂ at 4.00 atm. Find both partial pressures.
>    *(working space)*
> 2. Dry air is about 78% N₂ by moles. Find $P_{\text{N₂}}$ at
>    1.00 atm.
>    *(working space)*
> 3. Oxygen collected over water at 20 °C
>    ($P_{\text{H₂O}} = 17.5\,\mathrm{torr}$) reads 745 torr total.
>    Find the dry O₂ pressure.
>    *(working space)*
> 4. In question (a), which gas has the larger partial pressure, and
>    does it have the larger *mass*?
>    *(working space)*
> 
> > **check:** (a) N₂ 1.00 atm, H₂ 3.00 atm    
> (b) 0.78 atm     (c) 728 torr     (d) H₂ has the
> larger pressure but the smaller mass

## Ladder 7 • Kinetic molecular theory;
effusion

`ZUM §5.6–5.7`

KMT explains *why* the gas laws hold. Its postulates: particles are
point-like with negligible volume; they move randomly; collisions are
perfectly elastic; there are no attractive or repulsive forces; and the
**average kinetic energy is proportional to the absolute
temperature**.

That last point carries the consequences:

$$ \mathrm{KE}_{\text{avg}} = \tfrac{3}{2}RT \quad\text{(per mole)}    \qquad u_{\text{rms}} = \sqrt{\frac{3RT}{M}} $$

At a given temperature *all* gases share the same average kinetic
energy — so the lighter gas must move faster. Graham's law follows:

$$ \frac{\text{rate}_1}{\text{rate}_2} = \sqrt{\frac{M_2}{M_1}} $$

> 📘 **I do: comparing two gases at one temperature**
>
> Compare He ($M = 4.003$) and Ar ($M = 39.95$) at
> 300 K.
> 
> **Average kinetic energy:** identical — it depends only on $T$.
> This is the answer students most often get wrong by assuming the light
> gas has more energy.
> 
> **Relative speed / effusion rate:**
> 
> $$ \frac{\text{rate}_{\text{He}}}{\text{rate}_{\text{Ar}}}    = \sqrt{\frac{39.95}{4.003}} = \sqrt{9.98} = \mathbf{3.16} $$
> 
> Helium effuses about 3.2 times faster. Note the molar masses go
> *opposite* the rates — heavier means slower — which is why $M_2$
> sits on top.

> ✏️ **YOUR TURN 7 — four questions**
>
> 1. Rate ratio of H₂ ($M = 2.016$) to O₂ ($M = 32.00$):
>    *(working space)*
> 2. An unknown gas effuses 0.500 times as fast as He
>    ($M = 4.003$). Find its molar mass.
>    *(working space)*
> 3. Two flasks at the same temperature hold N₂ and CO₂.
>    Which has the greater average kinetic energy?
>    *(working space)*
> 4. Which KMT postulate fails first as a gas is compressed to high
>    pressure?
>    *(working space)*
> 
> > **check:** (a) 3.98     (b) 16.0 g/mol     (c) equal
> — same $T$     (d) negligible particle volume

## Ladder 8 • Real gases, and the atmosphere

`ZUM §5.8–5.10`

Real gases deviate from ideality where the two ignored facts bite:

- **High pressure** — particle volume is no longer
   negligible, so the real volume exceeds the ideal prediction.
- **Low temperature** — attractions have time to act,
   pulling particles together so the real pressure falls below the
   ideal prediction.

So gases behave *most* ideally at **low pressure and high
temperature**, and a gas with weak intermolecular forces and small size
(He, H₂) is closer to ideal than a large, polar one
(NH₃, H₂O). Van der Waals corrects both terms:

$$ \left(P + \frac{an^2}{V^2}\right)(V - nb) = nRT $$

with $a$ for attractions and $b$ for particle volume.

> 📘 **I do: reading the corrections**
>
> Two gases have van der Waals constants
> He: $a = 0.0341$, $b = 0.0237$;    
> NH₃: $a = 4.17$, $b = 0.0371$
> (in L²·atm/mol² and
> L/mol).
> 
> **Which is closer to ideal, and why?** He. Its $a$ is more than
> a hundred times smaller, meaning almost no intermolecular attraction — a
> tiny nonpolar atom. Ammonia is polar and hydrogen-bonds, so its $a$ is
> large.
> 
> **Which correction dominates for NH₃ at moderate pressure?**
> The $a$ term. Attractions reduce the force of wall collisions, so the
> measured pressure is *lower* than ideal — and the correction adds
> $an^2/V^2$ back on.
> 
> **Where does NH₃ behave most ideally?** At low pressure (far
> apart, so attractions rarely act) and high temperature (moving too fast
> to be captured).

> ✏️ **YOUR TURN 8 — four questions**
>
> 1. State the two conditions under which any real gas behaves most
>    ideally:
>    *(working space)*
> 2. Which deviates less from ideal at the same $P$ and $T$: H₂
>    or H₂O vapour? Why?
>    *(working space)*
> 3. In the van der Waals equation, which constant corrects for
>    particle volume, and does it make $V$ effectively larger or
>    smaller?
>    *(working space)*
> 4. Ozone in the stratosphere absorbs ultraviolet light. Name the
>    class of pollutant blamed for destroying it.
>    *(working space)*
> 
> > **check:** (a) low pressure, high temperature     (b) H₂ — no
> hydrogen bonding     (c) $b$; it makes the free volume smaller    
> (d) chlorofluorocarbons (CFCs)

## Mastery tracker

Tick a row only if **all four** YOUR TURN questions were right on
the first attempt.

| **First try?** | **Skill** | **Ladder** | **If not, re-read…** |
|---|---|---|---|
| $\square$ | pressure units | 1 | 1 atm $=$ 760 torr $=$ 101.325 kPa |
| $\square$ | combined gas law | 2 | kelvin first, then cancel |
| $\square$ | ideal gas law | 3 | one state vs. a change of state |
| $\square$ | molar mass and density | 4 | $M = dRT/P$; $d = PM/RT$ |
| $\square$ | gas stoichiometry | 5 | 22.4 L/mol is STP only |
| $\square$ | partial pressures | 6 | mole fractions; subtract water |
| $\square$ | KMT and effusion | 7 | same $T$ $\Rightarrow$ same KE |
| $\square$ | real gases | 8 | low $P$, high $T$; $a$ and $b$ |

> 📌 **Scoring yourself honestly**
>
> 8/8: move on to the end-of-chapter problems. 6–7: solid — redo the
> missed ladders tomorrow, not today. 5 or fewer: the recurring root causes
> in this chapter are exactly three — (1) temperature left in
> °C, (2) using 22.4 L/mol when the gas is not at STP, and
> (3) confusing *speed* with *kinetic energy* at a given
> temperature. Fix those three habits and most of the ladders fall
> together.

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
