"""
Measurements, Files and Spreadsheets - Importing and Exporting Data in Python
Subsection: Binary Data
Source: chapters/chapter10.tex, line 328
"""

import numpy as np

# Saving a NumPy array to a binary file
array = np.array([1, 2, 3])
np.save('array.npy', array)

# Loading a NumPy array from a binary file
loaded_array = np.load('array.npy')
print(loaded_array)  # Output: [1 2 3]
