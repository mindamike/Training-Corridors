# Recursive Substrate Theory: Axioms

Recursive Substrate Theory (RST) is a meta-dynamical framework describing how persistent structures emerge, stabilize, and fail across scales. It proposes that diverse phenomena—from neural training to nuclear decay to cosmological structure—can be understood through a common vocabulary of layered effective theories, finite pathway capacity, and structured resolution modes driven by two generic dynamics: **coherence** (constraint/localization) and **persistence** (propagation/transport).

RST does not replace standard physics (GR, QFT, ΛCDM). Instead, it provides a unifying language for why structures appear near capacity limits and predicts specific cross-scale signatures where the same low-bit constraint should recur.

---

## Core Axioms

### Axiom 1: Substrate and Conjugate Operations

At the deepest accessible layer, the substrate is energy. Two conjugate operations act on this substrate:

- **Cohere**: Localization and constraint of energy into more bound, lower-accessible-phase-space states (symmetry breaking, confinement, reduction of accessible configurations).
- **Persist**: Propagation and maintenance of correlations and influence across available degrees of freedom (transport, extension of coupling across the layer's accessible space).

These are not commands or agents, but abstracted tendencies describing how stable structure and propagation compete within physical dynamics.

**Mathematical grounding**: Coherence maps to Transcritical bifurcation boundaries; persistence maps to Saddle-Node boundaries. See *Bifurcation Structure Derivations* for formal proof.

---

### Axiom 2: Layer Generation

Effective layers arise through iterative application of the cohere–persist dynamic. The stabilized structures and constraints produced at layer N constitute the effective substrate and boundary conditions for layer N+1.

Layers are characterized by:
- Typical energy/length/time scales
- Effective degrees of freedom
- Topology of accessible phase space and pathways at that scale

**Mathematical grounding**: This is standard effective theory / renormalization group structure. RST elevates it to a unifying primitive.

---

### Axiom 3: Causal Propagation Through Pathways

Changes propagate through available structural pathways subject to the constraints of the layer.

Quantum entanglement is interpreted as persistent coherence across degrees of freedom prior to (or in the absence of) full pathway differentiation into independently localized effective states. This is a descriptive mapping: it does not alter quantum formalism, but interprets entanglement as "shared constraint structure."

---

### Axiom 4: Nontriviality Requires Initial Asymmetry

Nontrivial observable structure requires an initial asymmetry or boundary condition bias in the cohere–persist balance at the earliest accessible scales. This asymmetry selects non-degenerate structural pathways.

Without asymmetry, the theory reduces to trivial symmetry-preserving evolution with no preferred pathway selection.

**Mathematical grounding**: The 2:1 exponent ratio (Axiom 6 corollary) is the irreducible asymmetry that seeds all structure. Proved in *Constraint Escape Studies*.

---

### Axiom 5: Finite Capacity of Structural Pathways

Each layer's structural pathways have finite capacity to absorb throughput (energy flux, constraint-relevant flow) while maintaining coherent dynamics. Exceeding this capacity saturates available pathways and forces resolution via changes in effective structure and/or transfer of throughput to adjacent layers.

**Mathematical grounding**: Barrier heights in bifurcation systems scale as μ³ (TC) and μ^(3/2) (SN), creating finite escape times and capacity thresholds. Derived from Kramers escape theory.

---

### Axiom 6: Resolution Dichotomy

When a layer exceeds pathway capacity, resolution occurs through one of two modes:

1. **Emergent reconfiguration**: New stable pathways become accessible (within layer N) and/or an effective transition to a new regime (layer N+1) occurs, restoring coherent dynamics under the new constraints.

2. **Structural collapse**: Existing pathways fail; coherence at layer N is lost; throughput is transferred to adjacent layers including redistribution into degrees of freedom not previously active in the effective description.

**Mathematical grounding**: These map exactly onto bifurcation behavior: TC boundary (reconfiguration/continuity) and SN boundary (discontinuity/collapse). See *Global Alternation Theorem*.

---

### Axiom 7: Downward Collapse Cascade

If layer N saturates all viable pathways and no stable emergent reconfiguration is reachable (upward resolution fails), the system enters compulsory collapse: coherence at layer N is liquidated and throughput is released preferentially into layer N-1 (the lower substrate description).

This downward transfer can cascade across lower layers until the flux is either absorbed into stable pathways within a local system, or induces new pathway formation that restores coherent dynamics.

**Mathematical grounding**: SN well dominance (ΔV_SN / ΔV_TC ≈ 22:1 at typical operating points) means systems are trapped in SN regions; collapse cascades downward through energy redistribution across scales.

---

## Core Derived Principles

### The 2:1 Exponent Ratio (Universal Bifurcation Signature)

The noise-scaling exponents of the two primary failure modes satisfy an exact, parameter-independent ratio:

- **Transcritical exponent**: a_TC = 1/3
- **Saddle-Node exponent**: a_SN = 2/3
- **Ratio**: a_SN / a_TC = 2.0 (exactly, within measurement uncertainty)

This ratio is independent of model size, architecture, control parameters, and noise amplitude. It is a consequence of bifurcation geometry, not empirical tuning.

**Status**: Numerically confirmed to 4 decimal places across degradation systems, neural training, and nuclear physics. Analytically proved via Kramers escape law.

**Reference**: *Constraint Escape Studies* (constraint_escape_study.py); *Spectral V3 Studies* (spectral_v3_studies.py).

---

### Global Alternation Theorem

In a viability corridor bounded by two distinct bifurcation types (TC and SN), the boundary types must alternate across the hierarchy of nested effective descriptions. No adjacent pair of boundaries in the same system can both be TC or both be SN without violating structural stability.

**Consequence**: The universe-tree exhibits a forced sequence: TC-SN-TC-SN-... from quantum scales upward, which constrains which organizational levels are viable and which cannot persist.

**Status**: Derived, validated empirically in QCD conformal window, AGN Class structure (Yu et al. 2025), and cosmological hierarchy scaling.

**Reference**: *Directed Admissibility v5*; *RST Organizer v10*.

---

### Entropy Generation as Structural Necessity

Capacity of a layer (ability to sustain coherent dynamics) is fundamentally determined by its capacity to generate entropy. Systems operating at maximum entropy generation rate while maintaining coherence are at the edge of their viability corridor.

Approach to bifurcation boundaries is marked by characteristic changes in entropy production: narrowing access to microstates (approaching TC) or explosive state-space contraction (approaching SN).

**Consequence**: The organizational hierarchy is not arbitrary; it reflects the constraint topologies required to maintain entropy generation under nested resource limitations.

**Status**: Conceptual framework, grounded in bifurcation geometry and thermodynamic limits. Falsifiable via entropy production rate signatures near known phase transitions.

**Reference**: *Axioms Original Document* (Section 7, "Entropy as Organizational Principle").

---

## Scope and Falsifiability

**What RST claims:**
- Diverse phenomena across scales instantiate two generic bifurcation modes (TC and SN).
- Structure emerges at capacity limits, not in arbitrary regimes.
- Collapse cascades downward through layers with measurable energy redistribution.
- Cross-scale coherence in observed systems is evidence of low-bit boundary constraints, not noise.

**What RST does not claim:**
- New particles, forces, or violations of standard physics.
- Teleology or agency ("the universe wants X").
- That every anomaly is a sign of deep structure (many will wash out under controls).

**Critical falsifiers:**
- **F1**: Systems with measurable pathway capacity that indefinitely absorb throughput without qualitative transition.
- **F2**: Predicted low-bit constraint persistence that does not survive scale decomposition and robust null controls.
- **F3**: Collapse events with no measurable redistribution into adjacent layers or degrees of freedom.
- **F4**: Empirical failure of universality and effective theory under coarse-graining.

**What counts as supporting evidence:**
- Pre-registered statistics on known anomalies that persist under multiple controls (CMB hemispherical asymmetry, quasar coherence signatures).
- Cross-context scaling invariants (same exponent ratios across unrelated domains).
- Coherence persistence across adjacent representations (e.g., across multipole bands, across cadence-limited baselines).

See *Axioms Original Document* (Section 6, "Empirical Status") for detailed discussion of current evidence.

---

## Further Reading

- **Mathematical Foundations**: See `/technical summary/` for formal derivations of normal forms, barrier heights, and exponent ratios.
- **Applications**: See `/code/` for current state of specific implementations in training dynamics, degradation systems, nuclear physics, and cosmology.
- **Full Reasoning and Falsifiability Discussion**: See `docs/axioms_original_reasoning.docx`.

---

**Status**: Working framework, April 2026. Independent research, no institutional affiliation.
