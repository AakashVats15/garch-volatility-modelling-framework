import numpy as np
from src.models.arch_model import ARCHModel
from src.models.garch_model import GARCHModel
from src.models.mle_estimation import fit_arch, fit_garch

def test_arch_variance_recursion():
    model = ARCHModel(omega=0.1, alpha=0.2)
    r = np.array([0.0, 1.0, -1.0])
    h = model.conditional_variance(r)
    assert len(h) == len(r)
    assert np.all(h > 0)

def test_garch_variance_recursion():
    model = GARCHModel(omega=0.1, alpha=0.2, beta=0.5)
    r = np.array([0.0, 1.0, -1.0])
    h = model.conditional_variance(r)
    assert len(h) == len(r)
    assert np.all(h > 0)

def test_arch_loglik_finite():
    model = ARCHModel(omega=0.1, alpha=0.2)
    r = np.random.randn(100)
    ll = model.loglik(r)
    assert np.isfinite(ll)

def test_garch_loglik_finite():
    model = GARCHModel(omega=0.1, alpha=0.2, beta=0.5)
    r = np.random.randn(100)
    ll = model.loglik(r)
    assert np.isfinite(ll)

def test_arch_mle_runs():
    r = np.random.randn(200)
    res = fit_arch(ARCHModel, r)
    params = res["params"]
    assert len(params) == 2
    assert params["omega"] > 0
    assert params["alpha"] >= 0

def test_garch_mle_runs():
    r = np.random.randn(200)
    res = fit_garch(GARCHModel, r)
    params = res["params"]
    assert len(params) == 3
    assert params["omega"] > 0
    assert params["alpha"] >= 0
    assert params["beta"] >= 0