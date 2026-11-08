"""
Engineering Statistics and Data Analysis - Calculating Mean Along Rows and Columns Using NumPy

Output as printed in the book:
    Mean along columns: [3. 4.]
    Mean along rows: [2.  3.5 5. ]
"""

import numpy as np

# Define the matrix
x = np.array([[1, 3], [2, 5], [6, 4]])

# Mean along columns (axis=0 for column-wise operation)
mean_column = np.mean(x, axis=0)

# Mean along rows (axis=1 for row-wise operation)
mean_row = np.mean(x, axis=1)

print("Mean along columns:", mean_column)
print("Mean along rows:", mean_row)
