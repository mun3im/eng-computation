"""
Handling Imperfect Engineering Data - Missing Data and Outliers
Subsection: Handling Missing Data
Example: Handling Missing Data and Interpolation
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Define a vector of nonuniform sample points and evaluate the sine function over the points
x1 = np.arange(-4*np.pi, 0, 0.1)
x2 = np.arange(0.1, 4*np.pi, 0.2)
x = np.concatenate([x1, x2])
A = np.sin(x)

# Inject NaN values into A
A[(A < 0.75) & (A > 0.5)] = np.nan

# Fill the missing data using linear interpolation
F = np.copy(A)
nans = np.isnan(A)
F[nans] = np.interp(x[nans], x[~nans], A[~nans])
