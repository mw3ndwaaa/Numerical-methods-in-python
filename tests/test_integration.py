import math
from engineering_numerics import trapezoidal, simpson


def test_simpson_integrates_cubic_exactly():
    value = simpson(lambda x: x**3, 0, 2, n=10)
    assert abs(value - 4.0) < 1e-12


def test_trapezoidal_converges_for_sine():
    value = trapezoidal(math.sin, 0, math.pi, n=2000)
    assert abs(value - 2.0) < 1e-6
