from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from engineering_numerics import rk4


def main():
    ambient = 25.0
    k = 0.08
    T0 = 90.0
    f = lambda t, T: -k*(T-ambient)
    t, T = rk4(f, (0.0, 60.0), T0, dt=0.5)
    exact = ambient + (T0-ambient)*np.exp(-k*t)
    max_error = np.max(np.abs(T-exact))
    print(f"Maximum RK4 error: {max_error:.6e} °C")

    fig, ax = plt.subplots(figsize=(8.5, 5))
    ax.plot(t, T, label='RK4')
    ax.plot(t, exact, '--', label='Analytical solution')
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Temperature [°C]')
    ax.set_title("Newton's Law of Cooling: RK4 Verification")
    ax.grid(True, alpha=0.25)
    ax.legend()
    fig.tight_layout()
    out = Path(__file__).resolve().parents[1]/'assets'/'cooling_rk4.png'
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, dpi=180)


if __name__ == '__main__':
    main()
