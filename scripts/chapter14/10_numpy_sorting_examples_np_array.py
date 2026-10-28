"""
Engineering Statistics and Data Analysis - Data Sorting
Subsection: Sorting in NumPy
Example: NumPy Sorting Examples

Output as printed in the book:
    Sorted 1D Array: [2 3 6 7 8]
    
    Sorted 2D Array by Columns (ascending):
     [[3 2 2]
     [6 5 7]]
"""

import numpy as np

# Example 1: Sorting a 1D Array
x = np.array([6, 3, 7, 2, 8])
y = np.sort(x)
print("Sorted 1D Array:", y)

# Example 2: Sorting a 2D Array by Columns
X = np.array([[3, 5, 2], [6, 2, 7]])
Ycol = np.sort(X, axis=0)
print("\nSorted 2D Array by Columns (ascending):\n", Ycol)
