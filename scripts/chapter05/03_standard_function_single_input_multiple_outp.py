"""
Functions and Reusable Calculations - Standard Function: Single Input, Multiple Output
"""

def analyze_number(num):
    is_even = num % 2 == 0
    square = num ** 2
    return is_even, square

even, sq = analyze_number(5)
print("Is Even:", even, "Square:", sq)
# Output: Is Even: False Square: 25
