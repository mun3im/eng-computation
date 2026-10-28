"""
Arrays and Vectorized Computation - Array (Element-wise) Operations
Example: - Array Attributes

Output as printed in the book:
    Total number of elements in the array:
    4
    Number of dimensions of the array:
    2
    Size of each dimension:
    Rows: 2, Columns: 2
"""

# Total number of elements in the array
array_size = A.size
print("\nTotal number of elements in the array:")
print(array_size)  # 4

# Number of dimensions of the array
array_ndim = A.ndim
print("\nNumber of dimensions of the array:")
print(array_ndim)  # 2

# Size of each dimension
rows = len(A)        # Number of rows
columns = len(A[0])  # Number of columns
print("\nSize of each dimension:")
print(f"Rows: {rows}, Columns: {columns}")
