import pandas as pd

from src.features.hedge_error import hedge_error


def test_hedge_error():
    r1 = pd.Series([0.01, 0.02, -0.01])
    r2 = pd.Series([0.005, 0.01, -0.005])
    beta = pd.Series([2.0, 2.0, 2.0])
    he = hedge_error(r1, r2, beta)
    assert all(abs(v) < 1e-12 for v in he)
