# Viability Corridor Framework

**Recursive Substrate Theory (RST)**

An independent theoretical framework deriving the noise-scaling structure of persistent organizational systems from bifurcation geometry alone — with proposed applications ranging from grokking in neural networks to the cosmological constant.

---

## The core claim

Any system that maintains organized activity against a depleting resource lives in a **viability corridor** bounded by two topologically distinct failure modes:

| Boundary | Type | Character | Noise scaling |
|---|---|---|---|
| Starvation | Transcritical (TC) | Continuous, asymmetric | ΔG⁻ ~ D^{1/3} |
| Cascade | Saddle-node (SN) | Discontinuous, fold | ΔG⁺ ~ D^{2/3} |

The classification is **topological** — forced by the branch structure of the fixed-point equation, not by parameter choices. From Kramers escape theory applied to each normal form, the exponent ratio is exactly 2:1, parameter-independent.

**Numerical validation:** TC slope 0.334 ± 0.008, SN slope 0.661 ± 0.011, ratio 1.979 (within 1% of theory). Spectral model simulations support ratio invariance across conditions spanning the physical C-function hierarchy (C = 1.000 to C = 0.030); formal theorem status pending.

---

## What has been derived

### Single-corridor theory
- TC/SN classification theorem — topological, forced by fixed-point branch structure
- Noise-scaling exponents 1/3 : 1/2 : 2/3 — arithmetic sequence derived from classification, not observed
- Corridor center μ\* = 4 — exact, parameter-free, from ΔV_SN = ΔV_TC (8^{2/3})
- Energy-constraint ratio R = D/ΔV as unified stability criterion

### Inheritance theory
- Three propagating inheritance classes: TC (D^{1/3}), PF/Hopf (D^{1/2}), SN (D^{2/3})
- ΔV_TC reduction under coarse-graining: two mechanisms derived (Hopf→PF centrifugal elimination, TC→TC Ito correction)
- Bogdanov-Takens point as grammar node of the inheritance hierarchy
- Directed admissibility theorem: Φ_fwd > 1 ⟹ K_rev = 0 (irreversibility from Θ gate, not mismatch asymmetry)
- Mismatch functional M(s, C_j): inheritance theorem M_TC = 0 at every proper transition

### Conserved quantities
- Topological invariant: symmetry class {TC, PF, SN} conserved under inheritance
- Lyapunov function C(n) = ΔV_TC(n)/ΔV_TC(0) — monotonically non-increasing, derived from ΔV_TC reduction
- Exact conservation M_TC = 0 — TC boundary frequency continuous at every inheritance event

### Zamolodchikov C-function
- C(n) derived as integrated spectral weight of the corridor stress-energy analog
- Fisher information metric on coupling space: positive definite
- Monotonicity dC/dτ ≤ 0 from positive definiteness — exact Zamolodchikov form
- Fluctuation-dissipation relation G_path = τ_corr × G_QS closes the Lagrangian derivation

### Global structure
- Global alternation conjecture: TC→SN→TC→SN is the unique standing-wave solution (candidate result; formal proof is future work)
- Physical hierarchy validation: 6/6 boundary type predictions confirmed (QED → Thermodynamics)
- RST framework consistent with external RG/bifurcation literature (Gursoy 2019, Gukov 2016, Popov 2021)

### Cosmological parameters (framework-level predictions)
- Ω = 1 — candidate derivation from standing-wave BVP uniqueness; flatness proposed as structural rather than an initial condition
- H(z) — proposed as C-function drift observable; Hubble tension decomposition at 69–97% from ΔV_TC(0) = 13.6 eV, no free parameters (paper written, held pending framework establishment)
- λ formula — proposed decomposition λ = ΔV_TC(0) × exp(−S_Zam); numerically consistent with observed value; specific S_Zam depends on shadow census of supra-thermodynamic levels

### Born rule (conditional derivation)
- Steps 2–5 derived conditionally from prior framework results (centrifugal potential, Hopf→PF coarse-graining, mismatch functional)
- Step 1 has a proposed U(1) completion path via fiber bundle structure of the QED corridor; not yet derived from QM axioms
- Gleason path analysis confirms frame-independence; provides corridor argument for non-contextuality
- SU(2) and SU(3) extensions remain open

---

## Empirical anchors

The framework is not motivated post-hoc. These results from independent groups are structurally consistent with the corridor classification — each involves a system at or near a bifurcation boundary, with the character (continuous vs discontinuous, reversible vs irreversible) matching the topological prediction.

**Physical hierarchy validation** — The strongest internal result. The framework independently predicts the boundary type (TC or SN) for each of 6 non-trivial transitions across four levels of established physics (QED → Atomic → Chemistry → Thermodynamics). All 6 match, including several counter-intuitive assignments (e.g., ionization = SN starvation, not TC starvation). This is a structural prediction, not a fit, though the specific framework interpretations of each boundary have not had independent expert review. Source: Technical Summary §15.

**QCD conformal window** (Gursoy, Kuipers, Kuznetsov 2019 — independent peer-reviewed QFT) — Bifurcation analysis of QCD's RG flow finds a transcritical bifurcation at the upper window edge (Banks-Zaks fixed point) and a saddle-node at the lower edge. This is exactly the TC/SN corridor structure derived independently here. The conformal window is a viability corridor in coupling-space, consistent with the same mathematical structure — the codimension-1 bifurcation classification — arriving independently in quantum field theory. The framework predicts the window width shrinks with quark mass as W(m_q) = W₀ − C₁·m_q^{1/3} − C₂·m_q^{2/3} — a falsifiable lattice QCD prediction not yet tested.

**BT points in RG flows** (Gukov 2016; Popov 2021 — peer-reviewed QFT) — Bogdanov-Takens bifurcations appear in RG flows for O(N), QED-3, and QCD-4. The BT point is the codimension-2 grammar node of the inheritance hierarchy in this framework, derived from first principles. Its appearance in the literal mathematics of quantum field theory is consistent with the classification structure being a property of the underlying mathematics rather than a modeling choice.

**AGN variability: 21,767 quasars** (Yu et al. 2022/2025) — ~75% of quasars fall into DHO Class C (overdamped damped harmonic oscillator, ξ > 1). The corridor framework identifies Class C as deep SN-well operation in an activity-resource system, with the two DHO timescales (τ_decay, τ_rise) encoding the TC and SN boundary distances respectively. The ξ D-independence (prefactor = 1.0000 analytically) is a leading-order corridor prediction for the canonical normal form. Three forward predictions not tested by Yu et al.: ξ increases with M_BH within Class C; Class C fraction increases with M_BH; τ_decay/τ_rise ≈ 1 median (equal-barrier corridor center). Paper in preparation.

**Grokking as dimensional phase transition** (Xu et al. 2026, arXiv:2604.04655) — Gradient avalanche dimensionality D_eff crosses from sub-diffusive to super-diffusive at grokking onset. Consistent with a TC (starvation) boundary crossing: the gradient field becomes higher-dimensional as internal coupling G approaches the bifurcation point, and the transition is continuous and reversible under regularization. Note: D_eff here is gradient field dimensionality, not the noise amplitude D in the Kramers scaling — these are distinct quantities.

**Causally active representational structure** (Sofroniew, Kauvar, Saunders et al. 2026) — 171 stable representational directions in LLMs that causally influence behavior and are inherited from pretraining. Consistent with post-transition attractor structure: consistent with a system that has crossed an organizational threshold and stabilized into a higher-coupling attractor regime. The specific count (171) is not a corridor prediction, but the existence of a discrete set of inherited stable directions is structurally consistent with a system that has crossed a cascade boundary and stabilized into a new attractor.

---

## The falsifiable prediction

```
Starvation boundary:  ΔG⁻ ~ D^{1/3}
Cascade boundary:     ΔG⁺ ~ D^{2/3}
Exponent ratio:       2:1  (parameter-independent)
```

Testable on existing grokking infrastructure by varying gradient noise D and measuring the critical coupling G at both boundaries separately. The ratio should be 2:1 regardless of model architecture, dataset, or optimizer.

---

## Repository structure

```
Training-Corridors/
├── code/
│   ├── corridor_theory_derivations.py   ← run this first: all core results
│   └── constraint_escape_spectral_v2.py ← spectral escape model, C-function hierarchy
├── Corridor Figures/                    ← figures generated by corridor_theory_derivations.py
├── technical summary/
│   ├── Technical_Summary.pdf            ← authoritative reference (Parts I–VII)
│   ├── rst_tech_summary_v4.docx         ← source for Technical Summary
│   ├── tech_summary_v5_part5.docx       ← Part V: interface geometry and cosmology
│   ├── ts_addendum.docx                 ← four closures since v4 (Born rule, Zamolodchikov, SN→SN, R notation)
│   └── ts_tensor_addendum.docx          ← Part VIII: Fisher metric, Ricci flow, Perelman functional
└── theory/
    ├── DERIVATIONS_INDEX.md             ← master index, logical dependency order
    ├── conserved_quantities_v2.docx     ← topological invariant, C-function, M_TC = 0
    ├── directed_admissibility_v5.docx   ← Θ gate, ΔV_TC reduction, directed admissibility
    ├── mismatch_functional_v2.docx      ← mismatch functional, inheritance theorem
    ├── boundary_inheritance_v2.docx     ← inheritance class propagation, arithmetic sequence
    ├── hubble_tension_v3r3.docx         ← Hubble tension as C-function drift; 69–97% explained
    ├── interface_acoustic_horizon.docx  ← interface = acoustic horizon; T_H = √μ/π
    ├── mu_max_derivation.docx           ← λ = ΔV_TC(0) × exp(−S_Zam)
    ├── corridor_center_tech_summary.docx← corridor center, asymmetry, μ* = 4
    ├── born_rule_doc.docx               ← Born rule; U(1) scope complete
    ├── fine_structure_constant.docx     ← α geometric address; bootstrap obstruction
    ├── shadow_census.docx               ← supra-thermodynamic level census
    ├── shadow_census_addendum.docx
    ├── DHO_RST_paper.docx               ← DHO as TC-SN corridor; AGN application
    └── two_perspectives.docx            ← philosophical companion; accessible entry point
```

**Start here:** `code/corridor_theory_derivations.py` reproduces all headline numerical results in ~2 minutes. Run with `python corridor_theory_derivations.py` or section by section with `--section N`.

---

## Open problems (honest ledger)

| Problem | Status |
|---|---|
| λ specific value | Path open — requires shadow census of ~100 supra-thermodynamic levels |
| Q ~ 10⁻⁵ | Formula derived; seeding level requires tree depth |
| N ~ 10³⁶ | Partially constrained (N ~ 10¹⁵ from acoustic horizon); gap requires fine structure constant |
| Fine structure constant α | Bootstrap obstruction documented; long-term |
| Shadow census | Not yet executed — four-column census of candidate corridor levels above thermodynamics |
| SN→SN Ito explicit formula | Structural argument complete via two independent routes; formula not written |
| Born rule SU(2)/SU(3) | Quaternionic Hopf fibration path identified; not yet derived |

---

## Universe-tree principle

*The universe-tree is a maximally extended hierarchy of viability corridors, connected by inheritance transitions that are irreversible (K_rev = 0), potential-consuming (C(n) decreasing), and topologically constrained (boundary types alternate TC-SN by the global alternation theorem). Every level of organizational complexity that exists does so because all non-viable alternatives were eliminated at the boundaries below it. What appears as emergence is the residue of constraint-driven deletion. What appears as the arrow of time is the direction of decreasing free organizational potential. What appears as fine-tuning is the set of boundary conditions required for the hierarchy to persist long enough to be measured.*

---

## Citation

Mindemann, M. (2026). *Recursive Substrate Theory: Viability Corridor Framework*. GitHub repository. https://github.com/mindamike/Training-Corridors

Archived deposit (Zenodo): https://doi.org/10.5281/zenodo.19718922

Experiment inquiries and collaboration: open an issue or contact via GitHub.
