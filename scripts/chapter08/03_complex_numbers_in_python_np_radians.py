"""
Complex Numbers as an Engineering Tool - Complex Numbers in Python

Output as printed in the book:
    |Z| = 5.00, angle = 53.13 degrees
    back to rectangular: 3.00 + 4.00j
"""

import numpy as np

Z = 3 + 4j

# Rectangular -> polar
magnitude = abs(Z)
angle_deg = np.degrees(np.angle(Z))
print(f"|Z| = {magnitude:.2f}, angle = {angle_deg:.2f} degrees")

# Polar -> rectangular
a = magnitude * np.cos(np.radians(angle_deg))
b = magnitude * np.sin(np.radians(angle_deg))
print(f"back to rectangular: {a:.2f} + {b:.2f}j")
