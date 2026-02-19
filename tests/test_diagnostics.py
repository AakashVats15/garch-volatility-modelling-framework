import numpy as np
from src.diagnostics.acf_pacf import acf, pacf
from src.diagnostics.residual_tests import ljung_box, jb_test, residual_stats
from src.diagnostics.qq_plots import qq

def test_acf_zero_series():
    x = np.zeros(100)
    val = acf(x, 1)
    assert abs(val) < 1e-8

def test_acf_known_series():
    x = np.array([1, 2, 3, 4, 5], dtype=float)
    val = acf(x, 1)
    assert np.isfinite(val)

def test_pacf_zero_series():
    x = np.zeros(100)
    val = pacf(x, 1)
    assert abs(val) < 1e-8

def test_pacf_known_series():
    x = np.array([1, 2, 3, 4, 5], dtype=float)
    val = pacf(x, 1)
    assert np.isfinite(val)

def test_ljung_box_white_noise():
    x = np.random.randn(200)
    stat = ljung_box(x, lags=10)
    assert np.isfinite(stat)

def test_jb_test_output():
    x = np.random.randn(200)
    stat, p = jb_test(x)
    assert np.isfinite(stat)
    assert 0 <= p <= 1

def test_residual_stats_shape():
    x = np.random.randn(200)
    m, v, s, k = residual_stats(x)
    assert np.isfinite(m)
    assert np.isfinite(v)
    assert np.isfinite(s)
    assert np.isfinite(k)

def test_qq_plot_returns_figure():
    x = np.random.randn(200)
    fig, ax = qq(x)
    assert fig is not None
    assert ax is not None