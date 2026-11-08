"""
Arrays and Vectorised Computation - Selecting Values with a Boolean Mask
"""

import numpy as np

v = np.array([11.8, 12.1, 12.6, 11.4, 12.3])   # supply-rail readings (V)

in_tol = (v >= 11.5) & (v <= 12.5)   # parentheses are required
print(in_tol)          # [ True  True False False  True]
print(v[in_tol])       # [11.8 12.1 12.3]  -- only the good readings
print(in_tol.sum())    # 3  -- True counts as 1
