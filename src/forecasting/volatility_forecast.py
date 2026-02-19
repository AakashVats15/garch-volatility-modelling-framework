import numpy as np
from src.utils.stats_helpers import ensure_1d

def forecast_arch(model, returns, steps):
    r = ensure_1d(returns)
    h = model.conditional_variance(r)
    f = np.empty(steps)
    f[0] = model.omega + model.alpha * r[-1] ** 2
    for t in range(1, steps):
        f[t] = model.omega + model.alpha * f[t - 1]
    return f

def forecast_garch(model, returns, steps):
    r = ensure_1d(returns)
    h = model.conditional_variance(r)
    f = np.empty(steps)
    f[0] = model.omega + model.alpha * r[-1] ** 2 + model.beta * h[-1]
    for t in range(1, steps):
        f[t] = model.omega + (model.alpha + model.beta) * f[t - 1]
    return f