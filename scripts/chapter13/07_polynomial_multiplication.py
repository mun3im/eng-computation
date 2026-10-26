"""
Numerical Calculus and System Models - Polynomials and System Models
Subsection: Polynomial Multiplication
Example: Polynomial Multiplication
Source: chapters/chapter13.tex, line 464
"""

import numpy as np

# Define two polynomials
p1 = [2, 3, 4]  # 2x^2 + 3x + 4
p2 = [1, 2]     # x + 2

# Multiply the polynomials
result = np.polymul(p1, p2)
print(result)
