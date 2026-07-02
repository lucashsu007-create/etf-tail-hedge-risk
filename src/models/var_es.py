"""Historical VaR and Expected Shortfall."""

from __future__ import annotations

import pandas as pd


def historical_var(x: pd.Series, alpha: float = 0.05) -> float:
    """Historical lower-tail Value-at-Risk threshold."""
    if not 0 < alpha < 1:
        raise ValueError("alpha must be between 0 and 1")
    return float(x.dropna().quantile(alpha))


def historical_es(x: pd.Series, alpha: float = 0.05) -> float:
    """Historical lower-tail Expected Shortfall."""
    q = historical_var(x, alpha)
    tail = x.dropna()[x.dropna() <= q]
    if tail.empty:
        return float("nan")
    return float(tail.mean())
