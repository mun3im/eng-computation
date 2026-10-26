"""
Functions and Reusable Calculations - Pre-Defined Python Functions
Subsection: Built-in Functions
Source: chapters/chapter5.tex, line 171

Output as printed in the book:
    4
    13.2
    10.8
    11.875
    11.88
"""

readings = [12.0, 11.5, 13.2, 10.8]     # volts

print(len(readings))                     # 4      -- how many samples
print(max(readings))                     # 13.2   -- largest reading
print(min(readings))                     # 10.8   -- smallest reading
print(sum(readings) / len(readings))     # 11.875 -- the mean
print(round(sum(readings) / len(readings), 2))   # 11.88
