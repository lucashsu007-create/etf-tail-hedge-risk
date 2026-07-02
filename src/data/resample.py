"""Resampling utilities for TAQ-style data."""

from __future__ import annotations

import pandas as pd


def resample_last(series: pd.Series, freq: str = "5min") -> pd.Series:
    """Resample a timestamped series using last observation in each interval."""
    return series.sort_index().resample(freq).last().dropna()


def resample_sum(series: pd.Series, freq: str = "5min") -> pd.Series:
    """Resample a timestamped series using sum within each interval."""
    return series.sort_index().resample(freq).sum().dropna()


def regular_trading_hours(df: pd.DataFrame, start: str = "09:30", end: str = "16:00") -> pd.DataFrame:
    """Keep regular U.S. equity trading hours from a DatetimeIndex."""
    if not isinstance(df.index, pd.DatetimeIndex):
        raise TypeError("df must have a DatetimeIndex")
    return df.between_time(start, end)
