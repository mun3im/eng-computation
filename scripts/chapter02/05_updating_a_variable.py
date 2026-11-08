"""
Your First Python Programs - Updating a Variable

Output as printed in the book:
    Total: 35.3
    Average: 11.77
"""

total = 0              # nothing added yet
total = total + 12.0   # first reading
total = total + 11.5   # second reading
total += 11.8          # the same thing, written shorter

count = 3
average = total / count
print("Total:", total)
print("Average:", round(average, 2))
