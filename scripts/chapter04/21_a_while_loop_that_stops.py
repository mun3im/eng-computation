"""
Decisions and Repetition - A While Loop That Stops

Output as printed in the book:
    After 4 halvings, v = 0.750 V
"""

v = 12.0      # volts
steps = 0

while v >= 1.0:
    v = v / 2
    steps = steps + 1

print(f"After {steps} halvings, v = {v:.3f} V")
