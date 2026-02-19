import pandas as pd
from src.utils.data_loader import load_returns
from src.models.garch_model import GARCHModel
from src.models.mle_estimation import fit_garch
from src.simulation.garch_simulation import simulate_garch
from src.utils.plotting import line

path = "data/asset.csv"
df = load_returns(path)
r = df["returns"].values

res = fit_garch(GARCHModel, r)
model = res["model"]

n = 500
sim_r, sim_h = simulate_garch(model, n, seed=42)

fig1, ax1 = line(range(n), sim_r, title="Simulated Returns")
fig1.show()

fig2, ax2 = line(range(n), sim_h, title="Simulated Variance")
fig2.show()

print("Simulated returns:", sim_r)
print("Simulated variance:", sim_h)