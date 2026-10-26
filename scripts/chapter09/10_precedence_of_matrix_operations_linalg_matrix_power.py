"""
Matrices and Circuit Equations - Worked Matrix Examples
Subsection: Matrix Precedence
Example: Precedence of Matrix Operations
Source: chapters/chapter9.tex, line 491

Output as printed in the book:
    Precedence 3 (Power before Multiplication - np.linalg.matrix_power(A, 2) @ B):
    [[105 122]
     [229 266]]
    Precedence 4 (Multiplication before Division - np.linalg.solve(B.T, (A @ B).T).T):
    [[1. 2.]
     [3. 4.]]
"""

# 3. Demonstrate Power Precedence
# Power operation happens before multiplication
precedence_result_3 = np.linalg.matrix_power(A, 2) @ B
print("\nPrecedence 3 (Power before Multiplication - np.linalg.matrix_power(A, 2) @ B):")
print(precedence_result_3)

# 4. Demonstrate Multiplication and Division Precedence
# Multiplication happens before solving division operations
precedence_result_4 = np.linalg.solve(B.T, (A @ B).T).T
print("\nPrecedence 4 (Multiplication before Division - np.linalg.solve(B.T, (A @ B).T).T):")
print(precedence_result_4)
