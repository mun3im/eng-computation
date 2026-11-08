"""
Decisions and Repetition - Finding the Largest Value by Hand

Output as printed in the book:
    Largest: 9.1
"""

v = [3.2, 7.9, 5.4, 9.1, 6.6]

largest = v[0]            # start with the first value
for x in v:
    if x > largest:
        largest = x       # found a bigger one

print("Largest:", largest)
