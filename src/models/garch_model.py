import numpy as np
from src.utils.stats_helpers import ensure_1d

class GARCHModel:
    def __init__(self, omega, alpha, beta):
        self.omega = float(omega)
        self.alpha = float(alpha)
        self.beta = float(beta)

    def _check_params(self):
        if self.omega <= 0:
            raise ValueError("omega must be positive")
        if self.alpha < 0 or self.beta < 0:
            raise ValueError("alpha and beta must be non-negative")
        if self.alpha + self.beta >= 1:
            raise ValueError("alpha + beta must be < 1 for stationarity")

    def conditional_variance(self, returns):
        self._check_params()
        r = ensure_1d(returns)
        n = r.shape[0]
        h = np.empty(n)
        h[0] = np.var(r)
        for t in range(1, n):
            h[t] = self.omega + self.alpha * r[t - 1] ** 2 + self.beta * h[t - 1]
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