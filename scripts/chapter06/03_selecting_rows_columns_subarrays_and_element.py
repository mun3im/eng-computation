"""
Arrays and Vectorized Computation - Subscripting Notation in NumPy
Example: Selecting Rows, Columns, Subarrays, and Elements with Different Step Sizes
Source: chapters/chapter6.tex, line 297

Output as printed in the book:
    First Row:
    [1 2 3]
    
    First Column:
    [1 4 7]
    
    Subarray (0:2, 1:3):
    [[2 3]
     [5 6]]
    
    array[0:0:1] - Selecting from index 0 to 0 (exclusive):
    []
    
    array[::1] - Selecting every element:
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    
    Every Second Row:
    [[1 2 3]
     [7 8 9]]
"""

import numpy as np

# Creating a sample 2D array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Example 1: Selecting a specific row
first_row = array[0, :]
print("First Row:")
print(first_row)
# Output: array([1, 2, 3])

# Example 2: Selecting a specific column
first_column = array[:, 0]
print("\nFirst Column:")
print(first_column)
# Output: array([1, 4, 7])

# Example 3: Slicing a subarray (2x2)
subarray = array[0:2, 1:3]
print("\nSubarray (0:2, 1:3):")
print(subarray)
# Output: array([[2, 3], [5, 6]])

# Example 4: Selecting with various slicing notations
# a. Using array[0:0:1]
slice_0_0_1 = array[0:0:1]
print("\narray[0:0:1] - Selecting from index 0 to 0 (exclusive):")
print(slice_0_0_1)
# Output: []

# b. Using array[::1]
slice_double_colon_1 = array[::1]
print("\narray[::1] - Selecting every element:")
print(slice_double_colon_1)
# Output: array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# c. Selecting with step (every second row)
every_second_row = array[::2]  # Selects every second row
print("\nEvery Second Row:")
print(every_second_row)
# Output: array([[1, 2, 3]])
