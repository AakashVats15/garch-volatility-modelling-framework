## **Interpreting ARCH/GARCH Model Outputs**

This document explains how to interpret the parameters, diagnostics, forecasts, and simulations produced by the GARCH Volatility Modelling Framework. The goal is to help users understand what the model is telling them about volatility dynamics, persistence, and risk.

---

# **1. Interpreting Model Parameters**

Both ARCH(1) and GARCH(1,1) models estimate three key components of volatility behaviour:

### **1.1 ω — Long‑Run Variance Level**
- Represents the baseline volatility level.
- Higher values imply a higher unconditional variance.
- In GARCH, the unconditional variance is:

\[
\frac{\omega}{1 - \alpha - \beta}
\]

### **1.2 α — Reaction to Recent Shocks**
- Measures how strongly volatility reacts to new information.
- High α means large returns (positive or negative) immediately increase volatility.
- In ARCH(1), α is the only persistence term.

### **1.3 β — Volatility Persistence**
- Measures how slowly volatility decays after a shock.
- High β means volatility remains elevated for longer.
- In GARCH(1,1), persistence is:

\[
\alpha + \beta
\]

### **1.4 Persistence Interpretation**
- **α + β < 0.7** → fast‑decaying volatility  
- **0.7–0.9** → moderate persistence  
- **0.9–0.98** → highly persistent (common in equities)  
- **> 0.98** → near‑unit‑root behaviour (volatility shocks decay very slowly)  

---

# **2. Interpreting Residual Diagnostics**

Residual diagnostics determine whether the model has successfully captured volatility clustering.

### **2.1 ACF and PACF**
- ACF close to zero → no remaining autocorrelation  
- PACF close to zero → no remaining partial autocorrelation  
- Significant spikes → model underfits volatility dynamics  

### **2.2 Ljung–Box Test**
- Tests whether residuals are autocorrelated.
- High Q‑statistic → autocorrelation remains → model inadequate  
- Low Q‑statistic → residuals behave like white noise  

### **2.3 Jarque–Bera Test**
- Tests whether residuals are normally distributed.
- GARCH residuals often show fat tails, so normality is rarely perfect.
- Interpretation:
  - **High JB** → heavy tails remain  
  - **Low JB** → residuals close to Gaussian  

### **2.4 QQ‑Plot**
- Points on the 45° line → residuals match the normal distribution  
- Heavy tails → points deviate at extremes  
- Asymmetry → skewed distribution  

### **2.5 Summary Statistics**
- **Mean ≈ 0** → good  
- **Variance ≈ 1** → standardized residuals behave correctly  
- **Skewness ≠ 0** → asymmetry in shocks  
- **Kurtosis > 3** → fat tails  

---

# **3. Interpreting Volatility Forecasts**

Volatility forecasts show how the model expects future uncertainty to evolve.

### **3.1 Short‑Term Forecasts**
- Driven by recent returns and recent volatility.
- Large recent shocks → elevated short‑term forecasts.

### **3.2 Long‑Term Forecasts**
- Converge to the unconditional variance:

\[
\frac{\omega}{1 - \alpha - \beta}
\]

- The speed of convergence depends on persistence:
  - High persistence → slow convergence  
  - Low persistence → fast convergence  

### **3.3 Practical Interpretation**
- Rising forecast curve → volatility expected to increase  
- Falling curve → volatility shock decaying  
- Flat curve → stable volatility regime  

---

# **4. Interpreting GARCH Simulations**

Simulated paths help understand model behaviour under hypothetical scenarios.

### **4.1 Simulated Returns**
- Should show volatility clustering: periods of calm and turbulence.
- No autocorrelation in returns (GARCH models volatility, not direction).

### **4.2 Simulated Variance**
- Should remain positive and mean‑reverting.
- Should fluctuate around the unconditional variance.
- Persistence determines how long variance stays elevated after shocks.

### **4.3 Use Cases**
- scenario analysis  
- stress testing  
- synthetic data generation  
- risk modelling  
- strategy backtesting  

---

# **5. Model Adequacy Checklist**

A model is considered adequate if:

- residual ACF/PACF show no significant spikes  
- Ljung–Box test indicates no autocorrelation  
- volatility forecasts converge smoothly  
- simulated paths resemble empirical behaviour  
- parameters satisfy stationarity conditions  
- persistence is realistic for the asset class  

If these conditions fail, consider:

- adding more lags  
- switching to GJR‑GARCH or EGARCH  
- using Student‑t innovations  
- re‑examining the data preprocessing  

---

# **6. Practical Interpretation Examples**

### **Example 1: High Persistence**
If α = 0.12 and β = 0.85:

- persistence = 0.97  
- volatility shocks decay slowly  
- long‑run volatility is stable but elevated  
- forecasts converge slowly  

### **Example 2: Low Persistence**
If α = 0.25 and β = 0.40:

- persistence = 0.65  
- volatility decays quickly  
- shocks dissipate within a few days  
- forecasts flatten rapidly  

### **Example 3: Heavy‑Tailed Residuals**
If JB is large and QQ‑plot shows fat tails:

- normal likelihood may be inadequate  
- consider Student‑t GARCH  