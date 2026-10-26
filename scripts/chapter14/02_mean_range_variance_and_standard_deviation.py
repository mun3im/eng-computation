"""
Engineering Statistics and Data Analysis - Understanding Engineering Measurements
Subsection: Mean, Range, Variance and Standard Deviation
Source: chapters/chapter14.tex, line 108

Output as printed in the book:
    Mean:               100.24 ohms
    Range:              3.90 ohms
    Standard deviation: 1.36 ohms
"""

import numpy as np

# ohms
readings = np.array([98.2, 101.5, 99.7, 100.3, 102.1, 99.1, 100.8])

print(f"Mean:               {np.mean(readings):.2f} ohms")
print(f"Range:              {np.ptp(readings):.2f} ohms")
print(f"Standard deviation: {np.std(readings, ddof=1):.2f} ohms")
