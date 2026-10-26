"""
Decisions and Repetition - Loops
Subsection: while Loop
Example: Compound Interest Calculation using a while Loop
Source: chapters/chapter4.tex, line 1000

Output as printed in the book:
    n = 2, B = 116.64
    n = 4, B = 136.05
    n = 6, B = 158.69
    n = 8, B = 185.09
    n = 10, B = 215.89
"""

# Define the initial investment and interest rate
a = 100  # Initial investment amount in dollars
r = 0.08  # Annual interest rate

# Initialize the starting year and the step
n = 2

# Use a while loop to calculate for each specified year (2, 4, 6, 8, 10)
while n <= 10:
    B = a * (1 + r) ** n  # Calculate the final balance
    print(f'n = {n}, B = {B:.2f}')  # Display the year and the calculated balance
    n += 2  # Increment the year by 2
