"""
Numerical Calculus and System Models - Polynomials and System Models
Subsection: Vertical Displacement
Example: Analyzing Vertical Motion
"""

import numpy as np
import matplotlib.pyplot as plt

# Define constants
v = 30    # Initial velocity (m/s)
g = -9.8  # Acceleration due to gravity (m/s^2)

# Define the coefficients of the polynomial for displacement
# Corresponding to d = v*t + (g/2)*t^2
p = [g/2, v, 0]

# Find the roots of the polynomial
r = np.roots(p)

# The time when the object hits the ground (non-zero root)
tground = r[r != 0][0]
