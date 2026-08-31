from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class LinearFit:
    slope: float
    intercept: float
    r_squared: float


def linear_least_squares(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if x.shape != y.shape or x.size < 2:
        raise ValueError("x and y must have the same shape and at least two points.")
    A = np.column_stack([x, np.ones_like(x)])
    slope, intercept = np.linalg.lstsq(A, y, rcond=None)[0]
    predicted = slope*x + intercept
    ss_res = np.sum((y-predicted)**2)
    ss_tot = np.sum((y-y.mean())**2)
    r2 = 1.0 if ss_tot == 0 and ss_res == 0 else 1.0 - ss_res/ss_tot
    return LinearFit(float(slope), float(intercept), float(r2))
