"""
Decisions and Repetition - Loops
Subsection: Nested Loops
Example: Compound Interest with Nested Loops for Multiple Principal and Time Periods

Output as printed in the book:
    For a = 100, n = 2, B = 118.81
    For a = 100, n = 4, B = 141.16
    For a = 100, n = 6, B = 167.71
    For a = 100, n = 8, B = 199.26
    For a = 100, n = 10, B = 236.74
    For a = 500, n = 2, B = 594.05
    For a = 500, n = 4, B = 705.79
    For a = 500, n = 6, B = 838.55
    For a = 500, n = 8, B = 996.28
    For a = 500, n = 10, B = 1183.68
    For a = 800, n = 2, B = 950.48
    For a = 800, n = 4, B = 1129.27
    For a = 800, n = 6, B = 1341.68
    For a = 800, n = 8, B = 1594.05
    For a = 800, n = 10, B = 1893.89
"""

# Values for the principal amounts
a_values = [100, 500, 800]

# Values for the number of years
n_values = [2, 4, 6, 8, 10]

# Interest rate
r = 0.09

for a in a_values:  # Loop through each value of a
    for n in n_values:  # Loop through each value of n
        # Calculate the final balance using the compound formula
        B = a * (1 + r) ** n
        print(f"For a = {a}, n = {n}, B = {B:.2f}")  # Print the results
