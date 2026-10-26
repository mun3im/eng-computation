"""
Functions and Reusable Calculations - Variable Scope
Subsection: Example: Nested Functions Inside a Module
Source: chapters/chapter5.tex, line 930
"""

# my_module.py

def module_top():
    A = "Module A (green)"

    def module_nested():
        B = "Module B (red)"
        print("Inside module_nested:", A, B)

    module_nested()
    print("Inside module_top:", A)
