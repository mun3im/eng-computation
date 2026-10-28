"""
Numerical Calculus and System Models - Numerical Calculus
Subsection: Integration (Total Accumulation)

Output as printed in the book:
    Approximate area: 333.333500333834
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Create x values (independent variable)
x = np.linspace(0, 10, 1000)   # 1000 sample points from 0 to 10

# 2. Define the function y = x^2
y = x**2

# 3. Numerical integration using trapezoidal rule
area = np.trapezoid(y, x)

# 4. Print the result
print("Approximate area:", area)

# 5. Plot the function and shaded area
plt.plot(x, y, label="y = x²")
plt.fill_between(x, y, alpha=0.3)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Numerical Integration using np.trapezoid()")
plt.legend()
plt.show()
