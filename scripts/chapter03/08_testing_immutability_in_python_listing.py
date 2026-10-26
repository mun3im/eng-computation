"""
Numbers, Variables and Units - Mutability
Subsection: Testing Immutability in Python
Source: chapters/chapter3.tex, line 447
"""

# Step 1: Assign a variable to an integer value
a = 5
print("Value of a:", a)
print("Memory address of a:", id(a))

# Step 2: Reassign the variable to a new integer value
a = 10
print("Value of a after reassignment:", a)
print("Memory address of a after reassignment:", id(a))
