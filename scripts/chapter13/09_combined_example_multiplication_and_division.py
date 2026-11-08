"""
Numerical Calculus and System Models - Combined Example: Multiplication and Division

Output as printed in the book:
    f(x) (multiplication result) = [  1   3  -5 -13   0 -10]
    g(x) (division result) = [1. 3.]
    Remainder = [ 5. 17.]
"""

import numpy as np

# Define the polynomials as vectors
p1 = [1, 3, 0, 2]   # Represents x^3 + 3x^2 + 2
p2 = [1, 0, -5]     # Represents x^2 - 5

# Polynomial multiplication to find f(x)
f_x = np.polymul(p1, p2)
print("f(x) (multiplication result) =", f_x)

# Polynomial division to find g(x)
g_x, remainder = np.polydiv(p1, p2)
print("g(x) (division result) =", g_x)
print("Remainder =", remainder)
