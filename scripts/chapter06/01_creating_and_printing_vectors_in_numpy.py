"""
Arrays and Vectorised Computation - Creating and Printing Vectors in NumPy

Output as printed in the book:
    Row Vector (1D):
    [1 2 3]

    Row Vector (2D):
    [[1 2 3]]

    Column Vector (2D):
    [[1]
     [2]
     [3]]
"""

import numpy as np

# Creating a row vector (1D)
row_vector_1d = np.array([1, 2, 3])

# Creating a row vector (2D)
row_vector_2d = np.array([[1, 2, 3]])  # 2D row vector

# Creating a column vector (2D)
column_vector_2d = np.array([[1], [2], [3]])

# Print the vectors
print("Row Vector (1D):")
print(row_vector_1d)
# Output: array([1, 2, 3])

print("\nRow Vector (2D):")
print(row_vector_2d)
# Output: array([[1, 2, 3]])

print("\nColumn Vector (2D):")
print(column_vector_2d)
# Output: array([[1], [2], [3]])
