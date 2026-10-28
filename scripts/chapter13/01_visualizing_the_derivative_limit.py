"""
Numerical Calculus and System Models - Numerical Calculus
Subsection: Visualizing the Derivative Limit

Output as printed in the book:
    Exact derivative (cos(pi/4)): 0.707107
    
             h   Approximation        Error
           0.5        0.504886     0.202221
           0.1        0.670603     0.036504
          0.01        0.703559     0.003548
         0.001        0.706752     0.000355
        0.0001        0.707072     0.000035
"""

import numpy as np

x = np.pi / 4
exact = np.cos(x)  # Analytical derivative of sin(x) at x = pi/4

print(f"Exact derivative (cos(pi/4)): {exact:.6f}\n")
print(f"{'h':>10} {'Approximation':>15} {'Error':>12}")

h_values = [0.5, 0.1, 0.01, 0.001, 0.0001]
for h in h_values:
    approx = (np.sin(x + h) - np.sin(x)) / h
    error = abs(approx - exact)
    print(f"{h:>10} {approx:>15.6f} {error:>12.6f}")
