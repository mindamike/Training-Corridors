"""
constraint_escape_spectral_v2.py

Spectral escape law — calibrated against the Ito formula and C-function hierarchy.

CALIBRATION CHANGES FROM v1
-----------------------------

1. KAPPA VALUES RE-ANCHORED (primary fix)
   v1 kappa sweep [0, 0.5, 1.0, 1.5, 2.0] extended from L0/L1 to just past L2.
   The correct physical anchors (nmodes=16, escape_bias=1, directly solved):

     Level                 C(n)   kappa    D_eff/D verified
     L0/L1 QED/Atomic      1.000  0.000    1.0000
     L2 Chemistry          0.265  1.869    0.2650   <- v1 barely reached (kappa~1.87)
     L3 Thermodynamics     0.030  5.993    0.0300   <- v1 never reached

   The v1 kappa_scale approximation (kappa_scale*ln(1+correction)) was off by
   ~14x because R(kappa) is not a simple exponential in kappa.
   Correct method: bisect R(kappa) = C_target directly.

2. C-FUNCTION PROXY = D_eff/D DIRECTLY
   For DV_TC = mu^3/6: mu_c ∝ D_eff^{1/3}, so
     C(n)/C(0) = (mu_c(n)/mu_c(0))^3 = D_eff(kappa_n) / D_eff(kappa_0) = R(kappa_n)
   The spectral reduction R(kappa) is the C-function proxy without any cube correction.

3. D-SCALING IS ANALYTICAL, NOT IN SWEEP
   The Ito correction ∝ D implies kappa_n(D) = kappa_n^{ref} * (D/D_ref). Applying
   this in the simulation makes D_eff(D) non-monotonic and breaks loglog fitting.
   Kappa is kept fixed per run; D-scaling is documented as analytical metadata.

CORRIDOR GEOMETRY
-----------------
TC normal form: drift = mu*x - x^2,  DV_TC = mu^3/6,  a_TC,bare = 1/3
SN normal form: drift = mu - x^2,    DV_SN ~ mu^{3/2}, a_SN,bare = 2/3
Ratio: a_SN/a_TC = 2 (bare, parameter-independent)
"""

from __future__ import annotations
import argparse, math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, List, Tuple
import numpy as np
import matplotlib.pyplot as plt


# ─────────────────────────────────────────────────────────────────────────────
# C-function hierarchy (measured physical values)
# ─────────────────────────────────────────────────────────────────────────────

PHYSICAL_C = {"L0_QED": 1.000, "L1_Atomic": 1.000,
               "L2_Chem": 0.265, "L3_Thermo": 0.030}


def find_kappa_for_target(c_target: float, nmodes: int = 16,
                           bias: float = 1.0) -> float:
    """Bisect kappa such that R(kappa) = c_target. R(0)=1 by construction."""
    i = np.arange(1, nmodes + 1, dtype=float)
    w = i ** (2 * bias)
    W = w.sum()

    def R(k: float) -> float:
        return float(np.sum(w * np.exp(-k * (i - 1) / (nmodes - 1))) / W)

    if c_target >= 1.0:
        return 0.0
    lo, hi = 0.0, 25.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if R(mid) > c_target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# ─────────────────────────────────────────────────────────────────────────────
# Drifts and geometry
# ─────────────────────────────────────────────────────────────────────────────

def drift_tc(x: np.ndarray, mu: float) -> np.ndarray:
    return mu * x - x ** 2

def drift_sn(x: np.ndarray, mu: float) -> np.ndarray:
    return mu - x ** 2

def tc_geometry(mu: float, alpha: float) -> Tuple[float, float, float, float]:
    x_s, x_b = mu, 0.0
    w = abs(x_s - x_b)
    return x_s, x_b, w, x_b - alpha * w

def sn_geometry(mu: float, alpha: float) -> Tuple[float, float, float, float]:
    if mu <= 0:
        return 0.0, 0.0, 0.0, -np.inf
    x_s, x_b = math.sqrt(mu), -math.sqrt(mu)
    w = abs(x_s - x_b)
    return x_s, x_b, w, x_b - alpha * w


# ─────────────────────────────────────────────────────────────────────────────
# Config
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class Cfg:
    dt: float = 0.01
    tau: float = 10.0
    ntraj: int = 400
    seed: int = 0
    p_target: float = 0.20
    alpha: float = 0.25
    nmodes: int = 16
    kappa: float = 0.0
    bias: float = 1.0
    floor: float = 1e-9


# ─────────────────────────────────────────────────────────────────────────────
# Spectral model
# ─────────────────────────────────────────────────────────────────────────────

def _weights(cfg: Cfg) -> Tuple[np.ndarray, np.ndarray, float]:
    i = np.arange(1, cfg.nmodes + 1, dtype=float)
    lam = np.maximum(np.exp(cfg.kappa * (i - 1) / max(cfg.nmodes - 1, 1)), cfg.floor)
    u = i ** cfg.bias
    u = u / np.linalg.norm(u)
    return i, lam, float(np.sum(u ** 2 / lam))  # reduction = R(kappa)

def reduction(cfg: Cfg) -> float:
    _, _, R = _weights(cfg)
    return R

def D_eff(D: float, cfg: Cfg) -> float:
    return D * reduction(cfg)

def spectral_diag(cfg: Cfg) -> Dict[str, float]:
    i, lam, R = _weights(cfg)
    inv = 1.0 / lam
    p = inv / inv.sum()
    ent = float(-np.sum(p * np.log(p + 1e-15)))
    return {"R": R, "eff_rank": float(np.exp(ent)), "dom_mode": float(p.max())}


# ─────────────────────────────────────────────────────────────────────────────
# Escape simulations
# ─────────────────────────────────────────────────────────────────────────────

def _sim_escape(mu: float, D: float, cfg: Cfg,
                drift_fn: Callable, geom_fn: Callable) -> float:
    rng = np.random.default_rng(cfg.seed)
    n = int(cfg.tau / cfg.dt)
    sig = math.sqrt(2.0 * D_eff(D, cfg) * cfg.dt)
    x_s, _, _, x_commit = geom_fn(mu, cfg.alpha)
    if x_s == 0.0 and x_commit == -np.inf:
        return 1.0
    x = np.full(cfg.ntraj, x_s)
    alive = np.ones(cfg.ntraj, bool)
    for _ in range(n):
        idx = np.where(alive)[0]
        if not idx.size:
            break
        xv = x[idx]
        xv += drift_fn(xv, mu) * cfg.dt + sig * rng.standard_normal(idx.size)
        x[idx] = xv
        alive[idx[xv <= x_commit]] = False
    return float((~alive).mean())

def p_tc(mu, D, cfg): return _sim_escape(mu, D, cfg, drift_tc, tc_geometry)
def p_sn(mu, D, cfg): return _sim_escape(mu, D, cfg, drift_sn, sn_geometry)


# ─────────────────────────────────────────────────────────────────────────────
# Bisection and fitting
# ─────────────────────────────────────────────────────────────────────────────

def fit_slope(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.polyfit(np.log(x), np.log(y), 1)[0])

def bisect_mu(D: float, cfg: Cfg, fn: Callable,
              lo: float = 0.005, hi: float = 3.0) -> float:
    for _ in range(12):
        if fn(lo, D, cfg) >= cfg.p_target:
            break
        lo *= 0.5
    for _ in range(12):
        if fn(hi, D, cfg) <= cfg.p_target:
            break
        hi *= 2.0
    p_lo, p_hi = fn(lo, D, cfg), fn(hi, D, cfg)
    if not (p_lo >= cfg.p_target >= p_hi):
        raise RuntimeError(f"No bracket D={D:.3e} lo={lo:.4f}({p_lo:.3f}) hi={hi:.4f}({p_hi:.3f})")
    for _ in range(20):
        mid = math.sqrt(lo * hi)
        (lo if fn(mid, D, cfg) > cfg.p_target else None)
        if fn(mid, D, cfg) > cfg.p_target:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


# ─────────────────────────────────────────────────────────────────────────────
# Per-condition run and sweep
# ─────────────────────────────────────────────────────────────────────────────

def run_one(D_values: np.ndarray, cfg: Cfg) -> Dict:
    mu_tc_ = np.array([bisect_mu(D, cfg, p_tc) for D in D_values])
    mu_sn_ = np.array([bisect_mu(D, cfg, p_sn) for D in D_values])
    a_tc = fit_slope(D_values, mu_tc_)
    a_sn = fit_slope(D_values, mu_sn_)
    diag = spectral_diag(cfg)
    return {
        "mu_tc": mu_tc_, "mu_sn": mu_sn_,
        "a_tc": a_tc, "a_sn": a_sn,
        "chi_tc": a_tc - 1/3, "chi_sn": (a_sn - 2/3) / 2,
        "ratio": a_sn / a_tc, **diag,
    }


def sweep(tau_vals: np.ndarray, kappa_vals: np.ndarray,
          D_vals: np.ndarray, base: Cfg) -> Dict[str, np.ndarray]:
    rows = []
    for kappa in kappa_vals:
        for tau in tau_vals:
            cfg = Cfg(dt=base.dt, tau=float(tau), ntraj=base.ntraj, seed=base.seed,
                      p_target=base.p_target, alpha=base.alpha,
                      nmodes=base.nmodes, kappa=float(kappa), bias=base.bias)
            res = run_one(D_vals, cfg)
            rows.append([kappa, tau, res["a_tc"], res["a_sn"],
                         res["chi_tc"], res["chi_sn"], res["ratio"],
                         res["R"], res["eff_rank"]])
            print(f"  κ={kappa:.3f} τ={tau:.0f}: "
                  f"a_TC={res['a_tc']:.4f}  a_SN={res['a_sn']:.4f}  "
                  f"ratio={res['ratio']:.4f}  C_proxy={res['R']:.4f}")
    arr = np.array(rows)
    keys = ["kappa","tau","a_tc","a_sn","chi_tc","chi_sn","ratio","c_proxy","eff_rank"]
    return {k: arr[:, j] for j, k in enumerate(keys)}


# ─────────────────────────────────────────────────────────────────────────────
# Plots
# ─────────────────────────────────────────────────────────────────────────────

C_HLINES = [(1.000,":","gray","C=1.000 L0/L1"),
            (0.265,"--","darkorange","C=0.265 L2"),
            (0.030,"-.","firebrick","C=0.030 L3")]

def curves(res: Dict, key: str, outpath: Path, title: str, ylabel: str,
           hlines=None) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    for k in np.unique(res["kappa"]):
        m = res["kappa"] == k
        tau = res["tau"][m]
        y = res[key][m]
        idx = np.argsort(tau)
        ax.semilogx(tau[idx], y[idx], "o-", lw=1.5, ms=5,
                    label=f"κ={k:.3f}  C≈{reduction(Cfg(kappa=k)):.3f}")
    if hlines:
        for v, ls, col, lbl in hlines:
            ax.axhline(v, ls=ls, color=col, lw=0.9, label=lbl)
    ax.set_xlabel("tau"); ax.set_ylabel(ylabel); ax.set_title(title)
    ax.legend(fontsize=7, ncol=2); fig.tight_layout()
    fig.savefig(outpath, dpi=200); plt.close(fig)

def heatmap(xv, yv, zv, outpath, xlabel, ylabel, title) -> None:
    xu, yu = np.unique(xv), np.unique(yv)
    Z = np.full((len(yu), len(xu)), np.nan)
    for i, y in enumerate(yu):
        for j, x in enumerate(xu):
            m = (xv == x) & (yv == y)
            if m.any():
                Z[i, j] = zv[m][0]
    fig, ax = plt.subplots(figsize=(7, 5))
    im = ax.imshow(Z, origin="lower", aspect="auto",
                   extent=[xu.min(), xu.max(), yu.min(), yu.max()])
    ax.set_xlabel(xlabel); ax.set_ylabel(ylabel); ax.set_title(title)
    fig.colorbar(im, ax=ax); fig.tight_layout()
    fig.savefig(outpath, dpi=200); plt.close(fig)

def c_proxy_curve(nmodes: int, bias: float, kappa_vals: np.ndarray,
                  res: Dict, outpath: Path) -> None:
    """R(kappa) analytical curve with C-function anchors and simulated C_proxy."""
    k_dense = np.linspace(0, kappa_vals.max() * 1.1, 300)
    i = np.arange(1, nmodes + 1, dtype=float)
    w = i ** (2 * bias); W = w.sum()
    R_curve = [float(np.sum(w * np.exp(-k*(i-1)/(nmodes-1))) / W) for k in k_dense]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(k_dense, R_curve, "k-", lw=2, label="R(κ) analytical")

    taus = np.unique(res["tau"])
    tau_mid = taus[len(taus) // 2]
    m = res["tau"] == tau_mid
    ax.scatter(res["kappa"][m], res["c_proxy"][m], s=70, zorder=5,
               color="tab:blue", label=f"C_proxy sim (τ={tau_mid:.0f})")

    for v, ls, col, lbl in C_HLINES:
        k_anchor = find_kappa_for_target(v, nmodes, bias)
        ax.axhline(v, ls=ls, color=col, lw=0.9)
        ax.axvline(k_anchor, ls=ls, color=col, lw=0.9, label=lbl + f" κ={k_anchor:.2f}")

    ax.set_xlabel("κ"); ax.set_ylabel("D_eff / D  =  C-proxy")
    ax.set_title("Spectral reduction = C-function proxy\nPhysical hierarchy anchors")
    ax.legend(fontsize=8); ax.set_ylim(-0.02, 1.08)
    fig.tight_layout(); fig.savefig(outpath, dpi=200); plt.close(fig)

def exponents_vs_kappa(res: Dict, kappa_vals: np.ndarray, nmodes: int, bias: float,
                        outpath: Path) -> None:
    taus = np.unique(res["tau"])
    tau_mid = taus[len(taus) // 2]
    m = res["tau"] == tau_mid
    k_vals = res["kappa"][m]; idx = np.argsort(k_vals)
    k_L2 = find_kappa_for_target(0.265, nmodes, bias)
    k_L3 = find_kappa_for_target(0.030, nmodes, bias)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for ax, key, bare, ylabel in [
        (axes[0], "a_tc", 1/3, "a_TC"),
        (axes[1], "a_sn", 2/3, "a_SN"),
        (axes[2], "ratio", 2.0, "a_SN / a_TC"),
    ]:
        y = res[key][m][idx]
        ax.plot(k_vals[idx], y, "ko-", lw=2, ms=6, label=f"sim τ={tau_mid:.0f}")
        ax.axhline(bare, ls="--", color="royalblue", lw=1.2, label=f"bare={bare:.3f}")
        ax.axvline(k_L2, ls=":", color="darkorange", lw=1.5,
                   label=f"L2 Chem κ={k_L2:.2f}")
        ax.axvline(k_L3, ls=":", color="firebrick", lw=1.5,
                   label=f"L3 Thermo κ={k_L3:.2f}")
        ax.set_xlabel("κ"); ax.set_ylabel(ylabel)
        ax.set_title(f"{ylabel} vs κ")
        ax.legend(fontsize=8)
    fig.suptitle(
        f"Fitted exponents vs spectral compression  (τ={tau_mid:.0f})\n"
        f"L2 Chemistry → κ={k_L2:.2f}   |   L3 Thermo → κ={k_L3:.2f}",
        fontsize=10)
    fig.tight_layout(); fig.savefig(outpath, dpi=200); plt.close(fig)

def mu_crit_plot(mu_tc_d: Dict, mu_sn_d: Dict, D_vals: np.ndarray,
                 kappa_vals: np.ndarray, tau: float, outpath: Path) -> None:
    colors = plt.cm.plasma(np.linspace(0.1, 0.9, len(kappa_vals)))
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    for ax, mu_d, bare, title in [
        (axes[0], mu_tc_d, 1/3, "TC critical mu vs D"),
        (axes[1], mu_sn_d, 2/3, "SN critical mu vs D"),
    ]:
        ref = np.logspace(np.log10(D_vals.min()), np.log10(D_vals.max()), 50)
        ax.loglog(ref, 0.3 * ref**bare, "k--", lw=1, label=f"bare slope={bare:.3f}", alpha=0.6)
        for ci, kappa in enumerate(kappa_vals):
            mu = mu_d.get(kappa)
            if mu is None:
                continue
            a = fit_slope(D_vals, mu)
            ax.loglog(D_vals, mu, "o-", color=colors[ci], lw=1.5, ms=5,
                      label=f"κ={kappa:.2f}  a={a:.3f}")
        ax.set_xlabel("D"); ax.set_ylabel("mu_crit")
        ax.set_title(f"{title}  (τ={tau:.0f})")
        ax.legend(fontsize=7)
    fig.tight_layout(); fig.savefig(outpath, dpi=200); plt.close(fig)


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

def parse() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["quick","study"], default="quick")
    p.add_argument("--outdir", default="spectral_v2_outputs")
    p.add_argument("--dt", type=float, default=0.01)
    p.add_argument("--ntraj", type=int, default=400)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--p_target", type=float, default=0.20)
    p.add_argument("--alpha", type=float, default=0.25)
    p.add_argument("--nd", type=int, default=5)
    p.add_argument("--nmodes", type=int, default=16)
    p.add_argument("--bias", type=float, default=1.0)
    return p.parse_args()


def main():
    args = parse()
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    nm, bias = args.nmodes, args.bias

    k_L2 = find_kappa_for_target(0.265, nm, bias)
    k_L3 = find_kappa_for_target(0.030, nm, bias)

    print("\n=== CALIBRATION ===")
    print(f"  nmodes={nm}  escape_bias={bias:.2f}")
    for label, c in [("L0/L1",1.000),("L2 Chem",0.265),("L3 Thermo",0.030)]:
        k = find_kappa_for_target(c, nm, bias)
        print(f"  {label:<14}  C={c:.3f}  kappa={k:.4f}")
    print(f"\n  Analytical Ito D-scaling (not applied in sweep):")
    print(f"    kappa_L2(D) = {k_L2:.3f} * (D / D_ref)")
    print(f"    kappa_L3(D) = {k_L3:.3f} * (D / D_ref)")

    if args.mode == "quick":
        tau_vals   = np.array([10., 30., 80.])
        kappa_vals = np.array([0.0, round(k_L2*0.5,3), round(k_L2,3),
                                round((k_L2+k_L3)/2,3), round(k_L3,3)])
        D_vals = np.logspace(-3.5, -1, args.nd)
    else:
        tau_vals   = np.array([5., 10., 20., 40., 80., 160.])
        kappa_vals = np.array([0.0, round(k_L2*0.4,3), round(k_L2*0.7,3),
                                round(k_L2,3), round(k_L2*1.5,3), round(k_L3,3)])
        D_vals = np.logspace(-4, -1, args.nd)

    print(f"\n  kappa sweep: {list(kappa_vals)}")
    print(f"  tau sweep:   {list(tau_vals)}")
    print(f"  D values:    {list(np.round(D_vals, 5))}\n")

    base = Cfg(dt=args.dt, tau=tau_vals[0], ntraj=args.ntraj, seed=args.seed,
               p_target=args.p_target, alpha=args.alpha, nmodes=nm, bias=bias)

    res = sweep(tau_vals, kappa_vals, D_vals, base)

    # collect mu arrays for the middle tau
    tau_mid = tau_vals[len(tau_vals)//2]
    mu_tc_d, mu_sn_d = {}, {}
    for kappa in kappa_vals:
        cfg = Cfg(dt=args.dt, tau=float(tau_mid), ntraj=args.ntraj, seed=args.seed,
                  p_target=args.p_target, alpha=args.alpha, nmodes=nm,
                  kappa=float(kappa), bias=bias)
        r = run_one(D_vals, cfg)
        mu_tc_d[kappa] = r["mu_tc"]
        mu_sn_d[kappa] = r["mu_sn"]

    # ── Summary ───────────────────────────────────────────────────────────
    print("\n=== SUMMARY ===")
    print(f"{'kappa':<8} {'tau':<7} {'a_TC':<9} {'a_SN':<9} "
          f"{'ratio':<8} {'C_proxy':<10} {'eff_rank'}")
    for row in zip(res["kappa"],res["tau"],res["a_tc"],res["a_sn"],
                   res["ratio"],res["c_proxy"],res["eff_rank"]):
        print(f"{row[0]:<8.3f} {row[1]:<7.0f} {row[2]:<9.5f} {row[3]:<9.5f} "
              f"{row[4]:<8.5f} {row[5]:<10.5f} {row[6]:.4f}")

    print(f"\n=== C-FUNCTION LEVEL CLASSIFICATION ===")
    for k in kappa_vals:
        c = reduction(Cfg(nmodes=nm, kappa=float(k), bias=bias))
        if c > 0.90: lvl = "L0/L1 QED/Atomic"
        elif c > 0.15: lvl = "L2 Chemistry"
        elif c > 0.015: lvl = "L3 Thermodynamics"
        else: lvl = "> L3 deep compression"
        print(f"  kappa={k:.3f}  D_eff/D={c:.4f}  → {lvl}")

    # ── Plots ─────────────────────────────────────────────────────────────
    exponents_vs_kappa(res, kappa_vals, nm, bias, outdir/"exponents_vs_kappa.png")
    c_proxy_curve(nm, bias, kappa_vals, res, outdir/"c_proxy_curve.png")
    curves(res,"ratio", outdir/"ratio_vs_tau.png","a_SN/a_TC vs tau","a_SN/a_TC",
           [(2.0,"--","royalblue","bare=2.0",)])
    curves(res,"chi_tc",outdir/"chi_tc_vs_tau.png","χ_TC vs tau","χ_TC",
           [(0.0,"--","gray","bare χ=0",)])
    curves(res,"chi_sn",outdir/"chi_sn_vs_tau.png","χ_SN vs tau","χ_SN")
    curves(res,"c_proxy",outdir/"c_proxy_vs_tau.png","C-proxy vs tau","D_eff/D",
           C_HLINES)
    curves(res,"eff_rank",outdir/"eff_rank_vs_tau.png","Spectral eff rank vs tau","eff rank")
    mu_crit_plot(mu_tc_d, mu_sn_d, D_vals, kappa_vals, tau_mid, outdir/"mu_crit_vs_D.png")
    heatmap(res["tau"],res["kappa"],res["chi_tc"],outdir/"hmap_chi_tc.png","tau","κ","χ_TC")
    heatmap(res["tau"],res["kappa"],res["chi_sn"],outdir/"hmap_chi_sn.png","tau","κ","χ_SN")
    heatmap(res["tau"],res["kappa"],res["ratio"], outdir/"hmap_ratio.png","tau","κ","ratio")
    heatmap(res["tau"],res["kappa"],res["c_proxy"],outdir/"hmap_c_proxy.png","tau","κ","C_proxy")

    with open(outdir/"sweep_v2.txt","w") as f:
        f.write("kappa\ttau\ta_tc\ta_sn\tchi_tc\tchi_sn\tratio\tc_proxy\teff_rank\n")
        for row in zip(res["kappa"],res["tau"],res["a_tc"],res["a_sn"],
                       res["chi_tc"],res["chi_sn"],res["ratio"],
                       res["c_proxy"],res["eff_rank"]):
            f.write("\t".join(f"{v:.8f}" for v in row)+"\n")

    print(f"\nSaved to: {outdir.resolve()}")
    print(f"C-anchor summary: L2→κ={k_L2:.3f}  L3→κ={k_L3:.3f}")


if __name__ == "__main__":
    main()
