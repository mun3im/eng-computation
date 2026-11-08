"""
Functions and Reusable Calculations - Print or Return?

Output as printed in the book:
    12.5664
    a is None
    b is 12.5664
"""

def area_print(r):
    print(3.1416 * r ** 2)     # shows the value, gives nothing back

def area_return(r):
    return 3.1416 * r ** 2     # gives the value back

a = area_print(2)
b = area_return(2)
print("a is", a)
print("b is", b)
