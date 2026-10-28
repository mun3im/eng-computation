"""
Interpolation, Curve Fitting and Calibration - Curve Fitting Using Polynomials
Subsection: Data Modelling
Example: Polynomial Curve Fitting with R-Squared Evaluation for Water Usage Prediction
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from Excel, skipping the first row
file_path = 'waterusage.xlsx'  # Ensure the file path is correct
df = pd.read_excel(file_path, usecols='B:C', skiprows=1)

# Extract day and water usage data
day, water = df.iloc[:, 0].values, df.iloc[:, 1].values

# Define the number of polynomial degrees to fit
N = 5
# Fit and evaluate in one line
water_fit = [np.polyval(np.polyfit(day, water, n), day) for n in range(1, N + 1)]
labels = ['Measured Data'] + [f'Polynomial Order = {n}' for n in range(1, N + 1)]
