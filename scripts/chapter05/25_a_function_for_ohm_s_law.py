"""
Functions and Reusable Calculations - A Function for Ohm's Law

Output as printed in the book:
    0.02553191489361702
    0.005
    27.3 mA
"""

def current(v, r):
    """Return the current (A) through r ohms at v volts."""
    return v / r

print(current(12, 470))
print(current(5, 1000))
i = current(9, 330)
print(f"{i * 1000:.1f} mA")
