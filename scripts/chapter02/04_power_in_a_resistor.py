"""
Your First Python Programs - Power in a Resistor

Output as printed in the book:
    Current: 27.27 mA
    Power:   245.5 mW
"""

V = 9.0       # volts
R = 330.0     # ohms

I = V / R     # current, from Ohm's law
P = V * I     # power, in watts

print(f"Current: {I * 1000:.2f} mA")
print(f"Power:   {P * 1000:.1f} mW")
