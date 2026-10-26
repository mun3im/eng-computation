"""
Decisions and Repetition - Decisions
Subsection: Nested if
Source: chapters/chapter4.tex, line 841
"""

# Input values for a, b, and c
a = float(input('Input a value: '))
b = float(input('Input b value: '))
c = float(input('Input c value: '))

# Calculate the discriminant
d = b**2 - 4 * a * c

# Nested if statements
if a != 0:
    if d == 0:
        x1 = -b / (2 * a)
        x2 = x1
        print(f'The roots are both: {x1}')
    elif d > 0:
        x1 = (-b + (d**0.5)) / (2 * a)
        x2 = (-b - (d**0.5)) / (2 * a)
        print(f'The roots are: {x1} and {x2}')
    else:
        print('Complex root')
else:
    x1 = -c / b
    print(f'The root is: {x1}')
