"""
Engineering Statistics and Data Analysis - Temperature Data Analysis with Python

Output as printed in the book:
    Temperature data:-
                  Average  Variance    Median       Max       Min
    Dataset 1 :     11.97      6.10     12.00     19.00      8.00
    Dataset 2 :      8.23      3.01      8.00     12.00      5.00
    Dataset 3 :     19.87      4.82     20.00     24.00     15.00
    Overall   :     13.35      4.64     12.00     24.00      5.00
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
