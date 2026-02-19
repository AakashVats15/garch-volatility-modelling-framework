import pandas as pd
from src.utils.data_loader import load_returns
from src.models.garch_model import GARCHModel
from src.models.mle_estimation import fit_garch
from src.diagnostics.acf_pacf import acf, pacf
from src.diagnostics.qq_plots import qq
from src.diagnostics.residual_tests import ljung_box, jb_test, residual_stats

path = "data/asset.csv"
df = load_returns(path)
r = df["returns"].values

res = fit_garch(GARCHModel, r)
model = res["model"]
resid = model.residuals(r)

print("Mean, Var, Skew, Kurt:", residual_stats(resid))
print("Ljung-Box:", ljung_box(resid, lags=10))
print("Jarque-Bera:", jb_test(resid))
print("ACF(1):", acf(resid, 1))
print("PACF(1):", pacf(resid, 1))

fig, ax = qq(resid)
fig.show()