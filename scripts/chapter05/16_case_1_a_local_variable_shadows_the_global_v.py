"""
Functions and Reusable Calculations - Variable Scope
Subsection: Case 1: A Local Variable Shadows the Global Variable
"""

count = 0  # global variable

def increase():
    count = 5  # local variable created inside the function
    print("Inside function, count =", count)

increase()
print("Outside function, count =", count)
