"""
Arrays and Vectorized Computation - Vectorizing Formulas
Example: - Volume of Cones
Source: chapters/chapter6.tex, line 974

Output as printed in the book:
    Volumes of cones using vectorization:
    [  9.4248  39.2699 102.6254 212.0575 380.1327]
"""

import numpy as np

# Define arrays of diameters and heights for 5 different cones
D = np.array([3, 5, 7, 9, 11])   # Example diameters
H = np.array([4, 6, 8, 10, 12])  # Example heights

# Calculate the volumes using vectorized operations
V = (1/12) * np.pi * D**2 * H

# Display the calculated volumes
print("Volumes of cones using vectorization:")
print(np.round(V, 4))  # Rounded to four decimal places
