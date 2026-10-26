"""
Interpolation, Curve Fitting and Calibration - Straight-Line Trendlines
Source: chapters/chapter12.tex, line 477

Output as printed in the book:
    Best-fit line: y = 2.01x + 1.03
    Fitted values: [ 1.03  3.04  5.05  7.05  9.06 11.07]
"""

import numpy as np

# Noisy laboratory measurements: y should roughly follow y = 2x + 1
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([1.1, 2.9, 5.2, 6.8, 9.3, 11.0])

# Fit a degree-1 (straight-line) polynomial: returns [slope, intercept]
m, b = np.polyfit(x, y, 1)
print(f"Best-fit line: y = {m:.2f}x + {b:.2f}")

# Evaluate the fitted line at the original x values (or any new ones)
y_fit = np.polyval([m, b], x)
print("Fitted values:", y_fit)
