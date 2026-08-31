import numpy as np
from engineering_numerics import rk4, linear_least_squares


def test_rk4_exponential_growth():
    t, y = rk4(lambda t, y: y, (0, 1), 1.0, 0.05)
    assert abs(y[-1] - np.e) < 1e-5


def test_linear_fit_recovers_exact_line():
    x = np.arange(5.0)
    y = 3*x + 2
    fit = linear_least_squares(x, y)
    assert abs(fit.slope - 3) < 1e-12
    assert abs(fit.intercept - 2) < 1e-12
    assert abs(fit.r_squared - 1) < 1e-12
