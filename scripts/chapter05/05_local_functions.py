"""
Functions and Reusable Calculations - User-Defined Functions
Subsection: Local Functions
"""

def process_order(quantity, price_per_item):
    # Local function to calculate total price with a discount
    def calculate_total(qty, price):
        total = qty * price
        if total > 100:  # Apply a discount if total is over 100
            return total * 0.9  # 10% discount
        return total

    total_price = calculate_total(quantity, price_per_item)
    return f"Total Price: ${total_price:.2f}"

# Testing the local helper function
print(process_order(10, 15))
# Output: Total Price: $135.00 (with discount)
