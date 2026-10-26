"""
Arrays and Vectorized Computation - Subscripting Notation in NumPy
Subsection: Slicing and Vectorization in NumPy
Example: Selecting a Range of Rows and Flattening a 2D Array
Source: chapters/chapter6.tex, line 596

Output as printed in the book:
    A[j:k] - Selects rows from index j to k-1:
    [[ 50  60  70  80]
     [ 90 100 110 120]]
    
    A[:] - Selects all elements of A, treating it as a single vector:
    [ 10  20  30  40  50  60  70  80  90 100 110 120 130 140 150 160]
"""

import numpy as np

# Creating a sample 2D array for additional examples
A = np.array([[10, 20, 30, 40], [50, 60, 70, 80],
              [90, 100, 110, 120], [130, 140, 150, 160]])

# Example 7: Selects rows from index j to k-1 (exclusive) (j = 1, k = 3)
j = 1
k = 3
selected_rows = A[j:k]
print("\nA[j:k] - Selects rows from index j to k-1:")
print(selected_rows)
# Output: [[50, 60, 70, 80], [90, 100, 110, 120]]

# Example 8: Selects all elements of A, treating it as a single vector
single_vector = A.flatten()  # Flattens the array into a 1D vector
print("\nA[:] - Selects all elements of A, treating it as a single vector:")
print(single_vector)
# Output: [10, 20, ..., 160]
