"""
Numerical Calculus and System Models - Numerical Calculus
Subsection: The Mathematical Gradient
Source: chapters/chapter13.tex, line 215

Output as printed in the book:
    i_measured[0]   = 2.5532 mA
    i_from_slope[0] = 2.4996 mA
    Largest disagreement: 0.0536 mA
"""

import numpy as np

C = 100e-6                        # capacitance (F)
t = np.arange(0, 2.001, 0.02)
v = 12.0 * np.exp(-t / 0.47)      # stands in for the voltage_V column
i_measured = (v / 4700.0) * 1000  # stands in for the current_mA column

# Differentiate the voltage: i = -C dv/dt   (mA)
i_from_slope = -C * np.gradient(v, t) * 1000

print(f"i_measured[0]   = {i_measured[0]:.4f} mA")
print(f"i_from_slope[0] = {i_from_slope[0]:.4f} mA")
print(f"Largest disagreement: {np.max(np.abs(i_from_slope - i_measured)):.4f} mA")
