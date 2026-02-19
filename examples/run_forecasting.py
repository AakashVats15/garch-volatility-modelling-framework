import pandas as pd
from src.utils.data_loader import load_returns
from src.models.garch_model import GARCHModel
from src.models.mle_estimation import fit_garch
from src.forecasting.volatility_forecast import forecast_garch
from src.utils.plotting import line

path = "data/asset.csv"
df = load_returns(path)
r = df["returns"].values

res = fit_garch(GARCHModel, r)
model = res["model"]

steps = 30
f = forecast_garch(model, r, steps)

fig, ax = line(range(steps), f, title="GARCH Volatility Forecast")
fig.show()

print("Forecasted variances:", f)