# **GARCH Volatility Modelling Framework**

A modular Python framework for modelling, estimating, diagnosing, and forecasting financial market volatility using ARCH and GARCH models.  
This project is designed as a clean, extensible research codebase suitable for quant finance, risk modelling, and time‑series analysis.

---

## **📌 Overview**

Volatility is a central concept in financial modelling, risk management, and derivative pricing.  
This repository implements a full workflow for:

- ARCH and GARCH(1,1) volatility models  
- Maximum Likelihood Estimation (MLE) of model parameters  
- Volatility clustering analysis  
- Residual diagnostics (ACF, PACF, QQ‑plots, Ljung‑Box tests)  
- AIC/BIC model comparison  
- Multi‑step volatility forecasting  
- Simulation of return paths under calibrated GARCH  
- Visualisations and interpretation of results  

The codebase is structured to mirror how a quant research team would organise a modelling pipeline: modular, testable, and easy to extend.

---

## **📁 Folder Structure**

```
garch-volatility-modelling-framework/
│
├── data/
│   ├── raw/                # Unprocessed price/return data
│   └── processed/          # Cleaned returns, volatility series
│
├── src/
│   ├── models/             # ARCH/GARCH models + MLE estimation
│   │   ├── arch_model.py
│   │   ├── garch_model.py
│   │   └── mle_estimation.py
│   │
│   ├── diagnostics/        # ACF/PACF, QQ-plots, residual tests
│   │   ├── acf_pacf.py
│   │   ├── qq_plots.py
│   │   └── residual_tests.py
│   │
│   ├── forecasting/        # Volatility forecasting utilities
│   │   └── volatility_forecast.py
│   │
│   ├── simulation/         # GARCH return path simulation
│   │   └── garch_simulation.py
│   │
│   ├── utils/              # Data loading, plotting, helper functions
│   │   ├── data_loader.py
│   │   ├── plotting.py
│   │   └── stats_helpers.py
│   │
│   └── __init__.py
│
├── examples/               # Minimal runnable scripts
│   ├── run_estimation.py
│   ├── run_diagnostics.py
│   ├── run_forecasting.py
│   └── run_simulation.py
│
├── tests/                  # Unit tests for reliability
│   ├── test_models.py
│   ├── test_diagnostics.py
│   └── test_forecasting.py
│
├── docs/                   # Methodology + interpretation notes
│   ├── methodology.md
│   ├── interpretation.md
│   └── figures/
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── LICENSE                 # License information
└── .gitignore
```

---

## **🔧 What This Framework Implements**

### **1. ARCH & GARCH(1,1) Models**
- Conditional variance modelling  
- Log‑likelihood computation  
- Parameter constraints (positivity, stationarity)

### **2. MLE Parameter Estimation**
- Numerical optimisation (e.g., BFGS, Nelder‑Mead)  
- Robust handling of parameter bounds  
- Convergence diagnostics  

### **3. Volatility Clustering Analysis**
- Squared returns  
- Rolling variance  
- Visual inspection tools  

### **4. Residual Diagnostics**
- ACF & PACF of residuals and squared residuals  
- QQ‑plots for normality  
- Ljung‑Box tests  
- Standardised residual checks  

### **5. Model Comparison**
- AIC / BIC computation  
- Side‑by‑side comparison of ARCH vs GARCH  

### **6. Volatility Forecasting**
- One‑step and multi‑step forecasts  
- Forecast error evaluation  
- Plotting forecast paths  

### **7. Simulation**
- Simulated return paths under calibrated GARCH  
- Monte‑Carlo volatility scenarios  
- Reproducible random seeds  

### **8. Visualisation & Interpretation**
- Clean, publication‑quality plots  
- Interpretation notes in `/docs`  

---

## **🚀 Getting Started**

Install dependencies:

```
pip install -r requirements.txt
```

Run a full estimation example:

```
python examples/run_estimation.py
```