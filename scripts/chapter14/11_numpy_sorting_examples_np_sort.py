"""
Engineering Statistics and Data Analysis - Data Sorting
Subsection: Sorting in NumPy
Example: NumPy Sorting Examples
Source: chapters/chapter14.tex, line 452

Output as printed in the book:
    Sorted 2D Array by Rows (ascending):
     [[2 3 5]
     [2 6 7]]
    
    Sorted 2D Array by Columns (ascending - default):
     [[3 2 2]
     [6 5 7]]
"""

# Example 3: Sorting a 2D Array by Rows
Yrow = np.sort(X, axis=1)
print("\nSorted 2D Array by Rows (ascending):\n", Yrow)

# Example 4: Sorting a 2D Array in Ascending Order by Columns (default behaviour)
Ycolasc = np.sort(X, axis=0)
print("\nSorted 2D Array by Columns (ascending - default):\n", Ycolasc)
