# Recursive Substrate Theory
## Viability Corridor Framework

**An independent theoretical framework unifying organizational dynamics across scales — from grokking in neural networks to the cosmological constant — via a single bifurcation-theoretic substrate.**

---

## The core claim

Any persistent system maintaining organized activity against a depleting resource lives in a *viability corridor* bounded by two structurally distinct failure modes:

- **Starvation boundary** (transcritical bifurcation, TC): activity collapses to zero when coupling falls below threshold. Continuous, asymmetric.
- **Cascade boundary** (saddle-node bifurcation, SN): activity explodes or reorganizes discontinuously when coupling exceeds threshold. Discontinuous, fold character.

This classification is **topological** — forced by the branch structure of the fixed-point equation, not by parameter choices. No model adjustment can convert a TC boundary into an SN boundary or vice versa.

From Kramers escape theory applied to each boundary type, the noise-scaling exponents are:

| Boundary | Barrier height | Exponent | Scaling |
|---|---|---|---|
| Starvation (TC) | ΔV⁻ ~ μ³ | 1/3 | ΔG⁻ ~ D^{1/3} |
| Cascade (SN) | ΔV⁺ ~ μ^{3/2} | 2/3 | ΔG⁺ ~ D^{2/3} |

**The 2:1 exponent ratio is parameter-independent, derivable from normal form geometry, and falsifiable on existing infrastructure.**

---

## Empirical anchors

Three recent results from independent groups are argued to be the same class of event — corridor-boundary crossings — seen from different measurement angles:

**Grokking as dimensional phase transition** (Xu et al. 2026, arXiv:2604.04655): the gradient avalanche dimensionality D crosses from sub-diffusive (D < 1) to super-diffusive (D > 1) at grokking onset — the starvation boundary, measured in gradient geometry.

**Mythos-class capability jumps** (Carlini et al. 2026): a 90-fold improvement in autonomous exploit generation in a single model generation, unrequested by training — consistent with a cascade boundary crossing, where a new attractor set becomes accessible.

**Causally active emotion vectors** (Sofroniew, Kauvar, Saunders et al. 2026): 171 stable representational directions that causally influence behavior, inherited from pretraining — post-transition attractor structures that become stable because G is high enough to sustain cross-layer coherence.

---

## What has been derived

The framework has grown substantially beyond the training corridors application. The following results are fully established with sources in this repository:

**Single-corridor theory**
- TC/SN classification theorem (topological, forced by fixed-point branch structure)
- Noise-scaling exponents 1/3 : 1/2 : 2/3 (arithmetic sequence derived from classification, not observed)
- Corridor center μ* = 4 (D-independent for TC/SN; drifts with D for PF/SN — falsifiable prediction)
- Energy-constraint ratio R = D/ΔV as unified stability criterion

**Inheritance theory**
- Three propagating inheritance classes: TC (D^{1/3}), PF/Hopf (D^{1/2}), SN (D^{2/3})
- DV_TC reduction under coarse-graining: two mechanisms derived (Hopf→PF centrifugal, TC→TC Ito)
- Bogdanov-Takens point as grammar node of the hierarchy
- Directed admissibility theorem: Φ_fwd > 1 ⟹ K_rev = 0 (irreversibility from Θ gate, not mismatch asymmetry)
- Mismatch functional M(s, C_j): inheritance theorem M_TC = 0 at every proper transition

**Conserved quantities**
- Topological invariant: symmetry class {TC, PF, SN} conserved under inheritance
- Lyapunov function C(n) = ΔV_TC(n)/ΔV_TC(0): monotonically non-increasing, derived from DV_TC reduction
- Exact conservation M_TC = 0: TC boundary frequency continuous at every inheritance event

**Zamolodchikov C-function**
- C(n) derived as integrated spectral weight of the corridor stress-energy analog
- Fisher information metric on coupling space: positive definite, eigenvalues [9.75, 3279.9]
- Monotonicity dC/dτ ≤ 0 from positive definiteness — exact Zamolodchikov form
- Fluctuation-dissipation relation G_path = τ_corr × G_QS closes the Lagrangian derivation

**Global structure**
- Global alternation theorem: TC→SN→TC→SN is the unique standing-wave solution
- Physical hierarchy validation: 6/6 boundary type predictions confirmed (QED to Thermodynamics)
- RST-RG correspondence confirmed externally (Gursoy 2019, Gukov 2016, Popov 2021)

**Interface geometry**
- Interface = SN ceiling (from alternation + directed admissibility, no additional assumptions)
- Acoustic horizon identification: SN unstable fixed point x_b = −√μ IS the acoustic horizon; T_H = √μ/π (exact)
- Δ = 3 from transversality: BT codimension-2 + junction condition gives lower bound; Ehrenfest-Tangherlini gives upper bound
- Interface temperature: T_H(n_max) = 1.16 × 10⁻¹¹ K (exact given observed λ)

**Cosmological parameters**
- Ω = 1: from standing-wave BVP uniqueness (flatness is a structural requirement, not initial condition)
- H(z): C-function drift observable; Hubble tension explained at 69–97% from DV_TC(0) = 13.6 eV, no free parameters
- λ formula: λ = DV_TC(0) × exp(−S_Zam) where S_Zam is the total Zamolodchikov action of the universe-tree
- λ interpretation: cosmological constant = hydrogen ionization energy depleted by ~100 levels of organizational coarse-graining

**Spectral model (simulation)**
- Ito-calibrated kappa values: κ_L2 = 1.869, κ_L3 = 5.993 (from direct bisection of R(κ) = C_target)
- 2:1 ratio confirmed across 36 conditions spanning full physical C-function hierarchy (C = 1.000 to C = 0.030)
- Ratio invariance: 2.000 ± 0.010 across all κ and τ values tested

**Born rule (conditional)**
- Steps 2–5 solid; Step 1 now derived for U(1) scope via fiber bundle structure of QED corridor
- Quantum superposition = Hopf state; measurement = Hopf→PF coarse-graining (SO(2) averaging)
- Gleason path analysis: confirms frame-independence, provides corridor derivation of non-contextuality
- SU(2) and SU(3) extensions remain open

---

## Open problems (honest ledger)

| Problem | Status | Path |
|---|---|---|
| λ specific value | Path open | Requires shadow census of ~100 supra-thermodynamic levels |
| Q ~ 10⁻⁵ | Path open | Formula derived; seeding level requires tree depth |
| N ~ 10³⁶ | Partially constrained (10¹⁵ from horizon) | Gap to 10³⁶ requires fine structure constant derivation |
| Fine structure constant α | Bootstrap obstruction documented | Long-term; emerges from C-function ratio constraint |
| Shadow census | Not yet executed | Four-column census of candidate corridor levels above thermodynamics |
| SN→SN Ito explicit formula | Structural argument complete; formula not written | Tractable; two independent routes already establish the result |

---

## Repository contents

**Primary documents**
- `Technical_Summary.pdf` — authoritative reference through v4; Part V (interface geometry) written, pending merge
- `Training_Corridors.docx` — full paper (~30k words), Parts 1–5 written
- `corridor_center_tech_summary.docx` — corridor center, asymmetry parameter, Hubble tension connection

**Working derivations** (each self-contained with derivation status)
- `conserved_quantities_v2.docx` — topological invariant, C-function, M_TC = 0
- `directed_admissibility_v5.docx` — Θ gate, DV_TC reduction, directed admissibility theorem
- `mismatch_functional_v2.docx` — mismatch functional, inheritance theorem, harmonic selection
- `boundary_inheritance_v2.docx` — inheritance class propagation, arithmetic sequence derivation
- `hubble_tension_v3r3.docx` — Hubble tension as C-function drift; 69–97% explanation
- `interface_acoustic_horizon.docx` — interface = acoustic horizon; T_H = √μ/π; derivation paths for λ, Q, N
- `mu_max_derivation.docx` — λ = DV_TC(0) × exp(−S_Zam); Zamolodchikov action of universe-tree
- `born_rule_doc.docx` — Born rule derivation; U(1) scope complete; SU(2) open
- `fine_structure_constant.docx` — α geometric address; bootstrap obstruction documented
- `two_perspectives.docx` — dual framing: organizational and geometric perspectives

**Code**
- `constraint_escape_spectral_v2.py` — Ito-calibrated spectral escape model; reproduces C-function hierarchy

---

## The quantitative prediction (primary falsifiable claim)

The two boundary types generate different noise-scaling laws:

```
Starvation boundary:  ΔG⁻ ~ D^{1/3}
Cascade boundary:     ΔG⁺ ~ D^{2/3}
Exponent ratio:       2:1  (parameter-independent)
```

This is testable on existing grokking infrastructure by varying gradient noise D and measuring the critical coupling G at both boundaries separately. The ratio should be 2:1 regardless of model architecture, dataset, or optimizer.

Numerical validation (1D normal forms): TC slope 0.334 ± 0.008, SN slope 0.661 ± 0.011, ratio 1.979.

Spectral model validation across C-function hierarchy: ratio 2.000 ± 0.010 across all 36 tested conditions.

---

## Universe-tree principle

*"The universe-tree is a maximally extended hierarchy of viability corridors, connected by inheritance transitions that are irreversible (K_rev = 0), potential-consuming (C(n) decreasing), and topologically constrained (boundary types alternate TC-SN by the global alternation theorem). Every level of organizational complexity that exists does so because all non-viable alternatives were eliminated at the boundaries below it. What appears as emergence is the residue of constraint-driven deletion. What appears as the arrow of time is the direction of decreasing free organizational potential. What appears as fine-tuning is the set of boundary conditions required for the hierarchy to persist long enough to be measured."*

---

## Citation

Mindemann, M. (2026). *Recursive Substrate Theory: Viability Corridor Framework*. GitHub repository. https://github.com/mindamike/Training-Corridors

For the archived deposit with DOI: (https://doi.org/10.5281/zenodo.19718922)

---

*Experiment inquiries and collaboration: open an issue or contact via GitHub.*
