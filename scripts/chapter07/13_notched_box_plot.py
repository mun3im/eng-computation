"""
Data Visualisation - Notched Box Plot
"""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)   # fixed seed: the same data every run
data = rng.standard_normal((100, 3))
plt.figure()
plt.boxplot(data, notch=True)
plt.title('Notch Box Plot')
plt.show()
