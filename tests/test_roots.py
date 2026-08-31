import math
from engineering_numerics import bisection, newton, secant


def test_root_methods_find_sqrt2():
    f = lambda x: x*x - 2
    df = lambda x: 2*x
    for result in [bisection(f, 0, 2), newton(f, df, 1), secant(f, 0, 2)]:
        assert result.converged
        assert abs(result.root - math.sqrt(2)) < 1e-8
