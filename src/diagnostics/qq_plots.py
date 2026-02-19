import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

def qq(residuals):
    r = np.asarray(residuals, dtype=float)
    r = r[~np.isnan(r)]
    q = st.norm.ppf(np.linspace(0.001, 0.999, len(r)))
    s = np.sort(r)
    fig, ax = plt.subplots()
    ax.scatter(q, s, s=10)
    ax.plot(q, q, color="red")
    return fig, ax