"""
Arrays and Vectorized Computation - Array (Element-wise) Operations
Example: - Element-wise Addition, Subtraction, Multiplication, Division, and Power
Source: chapters/chapter6.tex, line 719

Output as printed in the book:
    Element-wise Multiplication (A * B):
    [[ 5 12]
     [21 32]]
    Element-wise Right Division (A / B):
    [[0.2        0.33333333]
     [0.42857143 0.5       ]]
"""

# 3. Element-wise Multiplication
element_wise_mul = A * B
print("\nElement-wise Multiplication (A * B):")
print(element_wise_mul)

# 4. Element-wise Right Division
element_wise_right_div = A / B
print("\nElement-wise Right Division (A / B):")
print(element_wise_right_div)
