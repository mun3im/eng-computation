"""
Arrays and Vectorized Computation - Array (Element-wise) Operations
Example: - Element-wise Addition, Subtraction, Multiplication, Division, and Power
Source: chapters/chapter6.tex, line 740

Output as printed in the book:
    Element-wise Left Division (B / A):
    [[5.         3.        ]
     [2.33333333 2.        ]]
    Element-wise Power (A ** 2):
    [[ 1  4]
     [ 9 16]]
"""

# 5. Element-wise Left Division
element_wise_left_div = B / A
print("\nElement-wise Left Division (B / A):")
print(element_wise_left_div)

# 6. Element-wise Power
element_wise_power = A ** 2
print("\nElement-wise Power (A ** 2):")
print(element_wise_power)
