"""
Decisions and Repetition - Loops
Subsection: Returning Vectors as Output
Example: b (using +=

Output as printed in the book:
    Q: [0.0, 1.0575, 1.9908, 2.8144]
    T: [0, 0.5, 1.0, 1.5]
"""

import math  # Import math for calculations
V = 9; R = 4; C = 1  # Set V, R, and C values
t = 0; q = 0  # Initialize time and charge
Q = []; T = []  # Lists for charge and time
time_increment = 0.5

# Use a while loop to calculate charge and time until charge exceeds 2
while q <= 2:
    q = C * V * (1 - math.exp(-t / (R * C)))  # Calculate charge
    Q += [round(q, 4)]  # Add the rounded charge value to Q
    T += [t]  # Add the time value to T
    t += time_increment  # Increment time

# Display the charge and time lists
print("Q:", Q)
print("T:", T)
