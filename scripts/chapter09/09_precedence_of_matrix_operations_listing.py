"""
Matrices and Circuit Equations - Worked Matrix Examples
Subsection: Matrix Precedence
Example: Precedence of Matrix Operations
Source: chapters/chapter9.tex, line 468

Output as printed in the book:
    Precedence 1 (Transpose before Multiplication - A.T @ B):
    [[26 30]
     [38 44]]
    Precedence 2 (Parentheses first - (A + B) @ B):
    [[ 86 100]
     [134 156]]
"""

# 1. Demonstrate Precedence of Transpose vs Multiplication
# Transpose happens before multiplication
precedence_result_1 = A.T @ B
print("\nPrecedence 1 (Transpose before Multiplication - A.T @ B):")
print(precedence_result_1)

# 2. Demonstrate Precedence of Parentheses
# Parentheses change the order of operations
precedence_result_2 = (A + B) @ B
print("\nPrecedence 2 (Parentheses first - (A + B) @ B):")
print(precedence_result_2)
