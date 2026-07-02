"""Placeholders for TAQ cleaning.

Fill these functions after you inspect the exact WRDS/TAQ column names.
"""

from __future__ import annotations

import pandas as pd

from src.features.liquidity import midpoint, relative_spread
from src.data.resample import regular_trading_hours


def clean_quotes_basic(
    quotes: pd.DataFrame,
    bid_col: str = "bid",
    ask_col: str = "ask",
    start: str = "09:30",
    end: str = "16:00",
) -> pd.DataFrame:
    """
    Basic quote cleaning placeholder.

    Expected input:
    - DatetimeIndex
    - bid column
    - ask column
    """
    if not isinstance(quotes.index, pd.DatetimeIndex):
        raise TypeError("quotes must have a DatetimeIndex")

    q = quotes.copy().sort_index()
    q = q[(q[bid_col] > 0) & (q[ask_col] > 0)]
    q = q[q[ask_col] >= q[bid_col]]
    q = regular_trading_hours(q, start=start, end=end)

    q["midpoint"] = midpoint(q[bid_col], q[ask_col])
    q["relative_spread"] = relative_spread(q[bid_col], q[ask_col])
    return q
