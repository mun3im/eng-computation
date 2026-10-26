"""
Data Visualization - Statistical Plots
Subsection: Grouped Box Plot
Source: chapters/chapter7.tex, line 733
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate random data for two groups
group1 = np.random.randn(100)
group2 = np.random.randn(100) + 2

# Create the grouped box plot
plt.boxplot([group1, group2])
plt.title('Grouped Box Plot')
plt.show()
