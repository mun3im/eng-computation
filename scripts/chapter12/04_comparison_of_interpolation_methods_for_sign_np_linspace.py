"""
Interpolation, Curve Fitting and Calibration - Increasing Signal Detail
Example: Comparison of Interpolation Methods for Signal Processing (Digital-to-Analog Converter)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, PchipInterpolator

# Load the DAC data from the CSV file
dac_data = pd.read_csv('dac_signal.csv')

# Extract time and amplitude from the CSV data
time = dac_data['Time(ms)'].values
amplitude = dac_data['Amplitude'].values

# Define the time points for interpolation (higher resolution)
time_interp = np.linspace(time.min(), time.max(), 50)

# Perform different interpolation methods
linear_interp = interp1d(time, amplitude, kind='linear')
nearest_interp = interp1d(time, amplitude, kind='nearest')
pchip_interp = PchipInterpolator(time, amplitude)
spline_interp = interp1d(time, amplitude, kind='cubic')

# Get the interpolated amplitudes for each method
amplitude_linear = linear_interp(time_interp)
amplitude_nearest = nearest_interp(time_interp)
amplitude_pchip = pchip_interp(time_interp)
amplitude_spline = spline_interp(time_interp)
