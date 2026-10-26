"""
Functions and Reusable Calculations - Variable Scope
Subsection: Scope Errors Can Be Masked
Source: chapters/chapter5.tex, line 767
"""

x = 10  # global variable

def show():
    x = 5  # local variable
    y = 7  # local variable
    print("Inside function:", x, y)

def display():
    print("Inside function:", x, y)  # error

show()
display()
print("Outside function:", x, y)     # error
