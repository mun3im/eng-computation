"""
Numerical Calculus and System Models - Numerical Calculus
Subsection: Bridge: Slopes and Sums in the Lab (An Intuitive Calculus Preview)

Output as printed in the book:
    Accumulated charge (Ah): [2.  4.  5.6 6.8 7.6 8. ]
    Recovered charging rate (A): [2.  1.6 1.2 0.8 0.4]
"""

import numpy as np

# Measured charging current, tapering off as the battery fills
# (typical constant-current/constant-voltage charging profile)
t = np.array([0, 1, 2, 3, 4, 5])          # hours
I = np.array([2.0, 2.0, 1.6, 1.2, 0.8, 0.4])  # amps

# ADDITION: summing current over time accumulates
# total charge delivered
Q = np.cumsum(I)   # amp-hours (dt = 1 hour, so no extra multiplication needed)
print("Accumulated charge (Ah):", Q)

# SUBTRACTION: differencing the accumulated charge recovers
# the charging rate
dq = np.diff(Q)
print("Recovered charging rate (A):", dq)
