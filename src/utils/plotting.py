import matplotlib.pyplot as plt
import numpy as np

def line(x, y, title=None):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    if title:
        ax.set_title(title)
    return fig, ax

def scatter(x, y, title=None):
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=10)
    if title:
        ax.set_title(title)
    return fig, ax

def histogram(x, bins=50, title=None):
    fig, ax = plt.subplots()
    ax.hist(np.asarray(x), bins=bins)
    if title:
        ax.set_title(title)
    return fig, ax

def dual_line(x, y1, y2, labels=None, title=None):
    fig, ax = plt.subplots()
    ax.plot(x, y1)
    ax.plot(x, y2)
    if labels:
        ax.legend(labels)
    if title:
        ax.set_title(title)
    return fig, ax