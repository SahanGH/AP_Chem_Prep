# Self-Study • CED 9.1–9.11, I do / You do

*Unit 9 • Thermodynamics and Electrochemistry*  
Twelve ladders • four YOUR TURN questions each • work alone, check after all four

[← all lessons](../index.md)

---

> 📌 **How to use these notes — read this first**
>
> Each skill is a **ladder**: a worked example, then **four**
> YOUR TURN questions — same skill, new numbers, no help. Work all four
> before checking anything.
> 
> **This unit is really one idea with two faces.** Thermodynamics asks
> whether a reaction is favourable; electrochemistry measures that same
> favourability as a voltage. The bridge is a single equation,
> $\Delta G^\circ = -nFE^\circ$, and once you see that, the second half of
> the unit is the first half with a voltmeter attached.
> 
> **The unit-conversion trap that costs the most marks.** $\Delta H$ is
> tabulated in **kilojoules** and $\Delta S$ in **joules** per
> kelvin. Mixing them in $\Delta G = \Delta H - T\Delta S$ produces an
> answer wrong by a factor of a thousand. Convert first, every time.
> 
> $R = 8.314\,\mathrm{J/mol/K}$,
> $F = 96485\,\mathrm{C/mol}$.
> 
> **One scope note.** The CED excludes labelling an electrode as
> positive or negative, since the convention differs between cell types.
> Anode and cathode *are* assessed, and the rule never changes:
> oxidation at the anode, in both kinds of cell.

## Ladder 1 • Predicting the sign of $\Delta S$

`CED 9.1`

Entropy measures the number of ways energy and matter can be arranged.
More particles, more freedom, more entropy — and **gases dominate**
every comparison they appear in.

> 📘 **I do: three processes**
>
> Predict the sign of $\Delta S^\circ$ for:
> (i) H₂O(l) → H₂O(g);
> (ii) 2NO₂(g) → N₂O₄(g);
> (iii) NaCl(s) → Na+(aq) + Cl⁻(aq).
> 
> **(i) Positive.** A liquid becomes a gas — an enormous increase in
> the freedom of the molecules. Phase changes to gas always raise entropy
> sharply.
> 
> **(ii) Negative.** Two moles of gas become one. Fewer gas particles
> means fewer arrangements.
> 
> **(iii) Positive.** Ions leave a highly ordered crystal lattice and
> disperse through the solvent.
> 
> **The shortcut worth internalizing:** if the number of moles of
> *gas* changes, that decides the sign almost every time. Only when the
> gas count is unchanged do you look at phases and particle counts.

> ✏️ **YOUR TURN 1 — four questions**
>
> 1. Sign of $\Delta S$ for CaCO₃(s) → CaO(s) + CO₂(g):
>    *(working space)*
> 2. Sign for N₂(g) + 3H₂(g) → 2NH₃(g): 
>    *(working space)*
> 3. Sign for water freezing: 
>    *(working space)*
> 4. Sign for H₂(g) + Cl₂(g) → 2HCl(g), and why it is small.
>    *(working space)*
> 
> > **check:** (a) positive     (b) negative     (c) negative    
> (d) near zero — 2 moles of gas become 2

## Ladder 2 • Calculating $\Delta S^\circ$

`CED 9.2`

$$ \Delta S^\circ = \sum S^\circ(\text{products}) -    \sum S^\circ(\text{reactants}) $$

Unlike $\Delta H_f^\circ$, the standard entropy of an element is
**not** zero.

> 📘 **I do: products minus reactants**
>
> Find $\Delta S^\circ$ for C(s) + O₂(g) → CO₂(g) from
> $S^\circ$: C(s) 5.7, O₂(g) 205.0,
> CO₂(g) 213.7 J/mol/K.
> 
> $$ \Delta S^\circ = 213.7 - (5.7 + 205.0) = 213.7 - 210.7    = \mathbf{+3.0~J/mol\,K} $$
> 
> **Why so small?** One mole of gas becomes one mole of gas. With the
> gas count unchanged, the dominant term cancels and only a small residue
> remains.
> 
> **Contrast with intuition:** you might expect burning to be strongly
> entropy-increasing. It is not, in this case — the disorder was already
> there in the O₂.
> 
> **Do not set the element to zero.** C(s) has
> $S^\circ = 5.7$, not 0. Absolute entropies are zero only at
> 0 K, and that is a different statement from the
> $\Delta H_f^\circ$ convention.

> ✏️ **YOUR TURN 2 — four questions**
>
> 1. Products total 400, reactants 560
>    J/mol/K. Find $\Delta S^\circ$.
>    *(working space)*
> 2. Is that consistent with a reaction that consumes gas?
>    *(working space)*
> 3. Why is $S^\circ$ of an element not zero? 
>    *(working space)*
> 4. Which has the larger $S^\circ$, H₂O(l) or H₂O(g)?
>    *(working space)*
> 
> > **check:** (a) $-160$ J/mol/K     (b) yes    
> (c) it has real disorder above 0 K     (d) the gas

## Ladder 3 • Gibbs free energy

`CED 9.3`

$$ \Delta G = \Delta H - T\Delta S $$

Negative $\Delta G$ means thermodynamically favourable. Convert
$\Delta S$ to kilojoules first.

> 📘 **I do: the conversion that decides the answer**
>
> For the ammonia synthesis,
> $\Delta H^\circ = -92.2\,\mathrm{kJ/mol}$ and
> $\Delta S^\circ = -198.7\,\mathrm{J/mol/K}$. Find
> $\Delta G^\circ$ at 298 K.
> 
> **Convert:** $\Delta S^\circ = -0.1987\,\mathrm{kJ/mol/K}$.
> 
> $$ \Delta G^\circ = -92.2 - (298)(-0.1987) = -92.2 + 59.2    = \mathbf{-33.0~kJ/mol} $$
> 
> Negative, so **favourable** at room temperature.
> 
> **Watch the double negative.** $\Delta S$ is negative, so
> $-T\Delta S$ is *positive* — it works against the reaction. The
> favourable enthalpy is what carries it.
> 
> **If you forget the conversion:** $-92.2 - (298)(-198.7)$ gives about
> $+59\,100$, wrong in both magnitude and sign, and it would reverse your
> conclusion entirely.

> ✏️ **YOUR TURN 3 — four questions**
>
> 1. $\Delta H = -50.0\,\mathrm{kJ}$,
>    $\Delta S = +100\,\mathrm{J/K}$, $T = 298$ K. Find
>    $\Delta G$.
>    *(working space)*
> 2. Is that reaction favourable? 
>    *(working space)*
> 3. $\Delta H = +30.0\,\mathrm{kJ}$,
>    $\Delta S = -50\,\mathrm{J/K}$. Favourable at any
>    temperature?
>    *(working space)*
> 4. What does $\Delta G = 0$ mean? 
>    *(working space)*
> 
> > **check:** (a) $-79.8$ kJ     (b) yes     (c) never    
> (d) at equilibrium

## Ladder 4 • Temperature dependence

`CED 9.3`

The four sign combinations give four behaviours. Only two of them depend
on temperature.

> 📘 **I do: the four cases and a crossover**
>
> Tabulate the cases, then find the crossover temperature for
> CaCO₃ → CaO + CO₂, with
> $\Delta H^\circ = +178.3\,\mathrm{kJ}$ and
> $\Delta S^\circ = +160.6\,\mathrm{J/K}$.
> 
> **The four cases.**
> $\Delta H0$: favourable at *all* temperatures.
> $\Delta H>0$, $\Delta S0$, $\Delta S>0$: favourable at **high** $T$ — this case.
> 
> **Crossover, where $\Delta G^\circ = 0$:**
> 
> $$ T = \frac{\Delta H^\circ}{\Delta S^\circ} = \frac{178.3}{0.1606}    = \mathbf{1110~K} $$
> 
> Above about 1110 K the decomposition becomes favourable —
> which is why a lime kiln runs near 1200 K and not at room
> temperature.
> 
> **Check at 298 K:**
> $178.3 - (298)(0.1606) = +130$ kJ — strongly unfavourable, as expected
> for limestone sitting on a shelf.

> ✏️ **YOUR TURN 4 — four questions**
>
> 1. $\Delta H0$. At which temperatures is it
>    favourable?
>    *(working space)*
> 2. $\Delta H **check:** (a) all     (b) low only     (c) 500 K    
> (d) $-T\Delta S$ is negative only then

## Ladder 5 • Thermodynamic versus kinetic control

`CED 9.4`

$\Delta G$ says whether a reaction *can* go and how far. It says
nothing about *when*.

> 📘 **I do: favourable and yet stuck**
>
> A mixture of petrol vapour and air has a strongly negative
> $\Delta G$, yet sits indefinitely in a fuel tank. Explain, and say what a
> spark does.
> 
> **Thermodynamically favourable:** combustion releases a great deal of
> energy and increases entropy. $\Delta G$ is large and negative.
> 
> **Kinetically blocked:** the reaction must begin by breaking strong
> C-H, C-C and O=O bonds — a large activation energy. At
> room temperature essentially no molecules have that much energy, so the
> rate is effectively zero.
> 
> **What a spark supplies:** enough energy for a small number of
> molecules to cross the barrier. Once started, the reaction is exothermic
> and supplies the energy to keep itself going.
> 
> **The general principle:** $\Delta G$ describes the destination,
> $E_a$ the journey. A large negative $\Delta G$ with a large $E_a$ is a
> reaction that is strongly favourable and completely stuck — which is
> fortunate, since it is why fuels can be stored at all.

> ✏️ **YOUR TURN 5 — four questions**
>
> 1. Does a negative $\Delta G$ guarantee a fast reaction?
>    *(working space)*
> 2. What quantity controls the rate? 
>    *(working space)*
> 3. Diamond to graphite has $\Delta G^\circ$ negative. Why do diamonds
>    persist?
>    *(working space)*
> 4. Name two ways to speed a favourable but slow reaction.
>    *(working space)*
> 
> > **check:** (a) no     (b) activation energy     (c) enormous $E_a$
>     (d) raise $T$; add a catalyst

## Ladder 6 • Free energy and the equilibrium constant

`CED 9.5`

$$ \Delta G^\circ = -RT\ln K $$

$\Delta G^\circ$ must be in **joules** to match $R$.

> 📘 **I do: both directions**
>
> Find $K$ at 298 K when
> $\Delta G^\circ = -20.0\,\mathrm{kJ/mol}$. Then state $K$ when
> $\Delta G^\circ = 0$.
> 
> $$ \ln K = -\frac{\Delta G^\circ}{RT}    = \frac{20\,000}{(8.314)(298)} = 8.073 $$
> 
> $$ K = e^{8.073} = \mathbf{3.2\times10^{3}} $$
> 
> Large $K$, as a negative $\Delta G^\circ$ requires.
> 
> **When $\Delta G^\circ = 0$:** $\ln K = 0$, so $\mathbf{K = 1}$ —
> neither side favoured under standard conditions.
> 
> **The three-way correspondence to memorize:**
> $\Delta G^\circ  1 \Leftrightarrow$ products
> favoured;
> $\Delta G^\circ = 0 \Leftrightarrow K = 1$;
> $\Delta G^\circ > 0 \Leftrightarrow K  favoured.
> 
> **The unit trap again:** leaving $\Delta G^\circ$ in kilojoules gives
> $\ln K = 0.0081$ and $K \approx 1.008$ — a wildly wrong answer that
> still looks like a number.

> ✏️ **YOUR TURN 6 — four questions**
>
> 1. $\Delta G^\circ = +15.0\,\mathrm{kJ/mol}$ at
>    298 K. Find $K$.
>    *(working space)*
> 2. Is $K$ greater or less than 1 when $\Delta G^\circ$ is negative?
>    *(working space)*
> 3. What is $K$ when $\Delta G^\circ = 0$? 
>    *(working space)*
> 4. Why must $\Delta G^\circ$ be converted to joules?
>    *(working space)*
> 
> > **check:** (a) 2.4e-3     (b) greater than 1     (c) 1    
> (d) to match $R$ in J/mol/K

## Ladder 7 • Free energy of dissolution

`CED 9.6`

Dissolving is a competition: breaking the lattice costs energy, hydration
releases it, and entropy almost always favours the process.

> 📘 **I do: endothermic yet spontaneous**
>
> Ammonium nitrate dissolves readily although the solution gets markedly
> colder. Explain.
> 
> **$\Delta H$ is positive.** The energy needed to pull the lattice
> apart exceeds what hydration releases, so the process absorbs energy from
> the water — which is why it cools.
> 
> **$\Delta S$ is strongly positive.** Ions locked in an ordered
> crystal become dispersed and mobile throughout the solvent — a large
> increase in the number of available arrangements.
> 
> **$\Delta G = \Delta H - T\Delta S$ is negative** because the
> $T\Delta S$ term outweighs the positive $\Delta H$ at room temperature.
> The process is entropy-driven.
> 
> **The general lesson:** spontaneity is not the same as
> exothermicity. An endothermic process proceeds whenever the entropy gain
> is large enough — and for dissolving an ionic solid, it usually is.

> ✏️ **YOUR TURN 7 — four questions**
>
> 1. Sign of $\Delta S$ when an ionic solid dissolves?
>    *(working space)*
> 2. What drives an endothermic dissolution? 
>    *(working space)*
> 3. If a salt is insoluble despite favourable entropy, what must be
>    true of $\Delta H$?
>    *(working space)*
> 4. Would cooling the water make NH₄NO₃ more or less soluble?
>    *(working space)*
> 
> > **check:** (a) positive     (b) the entropy increase    
> (c) strongly positive     (d) less soluble

## Ladder 8 • Coupled reactions

`CED 9.7`

Free energies add, exactly as enthalpies do in Hess's law. An unfavourable
reaction can be driven by pairing it with a strongly favourable one that
shares a species.

> 📘 **I do: driving an unfavourable step**
>
> Reaction A has $\Delta G^\circ = +60\,\mathrm{kJ/mol}$;
> reaction B, sharing a common species, has
> $\Delta G^\circ = -95\,\mathrm{kJ/mol}$. Find the coupled value.
> 
> $$ \Delta G^\circ_{\text{total}} = (+60) + (-95) = \mathbf{-35~kJ/mol} $$
> 
> Negative, so the coupled process **is** favourable even though A
> alone is not.
> 
> **The essential condition: a shared species.** The product of one
> reaction must be consumed by the other. Without that link they are two
> independent reactions that happen to be in the same beaker, and the
> unfavourable one still will not proceed.
> 
> **Where this matters:** metal extraction couples an unfavourable
> oxide decomposition to the favourable oxidation of carbon. In biology,
> ATP hydrolysis is coupled to thousands of otherwise unfavourable
> reactions — it is how cells do chemistry that thermodynamics would
> otherwise forbid.

> ✏️ **YOUR TURN 8 — four questions**
>
> 1. $+45$ and $-70$ kJ/mol. Coupled value, and is
>    it favourable?
>    *(working space)*
> 2. $+80$ and $-55$. Coupled value, and is it favourable?
>    *(working space)*
> 3. What condition must the two reactions satisfy?
>    *(working space)*
> 4. Why is coupling analogous to Hess's law? 
>    *(working space)*
> 
> > **check:** (a) $-25$, favourable     (b) $+25$, not favourable    
> (c) a shared species     (d) both are state functions and add

## Ladder 9 • Galvanic cells

`CED 9.8`

Oxidation at the anode, reduction at the cathode — in both cell types.
Electrons flow through the wire from anode to cathode.

> 📘 **I do: assembling a cell**
>
> Build a cell from iron ($E^\circ = -0.44$ V) and copper
> ($E^\circ = +0.34$ V). Give the half-reactions, the anode, $E^\circ$, and
> the directions of electron and anion flow.
> 
> **The more positive potential is reduced**, so copper is the
> cathode and iron is oxidized at the anode.
> 
> Fe(s) → Fe²⁺(aq) + 2e⁻ (anode)    
> Cu²⁺(aq) + 2e⁻ → Cu(s) (cathode)
> 
> $$ E^\circ = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}}    = 0.34 - (-0.44) = \mathbf{+0.78~V} $$
> 
> **Electrons** flow through the external wire from the **iron**
> to the **copper**.
> 
> **Anions** in the salt bridge migrate toward the **anode**,
> balancing the positive charge building up as Fe²⁺ enters that
> solution.
> 
> **Positive $E^\circ$ confirms it works** — a galvanic cell always
> has a positive cell potential, which is the same statement as
> $\Delta G^\circ$ being negative.

> ✏️ **YOUR TURN 9 — four questions**
>
> 1. Nickel ($-0.25$ V) and silver ($+0.80$ V): which is the anode, and
>    what is $E^\circ$?
>    *(working space)*
> 2. Which way do electrons flow in the external circuit?
>    *(working space)*
> 3. Which way do anions move in the salt bridge?
>    *(working space)*
> 4. What happens at the anode in an *electrolytic* cell?
>    *(working space)*
> 
> > **check:** (a) nickel; $+1.05$ V     (b) anode to cathode    
> (c) toward the anode     (d) oxidation — same as galvanic

## Ladder 10 • Cell potential and free energy

`CED 9.9`

$$ \Delta G^\circ = -nFE^\circ $$

$n$ is the number of electrons transferred in the balanced reaction.
$E^\circ$ is *intensive* — never multiply it.

> 📘 **I do: the bridge equation**
>
> For the iron–copper cell above ($E^\circ = +0.78$ V, $n = 2$), find
> $\Delta G^\circ$.
> 
> $$ \Delta G^\circ = -nFE^\circ = -(2)(96485)(0.78)    = -1.5e5~\text{J} = \mathbf{-151~kJ} $$
> 
> Negative, as it must be for a cell that delivers current on its own.
> 
> **The intensive property that trips everyone.** If you double the
> whole reaction, $n$ doubles and $\Delta G^\circ$ doubles — but
> $E^\circ$ does **not**. Potential is energy per unit charge, so
> scaling the reaction scales both energy and charge together and leaves the
> ratio alone. A cell's voltage does not depend on its size.
> 
> **The correspondence:** $E^\circ > 0 \Leftrightarrow \Delta G^\circ  1$. Three ways of saying the same
> thing.

> ✏️ **YOUR TURN 10 — four questions**
>
> 1. $E^\circ = +1.05$ V with $n = 2$. Find $\Delta G^\circ$.
>    *(working space)*
> 2. If a reaction is doubled, what happens to $E^\circ$ and to
>    $\Delta G^\circ$?
>    *(working space)*
> 3. What is the sign of $\Delta G^\circ$ for an electrolytic cell?
>    *(working space)*
> 4. A cell has $E^\circ = -0.30$ V. What does that tell you?
>    *(working space)*
> 
> > **check:** (a) $-203$ kJ     (b) $E^\circ$ unchanged, $\Delta G^\circ$
> doubles     (c) positive     (d) the reverse reaction is the
> favourable one

## Ladder 11 • The Nernst equation

`CED 9.10`

$$ E = E^\circ - \frac{0.0592}{n}\log Q \qquad    (25\,\mathrm{{}^\circ C}) $$

Non-standard concentrations shift the potential. As the cell runs, $Q$
rises and $E$ falls.

> 📘 **I do: which way does it move?**
>
> A Zn/Cu cell has $E^\circ = 1.10$ V and $n = 2$. Find $E$ when
> $Q = 0.010$, and when $Q = 100$.
> 
> **$Q = 0.010$:**
> 
> $$ E = 1.10 - \frac{0.0592}{2}\log(0.010) = 1.10 - (0.0296)(-2)    = \mathbf{1.16~V} $$
> 
> *Above* standard — $Q  driving force is greater.
> 
> **$Q = 100$:**
> 
> $$ E = 1.10 - (0.0296)(2) = \mathbf{1.04~V} $$
> 
> *Below* standard — products have accumulated.
> 
> **What happens as the cell discharges:** products build up, $Q$ rises,
> and $E$ falls steadily. A “dead” battery has reached equilibrium:
> $Q = K$ and $E = \mathbf{0}$.
> 
> **Note carefully: $E = 0$, not $E^\circ = 0$.** The standard
> potential is a constant of the chemistry and never changes; it is the
> actual potential that decays to zero.

> ✏️ **YOUR TURN 11 — four questions**
>
> 1. Does $E$ rise or fall as a cell discharges?
>    *(working space)*
> 2. What is $E$ for a dead battery? 
>    *(working space)*
> 3. $E^\circ = 0.80$ V, $n = 1$, $Q = 10$. Find $E$.
>    *(working space)*
> 4. Why does $E^\circ$ stay constant while $E$ changes?
>    *(working space)*
> 
> > **check:** (a) falls     (b) zero     (c) 0.74 V    
> (d) $E^\circ$ is defined at standard conditions

## Ladder 12 • Electrolysis and Faraday's law

`CED 9.11`

Charge is current times time; moles of electrons is charge over $F$; then
the half-reaction's electron count converts to moles of substance.

> 📘 **I do: the four-step chain**
>
> Copper is plated from Cu²⁺ at 2.50 A for
> 60.0 min. Find the mass deposited.
> 
> **Time to seconds:** $60.0 \times 60 = 3600\,\mathrm{s}$.
> 
> **Charge:** $Q = It = (2.50)(3600) = 9000\,\mathrm{C}$.
> 
> **Moles of electrons:**
> $9000/96485 = 0.0933$ mol.
> 
> **Through the half-reaction.** Cu²⁺ + 2e⁻ → Cu needs
> **two** electrons per atom:
> 
> $$ n(\text{Cu}) = \frac{0.09328}{2} = 0.04664~\text{mol} $$
> 
> $$ m = 0.04664 \times 63.55 = \mathbf{2.96~g} $$
> 
> **The step that is missed most often** is dividing by 2. Silver
> (Ag+ + e⁻ → Ag) needs only one electron, so the same charge
> deposits twice as many moles of silver as of copper.

> ✏️ **YOUR TURN 12 — four questions**
>
> 1. Charge delivered by 1.00 A for 30.0 min:
>    *(working space)*
> 2. Moles of electrons in that charge: 
>    *(working space)*
> 3. Mass of silver deposited by it
>    ($M = 107.87\,\mathrm{g/mol}$):
>    *(working space)*
> 4. Same charge through Al³⁺: more or fewer moles of metal than
>    silver, and by what factor?
>    *(working space)*
> 
> > **check:** (a) 1800 C     (b) 0.0187 mol    
> (c) 2.01 g     (d) one third as many

## Where you stand

Tick a ladder only if all four YOUR TURN questions were right first time.

| **First try?** | **Skill** | **Ladder** | **If not, re-read…** |
|---|---|---|---|
| $\square$ | sign of $\Delta S$ | 1 | count moles of gas |
| $\square$ | calculating $\Delta S^\circ$ | 2 | elements are not zero |
| $\square$ | Gibbs free energy | 3 | convert $\Delta S$ to kJ |
| $\square$ | temperature dependence | 4 | the four sign cases |
| $\square$ | kinetic vs thermodynamic | 5 | how far vs how fast |
| $\square$ | $\Delta G^\circ$ and $K$ | 6 | joules, to match $R$ |
| $\square$ | dissolution | 7 | entropy can drive it |
| $\square$ | coupled reactions | 8 | needs a shared species |
| $\square$ | galvanic cells | 9 | oxidation at the anode |
| $\square$ | $\Delta G^\circ = -nFE^\circ$ | 10 | never scale $E^\circ$ |
| $\square$ | the Nernst equation | 11 | $E \to 0$, not $E^\circ$ |
| $\square$ | Faraday's law | 12 | divide by the electron count |

> 📌 **Scoring yourself honestly**
>
> 12/12: move on to the unit worksheets and the free-response set.
> 9–11: solid — redo the missed ladders tomorrow from a blank page.
> 8 or fewer: the recurring root causes here are exactly three —
> (1) mixing kilojoules and joules in $\Delta G = \Delta H - T\Delta S$ or
> in $\Delta G^\circ = -RT\ln K$, (2) multiplying $E^\circ$ when the
> reaction is scaled, and (3) forgetting to divide by the number of
> electrons in a Faraday calculation. Fix those three and most of these
> ladders fall together.

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
