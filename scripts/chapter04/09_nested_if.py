"""
Decisions and Repetition - Nested if

Output as printed in the book:
    Input a value: 2
    Input b value: 3
    Input c value: 1
    The roots are: -0.5 and -1.0
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
    # a = 0: the equation is bx + c = 0
    if b != 0:
        x1 = -c / b
        print(f'The root is: {x1}')
    elif c != 0:
        print('No solution')
    else:
        print('Every x is a solution')
