"""
Your First Python Programs - Data Types
Subsection: Translating Math Notation to Code
Source: chapters/chapter2.tex, line 148
"""

import math

a, b, c = 1, -3, 2

# Correct translation: numerator and denominator are each fully
# parenthesized, exactly matching what the fraction bar implies.
x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

print(x1, x2)  # Output: 2.0 1.0
