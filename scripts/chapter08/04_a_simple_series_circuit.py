"""
Complex Numbers as an Engineering Tool - A Simple Series Circuit
Source: chapters/chapter8.tex, line 169

Output as printed in the book:
    Resistor Impedance:  40.0 Ohms
    Inductor Impedance:  75.40j Ohms
    Total Impedance (Z): 40.0 + 75.40j Ohms
    Impedance Magnitude: 85.35 Ohms
    Phase Angle (theta): 62.1 degrees
"""

import numpy as np

# 1. Define physical component values
R = 40.0       # Ohms
L = 0.2        # Henries (200 mH)
f = 60.0       # Frequency in Hz

# 2. Compute angular frequency (omega = 2 * pi * f)
omega = 2 * np.pi * f

# 3. Compute complex impedances
Z_R = R
Z_L = 1j * omega * L         # +j*w*L

# 4. Total series impedance is simply the sum
Z_total = Z_R + Z_L

# 5. Output results
print(f"Resistor Impedance:  {Z_R:.1f} Ohms")
print(f"Inductor Impedance:  {Z_L:.2f}j Ohms")
print(f"Total Impedance (Z): {Z_total.real:.1f} + {Z_total.imag:.2f}j Ohms")
print(f"Impedance Magnitude: {np.abs(Z_total):.2f} Ohms")
print(f"Phase Angle (theta): {np.degrees(np.angle(Z_total)):.1f} degrees")
