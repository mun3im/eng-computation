"""
Data Visualization - Statistical Plots
Subsection: Basic Box Plot
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100, 3)
plt.figure()
plt.boxplot(data)
plt.title('Basic Box Plot')
plt.show()
