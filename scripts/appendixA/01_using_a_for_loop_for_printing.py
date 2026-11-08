"""
Python Reference - Using a for Loop for Printing

Output as printed in the book:
    ω         sin(ω)
    0.0π      0.000
    0.5π      1.000
    1.0π      0.000
    1.5π     -1.000
"""

import math

# Define the values for w and s similar to MATLAB
w = [0, math.pi/2, math.pi, 3*math.pi/2]
s = [math.sin(wi) for wi in w]  # Calculate sine values

omega = 'ω'  # Unicode representation for omega

# Print the formatted header line using f-strings
print(f'{omega:<10}sin({omega})')

# Loop over w and s together with zip() to print each pair
for wi, si in zip(w, s):
    print(f'{wi/math.pi:1.1f}π {si:10.3f}')
