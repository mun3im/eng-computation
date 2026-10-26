"""
Handling Imperfect Engineering Data - Missing Data and Outliers
Subsection: Repairing a Signal by Interpolation
Source: chapters/chapter11.tex, line 659

Output as printed in the book:
    Number of missing samples: 7
    Max repair error vs. true signal: 0.165 deg C
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulate 20 seconds of a slowly oscillating temperature sensor reading
t = np.arange(0, 20, 0.5)
temp_true = 25 + 3 * np.sin(0.3 * t)

# Simulate a 3-second sensor dropout (e.g., a loose connector)
temp_measured = temp_true.copy()
dropout = (t >= 8) & (t <= 11)
temp_measured[dropout] = np.nan

# Locate and repair the dropout using linear interpolation
nans = np.isnan(temp_measured)
temp_repaired = temp_measured.copy()
temp_repaired[nans] = np.interp(t[nans], t[~nans], temp_measured[~nans])

print(f"Number of missing samples: {nans.sum()}")
print(f"Max repair error vs. true signal: {np.max(np.abs(temp_repaired - temp_true)):.3f} deg C")
