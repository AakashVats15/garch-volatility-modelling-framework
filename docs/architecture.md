## **System Architecture**

The GARCH Volatility Modelling Framework is organized into modular, self‑contained components that mirror the workflow used in quantitative research: data ingestion → model estimation → diagnostics → forecasting → simulation. Each module is isolated for clarity, testability, and extensibility.

The project follows a clean, layered architecture:

```
data → utils → models → diagnostics → forecasting → simulation → examples
```

This structure ensures that lower‑level utilities never depend on higher‑level modules, and each layer has a single responsibility.

---

## **Directory Structure**

```
garch-volatility-modelling-framework/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── models/
│   ├── diagnostics/
│   ├── forecasting/
│   ├── simulation/
│   ├── utils/
│   └── __init__.py
│
├── examples/
├── tests/
├── docs/
├── requirements.txt
├── README.md
└── .gitignore
```

Below is a detailed breakdown of each subsystem.

---

## **1. Data Layer (`data/`)**

### **Purpose**
Stores datasets used for model estimation, testing, and experimentation.

### **Structure**
- `raw/` — unmodified input data  
- `processed/` — cleaned or transformed datasets  

This separation ensures reproducibility and prevents accidental overwriting of raw data.

---

## **2. Utility Layer (`src/utils/`)**

### **Purpose**
Provides foundational tools used across the entire framework.

### **Modules**
- **`data_loader.py`** — loads and preprocesses return series  
- **`plotting.py`** — minimal plotting utilities  
- **`stats_helpers.py`** — helper functions for numeric casting and array handling  

These utilities form the base layer and have no dependencies on higher‑level modules.

---

## **3. Model Layer (`src/models/`)**

### **Purpose**
Implements volatility models and maximum likelihood estimation.

### **Modules**
- **`arch_model.py`** — ARCH(1) variance recursion, log‑likelihood, residuals  
- **`garch_model.py`** — GARCH(1,1) recursion, log‑likelihood, residuals  
- **`mle_estimation.py`** — generic MLE engine for ARCH/GARCH  

### **Design Notes**
- Models are deterministic and stateless  
- Parameter validation is strict  
- Log‑likelihood functions are isolated for clarity  
- MLE uses L‑BFGS‑B for stability  

This layer is the computational core of the framework.

---

## **4. Diagnostics Layer (`src/diagnostics/`)**

### **Purpose**
Evaluates model adequacy and residual behaviour.

### **Modules**
- **`acf_pacf.py`** — autocorrelation and partial autocorrelation  
- **`qq_plots.py`** — QQ‑plot generation  
- **`residual_tests.py`** — Ljung–Box, Jarque–Bera, residual statistics  

### **Role in the Pipeline**
Diagnostics validate whether the model has successfully captured volatility clustering and removed autocorrelation from residuals.

---

## **5. Forecasting Layer (`src/forecasting/`)**

### **Purpose**
Generates multi‑step volatility forecasts.

### **Modules**
- **`volatility_forecast.py`** — ARCH and GARCH forward variance recursion  

### **Design Notes**
Forecasting is deterministic and uses closed‑form recursion formulas derived from the model structure.

---

## **6. Simulation Layer (`src/simulation/`)**

### **Purpose**
Produces Monte‑Carlo return and variance paths.

### **Modules**
- **`garch_simulation.py`** — GARCH(1,1) simulation with stationary initialization  

### **Use Cases**
- scenario analysis  
- stress testing  
- synthetic data generation  
- model behaviour exploration  

---

## **7. Examples Layer (`examples/`)**

### **Purpose**
Provides ready‑to‑run scripts demonstrating the full workflow.

### **Scripts**
- `run_estimation.py` — fit ARCH/GARCH models  
- `run_diagnostics.py` — evaluate residuals  
- `run_forecasting.py` — generate volatility forecasts  
- `run_simulation.py` — simulate GARCH paths  

These scripts serve as practical entry points for users.

---

## **8. Testing Layer (`tests/`)**

### **Purpose**
Ensures correctness and stability of the framework.

### **Modules**
- `test_models.py` — model recursion and likelihood tests  
- `test_diagnostics.py` — statistical test validation  
- `test_forecasting.py` — forecast recursion tests  

This layer enforces reliability and prevents regressions.

---

## **9. Documentation Layer (`docs/`)**

### **Purpose**
Provides conceptual, mathematical, and practical explanations.

### **Files**
- `overview.md` — high‑level introduction  
- `architecture.md` — system design (this file)  
- `methodology.md` — modelling philosophy  
- `math_notes.md` — mathematical derivations  
- `usage.md` — how to use the framework  
- `interpretation.md` — how to interpret outputs  
- `examples.md` — explanation of example scripts  
- `figures/` — plots and diagrams  

---

## **Extensibility**

The architecture is designed to support:

- additional GARCH variants (EGARCH, GJR‑GARCH, APARCH)  
- alternative likelihoods (Student‑t, GED)  
- multivariate extensions (DCC‑GARCH)  
- richer diagnostics  
- integration with portfolio or risk systems  

Each module can be extended without modifying the rest of the system.
