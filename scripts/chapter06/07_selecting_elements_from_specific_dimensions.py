"""
Arrays and Vectorized Computation - Subscripting Notation in NumPy
Subsection: Accessing Elements in Multi-Dimensional Arrays
Example: Selecting Elements from Specific Dimensions

Output as printed in the book:
    A[i, j, :] - Selects all elements in the ith row and jth column:
    [50 60]
    
    A[i, j, k, :] - Selects all elements in the specified dimensions:
    [110 120]
"""

import numpy as np

# Creating a sample 3D array for examples involving three dimensions
A_3d = np.array([[[10, 20], [30, 40]],
                  [[50, 60], [70, 80]],
                  [[90, 100], [110, 120]]])

# Example 5: In a three-dimensional array A, select all elements
# in the ith row and jth column
i = 1  # Second layer
j = 0  # First row
elements_3d = A_3d[i, j, :]  # : refers to the column
print("\nA[i, j, :] - Selects all elements in the ith row and jth column:")
print(elements_3d)
# Output: [50, 60]

# Example 6: Selects all elements in the specified dimensions
# for a four-dimensional array
A_4d = np.array([[[[10, 20], [30, 40]], [[50, 60], [70, 80]]],
                  [[[90, 100], [110, 120]], [[130, 140], [150, 160]]]])
i = 1  # Second block
j = 0  # First layer
k = 1  # Second row
elements_4d = A_4d[i, j, k, :]  # : refers to the column
print("\nA[i, j, k, :] - Selects all elements in the specified dimensions:")
print(elements_4d)
# Output: [110, 120]
