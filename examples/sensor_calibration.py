from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from engineering_numerics import linear_least_squares


def main():
    mass_kg = np.array([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
    adc = np.array([468520, 574200, 680050, 785610, 891690, 997180, 1103100])
    fit = linear_least_squares(mass_kg, adc)
    print(f"Sensitivity: {fit.slope:.2f} counts/kg")
    print(f"Zero offset: {fit.intercept:.2f} counts")
    print(f"R²: {fit.r_squared:.6f}")

    x = np.linspace(0, 3, 100)
    fig, ax = plt.subplots(figsize=(8.5, 5))
    ax.scatter(mass_kg, adc, label='Calibration data')
    ax.plot(x, fit.slope*x + fit.intercept, label='Least-squares fit')
    ax.set_xlabel('Mass [kg]')
    ax.set_ylabel('ADC counts')
    ax.set_title('Load-Cell Calibration by Linear Least Squares')
    ax.grid(True, alpha=0.25)
    ax.legend()
    fig.tight_layout()
    out = Path(__file__).resolve().parents[1]/'assets'/'sensor_calibration.png'
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, dpi=180)


if __name__ == '__main__':
    main()
