"""
Matrices and Circuit Equations - Worked Matrix Examples
Example: - Matrix Addition, Subtraction, Multiplication, Division, Power, and Transpose

Output as printed in the book:
    Matrix Power (np.linalg.matrix_power(A, 2)):
    [[ 7 10]
     [15 22]]
    Matrix Transpose (A.T):
    [[1 3]
     [2 4]]
"""

# 6. Matrix Power
# Using np.linalg.matrix_power() to raise matrix A to the power of 2
matrix_power_result = np.linalg.matrix_power(A, 2)
print("\nMatrix Power (np.linalg.matrix_power(A, 2)):")
print(matrix_power_result)

# 7. Matrix Transpose
transpose_result = A.T
print("\nMatrix Transpose (A.T):")
print(transpose_result)
