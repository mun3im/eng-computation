"""
Decisions and Repetition - Counting Out-of-Tolerance Resistors

Output as printed in the book:
    104.2 ohms is out of tolerance
    95.6 ohms is out of tolerance
    2 of 6 resistors failed
"""

measured = [99.1, 101.8, 104.2, 100.3, 95.6, 98.9]   # ohms
nominal = 100.0
tolerance = 0.02                                      # 2 %

failed = 0
for r in measured:
    error = abs(r - nominal) / nominal
    if error > tolerance:
        failed = failed + 1
        print(f"{r} ohms is out of tolerance")

print(failed, "of", len(measured), "resistors failed")
