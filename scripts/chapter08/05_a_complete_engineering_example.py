"""
Complex Numbers as an Engineering Tool - A Complete Engineering Example
Source: chapters/chapter8.tex, line 240

Output as printed in the book:
    Total Impedance (Z): 40.0 + 22.35j Ohms
    Impedance Magnitude: 45.82 Ohms
    Phase Angle (theta): 29.2 degrees
"""

import numpy as np

R = 40.0       # Ohms
L = 0.2        # Henries
C = 50e-6      # Farads
f = 60.0       # Hz

omega = 2 * np.pi * f

Z_R = R
Z_L = 1j * omega * L
Z_C = -1j / (omega * C)

Z_total = Z_R + Z_L + Z_C

print(f"Total Impedance (Z): {Z_total.real:.1f} + {Z_total.imag:.2f}j Ohms")
print(f"Impedance Magnitude: {np.abs(Z_total):.2f} Ohms")
print(f"Phase Angle (theta): {np.degrees(np.angle(Z_total)):.1f} degrees")
