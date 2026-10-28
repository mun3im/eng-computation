"""
Functions and Reusable Calculations - Variable Scope
Subsection: Example: Nested Functions in the Main Program File
"""

# main_program.py

A = "Global A (blue)"
B = "Global B (blue)"

def top_function():
    A = "Top-Level A (black)"

    def nested_function():
        B = "Nested B (yellow)"
        print("Inside nested_function:", A, B)

    nested_function()
    print("Inside top_function:", A)

top_function()
print("Outside (main):", A, B)
