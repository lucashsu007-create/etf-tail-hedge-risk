"""Hedge-error construction."""

from __future__ import annotations

import pandas as pd


def hedge_error(r_primary: pd.Series, r_hedge: pd.Series, beta: pd.Series) -> pd.Series:
    """
    Compute hedge error:

        HE_t = r_primary,t - beta_t * r_hedge,t
    """
    aligned = pd.concat([r_primary, r_hedge, beta], axis=1).dropna()
    he = aligned.iloc[:, 0] - aligned.iloc[:, 2] * aligned.iloc[:, 1]
    he.name = "hedge_error"
    return he


def absolute_hedge_error(he: pd.Series) -> pd.Series:
    """Absolute hedge error."""
    out = he.abs()
    out.name = "absolute_hedge_error"
    return out
