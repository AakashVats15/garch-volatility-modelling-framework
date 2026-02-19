
## **GARCH Volatility Modelling Framework**

The GARCH Volatility Modelling Framework is a modular, research‑grade Python library for estimating, diagnosing, forecasting, and simulating volatility using ARCH and GARCH models. It is designed to mirror the structure and workflow used in quantitative research teams across asset management, trading, and risk management.

The framework emphasizes clarity, reproducibility, and extensibility. Each component is isolated into clean modules, enabling users to experiment with model variations, integrate new diagnostics, or extend the system to more advanced volatility models.

---

## **Core Capabilities**

### **1. Volatility Modelling**
- ARCH(1)  
- GARCH(1,1)  
- Maximum likelihood estimation  
- Parameter validation and stationarity checks  

### **2. Diagnostics**
- ACF and PACF analysis  
- Ljung–Box autocorrelation test  
- Jarque–Bera normality test  
- QQ‑plots  
- Residual summary statistics  

### **3. Forecasting**
- Multi‑step ARCH forecasts  
- Multi‑step GARCH forecasts  
- Deterministic forward variance recursion  

### **4. Simulation**
- Monte‑Carlo GARCH(1,1) return and variance paths  
- Stationary initialization  
- Deterministic seeding for reproducibility  

---

## **Design Philosophy**

The framework is built around three principles:

### **Modularity**
Each component—models, diagnostics, forecasting, simulation, utilities—is isolated into its own module. This makes the system easy to extend and maintain.

### **Determinism**
All functions behave predictably:
- no hidden state  
- no silent failures  
- strict parameter validation  
- reproducible simulations  

### **Transparency**
The mathematical structure of each model is reflected directly in the code. The goal is to make the implementation easy to audit, understand, and modify.

---

## **Project Structure**

```
garch-volatility-modelling-framework/
│
├── data/                     # Raw and processed datasets
├── src/                      # Core library code
│   ├── models/               # ARCH/GARCH models + MLE
│   ├── diagnostics/          # ACF/PACF, QQ-plots, tests
│   ├── forecasting/          # Volatility forecasting
│   ├── simulation/           # Monte-Carlo simulation
│   ├── utils/                # Data loading, plotting, helpers
│
├── examples/                 # Ready-to-run scripts
├── tests/                    # Unit tests
├── docs/                     # Documentation suite
├── requirements.txt
└── README.md
```

---

## **Who This Framework Is For**

This project is designed for:

- quantitative researchers  
- risk analysts  
- systematic traders  
- students learning volatility modelling  
- engineers building financial analytics tools  

It provides a clean foundation for experimentation, teaching, and extension into more advanced models such as EGARCH, GJR‑GARCH, or stochastic volatility.

---

## **How to Use This Documentation**

The `docs/` folder contains:

- **architecture.md** — system design and module interactions  
- **methodology.md** — modelling philosophy and workflow  
- **math_notes.md** — mathematical derivations  
- **usage.md** — practical guide to using the framework  
- **interpretation.md** — how to interpret model outputs  
- **examples.md** — explanation of example scripts  

Together, these documents provide a complete understanding of the framework from both an engineering and quantitative perspective.