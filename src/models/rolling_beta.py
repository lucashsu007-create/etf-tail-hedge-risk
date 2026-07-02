"""Rolling hedge-ratio estimation."""

from __future__ import annotations

import pandas as pd


def rolling_beta(y: pd.Series, x: pd.Series, window: int) -> pd.Series:
    """
    Estimate rolling beta of y on x using rolling covariance / variance.

    Parameters
    ----------
    y:
        Primary asset returns.
    x:
        Hedge asset returns.
    window:
        Rolling window length in observations.

    Returns
    -------
    pd.Series
        Time-varying hedge ratio.
    """
    if window <= 1:
        raise ValueError("window must be greater than 1")

    aligned = pd.concat([y, x], axis=1).dropna()
    y_aligned = aligned.iloc[:, 0]
    x_aligned = aligned.iloc[:, 1]

    cov = y_aligned.rolling(window).cov(x_aligned)
    var = x_aligned.rolling(window).var()
    beta = cov / var
    beta.name = "rolling_beta"
    return beta
