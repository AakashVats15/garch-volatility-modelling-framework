import pandas as pd
import numpy as np
import os

def load_csv(path, parse_dates=True, index_col=None):
    return pd.read_csv(path, parse_dates=parse_dates, index_col=index_col)

def load_prices(path, price_col="Close"):
    df = pd.read_csv(path, parse_dates=True)
    df = df[[price_col]].dropna()
    df[price_col] = pd.to_numeric(df[price_col], errors="coerce")
    return df.dropna()

def load_returns(path, price_col="Close"):
    df = load_prices(path, price_col)
    df["returns"] = np.log(df[price_col]).diff()
    return df.dropna()

def save_processed(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path)