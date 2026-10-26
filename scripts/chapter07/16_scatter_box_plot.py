"""
Data Visualization - Statistical Plots
Subsection: Scatter Box Plot
Source: chapters/chapter7.tex, line 784
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100)
plt.figure()
plt.boxplot(data, widths=0.5)

num_data_points = len(data)
x = np.ones(num_data_points)
x_jittered = x + 0.2 * np.random.randn(num_data_points)

plt.scatter(x_jittered, data, marker='.', edgecolor='b',
            facecolor='b', linewidth=1)
plt.title('Scatter Box Plot')
plt.xlabel('Data')
plt.ylabel('Values')
plt.show()
