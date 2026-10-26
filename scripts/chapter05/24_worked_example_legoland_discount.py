"""
Functions and Reusable Calculations - Testing Functions
Subsection: Worked Example: Legoland Discount
Source: chapters/chapter5.tex, line 1126
"""

# BUGGY implementation (off-by-one)
def legoland_price(age, base_price=50.0):
    if age < 12:  # off-by-one: 12-year-olds should also get discount
        return base_price * 0.5
    return base_price

# Tests (assertions) -- pick vectors that reveal the boundary problem
assert legoland_price(11) == 25.0, "11 should get discount"
assert legoland_price(12) == 25.0, "12-year-old should get discount (BOUNDARY) -- FAILS on buggy code!"
assert legoland_price(13) == 50.0, "13 should pay full price"
