## **Examples**

The `examples/` directory contains four self‑contained scripts demonstrating the full workflow of the GARCH Volatility Modelling Framework. Each script focuses on a specific stage of the modelling pipeline: estimation, diagnostics, forecasting, and simulation. Together, they provide a complete reference for how to use the framework in practice.

All scripts assume that a return series is stored in:

```
data/asset.csv
```

with a column named `returns`.

---

# **1. `run_estimation.py`**

### **Purpose**
Fits ARCH(1) and GARCH(1,1) models using maximum likelihood estimation.

### **What It Does**
- loads return data  
- estimates ARCH parameters  
- estimates GARCH parameters  
- prints:
  - estimated parameters  
  - log‑likelihood  
  - AIC and BIC  

### **Why It Matters**
This script demonstrates the core functionality of the framework: model estimation. It is the starting point for any volatility analysis workflow.

---

# **2. `run_diagnostics.py`**

### **Purpose**
Evaluates whether the fitted model adequately captures volatility dynamics.

### **What It Does**
- loads return data  
- fits a GARCH(1,1) model  
- extracts standardized residuals  
- computes:
  - ACF and PACF  
  - Ljung–Box statistic  
  - Jarque–Bera statistic  
  - residual summary statistics  
- generates a QQ‑plot  

### **Why It Matters**
Diagnostics are essential for validating model adequacy. This script shows how to check whether residuals behave like white noise and whether the model has captured volatility clustering.

---

# **3. `run_forecasting.py`**

### **Purpose**
Generates multi‑step volatility forecasts from a fitted GARCH model.

### **What It Does**
- loads return data  
- fits a GARCH(1,1) model  
- produces a 30‑step variance forecast  
- plots the forecast path  
- prints the forecasted variance values  

### **Why It Matters**
Forecasting is a central application of GARCH models. This script demonstrates how to project future volatility and visualize the expected decay or persistence of shocks.

---

# **4. `run_simulation.py`**

### **Purpose**
Simulates synthetic return and variance paths using a fitted GARCH model.

### **What It Does**
- loads return data  
- fits a GARCH(1,1) model  
- simulates 500 steps of:
  - returns  
  - conditional variance  
- plots both simulated series  
- prints the raw arrays  

### **Why It Matters**
Simulation is useful for:
- scenario analysis  
- stress testing  
- synthetic data generation  
- understanding model behaviour  

This script shows how to generate Monte‑Carlo paths consistent with the estimated volatility dynamics.

---

# **How to Run the Scripts**

From the project root:

```
python examples/run_estimation.py
python examples/run_diagnostics.py
python examples/run_forecasting.py
python examples/run_simulation.py
```

Each script is self‑contained and can be used as a template for custom workflows.

---

# **How These Examples Fit Together**

The examples follow the natural order of a quant research workflow:

1. **Estimate** the model  
2. **Diagnose** the residuals  
3. **Forecast** future volatility  
4. **Simulate** hypothetical scenarios  

This mirrors the structure used in professional risk and volatility modelling pipelines.
