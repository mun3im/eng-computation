"""
Functions and Reusable Calculations - Variable Scope
Subsection: Nested (Enclosing) Scope: A Simple Recap
"""

def outer():
    msg = "Hello"

    def inner():
        print(msg)  # found in enclosing scope

    inner()

outer()
