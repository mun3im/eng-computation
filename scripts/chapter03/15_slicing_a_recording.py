"""
Numbers, Variables and Units - Slicing a Recording

Output as printed in the book:
    [12.0, 11.5, 11.0, 10.6]
    [10.1, 9.7, 9.3, 8.9]
    Drop in the first half: 1.4 V
"""

v = [12.0, 11.5, 11.0, 10.6, 10.1, 9.7, 9.3, 8.9]

first_half = v[:4]
second_half = v[4:]
print(first_half)
print(second_half)
print("Drop in the first half:", round(v[0] - v[3], 2), "V")
