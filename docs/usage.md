## **Using the GARCH Volatility Modelling Framework**

This document provides a practical guide for loading data, estimating models, running diagnostics, generating forecasts, and simulating volatility using the framework. Each section includes minimal, reproducible examples aligned with the project’s modular architecture.

---

# **1. Loading Data**

The framework expects a return series stored in a CSV file with a column named `returns`.

```python
from src.utils.data_loader import load_returns

df = load_returns("data/asset.csv")
r = df["returns"].values
```

The loader handles:

- CSV ingestion  
- numeric casting  
- missing value removal  

---

# **2. Fitting ARCH and GARCH Models**

The MLE engine provides a unified interface for estimating both models.

### **ARCH(1)**

```python
from src.models.arch_model import ARCHModel
from src.models.mle_estimation import fit_arch

res = fit_arch(ARCHModel, r)
model = res["model"]
```

### **GARCH(1,1)**

```python
from src.models.garch_model import GARCHModel
from src.models.mle_estimation import fit_garch

res = fit_garch(GARCHModel, r)
model = res["model"]
```

Each result dictionary contains:

- `params` — estimated parameters  
- `loglik` — log‑likelihood  
- `aic`, `bic` — model selection metrics  
- `model` — fitted model instance  

---

# **3. Extracting Residuals**

Residuals are standardized using the model’s conditional variance.

```python
resid = model.residuals(r)
```

Residuals are used for diagnostics and model validation.

---

# **4. Running Diagnostics**

### **ACF and PACF**

```python
from src.diagnostics.acf_pacf import acf, pacf

acf1 = acf(resid, 1)
pacf1 = pacf(resid, 1)
```

### **Ljung–Box Test**

```python
from src.diagnostics.residual_tests import ljung_box

q = ljung_box(resid, lags=10)
```

### **Jarque–Bera Test**

```python
from src.diagnostics.residual_tests import jb_test

stat, p = jb_test(resid)
```

### **QQ‑Plot**

```python
from src.diagnostics.qq_plots import qq

fig, ax = qq(resid)
fig.show()
```

---

# **5. Forecasting Volatility**

The forecasting module provides multi‑step ARCH and GARCH forecasts.

### **GARCH Forecast Example**

```python
from src.forecasting.volatility_forecast import forecast_garch

steps = 30
f = forecast_garch(model, r, steps)
```

### **Plotting the Forecast**

```python
from src.utils.plotting import line

fig, ax = line(range(steps), f, title="Volatility Forecast")
fig.show()
```

---

# **6. Simulating GARCH Paths**

The simulation module generates Monte‑Carlo return and variance sequences.

```python
from src.simulation.garch_simulation import simulate_garch

sim_r, sim_h = simulate_garch(model, n=500, seed=42)
```

### **Plotting Simulated Series**

```python
fig1, ax1 = line(range(500), sim_r, title="Simulated Returns")
fig1.show()

fig2, ax2 = line(range(500), sim_h, title="Simulated Variance")
fig2.show()
```

---

# **7. Running Example Scripts**

The `examples/` directory contains ready‑to‑run workflows:

- `run_estimation.py` — fit ARCH/GARCH  
- `run_diagnostics.py` — evaluate residuals  
- `run_forecasting.py` — generate forecasts  
- `run_simulation.py` — simulate GARCH paths  

Run any script directly:

```
python examples/run_estimation.py
```

---

# **8. Extending the Framework**

The modular design allows easy extension:

- add new models under `src/models/`  
- add new diagnostics under `src/diagnostics/`  
- add new forecasting methods under `src/forecasting/`  
- add new simulation engines under `src/simulation/`  

Each module is isolated and follows a consistent interface.
