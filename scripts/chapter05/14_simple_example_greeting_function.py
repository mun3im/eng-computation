"""
Functions and Reusable Calculations - Using Functions from External Files
Subsection: Simple Example: Greeting Function
Source: chapters/chapter5.tex, line 563
"""

def greet(name):
    return f"Hello, {name}"

def main():
    user = "Alice"
    message = greet(user)
    print(message)

if __name__ == "__main__":
    main()
