"""
Arrays and Vectorized Computation - Vectorizing Formulas
Example: - Volume of Cones
Source: chapters/chapter6.tex, line 1000

Output as printed in the book:
    Number of samples: 101
    Time constant tau: 0.47 s
    v at t=0:   12.0000 V
    i at t=0:   2.5532 mA
    v at t=2s:  0.1703 V
"""

import numpy as np

V0   = 12.0        # initial capacitor voltage (V)
R    = 4700.0      # resistance (ohms)
C    = 100e-6      # capacitance (F)
tau  = R * C       # time constant = 0.47 s

# One array holding all 101 sample times, 20 ms apart
t = np.arange(0, 2.001, 0.02)

# Vectorized: every voltage and current computed in one expression each
v = V0 * np.exp(-t / tau)
i_mA = (v / R) * 1000

print(f"Number of samples: {t.size}")
print(f"Time constant tau: {tau:.2f} s")
print(f"v at t=0:   {v[0]:.4f} V")
print(f"i at t=0:   {i_mA[0]:.4f} mA")
print(f"v at t=2s:  {v[-1]:.4f} V")
