"""
Arrays and Vectorized Computation - Subscripting Notation in NumPy
Subsection: Creating Arrays: linspace
Example: Using linspace

Output as printed in the book:
    Array created with linspace:
    [0.   0.25 0.5  0.75 1.  ]
    
    Array created with arange:
    [0.   0.25 0.5  0.75 1.  ]
"""

import numpy as np

# Example 1: Using numpy.linspace
# Creating an array of 5 evenly spaced values from 0 to 1
linspace_array = np.linspace(0, 1, num=5)
print("Array created with linspace:")
print(linspace_array)
# Output: [0. 0.25 0.5 0.75 1. ]

# Example 2: Using numpy.arange
# Creating an array of numbers from 0 to 1 with a step of 0.25
arange_array = np.arange(0, 1.25, 0.25)  # Note that 1.25 is used to include 1
print("\nArray created with arange:")
print(arange_array)
# Output: [0. 0.25 0.5 0.75 1. ]
