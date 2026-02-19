import numpy as np

def simulate_garch(model, n, seed=None):
    if seed is not None:
        np.random.seed(seed)
    r = np.zeros(n)
    h = np.zeros(n)
    h[0] = model.omega / (1 - model.alpha - model.beta)
    for t in range(1, n):
        z = np.random.randn()
        r[t] = np.sqrt(h[t - 1]) * z
        h[t] = model.omega + model.alpha * r[t] ** 2 + model.beta * h[t - 1]
    return r, h