"""
Matrices and Circuit Equations - What ``Solving'' a Matrix Equation Means
"""

import numpy as np

S = np.array([[1.0, 2.0],
              [2.0, 4.0]])
b = np.array([1.0, 2.0])

print(np.linalg.det(S))      # 0.0  -- singular
x = np.linalg.solve(S, b)    # raises LinAlgError: Singular matrix
