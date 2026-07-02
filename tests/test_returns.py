import pandas as pd

from src.features.returns import compute_simple_returns


def test_compute_simple_returns():
    prices = pd.Series([100, 101, 102.01])
    returns = compute_simple_returns(prices)
    assert len(returns) == 2
    assert round(float(returns.iloc[0]), 4) == 0.01
