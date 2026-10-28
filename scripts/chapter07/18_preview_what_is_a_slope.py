"""
Data Visualization - Preview: What Is a Slope?

Output as printed in the book:
    Average slope between x=0 and x=1: 1.0
    Average slope between x=3 and x=4: 7.0
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 100)
y = x**2

plt.plot(x, y, label='$y = x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Slope over two different intervals of the same curve
for x1, x2 in [(0, 1), (3, 4)]:
    slope = (x2**2 - x1**2) / (x2 - x1)
    print(f"Average slope between x={x1} and x={x2}: {slope}")
