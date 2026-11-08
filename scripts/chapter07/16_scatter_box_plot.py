"""
Data Visualisation - Scatter Box Plot
"""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)   # fixed seed: the same data every run
data = rng.standard_normal(100)
plt.figure()
plt.boxplot(data, widths=0.5)

num_data_points = len(data)
x = np.ones(num_data_points)
x_jittered = x + 0.2 * rng.standard_normal(num_data_points)

plt.scatter(x_jittered, data, marker='.', edgecolor='b',
            facecolor='b', linewidth=1)
plt.title('Scatter Box Plot')
plt.xlabel('Data')
plt.ylabel('Values')
plt.show()
