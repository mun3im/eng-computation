"""
Data Visualization - 2-D Line Plots
Subsection: Basic Line and Marker Styles
Source: chapters/chapter7.tex, line 183
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 501, 10)
y = np.sin(5 * x)
plt.plot(x, y, '-mo')
# '-mo' represents a magenta line with circle markers
plt.xlabel('x')
plt.ylabel('sin(5x)')
plt.title('Sine Wave Plot')
plt.show()
