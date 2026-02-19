import numpy as np
from scipy.optimize import minimize

def _neg_loglik_arch(params, model_class, returns):
    omega, alpha = params
    if omega <= 0 or alpha < 0:
        return 1e10
    model = model_class(omega, alpha)
    ll = model.loglikelihood(returns)
    return -ll if np.isfinite(ll) else 1e10

def _neg_loglik_garch(params, model_class, returns):
    omega, alpha, beta = params
    if omega <= 0 or alpha < 0 or beta < 0 or alpha + beta >= 1:
        return 1e10
    model = model_class(omega, alpha, beta)
    ll = model.loglikelihood(returns)
    return -ll if np.isfinite(ll) else 1e10

def fit_arch(model_class, returns, start_params=None):
    r = np.asarray(returns, dtype=float)
    if start_params is None:
        var = np.var(r)
        start_params = np.array([0.1 * var, 0.8])
    res = minimize(_neg_loglik_arch, start_params, args=(model_class, r), method="L-BFGS-B")
    omega, alpha = res.x
    model = model_class(omega, alpha)
    ll = model.loglikelihood(r)
    k = 2
    aic = -2 * ll + 2 * k
    bic = -2 * ll + k * np.log(len(r))
    return {"model": model, "params": res.x, "loglik": ll, "aic": aic, "bic": bic, "success": res.success}

def fit_garch(model_class, returns, start_params=None):
    r = np.asarray(returns, dtype=float)
    if start_params is None:
        var = np.var(r)
        start_params = np.array([0.1 * var, 0.05, 0.9])
    res = minimize(_neg_loglik_garch, start_params, args=(model_class, r), method="L-BFGS-B")
    omega, alpha, beta = res.x
    model = model_class(omega, alpha, beta)
    ll = model.loglikelihood(r)
    k = 3
    aic = -2 * ll + 2 * k
    bic = -2 * ll + k * np.log(len(r))
    return {"model": model, "params": res.x, "loglik": ll, "aic": aic, "bic": bic, "success": res.success}