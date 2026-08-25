# Study Notes • §3.7–3.11 in Worked Examples

*Chapter 3 • Stoichiometry*  
Zumdahl §3.7–3.11 • PDF pp. 125–153 • read with a pencil

[← all lessons](../index.md)

---

> 📌 **What these five sections are, as one story**
>
> Section 3.7 answers “what *is* this compound?” — turning measured
> percentages or combustion data into a formula. Sections 3.8–3.9 give the
> grammar for writing what compounds *do*: the balanced equation.
> Sections 3.10–3.11 then use that equation as a conversion factor: given an
> amount of one substance, find the amount of any other — including the
> case where one reactant runs out first.
> 
> Every calculation in this span is the same three-step spine:
> 
> $$ \text{grams} \xrightarrow{\;\div M\;} \text{moles}    \xrightarrow{\;\text{mole ratio}\;} \text{moles}    \xrightarrow{\;\times M\;} \text{grams} $$
> 
> Only the middle step ever uses the chemical equation. Grams never talk to
> grams directly.

## §3.7 • Determining the formula of a
compound

`ZUM §3.7`

A formula determination always runs the same four steps:

1. Assume a 100 g sample, so percentages become grams.
2. Convert each element's mass to moles.
3. Divide every mole number by the smallest one.
4. If the ratios are not whole, multiply *all* of them by the
   same small integer. The result is the empirical formula;
   the molecular formula is the empirical formula times
   $M / M_{\text{empirical}}$.

> 📘 **Worked example 1: from percentages — nicotine**
>
> Nicotine is 74.03% C, 8.70% H, and 17.27% N, with a molar mass of
> 162.23 g/mol. Find both formulas.
> 
> **Step 1 — take 100 g:** 74.03 g C, 8.70 g H, 17.27 g N.
> 
> **Step 2 — to moles:**
> 
> $$ \text{C}: \frac{74.03}{12.01} = 6.164 \qquad    \text{H}: \frac{8.70}{1.008} = 8.63 \qquad    \text{N}: \frac{17.27}{14.01} = 1.233 $$
> 
> **Step 3 — divide by the smallest (1.233):**
> 
> $$ \text{C}: 5.00 \qquad \text{H}: 7.00 \qquad \text{N}: 1.00 $$
> 
> **Step 4 — already whole:** empirical formula C₅H₇N,
> $M_{\text{emp}} = 5(12.01) + 7(1.008) + 14.01 = 81.12\,\mathrm{g/mol}$.
> 
> $$ \frac{162.23}{81.12} = 2.00 \qquad\Longrightarrow\qquad    \textbf{molecular formula } \text{C₁₀H₁₄N₂} $$
> 
> Note what the molar mass was *for*: the percentages alone can never
> distinguish C₅H₇N from C₁₀H₁₄N₂ — both have identical
> composition. The empirical formula is what analysis gives; the molar mass
> picks the molecule.

> 📘 **Worked example 2: combustion analysis — a hydrocarbon**
>
> Burning 0.7210 g of a compound containing only C and H produces
> 2.201 g of CO₂ and 1.081 g of H₂O. The molar
> mass is 72.15 g/mol. Find both formulas.
> 
> **The idea:** in excess oxygen, every carbon atom ends up in a
> CO₂ and every hydrogen atom in an H₂O. Count them there.
> 
> **Carbon** (one C per CO₂):
> 
> $$ \frac{2.201}{44.01} = 0.05001\,\mathrm{mol}~\text{CO₂}    \;\Rightarrow\; 0.05001\,\mathrm{mol}~\text{C}    \;\Rightarrow\; 0.05001 \times 12.01 = 0.6006\,\mathrm{g}~\text{C} $$
> 
> **Hydrogen** (*two* H per H₂O — the factor everyone
> forgets):
> 
> $$ \frac{1.081}{18.02} = 0.05999\,\mathrm{mol}~\text{H₂O}    \;\Rightarrow\; 0.1200\,\mathrm{mol}~\text{H}    \;\Rightarrow\; 0.1200 \times 1.008 = 0.1210\,\mathrm{g}~\text{H} $$
> 
> **Mass check:** $0.6006 + 0.1210 = 0.7216\,\mathrm{g}$ — the whole
> sample is accounted for, so C and H really are the only elements.
> 
> **Ratio:** $\text{H}/\text{C} = 0.1200/0.05001 = 2.40 = 12/5$, so the
> empirical formula is C₅H₁₂ with
> $M_{\text{emp}} = 72.15\,\mathrm{g/mol}$ — equal to the molar mass,
> so the **molecular formula is also C₅H₁₂** (pentane). The
> multiplier can be 1; do not assume it is bigger.

> 📘 **Worked example 3: combustion with oxygen in the compound**
>
> Burning 2.000 g of a compound containing C, H, and O gives
> 2.868 g CO₂ and 1.566 g H₂O. The molar mass
> is 92.09 g/mol. Find both formulas.
> 
> **C and H exactly as before:**
> 
> $$ \text{C}: \frac{2.868}{44.01} = 0.06517\,\mathrm{mol}    \to 0.7827\,\mathrm{g} \qquad    \text{H}: 2 \times \frac{1.566}{18.02} = 0.1738\,\mathrm{mol}    \to 0.1752\,\mathrm{g} $$
> 
> **Oxygen must come by difference.** The sample's own oxygen atoms end
> up in the same CO₂ and H₂O as the oxygen from the air, so no
> measurement can see them separately:
> 
> $$ m_{\text{O}} = 2.000 - 0.7827 - 0.1752 = 1.042\,\mathrm{g}    \;\Rightarrow\; \frac{1.042}{16.00} = 0.06513\,\mathrm{mol} $$
> 
> **Divide by the smallest (0.06513):**
> 
> $$ \text{C}: 1.00 \qquad \text{H}: 2.67 \qquad \text{O}: 1.00 $$
> 
> 2.67 is $8/3$ — a value like this must **not** be rounded. Multiply
> all three by 3:
> 
> $$ \text{empirical } \text{C₃H₈O₃}, \quad M_{\text{emp}} = 92.09\,\mathrm{g/mol}    = M \;\Rightarrow\; \textbf{molecular } \text{C₃H₈O₃}~\text{(glycerol)} $$

> ⚠️ **AP trap**
>
> The rounding rule, stated once and used forever: ratios such as 1.99 or
> 3.02 round to whole numbers; ratios sitting near a simple fraction —
> 2.25 ($=9/4$), 2.33 ($=7/3$), 2.50, 2.67 ($=8/3$), 2.75 — are
> instructions to *multiply*, by 4, 3, 2, 3, 4 respectively. Rounding
> 2.67 to 3 produces a wrong formula that no later step can rescue.

### Check yourself — §3.7

1. A compound is 92.26% C and 7.74% H with molar mass
   78.11 g/mol. Both formulas:
   *(working space)*
2. Why does combustion analysis measure oxygen by difference rather
   than directly? 
3. A mole-ratio calculation gives C 1.00, H 1.33, O 1.00. The
   empirical formula is: C₃H₄O₃

## §3.8 • What a chemical equation says

`ZUM §3.8`

A chemical equation is a statement about *atoms rearranging*:

CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(g)

| **Symbol** | **Means** |  |
|---|---|---|
| (s), (l), (g) | solid, liquid, gas |  |
| (aq) | dissolved in water |  |
| coefficient | *relative* number of molecules or moles | never a fixed amount |

What the equation above claims: one CH₄ molecule and two O₂
molecules always rearrange into one CO₂ and two H₂O. The same
sentence read in moles: 1 mol CH₄ reacts with 2 mol O₂. It does
*not* claim you have 1 mol of anything — coefficients are ratios,
not inventory.

**Conserved:** atoms of each element, and therefore total mass.
**Not conserved:** molecules (3 become 3 here, but 4 become 3 in
ammonia synthesis) and moles. Only atoms are bookkept.

> ⚠️ **AP trap**
>
> **A coefficient multiplies the whole formula; a subscript is part of
> the substance's identity.** Balancing is done *only* with
> coefficients. “Fixing” H₂O to H₂O₂ to balance oxygen does not
> balance the equation — it changes water into hydrogen peroxide and
> describes a different reaction altogether.

### Check yourself — §3.8

1. In 2H₂ + O₂ → 2H₂O, four molecules become two. Is mass
   conserved? Explain in one sentence.
   
2. Write what 2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g) says about
   states. 

## §3.9 • Balancing chemical equations

`ZUM §3.9`

Balancing is done **by inspection**, but inspection with a strategy:

1. Start from the *most complicated* molecule.
2. Balance elements that appear in only one place on each side first.
3. Leave lone elements (O₂, H₂, metals) for *last* —
   their coefficient can be set freely without unbalancing anything
   else.
4. Count every atom on both sides at the end. Always.

> 📘 **Worked example 4: ethanol combustion, step by step**
>
> $$ \text{C₂H₅OH(l) + O₂(g) → CO₂(g) + H₂O(g)} \qquad \text{(unbalanced)} $$
> 
> **Start with ethanol** (most complex, sets C and H):
> carbon first — 2 C on the left forces
> C₂H₅OH + O₂ → 2CO₂ + H₂O
> hydrogen next — 6 H on the left ($5+1$) forces
> C₂H₅OH + O₂ → 2CO₂ + 3H₂O
> 
> **Oxygen last**, because O₂ stands alone. The right side now has
> $2(2) + 3(1) = 7$ O; the left has 1 in the ethanol, so O₂ must supply
> 6 atoms $= 3$ molecules:
> 
> $$ \boxed{\;\text{C₂H₅OH(l) + 3O₂(g) → 2CO₂(g) + 3H₂O(g)}\;} $$
> 
> **Final count:** C $2 = 2$; H $6 = 6$; O $1 + 6 = 4 + 3$. Balanced.

> 📘 **Worked example 5: when a fraction appears — hexane**
>
> C₆H₁₄(l) + O₂(g) → CO₂(g) + H₂O(g)
> C and H from the hexane: $6\,\text{CO₂}$ and $7\,\text{H₂O}$. The right side
> then carries $12 + 7 = 19$ oxygen atoms — an *odd* number, which a
> whole coefficient on O₂ cannot supply. Balance with a fraction first:
> C₆H₁₄ + tfrac{19}{2}O₂ → 6CO₂ + 7H₂O
> then clear it by doubling **every** coefficient:
> 
> $$ \boxed{\;\text{2C₆H₁₄(l) + 19O₂(g) → 12CO₂(g) + 14H₂O(g)}\;} $$
> 
> Count: C $12 = 12$; H $28 = 28$; O $38 = 24 + 14$. The doubling step must
> touch all four coefficients — doubling only the O₂ is the standard
> error.

### Check yourself — §3.9

Balance each (smallest whole coefficients):

1. Fe(s) + O₂(g) → Fe₂O₃(s)
   4Fe + 3O₂ → 2Fe₂O₃
2. C₃H₈(g) + O₂(g) → CO₂(g) + H₂O(g)
   C₃H₈ + 5O₂ → 3CO₂ + 4H₂O
3. Al(s) + HCl(aq) → AlCl₃(aq) + H₂(g)
   2Al + 6HCl → 2AlCl₃ + 3H₂
4. C₄H₁₀(g) + O₂(g) → CO₂(g) + H₂O(g)
   2C₄H₁₀ + 13O₂ → 8CO₂ + 10H₂O

## §3.10 • Stoichiometric calculations

`ZUM §3.10`

The balanced equation is a *mole-to-mole* conversion factor and
nothing more. Every mass problem is the same three moves:

> 
grams of A $\xrightarrow{\;\div M_A\;}$ moles of A
$\xrightarrow{\;\text{coefficients}\;}$ moles of B
$\xrightarrow{\;\times M_B\;}$ grams of B

> 📘 **Worked example 6: burning propane end to end**
>
> A grill burns 25.0 g of propane:
> C₃H₈(g) + 5O₂(g) → 3CO₂(g) + 4H₂O(g).
> What mass of O₂ is consumed, and what mass of CO₂ is produced?
> 
> **To moles once, at the start:**
> 
> $$ \frac{25.0}{44.09} = 0.567\,\mathrm{mol}~\text{C₃H₈} $$
> 
> **Mole ratios, straight off the coefficients:**
> 
> $$ \text{O₂}: 0.567 \times \frac{5}{1} = 2.835\,\mathrm{mol} \qquad    \text{CO₂}: 0.567 \times \frac{3}{1} = 1.701\,\mathrm{mol} $$
> 
> **Back to grams at the end:**
> 
> $$ m_{\text{O₂}} = 2.835 \times 32.00 = \mathbf{90.7~g} \qquad    m_{\text{CO₂}} = 1.701 \times 44.01 = \mathbf{74.9~g} $$
> 
> **Sanity check by conservation of mass:** reactants
> $25.0 + 90.7 = 115.7$ g; products $74.9 +$ water. Water:
> $0.567 \times 4 = 2.268$ mol $\times\, 18.02 = 40.9$ g, and
> $74.9 + 40.9 = 115.8$ g. The books balance (0.1 g is rounding). Thirty
> seconds of checking catches almost every slip in this chapter.

> 📘 **Worked example 7: working backward — iron from ore**
>
> Iron is produced in a blast furnace by
> Fe₂O₃(s) + 3CO(g) → 2Fe(l) + 3CO₂(g).
> What mass of Fe₂O₃ is required for 1.00 kg of iron?
> 
> $$ \frac{1000}{55.85} = 17.91\,\mathrm{mol}~\text{Fe}    \;\xrightarrow{\times 1/2}\; 8.953\,\mathrm{mol}~\text{Fe₂O₃}    \;\xrightarrow{\times 159.70}\; \mathbf{1.43\times10^{3}~g}    = \mathbf{1.43~kg} $$
> 
> The ratio ran “backwards” (product to reactant) with no change in
> method — the equation converts in either direction. Note the ratio is
> $\tfrac{1~\text{Fe₂O₃}}{2~\text{Fe}}$, taken *from the coefficients*,
> never from the formulas' subscripts.

### Check yourself — §3.10

1. Using worked example 6's equation, what mass of water forms when
   10.0 g of propane burns?
   *(working space)*
2. In 2Al + 3Cl₂ → 2AlCl₃, how many moles of Cl₂ react
   with 0.40 mol Al? 0.60 mol
3. A student converts 25.0 g C₃H₈ to grams of
   CO₂ by $25.0 \times \tfrac{3}{1}$. Name the two omitted
   steps. 

## §3.11 • Limiting reactant and percent
yield

`ZUM §3.11`

Real mixtures are not delivered in perfect stoichiometric ratio. Whichever
reactant runs out first — the limiting reactant — fixes how much
product can form; everything else is in excess and some of it is
left over.

**To find the limiting reactant**, convert every reactant to moles,
then pick either test:

**Required-vs-available.** Use the mole ratio to compute how
        much of B reactant A would need; compare with what is present.

**Smallest-product.** Compute the product each reactant could
        make alone; the smaller answer is the truth, and the reactant that
        produced it is limiting.

Both always agree. Use whichever reads more naturally, but *never*
compare raw masses or raw moles of the reactants — the comparison only
means anything after the coefficients are involved.

> 📘 **Worked example 8: ammonia synthesis, complete**
>
> 50.0 g of N₂ is mixed with 15.0 g of H₂:
> N₂(g) + 3H₂(g) → 2NH₃(g). Find the limiting reactant, the
> theoretical yield of NH₃, and the mass of the excess reactant left
> over.
> 
> **Everything to moles first:**
> 
> $$ \text{N₂}: \frac{50.0}{28.02} = 1.784\,\mathrm{mol} \qquad    \text{H₂}: \frac{15.0}{2.016} = 7.44\,\mathrm{mol} $$
> 
> **Test 1 (required vs available):** the N₂ present would need
> $1.784 \times 3 = 5.35\,\mathrm{mol}$ of H₂. Available: 7.44 mol —
> more than needed, so H₂ is in excess and **N₂ is
> limiting**. (Notice the raw moles pointed the other way: there is
> *more* H₂ by moles, yet N₂ still limits. The 3:1 ratio is
> what decides.)
> 
> **Theoretical yield** — from the limiting reactant only:
> 
> $$ 1.784 \times \frac{2~\text{NH₃}}{1~\text{N₂}} = 3.569\,\mathrm{mol}    \;\Rightarrow\; 3.569 \times 17.03 = \mathbf{60.8~g~\text{NH₃}} $$
> 
> **Leftover excess:** H₂ consumed $= 5.35$ mol, so
> 
> $$ 7.44 - 5.35 = 2.09\,\mathrm{mol} \;\Rightarrow\;    2.09 \times 2.016 = \mathbf{4.21~g~\text{H₂}~left} $$
> 
> **Mass check:** in $50.0 + 15.0 = 65.0$ g; out
> $60.8 + 4.21 = 65.0$ g. Balanced books again.

> 📘 **Worked example 9: percent yield**
>
> The synthesis in worked example 8 is run and 48.0 g of NH₃
> is actually collected.
> 
> $$ \%~\text{yield} = \frac{\text{actual}}{\text{theoretical}} \times 100    = \frac{48.0}{60.8} \times 100 = \mathbf{78.9\%} $$
> 
> The theoretical yield is a calculation; the actual yield is
> a measurement, and it is smaller for ordinary reasons — side reactions,
> incomplete reaction, product lost in handling. A percent yield over 100%
> is not good news: it means the product is wet or impure, or the
> bookkeeping is wrong.

> ⚠️ **AP trap**
>
> Three habits that prevent nearly every limiting-reactant error:
> theoretical yield is computed from the **limiting** reactant only,
> never from both; the leftover is
> $(\text{present}) - (\text{consumed})$, where consumed comes through the
> mole ratio; and the limiting reactant is **not** the one with fewer
> grams or fewer moles — 50.0 g of N₂ limited against
> 15.0 g of H₂ above.

### Check yourself — §3.11

5.40 g Al and 8.10 g Cl₂ react:
        2Al + 3Cl₂ → 2AlCl₃. Identify the limiting reactant and the
        theoretical yield of AlCl₃. 

*(working space)*

        

For that mixture, the mass of aluminum left over:
        

*(working space)*

        

If 9.20 g of AlCl₃ is collected, the percent
        yield (divide by the *unrounded* theoretical yield):
        90.6%

True or false, with a reason: the reactant present in the
        smaller mass is the limiting reactant.
        

> 📌 **The whole span in four sentences**
>
> A formula comes from mole ratios of elements (§3.7). A reaction is
> written as a balanced equation, using coefficients only (§3.8–3.9). The
> equation's coefficients convert moles of anything into moles of anything
> else, with grams only at the edges (§3.10). When amounts of two reactants
> are given, the mole ratio decides which one limits, and everything —
> yield and leftovers — follows from that one reactant (§3.11).

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
