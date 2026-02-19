## **Mathematical Foundations of ARCH and GARCH Modelling**

This document summarizes the core mathematical structures underlying the ARCH(1) and GARCH(1,1) models implemented in the framework. It covers variance recursion, likelihood functions, forecasting equations, stationarity conditions, and simulation formulas.

---

# **1. Return Process**

We assume a discrete‑time return process:

\[
r_t = \sigma_t z_t,
\]

where:

- \( z_t \sim \mathcal{N}(0,1) \) i.i.d.  
- \( \sigma_t^2 = h_t \) is the conditional variance  

The modelling objective is to specify and estimate the dynamics of \( h_t \).

---

# **2. ARCH(1) Model**

## **2.1 Variance Recursion**

\[
h_t = \omega + \alpha r_{t-1}^2,
\]

with constraints:

\[
\omega > 0, \quad \alpha \ge 0.
\]

## **2.2 Log‑Likelihood**

Given returns \( r_1, \dots, r_T \), the conditional log‑likelihood is:

\[
\ell(\theta) = -\frac{1}{2} \sum_{t=1}^T 
\left[
\log(2\pi) + \log(h_t) + \frac{r_t^2}{h_t}
\right],
\]

where \( \theta = (\omega, \alpha) \).

## **2.3 Stationarity**

ARCH(1) is covariance‑stationary if:

\[
\alpha < 1.
\]

---

# **3. GARCH(1,1) Model**

## **3.1 Variance Recursion**

\[
h_t = \omega + \alpha r_{t-1}^2 + \beta h_{t-1},
\]

with constraints:

\[
\omega > 0, \quad \alpha \ge 0, \quad \beta \ge 0.
\]

## **3.2 Log‑Likelihood**

\[
\ell(\theta) = -\frac{1}{2} \sum_{t=1}^T 
\left[
\log(2\pi) + \log(h_t) + \frac{r_t^2}{h_t}
\right],
\]

where \( \theta = (\omega, \alpha, \beta) \).

## **3.3 Stationarity**

The model is covariance‑stationary if:

\[
\alpha + \beta < 1.
\]

The unconditional variance is:

\[
\mathbb{E}[h_t] = \frac{\omega}{1 - \alpha - \beta}.
\]

---

# **4. Forecasting**

## **4.1 ARCH(1) Forecast**

One‑step:

\[
h_{T+1} = \omega + \alpha r_T^2.
\]

Multi‑step:

\[
h_{T+k} = \omega + \alpha h_{T+k-1}.
\]

Closed form:

\[
h_{T+k} = \omega \sum_{i=0}^{k-1} \alpha^i + \alpha^k h_T.
\]

---

## **4.2 GARCH(1,1) Forecast**

One‑step:

\[
h_{T+1} = \omega + \alpha r_T^2 + \beta h_T.
\]

Multi‑step:

\[
h_{T+k} = \omega + (\alpha + \beta) h_{T+k-1}.
\]

Closed form:

\[
h_{T+k} = \frac{\omega}{1 - \alpha - \beta}
+ (\alpha + \beta)^k \left(h_T - \frac{\omega}{1 - \alpha - \beta}\right).
\]

As \( k \to \infty \):

\[
h_{T+k} \to \frac{\omega}{1 - \alpha - \beta}.
\]

---

# **5. Simulation**

To simulate a GARCH(1,1) path:

1. Initialize:

\[
h_0 = \frac{\omega}{1 - \alpha - \beta}.
\]

2. For \( t = 1, \dots, T \):

\[
z_t \sim \mathcal{N}(0,1),
\]

\[
r_t = \sqrt{h_{t-1}}\, z_t,
\]

\[
h_t = \omega + \alpha r_t^2 + \beta h_{t-1}.
\]

This produces a stationary return and variance sequence.

---

# **6. Parameter Constraints**

To ensure positivity and stationarity:

\[
\omega > 0,
\quad
\alpha \ge 0,
\quad
\beta \ge 0,
\quad
\alpha + \beta < 1.
\]

These constraints are enforced in the implementation.

---

# **7. Maximum Likelihood Estimation**

MLE solves:

\[
\hat{\theta} = \arg\max_{\theta} \ell(\theta),
\]

using L‑BFGS‑B with box constraints.

The AIC and BIC are:

\[
\text{AIC} = -2\ell(\hat{\theta}) + 2k,
\]

\[
\text{BIC} = -2\ell(\hat{\theta}) + k \log(T),
\]

where \( k \) is the number of parameters.

---

# **8. Interpretation of Parameters**

- \( \omega \): long‑run variance level  
- \( \alpha \): sensitivity to recent shocks  
- \( \beta \): persistence of volatility  

Volatility persistence is:

\[
\alpha + \beta.
\]

Values close to 1 indicate slow decay of volatility shocks.
