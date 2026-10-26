"""
NumPy Reference - Detailed Comparison of np.array
Source: appendices/appendixB.tex, line 63

Output as printed in the book:
    2D Matrix:
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    
    Row Matrix (1x3):
    [[1 2 3]]
    
    Column Matrix (3x1):
    [[1]
     [2]
     [3]]
"""

import numpy as np

# Creating a 2D matrix
matrix_2d = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Creating a row matrix (1x3)
row_matrix = np.matrix([[1, 2, 3]])

# Creating a column matrix (3x1)
column_matrix = np.matrix([[1], [2], [3]])

# Print the matrices
print("2D Matrix:")
print(matrix_2d)
# Output: matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("\nRow Matrix (1x3):")
print(row_matrix)
# Output: matrix([[1, 2, 3]])

print("\nColumn Matrix (3x1):")
print(column_matrix)
# Output: matrix([[1], [2], [3]])
