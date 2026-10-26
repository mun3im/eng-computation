"""
Data Visualization - 2-D Line Plots
Subsection: 2-D Line Plot Example
Source: chapters/chapter7.tex, line 91
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y = np.exp(x / 2)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('exp(x/2)')
plt.title('Exponential Plot')
plt.show()
