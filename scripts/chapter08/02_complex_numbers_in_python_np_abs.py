"""
Complex Numbers as an Engineering Tool - Complex Numbers in Python
Source: chapters/chapter8.tex, line 97
"""

import numpy as np

Z = 3 + 4j

print("Real part:", Z.real)             # 3.0
print("Imaginary part:", Z.imag)        # 4.0

magnitude = abs(Z)                      # or np.abs(Z)
print(f"Magnitude: {magnitude:.2f}")    # 5.00

angle_rad = np.angle(Z)                 # radians
angle_deg = np.degrees(angle_rad)
print(f"Angle: {angle_deg:.2f} degrees") # 53.13
