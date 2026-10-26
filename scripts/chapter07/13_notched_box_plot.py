"""
Data Visualization - Statistical Plots
Subsection: Notched Box Plot
Source: chapters/chapter7.tex, line 709
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100, 3)
plt.figure()
plt.boxplot(data, notch=True)
plt.title('Notch Box Plot')
plt.show()
