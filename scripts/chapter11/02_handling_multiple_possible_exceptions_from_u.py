"""
Handling Imperfect Engineering Data - Writing Robust Code
Subsection: Handling User Input Safely
Listing: Handling multiple possible exceptions from user input
"""

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
