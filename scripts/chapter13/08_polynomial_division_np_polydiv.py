"""
Numerical Calculus and System Models - Polynomials and System Models
Subsection: Polynomial Division
Example: Polynomial Division
Source: chapters/chapter13.tex, line 486
"""

import numpy as np

# Define two polynomials
p1 = [2, 3, 4]  # 2x^2 + 3x + 4
p2 = [1, 2]     # x + 2

# Divide the polynomials
quotient, remainder = np.polydiv(p1, p2)
print("Quotient:", quotient)
print("Remainder:", remainder)
