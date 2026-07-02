"""Liquidity and stress-regime features."""

from __future__ import annotations

import pandas as pd


def midpoint(bid: pd.Series, ask: pd.Series) -> pd.Series:
    """Quote midpoint."""
    mid = (bid.astype(float) + ask.astype(float)) / 2
    mid.name = "midpoint"
    return mid


def quoted_spread(bid: pd.Series, ask: pd.Series) -> pd.Series:
    """Quoted spread."""
    spread = ask.astype(float) - bid.astype(float)
    spread.name = "quoted_spread"
    return spread


def relative_spread(bid: pd.Series, ask: pd.Series) -> pd.Series:
    """Relative quoted spread: (ask - bid) / midpoint."""
    mid = midpoint(bid, ask)
    rel = (ask.astype(float) - bid.astype(float)) / mid
    rel.name = "relative_spread"
    return rel


def realized_volatility(returns: pd.Series, window: int) -> pd.Series:
    """Rolling realized volatility proxy using rolling standard deviation."""
    if window <= 1:
        raise ValueError("window must be greater than 1")
    rv = returns.rolling(window).std()
    rv.name = "realized_volatility"
    return rv


def stress_label(df: pd.DataFrame, columns: list[str], quantile: float = 0.90) -> pd.Series:
    """
    Label stress periods when any selected feature exceeds its own quantile threshold.
    """
    if not 0 < quantile < 1:
        raise ValueError("quantile must be between 0 and 1")
    if not columns:
        raise ValueError("columns must be non-empty")

    flags = []
    for col in columns:
        if col not in df.columns:
            raise KeyError(f"Missing stress column: {col}")
        flags.append(df[col] > df[col].quantile(quantile))

    out = pd.concat(flags, axis=1).any(axis=1).astype(int)
    out.name = "stress"
    return out
