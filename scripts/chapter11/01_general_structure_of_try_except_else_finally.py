"""
Handling Imperfect Engineering Data - Errors and Exceptions in Python
Subsection: The try / except Anatomy
Listing: General structure of try/except/else/finally
Source: chapters/chapter11.tex, line 51
"""

try:
    # risky code
except ErrorType:
    # handle the error
else:
    # runs if no error
finally:
    # always runs (cleanup)
