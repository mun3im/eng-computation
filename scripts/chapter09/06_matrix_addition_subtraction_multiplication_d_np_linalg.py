"""
Matrices and Circuit Equations - Matrix Addition, Subtraction, Multiplication, Division, Power, and Transpose

Output as printed in the book:
    Matrix Right Division (np.linalg.solve(A.T, B.T).T):
    [[-1.  2.]
     [-2.  3.]]
    Matrix Left Division (np.linalg.solve(A, B)):
    [[-3. -4.]
     [ 4.  5.]]
"""

# 4. Matrix Right Division
# Solving XA = B, i.e. X = B A^-1 (MATLAB's B / A)
matrix_right_div_result = np.linalg.solve(A.T, B.T).T
print("\nMatrix Right Division (np.linalg.solve(A.T, B.T).T):")
print(matrix_right_div_result)

# 5. Matrix Left Division
# Solving AX = B, i.e. X = A^-1 B (MATLAB's A \ B)
matrix_left_div_result = np.linalg.solve(A, B)
print("\nMatrix Left Division (np.linalg.solve(A, B)):")
print(matrix_left_div_result)
