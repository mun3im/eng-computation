"""
Engineering Statistics and Data Analysis - Basic Statistical Analysis
Subsection: Choosing an Axis for Matrix Statistics
Example: Temperature Data Analysis with Python
Source: chapters/chapter14.tex, line 371
"""

import numpy as np
import pandas as pd
from datastat_module import datastat

# Load ydata from the CSV file
ydata = pd.read_csv('dataTemp1.csv').values

# Load daypersample from the text file
with open('daypersample.txt', 'r') as file:
    daypersample = float(file.read().strip())

# Generate xdata
xdata = np.arange(1, len(ydata[:, 0]) * daypersample + 1, daypersample)

# Call the datastat function
datastat(xdata, ydata, 'Days', 'Temperature', 'PLOT')
