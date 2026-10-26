"""
Engineering Statistics and Data Analysis - Data Sorting
Subsection: Sorting in NumPy
Example: NumPy Sorting Examples
Source: chapters/chapter14.tex, line 472

Output as printed in the book:
    Sorted 2D Array by Columns (descending):
     [[6 5 7]
     [3 2 2]]
    
    Sorted 2D Array by Rows (descending):
     [[5 3 2]
     [7 6 2]]
"""

# Example 5: Sorting a 2D Array in Descending Order by Columns
Ycoldes = np.sort(X, axis=0)[::-1]
print("\nSorted 2D Array by Columns (descending):\n", Ycoldes)

# Example 6: Sorting a 2D Array in Descending Order by Rows
Yrowdes = np.sort(X, axis=1)[:, ::-1]
print("\nSorted 2D Array by Rows (descending):\n", Yrowdes)
