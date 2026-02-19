import numpy as np

def acf(x, lag):
    x = np.asarray(x)
    mean = np.mean(x)

    num = np.sum((x[:-lag] - mean) * (x[lag:] - mean))
    denom = np.sum((x - mean)**2)

    if denom == 0:
        return 0.0 

    return num / denom

def pacf(x, lag):
    x = np.asarray(x, dtype=float)
    y = x[lag:]
    X = np.column_stack([x[lag - i - 1 : -i - 1] for i in range(lag)])
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    return beta[-1]