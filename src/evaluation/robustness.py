"""Robustness helpers."""

from __future__ import annotations

import pandas as pd


def split_by_stress(x: pd.Series, stress: pd.Series) -> tuple[pd.Series, pd.Series]:
    """Split a series into normal and stress samples."""
    aligned = pd.concat([x, stress], axis=1).dropna()
    values = aligned.iloc[:, 0]
    labels = aligned.iloc[:, 1].astype(int)

    normal = values[labels == 0]
    stressed = values[labels == 1]
    return normal, stressed
