"""
Decisions and Repetition - Loops
Subsection: Returning Vectors as Output
Example: a (using append
Source: chapters/chapter4.tex, line 1037

Output as printed in the book:
    Q: [0.0, 1.0575, 1.9908, 2.8144]
    T: [0, 0.5, 1.0, 1.5]
"""

import math  # Import math for calculations
V = 9; R = 4; C = 1  # Set V, R, and C values
t = 0; q = 0  # Initialize time and charge
Q = []; T = []  # Lists for charge and time

# Loop until charge exceeds 2 units
while q <= 2:
    q = C * V * (1 - math.exp(-t / (R * C)))  # Calculate charge
    Q.append(q); T.append(t)  # Store charge and time
    t += 0.5  # Increment time

# Display the charge and time, rounding charge to 4 decimal places
print("Q:", [round(val, 4) for val in Q])
print("T:", T)
