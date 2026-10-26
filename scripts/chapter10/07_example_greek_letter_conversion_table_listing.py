"""
Measurements, Files and Spreadsheets - Importing and Exporting Data in Python
Subsection: Example: Greek Letter Conversion Table
Source: chapters/chapter10.tex, line 390
"""

# main.py
# Import the function from the module
from greek_conversion import greek_to_hex

# Call the function with desired input
hex_value = greek_to_hex('alpha')
print(hex_value)  # Output: 3B1
