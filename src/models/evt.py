"""Basic EVT utilities.

This is intentionally simple and exploratory. Validate all EVT choices before making
research claims.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import genpareto


def lower_tail_losses(x: pd.Series) -> pd.Series:
    """Convert lower-tail negative observations into positive losses."""
    return -x.dropna()


def fit_gpd_to_excesses(losses: pd.Series, threshold_quantile: float = 0.95) -> dict:
    """
    Fit a Generalized Pareto Distribution to excess losses above a threshold.

    Returns a dictionary with threshold, shape, loc, scale, and number of excesses.
    """
    if not 0 < threshold_quantile < 1:
        raise ValueError("threshold_quantile must be between 0 and 1")

    losses = losses.dropna()
    threshold = float(losses.quantile(threshold_quantile))
    excesses = losses[losses > threshold] - threshold

    if len(excesses) < 20:
        raise ValueError("Too few excesses for even exploratory GPD fitting.")

    shape, loc, scale = genpareto.fit(excesses, floc=0)

    return {
        "threshold": threshold,
        "shape": float(shape),
        "loc": float(loc),
        "scale": float(scale),
        "n_excesses": int(len(excesses)),
        "n_total": int(len(losses)),
    }


def evt_var_loss(params: dict, alpha: float = 0.99) -> float:
    """
    Estimate high-quantile loss VaR from POT/GPD parameters.

    alpha is the target loss quantile, e.g. 0.99.
    """
    u = params["threshold"]
    xi = params["shape"]
    beta = params["scale"]
    n = params["n_total"]
    nu = params["n_excesses"]

    p_exceed = nu / n
    tail_prob = 1 - alpha

    if tail_prob <= 0 or tail_prob >= p_exceed:
        raise ValueError("alpha must correspond to a quantile beyond the threshold.")

    if abs(xi) < 1e-8:
        return float(u + beta * np.log(p_exceed / tail_prob))

    return float(u + (beta / xi) * ((p_exceed / tail_prob) ** xi - 1))
