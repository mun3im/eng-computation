"""
Python Reference - Special Characters
Subsection: Using a for
Source: appendices/appendixA.tex, line 380
"""

import math

# Define the values for w and s similar to MATLAB
w = [0, math.pi/2, math.pi, 3*math.pi/2]
s = [math.sin(wi) for wi in w]  # Calculate sine values

omega = 'ω'  # Unicode representation for omega

# Print the formatted header line using f-strings
print(f'{omega} sin({omega})')

# Loop over w and s together with zip() to print each pair
for wi, si in zip(w, s):
    print(f'{wi/math.pi:1.1f}π {si:10.3f}')
