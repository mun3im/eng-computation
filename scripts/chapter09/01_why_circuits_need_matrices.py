"""
Matrices and Circuit Equations - Why Circuits Need Matrices

Output as printed in the book:
    I1 = 60.345 mA
    I2 = 33.229 mA
"""

import numpy as np

R1, R2, R3 = 100.0, 220.0, 330.0    # ohms
V1, V2 = 12.0, 5.0                  # volts

# Build the coefficient matrix A and the source vector b
A = np.array([[R1 + R2, -R2],
              [-R2,     R2 + R3]])
b = np.array([V1, V2])

# Solve A x = b for the loop currents
I = np.linalg.solve(A, b)

print(f"I1 = {I[0]*1000:.3f} mA")
print(f"I2 = {I[1]*1000:.3f} mA")
