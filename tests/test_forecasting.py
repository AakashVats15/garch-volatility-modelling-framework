import numpy as np
from src.models.garch_model import GARCHModel
from src.forecasting.volatility_forecast import forecast_garch

def test_garch_one_step_forecast():
    # Simple deterministic setup
    model = GARCHModel(omega=0.1, alpha=0.2, beta=0.5)
    r = np.array([1.0, -1.0, 0.5])

    # Manual 1-step forecast
    h = model.conditional_variance(r)
    expected = 0.1 + 0.2 * r[-1]**2 + 0.5 * h[-1]

    f = forecast_garch(model, r, steps=1)
    assert np.isclose(f[0], expected, atol=1e-6)

def test_garch_multi_step_forecast_length():
    model = GARCHModel(omega=0.1, alpha=0.2, beta=0.5)
    r = np.random.randn(100)

    f = forecast_garch(model, r, steps=10)
    assert len(f) == 10

def test_garch_forecast_positive():
    model = GARCHModel(omega=0.1, alpha=0.2, beta=0.5)
    r = np.random.randn(100)

    f = forecast_garch(model, r, steps=20)
    assert np.all(f > 0)

def test_garch_forecast_converges_to_unconditional():
    model = GARCHModel(omega=0.1, alpha=0.2, beta=0.5)
    r = np.random.randn(200)

    f = forecast_garch(model, r, steps=200)

    # Unconditional variance
    unconditional = model.omega / (1 - model.alpha - model.beta)

    # Last forecast should be close to unconditional variance
    assert np.isclose(f[-1], unconditional, atol=1e-3)