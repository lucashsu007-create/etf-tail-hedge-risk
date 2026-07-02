"""Public/dummy data loading.

This file is intentionally minimal. Before WRDS approval, use this only to test
pipeline mechanics, not to produce research claims.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def make_dummy_prices(
    n: int = 1_000,
    seed: int = 42,
    start: str = "2024-01-01 09:30",
    freq: str = "5min",
) -> pd.DataFrame:
    """Create synthetic near-substitute ETF price series for pipeline testing."""
    rng = np.random.default_rng(seed)
    index = pd.date_range(start=start, periods=n, freq=freq)

    common = rng.normal(0, 0.0008, size=n)
    noise_a = rng.normal(0, 0.00005, size=n)
    noise_b = rng.normal(0, 0.00007, size=n)

    r_a = common + noise_a
    r_b = 0.995 * common + noise_b

    prices = pd.DataFrame(
        {
            "ETF_A": 100 * (1 + pd.Series(r_a, index=index)).cumprod(),
            "ETF_B": 100 * (1 + pd.Series(r_b, index=index)).cumprod(),
        }
    )
    return prices
