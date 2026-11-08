"""
Data Visualisation - Basic Line and Marker Styles
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(5 * x)
plt.plot(x, y, '-mo')
# '-mo' represents a magenta line with circle markers
plt.xlabel('x')
plt.ylabel('sin(5x)')
plt.title('Sine Wave Plot')
plt.show()
