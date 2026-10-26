"""
Engineering Statistics and Data Analysis - Data Sorting
Subsection: Sorting in NumPy
Example: Finding the Top 2 Highest and Lowest Temperatures with Day
Source: chapters/chapter14.tex, line 504
"""

import numpy as np

# Temperature values for 9 consecutive days
x = np.array([19, 20, 18, 17, 20, 23, 25, 24, 23])

# Sort and find indices for the 2 highest and 2 lowest temperatures
sorted_x_desc = np.sort(x)[::-1]  # Sort in descending order
sorted_x_asc = np.sort(x)         # Sort in ascending order

# Highest 2 values and their respective days
highest_values = sorted_x_desc[:2]
highest_indices = np.argsort(x)[::-1][:2] + 1  # Days are indices + 1

# Lowest 2 values and their respective days
lowest_values = sorted_x_asc[:2]
lowest_indices = np.argsort(x)[:2] + 1  # Days are indices + 1
