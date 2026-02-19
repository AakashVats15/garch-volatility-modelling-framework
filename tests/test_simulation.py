import numpy as np
from src.models.garch_model import GARCHModel
from src.simulation.garch_simulation import simulate_garch

def test_simulation_output_shapes():
    model = GARCHModel(omega=0.1, alpha=0.2, beta=0.5)
    n = 300
    r, h = simulate_garch(model, n, seed=42)

    assert len(r) == n
    assert len(h) == n
    assert r.shape == h.shape

def test_simulated_variance_positive():
    model = GARCHModel(omega=0.1, alpha=0.2, beta=0.5)
    r, h = simulate_garch(model, n=500, seed=1)

    assert np.all(h > 0)

def test_simulation_deterministic_with_seed():
    model = GARCHModel(omega=0.1, alpha=0.2, beta=0.5)

    r1, h1 = simulate_garch(model, n=200, seed=123)
    r2, h2 = simulate_garch(model, n=200, seed=123)

    assert np.allclose(r1, r2)
    assert np.allclose(h1, h2)

def test_simulation_stationary_initialization():
    model = GARCHModel(omega=0.1, alpha=0.2, beta=0.5)

    # Unconditional variance
    unconditional = model.omega / (1 - model.alpha - model.beta)

    _, h = simulate_garch(model, n=1, seed=0)

    # First variance should be close to unconditional variance
    assert np.isclose(h[0], unconditional, atol=1e-6)

def test_simulation_recursion_structure():
    model = GARCHModel(omega=0.1, alpha=0.2, beta=0.5)
    r, h = simulate_garch(model, n=5, seed=0)

    # Check GARCH recursion for t=1..4
    for t in range(1, 5):
        expected = (
            model.omega
            + model.alpha * r[t-1]**2
            + model.beta * h[t-1]
        )
        assert np.isclose(h[t], expected, atol=1e-6)