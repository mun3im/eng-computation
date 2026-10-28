"""
Arrays and Vectorized Computation - Subscripting Notation in NumPy
Subsection: Reading Slice Notation on Rows
Example: Slicing Specific Rows from a 2D Array

Output as printed in the book:
    array[2:4] - Selecting rows from index 2 to 4 (exclusive):
    [[ 7  8  9]
     [10 11 12]]
    
    array[2:2] - Selecting rows from index 2 to 2 (exclusive):
    []
    
    array[1:3] - Selecting rows from index 1 to 3 (exclusive):
    [[4 5 6]
     [7 8 9]]
"""

import numpy as np

# Creating a sample 2D array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],
                   [10, 11, 12], [13, 14, 15]])

# Example 1: Slicing with array[2:4]
slice_2_4 = array[2:4]
print("array[2:4] - Selecting rows from index 2 to 4 (exclusive):")
print(slice_2_4)
# Output: [[7, 8, 9], [10, 11, 12]]

# Example 2: Slicing with array[2:2]
slice_2_2 = array[2:2]
print("\narray[2:2] - Selecting rows from index 2 to 2 (exclusive):")
print(slice_2_2)
# Output: []

# Example 3: Slicing with array[1:3]
slice_1_3 = array[1:3]
print("\narray[1:3] - Selecting rows from index 1 to 3 (exclusive):")
print(slice_1_3)
# Output: [[4, 5, 6], [7, 8, 9]]
