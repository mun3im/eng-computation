"""
Functions and Reusable Calculations - User-Defined Functions
Subsection: Standard Function: Multiple Input, Multiple Output
"""

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else None
    return addition, subtraction, multiplication, division

add_result, sub_result, mul_result, div_result = calculate(8, 2)
print("Addition:", add_result, "Subtraction:", sub_result,
      "Multiplication:", mul_result, "Division:", div_result)
# Output: Addition: 10 Subtraction: 6 Multiplication: 16 Division: 4.0
