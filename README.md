# Training Corridors

**A unified account of grokking, capability jumps, and emergent internal structure in large language models.**

---

## The claim

Training dynamics in large neural networks instantiate an *activity-resource system* governed by an effective internal coupling parameter **G**. Viable training operates within a corridor bounded by two structurally distinct failure modes — a starvation boundary (transcritical bifurcation) governing generalization onset, and a cascade boundary (saddle-node bifurcation) governing qualitative reorganization into new capability regimes. Three recent empirical phenomena are argued to be the same class of event seen from different measurement angles:

- **Grokking as dimensional phase transition** (Xu et al. 2026, arXiv:2604.04655): the gradient avalanche dimensionality D crosses from sub-diffusive (D < 1) to super-diffusive (D > 1) at grokking onset — the starvation boundary, measured in gradient geometry.
- **Mythos-class capability jumps** (Carlini et al. 2026): a 90-fold improvement in autonomous exploit generation in a single model generation, unrequested by training — consistent with a cascade boundary crossing, where a new attractor set becomes accessible.
- **Causally active emotion vectors** (Sofroniew, Kauvar, Saunders et al. 2026): 171 stable representational directions that causally influence behavior, inherited from pretraining — post-transition attractor structures that become stable because G is high enough to sustain cross-layer coherence.

---

## The quantitative prediction

The two boundary types generate different noise-scaling laws, derivable from their respective bifurcation geometries via Kramers escape theory:

![Predicted noise-scaling](Corridor%20Figures/fig4_noise_scaling.png)

| Boundary | Bifurcation class | Barrier scaling | Noise prediction |
|---|---|---|---|
| Starvation (grokking) | Transcritical | ΔV ~ μ³ | ΔG⁻ ~ D^{1/3} |
| Cascade (capability jump) | Saddle-node | ΔV ~ μ^{3/2} | ΔG⁺ ~ D^{2/3} |
| **Ratio** | | | **2:1** |

The **2:1 exponent ratio** is independent of model size, architecture, optimizer, learning rate, weight decay, and task. It follows from the bifurcation class of each boundary, not from any model-specific calculation. It is falsifiable by a label-noise sweep on existing grokking infrastructure — Experiment 1 in the paper, achievable on a single GPU within days.

---

## The monitoring proposal

Current training monitoring tracks loss (the loss landscape, which changes smoothly) and behavioral benchmarks (which detect capabilities after they appear). Neither tracks **G**, the internal coupling strength that determines when corridor-boundary events occur.

Three measurable G-proxies are proposed — gradient avalanche dimensionality, neural synergy (O-information), and emotion vector coherence — each grounded in existing empirical literature and computable from training data. Together they form a monitoring protocol that is *prospective* rather than retrospective: detecting approach to cascade boundaries before capability jumps appear in behavioral benchmarks.

The framework also offers an account of a standing controversy: the discontinuities documented by Wei et al. (2022) and the smooth continuous-metric behavior documented by Schaeffer et al. (2023) are both consistent with the corridor picture, because they track different mathematical objects — attractor existence (discontinuous at saddle-node events) and loss landscape (smooth through those same events) — which change differently at cascade boundaries.

---

## Contents

```
training_corridors_unified_v4.docx        Full paper (22 sections, ~30,000 words)
Corridor Figures/
    fig2_potentials.png                   Normal-form potentials at each boundary
    fig4_noise_scaling.png                Predicted noise-scaling (the 2:1 prediction)
    fig5_D_trajectory.png                 Schematic D(t): starvation vs. cascade signatures
    fig10_experiment_table.png            Experimental program overview
```

---

## Status

Working paper, April 2026. Independent research; no institutional affiliation.

The core noise-scaling predictions are falsifiable against existing datasets without new experiments. The Khanh et al. (2026) dataset (293 grokking training runs, arXiv:2603.13331) could be reanalyzed to test whether T_grok varies with effective noise amplitude when γ_eff is held fixed. The Xu et al. (2026) gradient avalanche data (arXiv:2604.04655) could be reanalyzed for starvation vs. cascade D-signature contrast.

If you have access to grokking training infrastructure or large-model checkpoint data and are interested in running any of the five experiments, feel free to open an issue or reach out directly.

---

## Key references

- Xu, Z. et al. (2026). Grokking as dimensional phase transition. arXiv:2604.04655
- Khanh, T. X. et al. (2026). Why grokking takes so long. arXiv:2603.13331
- Carlini, N. et al. (2026). Assessing Claude Mythos Preview's cybersecurity capabilities. Anthropic red team report.
- Sofroniew, N., Kauvar, I., Saunders, W. et al. (2026). Emotion concepts and their function in a large language model. transformer-circuits.pub
- Clauw, S. et al. (2024). Information-theoretic progress measures reveal grokking is an emergent phase transition. arXiv:2408.08944
- Wei, J. et al. (2022). Emergent abilities of large language models. TMLR.
- Schaeffer, R., Miranda, B., Koyejo, S. (2023). Are emergent abilities of large language models a mirage? NeurIPS 2023.
- Rosas, F. E. et al. (2019). Quantifying high-order interdependencies via multivariate extensions of the mutual information. Phys. Rev. E 100, 032305.
- Dykman, M., Golding, B., Ryvkine, D. (2004). Critical exponent crossovers in escape near a bifurcation point. Phys. Rev. Lett. 92, 080602.
