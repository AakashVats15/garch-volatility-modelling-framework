# **GARCH Volatility Modelling Framework**

A modular, research‑grade Python framework for estimating, diagnosing, forecasting, and simulating volatility using ARCH and GARCH models. Designed with clarity, reproducibility, and extensibility in mind, this project mirrors the workflow used in quantitative research teams across trading, asset management, and risk analytics.

---

## **📌 Features**

### **Volatility Modelling**
- ARCH(1)  
- GARCH(1,1)  
- Maximum likelihood estimation (L‑BFGS‑B)  
- AIC/BIC model selection  
- Strict parameter validation  

### **Diagnostics**
- ACF & PACF  
- Ljung–Box autocorrelation test  
- Jarque–Bera normality test  
- QQ‑plots  
- Residual summary statistics  

### **Forecasting**
- Multi‑step ARCH forecasts  
- Multi‑step GARCH forecasts  
- Deterministic forward variance recursion  

### **Simulation**
- Monte‑Carlo GARCH(1,1) return & variance paths  
- Stationary initialization  
- Deterministic seeding  

### **Engineering**
- Clean modular architecture  
- Fully documented (`docs/`)  
- Unit tests (`tests/`)  
- Ready‑to‑run examples (`examples/`)  

---

## **📂 Project Structure**

```
garch-volatility-modelling-framework/
│
├── data/
│   ├── raw/                
│   └── processed/          
│
├── src/
│   ├── models/             
│   │   ├── arch_model.py
│   │   ├── garch_model.py
│   │   └── mle_estimation.py
│   │
│   ├── diagnostics/        
│   │   ├── acf_pacf.py
│   │   ├── qq_plots.py
│   │   └── residual_tests.py
│   │
│   ├── forecasting/        
│   │   └── volatility_forecast.py
│   │
│   ├── simulation/         
│   │   └── garch_simulation.py
│   │
│   ├── utils/             
│   │   ├── data_loader.py
│   │   ├── plotting.py
│   │   └── stats_helpers.py
│   │
│   └── __init__.py
│
├── examples/               
│   ├── run_estimation.py
│   ├── run_diagnostics.py
│   ├── run_forecasting.py
│   └── run_simulation.py
│
├── tests/                  
│   ├── test_models.py
│   ├── test_diagnostics.py
│   └── test_forecasting.py
│
├── docs/                   
│   ├── overview.md
│   ├── architecture.md
│   ├── methodology.md
│   ├── math_notes.md
│   ├── usage.md
│   ├── interpretation.md
│   ├── examples.md
│   └── figures/
│
├── requirements.txt        
├── README.md               
└── .gitignore
```

---

## **🚀 Getting Started**

### **1. Install Dependencies**

```
pip install -r requirements.txt
```

### **2. Prepare Your Data**

Place your return series in:

```
data/asset.csv
```

with a column named:

```
returns
```

### **3. Run an Example**

```
python examples/run_estimation.py
```

---

## **📘 Documentation**

The `docs/` folder contains a complete documentation suite:

- **overview.md** — high‑level introduction  
- **architecture.md** — system design  
- **methodology.md** — modelling workflow  
- **math_notes.md** — mathematical derivations  
- **usage.md** — practical guide  
- **interpretation.md** — how to interpret outputs  
- **examples.md** — explanation of example scripts  

This makes the project easy to understand, audit, and extend.

---

## **🧪 Testing**

Run the unit tests:

```
pytest tests/
```

Tests cover:

- model recursion  
- likelihood evaluation  
- diagnostics  
- forecasting logic  

---

## **📈 Extending the Framework**

The modular design allows easy extension:

- EGARCH  
- GJR‑GARCH  
- APARCH  
- Student‑t likelihood  
- DCC‑GARCH  
- richer diagnostics  
- alternative optimizers  

Each module is isolated and follows a consistent interface.

---

## **🎯 Purpose of This Project**

This framework is ideal for:

- quantitative research  
- risk modelling  
- academic study  
- strategy development  
- teaching volatility modelling  

It provides a clean, transparent foundation for understanding and experimenting with volatility dynamics.
