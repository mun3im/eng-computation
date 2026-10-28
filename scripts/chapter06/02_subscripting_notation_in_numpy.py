"""
Arrays and Vectorized Computation - Subscripting Notation in NumPy
"""

import numpy as np

A = np.array([1, 2, 3, 4])
v = A[1:3]      # a view, not a copy
v[0] = 99
print(A)        # [ 1 99  3  4]  -- the original changed!

B = np.array([1, 2, 3, 4])
c = B[1:3].copy()   # ask explicitly for a copy
c[0] = 99
print(B)        # [1 2 3 4]  -- the original is safe
