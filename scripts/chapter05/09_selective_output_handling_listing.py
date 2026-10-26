"""
Functions and Reusable Calculations - User-Defined Functions
Subsection: Selective Output Handling
Source: chapters/chapter5.tex, line 446
"""

# Case 2a: Requesting only the first output
distance = motion(t)[0]  # Getting only the first output
print("Distance:", distance)
# Output: Distance: [0.0, 1e-06, 4e-06, 9e-06, 1.6e-05, 2.5e-05]

# Case 2b: Requesting only the first output
distance, _ = motion(t)  # Getting only the first output
print("Distance:", distance)
# Output: Distance: [0.0, 1e-06, 4e-06, 9e-06, 1.6e-05, 2.5e-05]

# Case 3: Requesting only the second output
_, acceleration = motion(t)  # Unpacking, discarding the first output
print("Acceleration:", acceleration)
# Output: Acceleration: [0.0, 2.5e-05, 1e-04, 2.25e-04, 4e-04, 6.25e-04]
