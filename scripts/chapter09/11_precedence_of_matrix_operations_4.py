"""
Matrices and Circuit Equations - Worked Matrix Examples
Subsection: Matrix Precedence
Example: Precedence of Matrix Operations
Source: chapters/chapter9.tex, line 514

Output as printed in the book:
    Precedence 5 (Multiplication before Addition - A @ B + B):
    [[24 28]
     [50 58]]
    Precedence 6 (Combination of Power, Transpose, Addition, and Division):
    [[-12.  -7.]
     [-19. -10.]]
"""

# 5. Demonstrate Precedence of Addition and Multiplication
# Multiplication happens before addition
precedence_result_5 = A @ B + B
print("\nPrecedence 5 (Multiplication before Addition - A @ B + B):")
print(precedence_result_5)

# 6. Combining Multiple Precedence
# Complex combination to demonstrate full precedence
precedence_result_6 = (np.linalg.matrix_power(A, 2) + A.T) @ np.linalg.solve(B, A)
print("\nPrecedence 6 (Combination of Power, Transpose, Addition, and Division):")
print(precedence_result_6)
