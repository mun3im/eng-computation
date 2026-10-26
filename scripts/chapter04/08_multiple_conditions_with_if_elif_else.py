"""
Decisions and Repetition - Decisions
Subsection: Multiple Conditions with if-elif-else
Source: chapters/chapter4.tex, line 808

Output as printed in the book:
    Input a value: 1
    Input b value: 2
    Input c value: 1
    The roots are both: -1.0
"""

# Input values for a, b, and c
a = float(input('Input a value: '))
b = float(input('Input b value: '))
c = float(input('Input c value: '))

# Calculate the discriminant
d = b**2 - 4 * a * c

# Check for conditions using if-elif-else
if d == 0 and a != 0:
    x1 = -b / (2 * a)
    x2 = x1
    print(f'The roots are both: {x1}')
elif d > 0 and a != 0:
    x1 = (-b + (d**0.5)) / (2 * a)
    x2 = (-b - (d**0.5)) / (2 * a)
    print(f'The roots are: {x1} and {x2}')
else:
    print('Complex root')
