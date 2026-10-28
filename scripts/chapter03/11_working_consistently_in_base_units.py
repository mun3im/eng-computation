"""
Numbers, Variables and Units - Engineering Units and Dimensions
Subsection: Working Consistently in Base Units

Output as printed in the book:
    Time constant: 1.0 s
    Time constant: 1000.0 ms
"""

# An RC circuit: 10 kilohm resistor, 100 microfarad capacitor
R = 10e3       # ohms  (NOT 10, which would mean 10 ohms)
C = 100e-6     # farads (NOT 100, which would mean 100 farads)

tau = R * C    # time constant, in seconds

print(f"Time constant: {tau} s")
print(f"Time constant: {tau * 1000} ms")   # convert only for display
