"""
Matrices and Circuit Equations - Worked Matrix Examples
Example: - Matrix Addition, Subtraction, Multiplication, Division, Power, and Transpose
Source: chapters/chapter9.tex, line 363

Output as printed in the book:
    Matrix Multiplication (A @ B):
    [[19 22]
     [43 50]]
    Matrix Multiplication (np.matmul(A, B)):
    [[19 22]
     [43 50]]
"""

# 3. Matrix Multiplication
# Using @ operator
matrix_mul_result = A @ B
print("\nMatrix Multiplication (A @ B):")
print(matrix_mul_result)

# Alternatively, using np.matmul()
matrix_mul_result_alt = np.matmul(A, B)
print("\nMatrix Multiplication (np.matmul(A, B)):")
print(matrix_mul_result_alt)
