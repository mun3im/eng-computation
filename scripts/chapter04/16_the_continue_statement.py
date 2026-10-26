"""
Decisions and Repetition - Loops
Subsection: The continue Statement
Source: chapters/chapter4.tex, line 1130

Output as printed in the book:
    Divisible by 7: 7
    Divisible by 7: 14
    Divisible by 7: 21
    Divisible by 7: 28
    Divisible by 7: 35
    Divisible by 7: 42
    Divisible by 7: 49
"""

# Loop through numbers from 1 to 50
for n in range(1, 51):
    # Check if n is not divisible by 7
    if n % 7 != 0:
        continue  # Skip the rest of the loop if n is not divisible by 7
    # Print the number if it is divisible by 7
    print(f"Divisible by 7: {n}")
