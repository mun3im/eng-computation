"""
Functions and Reusable Calculations - Using Functions from External Files
Subsection: Creating and Using a Module
"""

# use_add.py
# This script imports and uses the add function
# specifically from math_operations.

# Import only the add function from the module
from math_operations import add

# Using the imported add function
print(add(7, 3))  # Output: 10
