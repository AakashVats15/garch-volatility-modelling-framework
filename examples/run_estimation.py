import pandas as pd
from src.utils.data_loader import load_returns
from src.models.arch_model import ARCHModel
from src.models.garch_model import GARCHModel
from src.models.mle_estimation import fit_arch, fit_garch

path = "data/asset.csv"
df = load_returns(path)
r = df["returns"].values

arch_res = fit_arch(ARCHModel, r)
garch_res = fit_garch(GARCHModel, r)

print("ARCH params:", arch_res["params"])
print("ARCH loglik:", arch_res["loglik"])
print("ARCH AIC:", arch_res["aic"])
print("ARCH BIC:", arch_res["bic"])

print("GARCH params:", garch_res["params"])
print("GARCH loglik:", garch_res["loglik"])
print("GARCH AIC:", garch_res["aic"])
print("GARCH BIC:", garch_res["bic"])