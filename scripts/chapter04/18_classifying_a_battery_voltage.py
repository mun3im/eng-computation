"""
Decisions and Repetition - Classifying a Battery Voltage

Output as printed in the book:
    Partly charged
"""

v = 12.4      # measured battery voltage (V)

if v >= 12.6:
    print("Fully charged")
elif v >= 12.2:
    print("Partly charged")
else:
    print("Needs charging")
