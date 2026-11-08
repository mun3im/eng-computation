"""
Numbers, Variables and Units - A Dictionary of Components

Output as printed in the book:
    {'R1': 4700, 'R2': 330, 'C1': 0.0001}
    R2 is 330 ohms
    Is there an R3? False
    Number of parts: 3
"""

parts = {"R1": 4700, "R2": 220}
parts["C1"] = 100e-6         # add a new part
parts["R2"] = 330            # replace a value

print(parts)
print("R2 is", parts["R2"], "ohms")
print("Is there an R3?", "R3" in parts)
print("Number of parts:", len(parts))
