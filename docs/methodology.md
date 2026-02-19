## **Methodology for ARCH/GARCH Volatility Modelling**

This document outlines the modelling philosophy, workflow, and methodological decisions behind the GARCH Volatility Modelling Framework. It explains how the system processes data, estimates models, validates results, and produces forecasts and simulations. The goal is to provide a transparent, research‑grade foundation for volatility analysis.

---

# **1. Modelling Philosophy**

The framework is built around three core principles:

### **1.1 Parsimony**
ARCH(1) and GARCH(1,1) models are intentionally simple. They capture the essential features of financial volatility:

- volatility clustering  
- mean reversion  
- persistence  
- heavy‑tailed residuals  

These models serve as a baseline for more advanced extensions.

### **1.2 Transparency**
The implementation mirrors the mathematical structure directly:

- explicit variance recursion  
- explicit log‑likelihood  
- deterministic forecasting  
- deterministic simulation  

This makes the system easy to audit, extend, and validate.

### **1.3 Reproducibility**
All components are:

- deterministic  
- modular  
- testable  
- free of hidden state  

This ensures consistent results across runs and environments.

---

# **2. Data Workflow**

The modelling pipeline begins with a return series:

\[
r_t = \log(P_t) - \log(P_{t-1})
\]

The data loader:

- reads CSV files  
- casts to numeric  
- removes missing values  
- returns a clean NumPy array  

This ensures that all downstream modules operate on standardized input.

---

# **3. Model Estimation**

The framework implements ARCH(1) and GARCH(1,1) using maximum likelihood estimation (MLE).

### **3.1 Likelihood Function**

For both models, the conditional log‑likelihood is:

\[
\ell(\theta) = -\frac{1}{2} \sum_{t=1}^T 
\left[
\log(2\pi) + \log(h_t) + \frac{r_t^2}{h_t}
\right]
\]

### **3.2 Optimization**

MLE is performed using:

- L‑BFGS‑B  
- strict parameter bounds  
- stable initialization  
- deterministic recursion  

### **3.3 Model Selection**

The framework computes:

\[
\text{AIC} = -2\ell + 2k
\]

\[
\text{BIC} = -2\ell + k \log(T)
\]

These metrics help compare ARCH vs. GARCH or future model extensions.

---

# **4. Diagnostics Methodology**

Diagnostics validate whether the fitted model adequately captures volatility dynamics.

### **4.1 Residual Analysis**

Standardized residuals:

\[
\hat{z}_t = \frac{r_t}{\sqrt{h_t}}
\]

should behave like white noise.

### **4.2 Autocorrelation Checks**

- ACF  
- PACF  
- Ljung–Box test  

These detect remaining structure in residuals.

### **4.3 Distributional Checks**

- Jarque–Bera test  
- QQ‑plots  
- skewness and kurtosis  

These assess normality and tail behaviour.

### **4.4 Adequacy Criteria**

A model is considered adequate if:

- residual autocorrelation is negligible  
- volatility clustering is captured  
- standardized residuals resemble Gaussian noise  
- persistence is realistic  

---

# **5. Forecasting Methodology**

Forecasts are generated using closed‑form variance recursion.

### **5.1 ARCH Forecasting**

\[
h_{T+k} = \omega + \alpha h_{T+k-1}
\]

### **5.2 GARCH Forecasting**

\[
h_{T+k} = \omega + (\alpha + \beta) h_{T+k-1}
\]

### **5.3 Long‑Run Convergence**

Forecasts converge to:

\[
\frac{\omega}{1 - \alpha - \beta}
\]

The speed of convergence reflects volatility persistence.

---

# **6. Simulation Methodology**

Simulation follows the GARCH(1,1) recursion:

1. Initialize:

\[
h_0 = \frac{\omega}{1 - \alpha - \beta}
\]

2. Generate:

\[
z_t \sim \mathcal{N}(0,1)
\]

\[
r_t = \sqrt{h_{t-1}}\, z_t
\]

\[
h_t = \omega + \alpha r_t^2 + \beta h_{t-1}
\]

Simulated paths are used for:

- scenario analysis  
- stress testing  
- synthetic data generation  
- model behaviour exploration  

---

# **7. Extensibility**

The framework is designed to support:

- EGARCH  
- GJR‑GARCH  
- APARCH  
- Student‑t likelihood  
- multivariate DCC‑GARCH  

Each module is isolated, making extensions straightforward.

---

# **8. Summary**

The methodology behind the framework emphasizes:

- mathematical clarity  
- engineering discipline  
- reproducibility  
- extensibility  

This makes the system suitable for research, teaching, and real‑world volatility modelling.