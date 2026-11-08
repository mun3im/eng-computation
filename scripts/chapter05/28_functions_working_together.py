"""
Functions and Reusable Calculations - Functions Working Together

Output as printed in the book:
    Total resistance: 232.0 ohms
"""

def series(r1, r2):
    return r1 + r2

def parallel(r1, r2):
    return r1 * r2 / (r1 + r2)

R = series(100, parallel(220, 330))
print(f"Total resistance: {R:.1f} ohms")
