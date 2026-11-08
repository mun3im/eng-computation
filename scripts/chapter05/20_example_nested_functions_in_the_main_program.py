"""
Functions and Reusable Calculations - Example: Nested Functions in the Main Program File

Output as printed in the book:
    Inside nested_function: Top-Level A (black) Nested B (yellow)
    Inside top_function: Top-Level A (black)
    Outside (main): Global A (blue) Global B (blue)
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
