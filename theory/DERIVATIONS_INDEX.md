# Derivations Index
## Recursive Substrate Theory — Complete Document Record

This index covers every document in the repository with a one-line description,
derivation status, and what each one proves or establishes.
Read the README first for the overall framework. This index is the map to the detail.

**Status codes:**
- ✓ PROVED — derived from first principles, no remaining gaps
- ~ STRUCTURAL — correctly derived in structure; specific values require empirical input
- → PATH OPEN — formula or approach established; evaluation requires additional work
- ✗ OPEN — genuine gap; requires new machinery or data

---

## /technical_summary/ — Primary Reference Documents

| File | What it covers | Status |
|---|---|---|
| `Technical_Summary.pdf` | Authoritative reference through v4. Parts I–VII: single-corridor theory, inheritance, conserved quantities, Zamolodchikov C-function, global structure, applications, open problems. Start here. | ✓ Parts I–IV; ~ Parts V–VII |
| `rst_tech_summary_v4.docx` | Source document for the PDF above. Same content, editable. | ✓ / ~ same as above |
| `tech_summary_v5_part5.docx` | Part V: Interface geometry and cosmology. Interface = acoustic horizon (Theorem 17.1), T_H = √μ/π exact, Δ=3 transversality proof, Ω=1, H(z), λ formula, Q and N derivation paths. | ✓ Δ=3, Ω=1, H(z); → λ value, Q, N |
| `ts_addendum.docx` | Four closures since v4: Born rule Step 1 derived for U(1); Zamolodchikov formal gap closed via FDT; SN→SN confirmed; R=D/ΔV notation adopted. | ✓ all four |
| `ts_tensor_addendum.docx` | Part VIII: Full tensor framework. Analytic Fisher metric, Ricci flow, Perelman F-functional, finite-time singularity, C-theorem as Ricci trace, Israel junction conditions, directed admissibility as Penrose energy condition. | ✓ structural; ~ specific values |

---

## /theory/ — Working Derivation Documents

Listed in logical dependency order — each document builds on the ones above it.

| File | What it proves | Status |
|---|---|---|
| `boundary_inheritance_v2.docx` | Three propagating inheritance classes (TC, PF/Hopf, SN) and the arithmetic sequence of exponents 1/3 : 1/2 : 2/3. Hopf coarse-grains to PF under SO(2) averaging. Bogdanov-Takens point as the grammar node of the hierarchy. | ✓ |
| `conserved_quantities_v2.docx` | Three conserved objects: topological invariant (boundary class), Lyapunov function C(n) = ΔV_TC(n)/ΔV_TC(0), and exact conservation M_TC = 0. TC→TC Ito correction derived. Arithmetic sequence proved from classification theorem. | ✓ |
| `directed_admissibility_v5.docx` | Directed admissibility theorem proved unconditionally: Φ_fwd > 1 ⟹ K_rev = 0. Θ gate derived from Kramers. DV_TC reduction via Hopf→PF centrifugal and TC→TC Ito both established. | ✓ |
| `mismatch_functional_v2.docx` | Mismatch functional M(s_n, C_j) derived. Inheritance theorem M_TC = 0 proved. Harmonic selection: low-order rational ratio_SN values exponentially preferred. Physical hierarchy values confirmed. | ✓ |
| `corridor_center_tech_summary.docx` | Corridor center μ*=4 and D-independence derived. Asymmetry parameter Λ=Γρ. Recursive inheritance and self-similarity. Hubble tension as Λ. Complete results table. | ✓ |
| `two_perspectives.docx` | Dual framing: organizational (corridors, inheritance, C-function) and geometric (Fisher manifold, Ricci flow, interface). Shows these are dual descriptions of the same structure. Free/bound potential accounting. | ✓ |
| `conserved_quantities_v2.docx` | See above — also contains the Zamolodchikov C-function formal derivation including the two-point function G_T(r) = μ²·exp(−r·μ) and spectral positivity proof. | ✓ |
| `hubble_tension_v3r3.docx` | H(z) identified as C-function drift observable. Three contributions from the Saha ionization correction (kinematic void bias, Buchert backreaction, dark energy transition) sum to 69–97% of the observed Hubble tension gap from DV_TC(0) = 13.6 eV. No free parameters. | ✓ structural; ~ 69–97% range |
| `interface_acoustic_horizon.docx` | SN unstable fixed point x_b = −√μ identified as acoustic horizon exactly (Theorem 17.1). Surface gravity κ_sg = 2√μ. Hawking temperature T_H = √μ/π. Two-point function = Hawking propagator. Interface temperature T_H(n_max) = 1.16 × 10⁻¹¹ K derived from observed λ. | ✓ |
| `mu_max_derivation.docx` | Three closing conditions for μ_max ruled out (all give O(1), not 10⁻³²). Main result: λ = DV_TC(0) × exp(−S_Zam) where S_Zam is the Zamolodchikov action of the universe-tree. S_Zam = 218 required; consistent with ~100 levels at L2→L3 rate. Cosmological constant = hydrogen ionization energy depleted by organizational coarse-graining. | ~ formula proved; → value requires shadow census |
| `born_rule_doc.docx` | Five-step Born rule derivation. Steps 2–5 solid. Step 1 now derived for U(1) scope via QED fiber bundle structure. Quantum superposition = Hopf state; measurement = SO(2) averaging. Gleason path confirms frame-independence. | ✓ U(1); ✗ SU(2), SU(3) |
| `fine_structure_constant.docx` | α geometric address identified: α = sqrt(2·DV_TC/DV_SN) at QED level. Bootstrap obstruction documented: virial theorem fixes D independently, preventing closed-form derivation. Long-term open problem. | → path identified; ✗ derivation blocked |
| `rst_references.docx` | Complete reference record: all external confirmations, internal documents, pending publications, open problems ledger, and Zenodo deposit manifest. The bibliography for all papers in the pipeline. | Living document |

---

## /code/ — Simulation and Derivation Code

| File | What it does | Key result |
|---|---|---|
| `constraint_escape_spectral_v2.py` | Ito-calibrated spectral escape model. Kappa values from direct bisection of R(κ) = C_target (corrects v1 approximation off by ~14×). Sweeps physical C-function hierarchy from L0/L1 (C=1.000) through L2 Chemistry (C=0.265) to L3 Thermodynamics (C=0.030). | 2:1 ratio confirmed: 2.000 ± 0.010 across all 36 conditions. |

---

## Root Level

| File | What it is |
|---|---|
| `README.md` | Start here. Overview of the framework, all derived results, open problems, and repo navigation. |
| `Training Corridors.docx` | The primary paper. Parts 1–5 written (~30k words). TC/SN classification, training dynamics application, three empirical anchors (Xu 2026, Carlini 2026, Sofroniew 2026), 2:1 prediction. |
| `LICENSE` | MIT. Use freely, attribute. |
| `Corridor Figures/` | Figures for the Training Corridors paper. |

---

## Reading order for a new arrival

**If you work in ML / AI safety:**
README → Training Corridors.docx → Technical_Summary.pdf Parts I–III → constraint_escape_spectral_v2.py

**If you work in physics / dynamical systems:**
README → Technical_Summary.pdf → interface_acoustic_horizon.docx → mu_max_derivation.docx → hubble_tension_v3r3.docx

**If you work in industrial condition monitoring / fault detection:**
README → boundary_inheritance_v2.docx → conserved_quantities_v2.docx → constraint_escape_spectral_v2.py → ts_addendum.docx

**If you want the full derivation chain:**
boundary_inheritance → conserved_quantities → directed_admissibility → mismatch_functional → corridor_center → two_perspectives → interface_acoustic_horizon → mu_max_derivation

---

*DOI: 10.5281/zenodo.19718922 | Mindemann, M. | April 2026 | MIT License*
*Living document — updated when new derivations are added or open problems are closed.*
