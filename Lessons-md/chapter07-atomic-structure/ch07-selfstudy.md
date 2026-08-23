# Self-Study • Chapter 7, I do / You do

*Chapter 7 • Atomic Structure and Periodicity*  
Zumdahl §7.1–7.13 • PDF pp. 331–390 • four YOUR TURN questions per ladder

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
> **The one sentence this chapter is built on.** Every property in
> Ladders 5–8 — orbital energy, ionization energy, atomic radius,
> electronegativity — is decided by **Coulomb's law**: how strongly
> the nucleus pulls on an electron, which depends on the nuclear charge,
> the distance, and how much shielding sits in between. If you can say
> those three things about any electron, you can predict every trend
> without memorizing a single arrow.
> 
> **Constants:** $c = 3.00e8\,\mathrm{m/s}$,
> $h = 6.626e-34\,\mathrm{J\cdot s}$,
> $N_A = 6.022e23\,\mathrm{/mol}$.

## Ladder 1 • Wavelength, frequency, energy

`ZUM §7.1–7.2`

$$ c = \lambda\nu \qquad E = h\nu = \frac{hc}{\lambda} $$

Read the second equation as a sentence: **short wavelength means
high frequency means high energy**. Gamma rays sit at one end, radio waves
at the other, and visible light occupies a narrow band from about
400 nm (violet) to 700 nm (red).

A photon's energy is per *photon*. Multiply by $N_A$ to reach the
per-*mole* figures chemists quote.

> 📘 **I do: one photon, three quantities**
>
> Green light has a wavelength of 525 nm. Find its
> frequency, the energy of one photon, and the energy per mole.
> 
> **Metres first — always convert before substituting:**
> 
> $$ 525~\text{nm} = 5.25e-7\,\mathrm{m} $$
> 
> **Frequency:**
> 
> $$ \nu = \frac{c}{\lambda} = \frac{3.00\times10^{8}}{5.25\times10^{-7}}    = 5.71e14\,\mathrm{/s} $$
> 
> **Energy per photon:**
> 
> $$ E = h\nu = (6.626\times10^{-34})(5.71\times10^{14})    = 3.78e-19\,\mathrm{J} $$
> 
> **Per mole:**
> 
> $$ (3.78\times10^{-19})(6.022\times10^{23})    = 2.28e5\,\mathrm{J/mol} = 228\,\mathrm{kJ/mol} $$
> 
> **Two sense checks worth thirty seconds.** A single photon carries
> around $10^{-19}$ J — if your answer is $10^{-30}$ or $10^{-5}$, a
> conversion went wrong. And a mole of visible photons carries a couple of
> hundred kJ, comparable to a chemical bond energy, which is precisely why
> visible light can drive chemistry.

> ✏️ **YOUR TURN 1 — four questions**
>
> 1. Frequency of light with $\lambda = 650\,\mathrm{nm}$:
>    *(working space)*
> 2. Energy of one photon of that light: 
>    *(working space)*
> 3. Wavelength, in nm, of a photon carrying
>    4.50e-19 J:
>    *(working space)*
> 4. Which has more energy per photon, a 200 nm
>    ultraviolet photon or a 700 nm red one? Answer
>    without calculating.
>    *(working space)*
> 
> > **check:** (a) 4.62e14 /s     (b)
> 3.06e-19 J     (c) 442 nm     (d) the
> ultraviolet one — shorter wavelength

## Ladder 2 • The photoelectric effect

`ZUM §7.2`

Shine light on a metal and electrons are ejected — but only if the
light's **frequency** exceeds a threshold. Brighter light below that
threshold ejects nothing, however long you wait.

That single observation is what forced the particle picture. A wave would
let energy accumulate, so any colour should eventually work. A stream of
photons would not: one photon hits one electron, and if that photon is
too weak, nothing happens no matter how many arrive.

$$ E_{\text{photon}} = \Phi + \mathrm{KE}_{\text{electron}} $$

where $\Phi$ (the work function) is the minimum energy to free an
electron. Energy above the work function becomes kinetic energy.

> 📘 **I do: reading the energy budget**
>
> A metal has a work function of 3.20e-19 J. Light of
> wavelength 400. nm strikes it.
> 
> **Photon energy:**
> 
> $$ E = \frac{hc}{\lambda}    = \frac{(6.626\times10^{-34})(3.00\times10^{8})}{4.00\times10^{-7}}    = 4.97e-19\,\mathrm{J} $$
> 
> **Is it above the threshold?** $4.97 > 3.20$, so yes — electrons
> are ejected.
> 
> **Kinetic energy of each ejected electron:**
> 
> $$ \mathrm{KE} = 4.97\times10^{-19} - 3.20\times10^{-19}    = 1.77e-19\,\mathrm{J} $$
> 
> **Now the conceptual half.** What if we doubled the
> *intensity* at the same wavelength? Twice as many photons arrive, so
> twice as many electrons are ejected — but each still receives exactly
> one photon's worth of energy, so the kinetic energy per electron is
> **unchanged**. Intensity controls how many; frequency controls how
> energetic. Confusing those two is the classic error here.

> ✏️ **YOUR TURN 2 — four questions**
>
> A metal has work function 4.00e-19 J.
> 
> 1. Energy of a 450 nm photon: 
>    *(working space)*
> 2. Are electrons ejected, and if so with what kinetic energy?
>    *(working space)*
> 3. What is the longest wavelength that will eject any electron from
>    this metal?
>    *(working space)*
> 4. Very intense 600 nm light is shone on the metal
>    for an hour. Predict what happens, and why.
>    *(working space)*
> 
> > **check:** (a) 4.42e-19 J     (b) yes, KE $=$
> 4.2e-20 J     (c) 497 nm     (d) nothing
> — each photon is below the work function

## Ladder 3 • Line spectra and the Bohr model

`ZUM §7.3–7.4`

Heat hydrogen and it emits only *certain* wavelengths — a line
spectrum, not a continuous rainbow. That is the direct evidence that
electron energies are **quantized**: an electron can occupy only
allowed levels, and a photon is emitted with exactly the energy of the
gap it falls across.

For hydrogen only:

$$ E_n = -2.178\times10^{-18}\left(\frac{1}{n^{2}}\right)~\text{J}    \qquad    \Delta E = E_{\text{final}} - E_{\text{initial}} $$

The negative sign means bound. $n = \infty$ is zero energy — the
electron just barely free — so every bound level lies below it.

> 📘 **I do: an emission line, end to end**
>
> Find the wavelength emitted when a hydrogen electron falls from
> $n = 4$ to $n = 2$.
> 
> **The two levels:**
> 
> $$ E_4 = \frac{-2.178\times10^{-18}}{16} = -1.361e-19\,\mathrm{J}    \qquad    E_2 = \frac{-2.178\times10^{-18}}{4} = -5.445e-19\,\mathrm{J} $$
> 
> **The change:**
> 
> $$ \Delta E = E_2 - E_4 = -5.445\times10^{-19} - (-1.361\times10^{-19})    = -4.084e-19\,\mathrm{J} $$
> 
> Negative because the atom *lost* energy. The photon carries that
> energy away, so use its magnitude:
> 
> $$ \lambda = \frac{hc}{|\Delta E|}    = \frac{(6.626\times10^{-34})(3.00\times10^{8})}{4.084\times10^{-19}}    = 4.87\times10^{-7}~\text{m} = \mathbf{487~nm} $$
> 
> **Check against reality:** 487 nm is blue-green, and the
> $4 \to 2$ line is indeed one of the visible hydrogen lines. Any
> transition ending at $n = 2$ lands in or near the visible; those ending
> at $n = 1$ are far more energetic and fall in the ultraviolet.

> ✏️ **YOUR TURN 3 — four questions**
>
> 1. Energy of the $n = 3$ level in hydrogen: 
>    *(working space)*
> 2. $\Delta E$ for an electron falling from $n = 3$ to $n = 2$:
>    *(working space)*
> 3. Wavelength of the photon emitted in (b): 
>    *(working space)*
> 4. Is energy absorbed or emitted for $n = 1 \to n = 3$, and how do
>    you know from the sign?
>    *(working space)*
> 
> > **check:** (a) -2.420e-19 J     (b)
> -3.025e-19 J     (c) 657 nm    
> (d) absorbed — $\Delta E$ is positive

## Ladder 4 • Quantum numbers

`ZUM §7.6–7.8`

Four numbers address one electron, and each answers a different question.

| **Symbol** | **Name** | **Allowed values** | **What it fixes** |
|---|---|---|---|
| $n$ | principal | $1, 2, 3, \ldots$ | shell; size and energy |
| $\ell$ | angular momentum | $0$ to $n-1$ | subshell shape
  ($0=s$, $1=p$, $2=d$, $3=f$) |
| $m_\ell$ | magnetic | $-\ell$ to $+\ell$ | which orbital, i.e.\
  orientation |
| $m_s$ | spin | $+\tfrac{1}{2}$ or $-\tfrac{1}{2}$ | which of the two
  electrons |

The Pauli exclusion principle says no two electrons in an atom
share all four — which is exactly why an orbital holds two electrons
and no more.

> 📘 **I do: counting, then judging legality**
>
> **(a) How many orbitals are in the $n = 3$ shell, and how many
> electrons can it hold?**
> 
> $\ell$ runs $0, 1, 2$ — so $3s$, $3p$, $3d$. Counting orbitals by
> $m_\ell$: $s$ has 1, $p$ has 3, $d$ has 5, total $\mathbf{9}$ orbitals.
> Two electrons each gives $\mathbf{18}$ — and $2n^{2} = 2(9) = 18$
> confirms it.
> 
> **(b) Is $n = 2$, $\ell = 2$ legal?** No. $\ell$ may run only to
> $n - 1 = 1$, so there is no $2d$ subshell — the first $d$ subshell is
> $3d$.
> 
> **(c) Is $n = 3$, $\ell = 1$, $m_\ell = -2$ legal?** No. With
> $\ell = 1$, $m_\ell$ is limited to $-1, 0, +1$; the value $-2$ lies
> outside that range.
> 
> **The procedure:** check the numbers *in order*. $\ell$ is
> constrained by $n$, and $m_\ell$ is constrained by $\ell$ — so an
> illegal set usually breaks at the first constraint you test.

> ✏️ **YOUR TURN 4 — four questions**
>
> 1. How many orbitals and how many electrons in the $n = 4$ shell?
>    *(working space)*
> 2. Which subshell is $n = 4$, $\ell = 2$, and how many orbitals does
>    it contain?
>    *(working space)*
> 3. Is $n = 2$, $\ell = 1$, $m_\ell = 0$,
>    $m_s = +\tfrac{1}{2}$ a legal set?
>    *(working space)*
> 4. Explain, using the Pauli principle, why an orbital holds at most
>    two electrons.
>    *(working space)*
> 
> > **check:** (a) 16 orbitals, 32 electrons     (b) $4d$, 5 orbitals
>     (c) yes     (d) only two $m_s$ values exist, so a third electron
> would duplicate all four numbers

## Ladder 5 • Electron configurations

`ZUM §7.11`

Fill in order of increasing energy, obeying three rules:

- Aufbau: lowest-energy subshell first.
- Pauli: two electrons per orbital, opposite spins.
- Hund: within a subshell, occupy every orbital singly
   before pairing — electrons repel, so they spread out first.

The periodic table *is* the filling order: read across the rows and
the blocks give you the sequence without memorizing a diagonal diagram.

> 📘 **I do: an atom, an ion, and an anomaly**
>
> **(a) Sulfur (Z = 16).**
> 
> $$ 1s^{2}\,2s^{2}\,2p^{6}\,3s^{2}\,3p^{4}    \qquad\text{or}\qquad [\text{Ne}]\,3s^{2}\,3p^{4} $$
> 
> Check the electron count: $2+2+6+2+4 = 16$. Always run that sum.
> 
> **(b) The S²⁻ ion.** Two extra electrons complete the $3p$:
> 
> $$ [\text{Ne}]\,3s^{2}\,3p^{6} = [\text{Ar}] $$
> 
> **(c) Copper (Z = 29), an anomaly.** Aufbau predicts
> $[\text{Ar}]\,4s^{2}\,3d^{9}$, but the actual configuration is
> 
> $$ [\text{Ar}]\,4s^{1}\,3d^{10} $$
> 
> A filled $d$ subshell is low enough in energy to be worth promoting one
> $4s$ electron. Chromium does the same thing for a half-filled shell:
> $[\text{Ar}]\,4s^{1}\,3d^{5}$. These two are the anomalies worth knowing.
> 
> **The trap in (b) that catches everyone:** for a transition-metal
> *cation*, electrons leave the $4s$ *before* the $3d$, even
> though $4s$ filled first. Fe²⁺ is $[\text{Ar}]\,3d^{6}$, not
> $[\text{Ar}]\,4s^{2}\,3d^{4}$.

> ✏️ **YOUR TURN 5 — four questions**
>
> 1. Write the full configuration for calcium (Z = 20).
>    *(working space)*
> 2. Write the noble-gas configuration for bromine (Z = 35).
>    *(working space)*
> 3. Write the configuration for Fe³⁺ (Fe is Z = 26).
>    *(working space)*
> 4. How many unpaired electrons does nitrogen (Z = 7) have, and
>    which rule decides it?
>    *(working space)*
> 
> > **check:** (a) $1s^{2}2s^{2}2p^{6}3s^{2}3p^{6}4s^{2}$     (b)
> $[\text{Ar}]4s^{2}3d^{10}4p^{5}$     (c) $[\text{Ar}]3d^{5}$    
> (d) three, by Hund's rule

## Ladder 6 • Photoelectron spectroscopy

`ZUM §7.9`

A PES spectrum is a direct picture of an atom's subshells. Read it with
two rules and nothing else:

> 
**Peak position** $=$ binding energy $=$ how tightly that subshell
is held.  

**Peak area (height)** $=$ *how many electrons* are in that
subshell.

> ⚠️ **AP trap**
>
> Do not confuse this with a **mass spectrum**, where height gives
> isotope *abundance*. In PES the vertical axis counts
> *electrons in a subshell*, and the ratios come out as
> $2:2:6:2:\ldots$ — exactly the subshell populations of a
> configuration.

> 📘 **I do: identifying an element from its spectrum**
>
> A PES spectrum shows peaks at 1.36, 0.10, and 0.06 MJ/mol with relative
> areas $2 : 2 : 1$.
> 
> **Read the areas as electron counts.** $2 : 2 : 1$ means 2, 2, and
> 1 electrons — five in total, so $Z = 5$: **boron**.
> 
> **Assign the peaks.** The largest binding energy belongs to the
> electrons closest to the nucleus and least shielded:
> 
> $$ 1.36 = 1s^{2} \qquad 0.10 = 2s^{2} \qquad 0.06 = 2p^{1} $$
> 
> Configuration $1s^{2}2s^{2}2p^{1}$ — boron, confirmed twice over.
> 
> **Why 1.36 is so much larger than the rest.** The $1s$ electrons
> sit closest to the $+5$ nucleus with essentially nothing between them
> and it. The $n = 2$ electrons are further out *and* shielded by
> the $1s$ pair, so the nucleus pulls on them far more weakly — a
> Coulombic argument, and the only kind that earns credit.
> 
> **And why $2s$ exceeds $2p$:** the $2s$ orbital penetrates closer
> to the nucleus, so a $2s$ electron spends more time inside the shielding
> and is held more tightly.

> ✏️ **YOUR TURN 6 — four questions**
>
> A PES spectrum shows peaks at 6.84, 0.68, 0.40 MJ/mol with relative
> areas $2 : 2 : 4$.
> 
> 1. How many electrons in total, and which element is it?
>    *(working space)*
> 2. Assign each peak to a subshell. 
>    *(working space)*
> 3. Explain, in Coulombic terms, why the 6.84 peak is so much larger
>    than the others.
>    *(working space)*
> 4. In a PES spectrum, what does peak *height* represent — and
>    what does it represent in a mass spectrum?
>    *(working space)*
> 
> > **check:** (a) 8 electrons — oxygen     (b) $1s^{2}$, $2s^{2}$,
> $2p^{4}$     (c) closest to the nucleus and unshielded    
> (d) electrons per subshell; isotope abundance

## Ladder 7 • Successive ionization energies

`ZUM §7.12`

Removing electrons one at a time gives IE$_1$, IE$_2$, IE$_3$, … —
each larger than the last, because pulling a negative electron away from
an increasingly positive ion is harder every time.

The information is in the **jump**. A sudden large increase means
the next electron had to come from a *new, inner* shell — much
closer to the nucleus and much less shielded. Count the electrons removed
before the jump and you have the number of valence electrons, hence the
group.

> 📘 **I do: identifying a group from the jumps**
>
> An element has successive ionization energies, in MJ/mol, of
> 
> $$ 0.74,\quad 1.45,\quad 7.73,\quad 10.5 $$
> 
> Which group does it belong to?
> 
> **Look at the ratios, not the differences.**
> 
> $$ \frac{1.45}{0.74} = 2.0 \qquad    \frac{7.73}{1.45} = 5.3 \qquad    \frac{10.5}{7.73} = 1.4 $$
> 
> **The jump is from IE$_2$ to IE$_3$** — a factor of more than
> five, against modest steps either side.
> 
> **Interpretation.** Two electrons came off comparatively easily;
> the third was drastically harder. So the atom has **two valence
> electrons** and is in **group 2A**. (The values are magnesium's.)
> 
> **Say why in Coulombic terms.** The first two electrons came from
> the $3s$ subshell — far from the nucleus and shielded by the $n = 1$
> and $n = 2$ electrons. The third had to come from $n = 2$: much closer
> to the nucleus and shielded only by the $1s$ pair, so the attraction to
> overcome is several times greater.
> 
> **What earns zero here:** “the ion had a full octet and wanted to
> stay stable.” That names the pattern instead of explaining it. Every
> ionization-energy explanation must cite nuclear charge, distance, or
> shielding.

> ✏️ **YOUR TURN 7 — four questions**
>
> An element has IEs, in MJ/mol, of $1.01$, $1.91$, $2.91$, $4.96$,
> $6.27$, $21.3$, $25.4$.
> 
> 1. Between which two ionizations is the large jump?
>    *(working space)*
> 2. How many valence electrons, and which group? 
>    *(working space)*
> 3. Explain the jump in Coulombic terms — no octet language.
>    *(working space)*
> 4. Why is IE$_2$ always larger than IE$_1$ for any element?
>    *(working space)*
> 
> > **check:** (a) between IE$_5$ and IE$_6$     (b) five valence
> electrons, group 5A     (c) the sixth comes from an inner shell —
> closer, less shielded     (d) removing from a more positive ion

## Ladder 8 • Periodic trends, one engine

`ZUM §7.12–7.13`

Three trends, and they all run on the same Coulombic reasoning:

| **Trend** | **Across a period ($\to$)** | **Down a group ($\downarrow$)** |
|---|---|---|
| Atomic radius | decreases | increases |
| Ionization energy | increases | decreases |
| Electronegativity | increases | decreases |

**Why, in one paragraph.** Across a period, protons are added while
electrons enter the *same* shell, so shielding barely changes: the
effective nuclear charge rises, the electrons are pulled in tighter, and
the atom shrinks while holding its electrons more strongly. Down a
group, each element adds a whole new shell: the outer electrons are much
*further* from the nucleus and shielded by every inner shell, so
they are held far more loosely.

> ⚠️ **AP trap**
>
> **The language rule for this entire chapter.** Every trend
> explanation must cite **nuclear charge, distance, or shielding**.
> Answers built on “full shells”, “octets”, or “wanting to be
> stable” describe the pattern rather than explaining it, and earn
> **zero** on this course's rubrics — however confidently they are
> written.

> 📘 **I do: comparisons, each justified Coulombically**
>
> **(a) Which has the larger radius, Na or Mg?**
> **Na**. Magnesium has one more proton pulling on electrons in
> the same $n = 3$ shell with essentially the same shielding, so its
> effective nuclear charge is higher and its electron cloud is drawn in
> tighter.
> 
> **(b) Which has the higher first ionization energy, Li or
> Cs?** **Li**. Its outer electron sits in $n = 2$, close to
> the nucleus and shielded only by the $1s$ pair. Caesium's outer electron
> is in $n = 6$, far away and shielded by five inner shells, so it is held
> weakly and easily removed — which is exactly why caesium is so
> reactive.
> 
> **(c) Which is larger, Cl or Cl-?** **Cl-**.
> The added electron does not change the nuclear charge, but it increases
> electron–electron repulsion in the valence shell, so the cloud expands.
> Anions are always larger than their parent atoms; cations are always
> smaller, for the mirror-image reason.
> 
> **Notice what none of these answers mentioned:** octets, full
> shells, or stability. Each one named a charge, a distance, or a
> shielding difference.

> ✏️ **YOUR TURN 8 — four questions**
>
> Answer each with a Coulombic justification.
> 
> 1. Larger radius: K or Br? 
>    *(working space)*
> 2. Higher first ionization energy: Ne or Na?
>    *(working space)*
> 3. Larger: Mg or Mg²⁺? 
>    *(working space)*
> 4. Na+ and F- both have 10 electrons. Which is smaller,
>    and why?
>    *(working space)*
> 
> > **check:** (a) K     (b) Ne     (c) Mg    
> (d) Na+ — more protons pulling on the same ten electrons

## Mastery tracker

Tick a row only if **all four** YOUR TURN questions were right on
the first attempt.

| **First try?** | **Skill** | **Ladder** | **If not, re-read…** |
|---|---|---|---|
| $\square$ | wavelength, frequency, energy | 1 | convert to metres first |
| $\square$ | the photoelectric effect | 2 | intensity vs. frequency |
| $\square$ | line spectra and Bohr levels | 3 | sign of $\Delta E$ |
| $\square$ | quantum numbers | 4 | check them in order |
| $\square$ | electron configurations | 5 | $4s$ leaves before $3d$ |
| $\square$ | photoelectron spectroscopy | 6 | area $=$ electron count |
| $\square$ | successive ionization energies | 7 | find the jump |
| $\square$ | periodic trends | 8 | charge, distance, shielding |

> 📌 **Scoring yourself honestly**
>
> 8/8: this chapter feeds Units 1 and 2 directly, so you are in good shape
> for both. 6–7: redo the missed ladders tomorrow, not today.
> 5 or fewer: check where the misses fall. Ladders 1–3 are
> *arithmetic* — almost always a unit conversion, usually nm to m.
> Ladders 6–8 are *explanation*, and there the failure is nearly
> always reaching for octets and stability instead of naming a nuclear
> charge, a distance, or a shielding difference. Those are two different
> problems with two different fixes; diagnose which one you have before
> redoing anything.

---

*AP Chemistry course materials • student edition • CC BY-NC-SA 4.0*
