"""
Numerical Calculus and System Models - Polynomial Multiplication

Output as printed in the book:
    [ 2  7 10  8]
"""

import numpy as np

# Define two polynomials
p1 = [2, 3, 4]  # 2x^2 + 3x + 4
p2 = [1, 2]     # x + 2

# Multiply the polynomials
result = np.polymul(p1, p2)
print(result)
