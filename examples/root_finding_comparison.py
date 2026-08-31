from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from engineering_numerics import bisection, newton, secant


def main():
    # Nonlinear spring equilibrium: k*x + alpha*x^3 = F
    k, alpha, F = 120.0, 850.0, 35.0
    f = lambda x: k*x + alpha*x**3 - F
    df = lambda x: k + 3*alpha*x**2

    methods = {
        'Bisection': bisection(f, 0.0, 1.0),
        'Newton': newton(f, df, 0.2),
        'Secant': secant(f, 0.0, 0.5),
    }
    for name, result in methods.items():
        print(f"{name:10s}: x = {result.root:.8f} m, iterations = {result.iterations}, residual = {result.residual:.3e}")

    x = np.linspace(0, 0.5, 400)
    y = [f(v) for v in x]
    fig, ax = plt.subplots(figsize=(8.5, 5))
    ax.plot(x, y, label='Equilibrium residual')
    ax.axhline(0, linewidth=1)
    ax.scatter([methods['Newton'].root], [0], zorder=3, label='Solved equilibrium')
    ax.set_xlabel('Displacement x [m]')
    ax.set_ylabel('k x + α x³ - F [N]')
    ax.set_title('Nonlinear Spring Equilibrium Root')
    ax.grid(True, alpha=0.25)
    ax.legend()
    fig.tight_layout()
    out = Path(__file__).resolve().parents[1]/'assets'/'nonlinear_spring_root.png'
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, dpi=180)


if __name__ == '__main__':
    main()
