"""
Decisions and Repetition - Loops
Subsection: for Loop
Example: Compound Interest Calculation using a for Loop
Source: chapters/chapter4.tex, line 925

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

# Loop over the specified years (2, 4, 6, 8, 10)
for n in range(2, 11, 2):
    B = a * (1 + r) ** n  # Calculate the final balance using the formula
    print(f'n = {n}, B = {B:.2f}')  # Display the year and the calculated balance
