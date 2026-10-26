"""
Functions and Reusable Calculations - User-Defined Functions
Subsection: Selective Output Handling
Source: chapters/chapter5.tex, line 425
"""

# Define a function that returns multiple outputs
def motion(t):
    # Example calculations for demonstration
    distance = [0.0001 * i ** 2 for i in t]
    acceleration = [0.0025 * i ** 2 for i in t]
    return distance, acceleration

# Calling the function with t as input
t = [0, 0.1, 0.2, 0.3, 0.4, 0.5]

# Case 1: Requesting both outputs
distance, acceleration = motion(t)  # Unpacking both outputs
print("Distance:", distance)
# Output: Distance: [0.0, 1e-06, 4e-06, 9e-06, 1.6e-05, 2.5e-05]
print("Acceleration:", acceleration)
# Output: Acceleration: [0.0, 2.5e-05, 1e-04, 2.25e-04, 4e-04, 6.25e-04]
