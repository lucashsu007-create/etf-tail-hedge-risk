import pandas as pd

from src.models.var_es import historical_var, historical_es


def test_historical_var_es():
    x = pd.Series([-5, -4, -3, 0, 1, 2, 3, 4, 5])
    var = historical_var(x, alpha=0.2)
    es = historical_es(x, alpha=0.2)
    assert var <= 0
    assert es <= var
