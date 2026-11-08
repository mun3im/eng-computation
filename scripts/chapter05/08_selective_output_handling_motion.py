"""
Functions and Reusable Calculations - Selective Output Handling
"""

# Define a function that returns multiple outputs
def motion(t):
    # Motion from rest with constant velocity a = 2 m/s^2
    a = 2.0
    distance = [0.5 * a * ti ** 2 for ti in t]   # s = a t^2 / 2
    velocity = [a * ti for ti in t]               # v = a t
    return distance, velocity

# Calling the function with t as input
t = [0, 0.5, 1.0, 1.5, 2.0]

# Case 1: Requesting both outputs
distance, velocity = motion(t)  # Unpacking both outputs
print("Distance:", distance)
# Output: Distance: [0.0, 0.25, 1.0, 2.25, 4.0]
print("Velocity:", velocity)
# Output: Velocity: [0.0, 1.0, 2.0, 3.0, 4.0]
