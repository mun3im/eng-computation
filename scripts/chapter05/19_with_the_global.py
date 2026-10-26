"""
Functions and Reusable Calculations - Variable Scope
Subsection: With the global
Source: chapters/chapter5.tex, line 819
"""

count = 0  # global variable

def increase():
    global count  # use the global one, not a new local one
    count = count + 1
    print("Inside function:", count)

increase()
print("Outside function:", count)
