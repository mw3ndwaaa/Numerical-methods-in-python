import numpy as np


def trapezoidal(f, a: float, b: float, n: int = 100):
    if n < 1:
        raise ValueError("n must be at least 1.")
    x = np.linspace(a, b, n+1)
    y = np.asarray([f(xi) for xi in x], dtype=float)
    h = (b-a)/n
    return h * (0.5*y[0] + y[1:-1].sum() + 0.5*y[-1])


def simpson(f, a: float, b: float, n: int = 100):
    if n < 2 or n % 2:
        raise ValueError("Simpson's rule requires a positive even n >= 2.")
    x = np.linspace(a, b, n+1)
    y = np.asarray([f(xi) for xi in x], dtype=float)
    h = (b-a)/n
    return h/3.0 * (y[0] + y[-1] + 4*y[1:-1:2].sum() + 2*y[2:-1:2].sum())
