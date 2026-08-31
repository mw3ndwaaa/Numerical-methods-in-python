from dataclasses import dataclass


@dataclass(frozen=True)
class RootResult:
    root: float
    iterations: int
    residual: float
    converged: bool


def bisection(f, a: float, b: float, tol: float = 1e-10, max_iter: int = 100):
    fa, fb = f(a), f(b)
    if fa == 0:
        return RootResult(a, 0, 0.0, True)
    if fb == 0:
        return RootResult(b, 0, 0.0, True)
    if fa * fb > 0:
        raise ValueError("Bisection requires a sign change over [a, b].")
    for k in range(1, max_iter + 1):
        c = 0.5 * (a + b)
        fc = f(c)
        if abs(fc) <= tol or 0.5 * abs(b-a) <= tol:
            return RootResult(c, k, abs(fc), True)
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    c = 0.5 * (a+b)
    return RootResult(c, max_iter, abs(f(c)), False)


def newton(f, df, x0: float, tol: float = 1e-10, max_iter: int = 50):
    x = float(x0)
    for k in range(1, max_iter + 1):
        fx, dfx = f(x), df(x)
        if abs(fx) <= tol:
            return RootResult(x, k-1, abs(fx), True)
        if abs(dfx) < 1e-15:
            raise ZeroDivisionError("Derivative is too close to zero in Newton iteration.")
        x -= fx / dfx
    return RootResult(x, max_iter, abs(f(x)), False)


def secant(f, x0: float, x1: float, tol: float = 1e-10, max_iter: int = 50):
    f0, f1 = f(x0), f(x1)
    for k in range(1, max_iter + 1):
        denom = f1 - f0
        if abs(denom) < 1e-15:
            raise ZeroDivisionError("Secant slope is too close to zero.")
        x2 = x1 - f1 * (x1 - x0) / denom
        f2 = f(x2)
        if abs(f2) <= tol or abs(x2-x1) <= tol:
            return RootResult(float(x2), k, abs(f2), True)
        x0, f0, x1, f1 = x1, f1, x2, f2
    return RootResult(float(x1), max_iter, abs(f1), False)
