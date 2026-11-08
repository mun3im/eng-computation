"""
Functions and Reusable Calculations - Simple Example: Greeting Function
"""

def greet(name):
    return f"Hello, {name}"

def main():
    user = "Alice"
    message = greet(user)
    print(message)

if __name__ == "__main__":
    main()
