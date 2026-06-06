"""
Pressure-test of Theorem 1(ii): does the greedy, censoring-aware,
contamination-blind learner exhibit a genuine tipping point (saddle-node
fold -> bistable collapse), or only a smooth biased fixed point (spiral to
a biased equilibrium)?

Mechanism modeled: MASKED STOCKOUTS VIA RETURNS / CORRECTIONS.
  - True demand D ~ F.  Order q.  Stockout when D >= q (prob 1-F(q)).
  - On a stockout day, with intensity eps a returns batch or feed correction
    is booked to that period, reducing recorded demand to ~ G and suppressing
    the stockout label.  The returns-and-corrections log records the booking.
  - Otherwise the stockout is correctly recorded as censored at q.
  - The learner trusts labels, runs KM (single censoring level => empirical
    CDF on [0,q]), and orders the beta-quantile of its estimate.

Audit trigger (observable): CORRECTION-LOG ALARM.
  - Fires on logged correction days, not on stockout-flagged days.
  - A fraction phi of logged days is reviewed; corrected records are relabeled
    as censored at q.  Uncorrected masked days remain contaminated.

Derived mean-field CDF the learner estimates while operating at order q:
      Fhat(x) = F(x) + eps * (1 - F(q)) * G(x),   x <= q.
Fixed points of the order map solve  Fhat(q) = beta, i.e.
      H(q) := F(q) + eps * (1 - F(q)) * G(q) = beta.
"""

import math
import numpy as np

SQRT2 = math.sqrt(2.0)

def ncdf(x, mu, sd):
    return 0.5 * (1.0 + math.erf((x - mu) / (sd * SQRT2)))

def npdf(x, mu, sd):
    return math.exp(-0.5 * ((x - mu) / sd) ** 2) / (sd * math.sqrt(2 * math.pi))

def nppf(p, mu, sd):
    lo, hi = mu - 12 * sd, mu + 12 * sd
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if ncdf(mid, mu, sd) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

MU, SD = 100.0, 30.0
MU_G, SD_G = 40.0, 10.0

def F(x):  return ncdf(x, MU, SD)
def f(x):  return npdf(x, MU, SD)
def G(x):  return ncdf(x, MU_G, SD_G)

def H(q, eps):
    return F(q) + eps * (1.0 - F(q)) * G(q)

def count_roots(eps, beta, lo=1.0, hi=250.0, n=4000):
    qs = np.linspace(lo, hi, n)
    vals = np.array([H(q, eps) - beta for q in qs])
    roots = []
    for i in range(n - 1):
        if vals[i] == 0.0:
            roots.append(qs[i])
        elif vals[i] * vals[i + 1] < 0:
            a, b = qs[i], qs[i + 1]
            for _ in range(80):
                m = 0.5 * (a + b)
                if (H(a, eps) - beta) * (H(m, eps) - beta) <= 0:
                    b = m
                else:
                    a = m
            roots.append(0.5 * (a + b))
    return roots

def Hprime_min(eps, lo=1.0, hi=250.0, n=4000):
    qs = np.linspace(lo, hi, n)
    dq = qs[1] - qs[0]
    hv = np.array([H(q, eps) for q in qs])
    dh = np.gradient(hv, dq)
    return dh.min()

print("=" * 70)
print("PART 1: fixed-point structure of H(q)=beta  (roots => equilibria)")
print("=" * 70)
print(f"{'beta':>5} {'eps':>5} {'#roots':>7} {'q_inf':>8} {'F(q_inf)':>9} "
      f"{'bias':>13} {'minHp':>8}")
for beta in [0.30, 0.50, 0.70, 0.90]:
    qstar = nppf(beta, MU, SD)
    for eps in [0.0, 0.05, 0.10, 0.20, 0.30, 0.50, 0.80]:
        roots = count_roots(eps, beta)
        qinf = max(roots) if roots else float('nan')
        svc = F(qinf) if roots else float('nan')
        mind = Hprime_min(eps)
        print(f"{beta:>5.2f} {eps:>5.2f} {len(roots):>7d} {qinf:>8.2f} "
              f"{svc:>9.3f} {qstar - qinf:>13.2f} {mind:>8.4f}")
    print()

print("=" * 70)
print("PART 2: sensitivity of equilibrium service to contamination")
print("  analytic: d q_inf/d eps |_{eps=0} = -(1-beta) G(q*) / f(q*)")
print("=" * 70)
print(f"{'beta':>5} {'q*':>8} {'f(q*)':>8} {'G(q*)':>8} {'dq/deps':>9} "
      f"{'d(svc)/deps':>12}")
for beta in [0.30, 0.50, 0.70, 0.90]:
    qstar = nppf(beta, MU, SD)
    dq_deps = -(1 - beta) * G(qstar) / f(qstar)
    dsvc_deps = f(qstar) * dq_deps
    print(f"{beta:>5.2f} {qstar:>8.2f} {f(qstar):>8.5f} {G(qstar):>8.4f} "
          f"{dq_deps:>9.2f} {dsvc_deps:>12.4f}")

print()
print("=" * 70)
print("PART 3: simulation with correction-log alarm")
print("  phi = fraction of logged correction days the human audits.")
print("  Audited masked stockouts are relabeled as censored at q.")
print("=" * 70)
rng = np.random.default_rng(7)

def nv_cost(q, beta):
    b = beta / (1.0 - beta)
    z = (q - MU) / SD
    phi = npdf(q, MU, SD) * SD
    Phi = ncdf(q, MU, SD)
    E_short = SD * (phi / 1.0 - z * (1.0 - Phi))
    E_over = SD * (phi / 1.0 + z * Phi)
    return b * E_short + 1.0 * E_over

def simulate(beta, eps, phi=0.0, T=4000, N=200, W=60, q0=160.0):
    """Censoring-aware learner with masked stockouts and correction-log audit."""
    qstar = nppf(beta, MU, SD)
    hist = []
    q = q0
    path = []
    audits = 0
    days = 0
    for t in range(T):
        D = rng.normal(MU, SD, N)
        U = rng.random(N)
        stock = D >= q
        corrupt = stock & (U <= eps)
        audited = corrupt & (rng.random(N) < phi)
        corrupt_uncaught = corrupt & ~audited
        genuine_cens = stock & ~corrupt

        unc = list(D[~stock])
        if corrupt_uncaught.any():
            unc.extend(rng.normal(MU_G, SD_G, int(corrupt_uncaught.sum())))
        n_cens = int(genuine_cens.sum() + audited.sum())

        audits += int(audited.sum())
        days += N

        hist.append((np.array(unc), n_cens))
        if len(hist) > W:
            hist.pop(0)
        all_unc = np.concatenate([h[0] for h in hist]) if hist else np.array([])
        total = sum(len(h[0]) + h[1] for h in hist)
        if total == 0 or len(all_unc) == 0:
            q = q0
            path.append(q)
            continue
        target = beta * total
        s = np.sort(all_unc)
        k = int(np.ceil(target))
        q = float(s[min(k, len(s)) - 1]) if k <= len(s) else float(s[-1])
        path.append(q)
    return np.array(path), qstar, audits / days

print(f"{'beta':>5} {'eps':>5} {'phi':>5} {'mf q_inf':>9} {'sim q_inf':>10} "
      f"{'(sd)':>6} {'service':>8} {'cost gap%':>10} {'audit load':>11}")
for beta in [0.30, 0.70]:
    qstar = nppf(beta, MU, SD)
    c_opt = nv_cost(qstar, beta)
    rows = [(0.00, None)] + [(0.30, phi) for phi in (0.0, 0.5, 1.0)]
    for eps, phi in rows:
        ph = 0.0 if phi is None else phi
        path, _, load = simulate(beta, eps, ph)
        tail = path[-500:]
        qsim = tail.mean()
        eps_eff = eps * (1.0 - ph)
        mf = max(count_roots(eps_eff, beta))
        gap = 100.0 * (nv_cost(qsim, beta) - c_opt) / c_opt
        lab_phi = "-" if phi is None else f"{phi:.1f}"
        print(f"{beta:>5.2f} {eps:>5.2f} {lab_phi:>5} {mf:>9.2f} {qsim:>10.2f} "
              f"{tail.std():>6.2f} {F(qsim):>8.3f} {gap:>10.1f} {load:>11.3f}")
    print()
