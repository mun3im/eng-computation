"""
Functions and Reusable Calculations - Variable Scope
Subsection: Without the global
"""

count = 0  # global variable

def increase():
    count = count + 1  # trying to change count without global
    print("Inside function:", count)

increase()
print("Outside function:", count)
