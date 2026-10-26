"""
Functions and Reusable Calculations - User-Defined Functions
Subsection: Adding Help Documentation to Functions
Source: chapters/chapter5.tex, line 404
"""

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Parameters:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius ** 2

# Accessing help
help(calculate_circle_area)
