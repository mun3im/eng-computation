"""
Complex Numbers as an Engineering Tool - Complex Numbers as Vectors
"""

import matplotlib.pyplot as plt

Z = 40 + 75.40j    # the R-L impedance computed above

plt.plot([0, Z.real], [0, 0], '--', label='R = 40 ohms')
plt.plot([Z.real, Z.real], [0, Z.imag], '--', label='X_L = 75.40 ohms')
plt.annotate('', xy=(Z.real, Z.imag), xytext=(0, 0),
             arrowprops=dict(arrowstyle='->', linewidth=2))   # Z itself
plt.xlabel('Real part (ohms)')
plt.ylabel('Imaginary part (ohms)')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
