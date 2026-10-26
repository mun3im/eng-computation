"""
Arrays and Vectorized Computation - Subscripting Notation in NumPy
Subsection: Array Splitting Practice
Source: chapters/chapter6.tex, line 653
"""

print(A[1, :])        # [5 6 7 8]
print(A[:, 2])         # [ 3  7 11 15]
print(A[1:3, :])       # [[ 5  6  7  8] [ 9 10 11 12]]
print(A[:, 1:3])       # [[ 2  3] [ 6  7] [10 11] [14 15]]
print(A[1:3, 1:3])     # [[ 6  7] [10 11]]
print(A[::2, :])       # [[ 1  2  3  4] [ 9 10 11 12]]
print(A[::-1, :])      # rows in reverse order
print(A[-1, :])        # [13 14 15 16]  -- last row
print(A[:, -1])        # [ 4  8 12 16]  -- last column
