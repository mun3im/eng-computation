"""
Functions and Reusable Calculations - With the global Keyword: Correct Modification

Output as printed in the book:
    Inside function: 1
    Outside function: 1
"""

count = 0  # global variable

def increase():
    global count  # use the global one, not a new local one
    count = count + 1
    print("Inside function:", count)

increase()
print("Outside function:", count)
