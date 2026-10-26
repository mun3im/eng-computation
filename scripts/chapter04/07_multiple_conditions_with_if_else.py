"""
Decisions and Repetition - Decisions
Subsection: Multiple Conditions with if-else
Source: chapters/chapter4.tex, line 772
"""

# Input values for a, b, and c
a = float(input('Input a value: '))
b = float(input('Input b value: '))
c = float(input('Input c value: '))

# Calculate the discriminant
d = b**2 - 4 * a * c

# Check for specific conditions
if d == 0 and a != 0:
    x = -b / (2 * a)
    print(f'The value of x is: {x}')
else:
    print('Different root')
