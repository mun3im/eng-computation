"""
Handling Imperfect Engineering Data - Missing Data and Outliers
Subsection: Data Imputation
Source: chapters/chapter11.tex, line 847

Output as printed in the book:
    Mean-filled: [12.5   12.975 13.1   12.9   12.975 13.4  ]
    Forward-filled: [12.5 12.5 13.1 12.9 12.9 13.4]
"""

import numpy as np

data = np.array([12.5, np.nan, 13.1, 12.9, np.nan, 13.4])

# Strategy 1: replace missing values with the overall mean
mean_value = np.nanmean(data)
filled_with_mean = np.where(np.isnan(data), mean_value, data)
print("Mean-filled:", filled_with_mean)

# Strategy 2: forward-fill -- repeat the last known good value
filled_with_ffill = data.copy()
for i in range(1, len(filled_with_ffill)):
    if np.isnan(filled_with_ffill[i]):
        filled_with_ffill[i] = filled_with_ffill[i - 1]
print("Forward-filled:", filled_with_ffill)
