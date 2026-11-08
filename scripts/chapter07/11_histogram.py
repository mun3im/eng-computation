"""
Data Visualisation - Histogram
"""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)   # fixed seed: the same data every run
data = rng.standard_normal(1000)
plt.hist(data, bins=50)
plt.xlabel('Data Value')
plt.ylabel('Frequency')
plt.title('Histogram as part of EDA')
plt.show()
