"""
Data Visualisation - Grouped Box Plot
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate random data for two groups
rng = np.random.default_rng(0)
group1 = rng.standard_normal(100)
group2 = rng.standard_normal(100) + 2

# Create the grouped box plot
plt.boxplot([group1, group2])
plt.title('Grouped Box Plot')
plt.show()
