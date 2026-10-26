"""
Arrays and Vectorized Computation - Array (Element-wise) Operations
Example: - Array Attributes
Source: chapters/chapter6.tex, line 765

Output as printed in the book:
    Array A:
    [[1 2]
     [3 4]]
    Shape of the array (rows, columns):
    (2, 2)
"""

import numpy as np

# Define an array (2x2)
A = np.array([[1, 2], [3, 4]])
print("Array A:")
print(A)

# Shape of the array (rows, columns)
array_shape = A.shape
print("\nShape of the array (rows, columns):")
print(array_shape)  # (2, 2)
