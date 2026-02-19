import numpy as np

def acf(x, lag):
    x = np.asarray(x, dtype=float)
    x = x - np.mean(x)
    n = len(x)
    denom = np.sum(x ** 2)
    num = np.sum(x[: n - lag] * x[lag:])
    return num / denom

def pacf(x, lag):
    x = np.asarray(x, dtype=float)
    y = x[lag:]
    X = np.column_stack([x[lag - i - 1 : -i - 1] for i in range(lag)])
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    return beta[-1]