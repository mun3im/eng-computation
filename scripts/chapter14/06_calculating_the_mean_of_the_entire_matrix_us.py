"""
Engineering Statistics and Data Analysis - Basic Statistical Analysis
Subsection: Choosing an Axis for Matrix Statistics
Example: Calculating the Mean of the Entire Matrix Using NumPy
"""

import numpy as np

# Define the matrix
x = np.array([[1, 3], [2, 5], [6, 4]])

# Compute the mean of the entire matrix
mean_all = np.mean(x)
print("Mean of entire matrix:", mean_all)
