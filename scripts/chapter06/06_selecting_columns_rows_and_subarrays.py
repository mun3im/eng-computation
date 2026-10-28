"""
Arrays and Vectorized Computation - Subscripting Notation in NumPy
Subsection: Subscripting: Using the Colon Operator in NumPy
Example: Selecting Columns, Rows, and Subarrays

Output as printed in the book:
    A[:, j] - Selects the jth column of A:
    [ 20  60 100 140]
    
    A[i, :] - Selects the ith row of A:
    [10 20 30 40]
    
    A[:, :] - Selects all elements of A:
    [[ 10  20  30  40]
     [ 50  60  70  80]
     [ 90 100 110 120]
     [130 140 150 160]]
    
    A[:, j:k] - Selects all rows in columns from j to k-1:
    [[ 20  30]
     [ 60  70]
     [100 110]
     [140 150]]
"""

import numpy as np

# Creating a sample 2D array
A = np.array([[10, 20, 30, 40], [50, 60, 70, 80],
              [90, 100, 110, 120], [130, 140, 150, 160]])

# Example 1: Selects the jth column of the array A (j = 1)
j = 1
column_j = A[:, j]
print("A[:, j] - Selects the jth column of A:")
print(column_j)
# Output: [20, 60, 100, 140]

# Example 2: Selects the ith row of the array A (i = 0)
i = 0
row_i = A[i, :]
print("\nA[i, :] - Selects the ith row of A:")
print(row_i)
# Output: [10, 20, 30, 40]

# Example 3: Selects all elements of A
all_elements = A[:, :]
print("\nA[:, :] - Selects all elements of A:")
print(all_elements)

# Example 4: Selects all rows in columns from j to k-1 (exclusive) (j = 1, k = 3)
k = 3
subarray = A[:, j:k]
print("\nA[:, j:k] - Selects all rows in columns from j to k-1:")
print(subarray)
# Output: [[20, 30], [60, 70], [100, 110], [140, 150]]
