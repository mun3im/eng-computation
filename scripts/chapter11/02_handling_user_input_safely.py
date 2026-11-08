"""
Handling Imperfect Engineering Data - Handling User Input Safely
"""

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
