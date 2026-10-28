"""
Your First Python Programs - Data Types
Subsection: Translating Math Notation to Code
"""

P = 1000     # Principal
r = 0.05     # Annual interest rate (5%)
n = 12       # Compounded monthly
t = 10       # 10 years

# Every implied grouping from the formula becomes an explicit
# parenthesis: (1 + r/n) is grouped, and the whole thing is raised
# to the power (n*t) -- not just to n, or just to t.
A = P * (1 + r/n)**(n*t)

print(f"A = {A:.2f}")  # Output: A = 1647.01
