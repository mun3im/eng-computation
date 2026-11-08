"""
Functions and Reusable Calculations - Without the global Keyword: An Error

Output as printed in the book:
    UnboundLocalError: local variable 'count' referenced before assignment
"""

count = 0  # global variable

def increase():
    count = count + 1  # trying to change count without global
    print("Inside function:", count)

increase()
print("Outside function:", count)
