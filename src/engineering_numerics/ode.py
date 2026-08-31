import numpy as np


def rk4(f, t_span, y0, dt: float):
    t0, tf = map(float, t_span)
    if tf <= t0 or dt <= 0:
        raise ValueError("Require tf > t0 and dt > 0.")
    n = int(np.ceil((tf-t0)/dt))
    t = np.linspace(t0, tf, n+1)
    y0_arr = np.atleast_1d(np.asarray(y0, dtype=float))
    y = np.zeros((n+1, y0_arr.size), dtype=float)
    y[0] = y0_arr
    for k in range(n):
        h = t[k+1]-t[k]
        tk, yk = t[k], y[k]
        k1 = np.atleast_1d(f(tk, yk))
        k2 = np.atleast_1d(f(tk+h/2, yk+h*k1/2))
        k3 = np.atleast_1d(f(tk+h/2, yk+h*k2/2))
        k4 = np.atleast_1d(f(tk+h, yk+h*k3))
        y[k+1] = yk + h*(k1+2*k2+2*k3+k4)/6
    return t, y[:, 0] if y0_arr.size == 1 else y
