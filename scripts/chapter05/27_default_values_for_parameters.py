"""
Functions and Reusable Calculations - Default Values for Parameters

Output as printed in the book:
    150.0
    90.0
    1000.0
"""

def led_resistor(v_supply, v_led=2.0, i=0.02):
    """Series resistor (ohms) for an LED."""
    return (v_supply - v_led) / i

print(round(led_resistor(5), 1))            # red LED at 20 mA
print(round(led_resistor(5, 3.2), 1))       # blue LED
print(round(led_resistor(12, i=0.01), 1))   # 12 V supply, 10 mA
