import numpy as np
from scipy.stats import jarque_bera

def ljung_box(x, lags=10):
    x = np.asarray(x, dtype=float)
    x = x - np.mean(x)
    n = len(x)
    acf_vals = []
    for k in range(1, lags + 1):
        num = np.sum(x[k:] * x[:-k])
        den = np.sum(x ** 2)
        acf_vals.append(num / den)
    q = n * (n + 2) * np.sum([(acf_vals[k - 1] ** 2) / (n - k) for k in range(1, lags + 1)])
    return q

def jb_test(x):
    x = np.asarray(x, dtype=float)
    stat, p = jarque_bera(x)
    return stat, p

def residual_stats(x):
    x = np.asarray(x, dtype=float)
    m = np.mean(x)
    v = np.var(x)
    s = np.mean((x - m) ** 3) / v ** 1.5
    k = np.mean((x - m) ** 4) / v ** 2
    return m, v, s, k