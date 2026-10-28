"""
Interpolation, Curve Fitting and Calibration - Curve Fitting Using Polynomials
Subsection: Data Trends
Example: Predicting Internet Usage with Polynomial Curve Fitting
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the provided Excel file, skipping the first row of labels
file_path = 'internetusage.xlsx'
df = pd.read_excel(file_path, skiprows=1)

# Extracting the usage data (rows are persons, columns are months)
data = df.iloc[:, 1:7].values  # Extract data from columns B to G

# Define months as a vector (1 to 6)
months = np.arange(1, 7)

# Replicate the month vector to match the shape of the data matrix (5 rows for 5 persons)
month_matrix = np.tile(months, (data.shape[0], 1))

# Apply polynomial fitting for each degree (1st, 2nd, 3rd)
p1 = np.polyfit(month_matrix.flatten(), data.flatten(), 1)
p2 = np.polyfit(month_matrix.flatten(), data.flatten(), 2)
p3 = np.polyfit(month_matrix.flatten(), data.flatten(), 3)
