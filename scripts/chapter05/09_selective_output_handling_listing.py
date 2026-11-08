"""
Functions and Reusable Calculations - Selective Output Handling
"""

# Case 2a: Requesting only the first output
distance = motion(t)[0]  # Getting only the first output
print("Distance:", distance)
# Output: Distance: [0.0, 0.25, 1.0, 2.25, 4.0]

# Case 2b: Requesting only the first output
distance, _ = motion(t)  # Getting only the first output
print("Distance:", distance)
# Output: Distance: [0.0, 0.25, 1.0, 2.25, 4.0]

# Case 3: Requesting only the second output
_, velocity = motion(t)  # Unpacking, discarding the first output
print("Velocity:", velocity)
# Output: Velocity: [0.0, 1.0, 2.0, 3.0, 4.0]
