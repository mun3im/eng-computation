"""
Functions and Reusable Calculations - User-Defined Functions
Subsection: Multiple Local Functions
Source: chapters/chapter5.tex, line 351
"""

def process_order(quantity, price_per_item):
    # Two local functions to calculate total price with a discount and tax
    def calculate_total(qty, price):
        total = qty * price
        if total > 100:
            return total * 0.9  # Apply 10% discount
        return total

    def apply_tax(amount, tax_rate=0.05):  # Apply 5% tax
        return amount * (1 + tax_rate)

    total_price = apply_tax(calculate_total(quantity, price_per_item))
    return f"Total Price after tax: {total_price}"

# Test the function
print(process_order(10, 15))
# Output: Total Price after tax: 141.75
