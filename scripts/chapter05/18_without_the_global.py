"""
Functions and Reusable Calculations - Variable Scope
Subsection: Without the global
Source: chapters/chapter5.tex, line 796
"""

count = 0  # global variable

def increase():
    count = count + 1  # trying to change count without global
    print("Inside function:", count)

increase()
print("Outside function:", count)
