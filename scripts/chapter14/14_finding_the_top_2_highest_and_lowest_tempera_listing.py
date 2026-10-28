"""
Engineering Statistics and Data Analysis - Data Sorting
Subsection: Sorting in NumPy
Example: Finding the Top 2 Highest and Lowest Temperatures with Day

Output as printed in the book:
    Highest 2
    no.   Temp  Day
    1     25    7
    2     24    8
    
    Lowest 2
    no.   Temp  Day
    1     17    4
    2     18    3
"""

# Printing formatted output
print("Highest 2")
print(f"{'no.':<5} {'Temp':<5} {'Day':<5}")
for i, (temp, day) in enumerate(zip(highest_values, highest_indices), start=1):
    print(f"{i:<5} {temp:<5} {day:<5}")

print("Lowest 2")
print(f"{'no.':<5} {'Temp':<5} {'Day':<5}")
for i, (temp, day) in enumerate(zip(lowest_values, lowest_indices), start=1):
    print(f"{i:<5} {temp:<5} {day:<5}")
