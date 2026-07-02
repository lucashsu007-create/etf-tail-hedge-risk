"""Return calculations."""

from __future__ import annotations

import pandas as pd


def compute_simple_returns(prices: pd.Series) -> pd.Series:
    """Compute simple returns from a price series."""
    prices = prices.astype(float).sort_index()
    return prices.pct_change().dropna()


def compute_log_returns(prices: pd.Series) -> pd.Series:
    """Compute log returns from a price series."""
    import numpy as np

    prices = prices.astype(float).sort_index()
    return np.log(prices).diff().dropna()


def align_returns(*series: pd.Series) -> pd.DataFrame:
    """Align multiple return series by timestamp."""
    return pd.concat(series, axis=1).dropna()
