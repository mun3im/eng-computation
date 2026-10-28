"""
Interpolation, Curve Fitting and Calibration - Curve Fitting Using Polynomials
Subsection: EE Focus: Measuring the Time Constant of the Bench Circuit

Output as printed in the book:
    Fitted slope:      -2.12766 per second
    Measured tau:      0.4700 s
    Measured V0:       12.0000 V
"""

import numpy as np

# The measured discharge (loaded from bench_rc.csv in Chapter 10)
t = np.arange(0, 2.001, 0.02)
v = 12.0 * np.exp(-t / 0.47)      # stands in for the measured column

# Fit a straight line to ln(v) against t
slope, intercept = np.polyfit(t, np.log(v), 1)

tau_measured = -1 / slope
V0_measured  = np.exp(intercept)

print(f"Fitted slope:      {slope:.5f} per second")
print(f"Measured tau:      {tau_measured:.4f} s")
print(f"Measured V0:       {V0_measured:.4f} V")
