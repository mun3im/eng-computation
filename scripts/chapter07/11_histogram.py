"""
Data Visualization - Statistical Plots
Subsection: Histogram
Source: chapters/chapter7.tex, line 660
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)
plt.hist(data, bins=50)
plt.xlabel('Data Value')
plt.ylabel('Frequency')
plt.title('Histogram as part of EDA')
plt.show()
