"""
Functions and Reusable Calculations - Example: Nested Functions Inside a Module

Output as printed in the book:
    Inside module_nested: Module A (green) Module B (red)
    Inside module_top: Module A (green)
"""

# my_module.py

def module_top():
    A = "Module A (green)"

    def module_nested():
        B = "Module B (red)"
        print("Inside module_nested:", A, B)

    module_nested()
    print("Inside module_top:", A)
