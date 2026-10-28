"""
Engineering Statistics and Data Analysis - Understanding Engineering Measurements
Subsection: Population and Sample

Output as printed in the book:
    Population variance: 1.5881632653061184
    Sample variance:     1.852857142857138
"""

import numpy as np

# ohms
readings = np.array([98.2, 101.5, 99.7, 100.3, 102.1, 99.1, 100.8])

# divides by N
print("Population variance:", np.var(readings))

# divides by N-1
print("Sample variance:    ", np.var(readings, ddof=1))
