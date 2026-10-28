"""
Functions and Reusable Calculations - Using Functions from External Files
Subsection: Practical Example: Temperature Conversion
"""

import numpy as np

def celsius_to_fahrenheit(celsius_array):
    return (celsius_array * 9/5) + 32

def main():
    celsius_array = np.linspace(-20, 100, 10)
    fahrenheit_array = celsius_to_fahrenheit(celsius_array)
    print(f"Celsius temperatures: {celsius_array}")
    print(f"Fahrenheit temperatures: {fahrenheit_array}")

if __name__ == "__main__":
    main()
