"""
Functions and Reusable Calculations - Variable Scope
Subsection: Nested (Enclosing) Scope: A Simple Recap
Source: chapters/chapter5.tex, line 976
"""

def outer():
    msg = "Hello"

    def inner():
        print(msg)  # found in enclosing scope

    inner()

outer()
