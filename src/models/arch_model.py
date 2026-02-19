import numpy as np
from src.utils.stats_helpers import ensure_1d

class ARCHModel:
    def __init__(self, omega, alpha):
        self.omega = float(omega)
        self.alpha = float(alpha)

    def _check_params(self):
        if self.omega <= 0:
            raise ValueError("omega must be positive")
        if self.alpha < 0:
            raise ValueError("alpha must be non-negative")

    def conditional_variance(self, returns):
        self._check_params()
        r = ensure_1d(returns)
        n = r.shape[0]
        h = np.empty(n)
        h[0] = np.var(r)
        for t in range(1, n):
            h[t] = self.omega + self.alpha * r[t - 1] ** 2
        return h

    def loglikelihood(self, returns):
        r = ensure_1d(returns)
        h = self.conditional_variance(r)
        if np.any(h <= 0):
            return -np.inf
        ll = -0.5 * (np.log(2 * np.pi) + np.log(h) + (r ** 2) / h)
        return np.sum(ll)

    def residuals(self, returns):
        r = ensure_1d(returns)
        h = self.conditional_variance(r)
        return r / np.sqrt(h)