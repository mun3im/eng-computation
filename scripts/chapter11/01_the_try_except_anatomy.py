"""
Handling Imperfect Engineering Data - The try / except Anatomy
"""

try:
    # risky code
except ErrorType:
    # handle the error
else:
    # runs if no error
finally:
    # always runs (cleanup)
