import numpy as np
import pandas as pd

def ensure_1d(x):
    x = np.asarray(x).astype(float)
    return x.reshape(-1)

def mean(x):
    return np.mean(ensure_1d(x))

def variance(x):
    x = ensure_1d(x)
    m = np.mean(x)
    return np.mean((x - m) ** 2)

def autocovariance(x, lag=1):
    x = ensure_1d(x)
    m = np.mean(x)
    return np.mean((x[:-lag] - m) * (x[lag:] - m))

def autocorrelation(x, lag=1):
    return autocovariance(x, lag) / variance(x)

def standardize(x):
    x = ensure_1d(x)
    return (x - np.mean(x)) / np.std(x)

def rolling_variance(x, window):
    x = ensure_1d(x)
    return pd.Series(x).rolling(window).var().dropna().values