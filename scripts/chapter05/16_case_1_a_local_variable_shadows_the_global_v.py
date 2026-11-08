"""
Functions and Reusable Calculations - Case 1: A Local Variable Shadows the Global Variable

Output as printed in the book:
    Inside function, count = 5
    Outside function, count = 0
"""

count = 0  # global variable

def increase():
    count = 5  # local variable created inside the function
    print("Inside function, count =", count)

increase()
print("Outside function, count =", count)
