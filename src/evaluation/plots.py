"""Plotting helpers."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


def plot_series(x: pd.Series, title: str, ylabel: str = ""):
    """Plot one time series."""
    fig, ax = plt.subplots()
    x.plot(ax=ax)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel("")
    fig.tight_layout()
    return fig, ax


def plot_histogram(x: pd.Series, title: str, bins: int = 50):
    """Plot histogram of a series."""
    fig, ax = plt.subplots()
    x.dropna().hist(ax=ax, bins=bins)
    ax.set_title(title)
    fig.tight_layout()
    return fig, ax
