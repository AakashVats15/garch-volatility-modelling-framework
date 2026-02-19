import numpy as np

def simulate_garch(model, n, seed=None):
    if seed is not None:
        np.random.seed(seed)

    omega, alpha, beta = model.omega, model.alpha, model.beta
    h = np.zeros(n)
    r = np.zeros(n)

    h[0] = omega / (1 - alpha - beta)
    z = np.random.randn(n)
    r[0] = np.sqrt(h[0]) * z[0]

    for t in range(1, n):
        h[t] = omega + alpha * r[t-1]**2 + beta * h[t-1]
        r[t] = np.sqrt(h[t]) * z[t]

    return r, h
