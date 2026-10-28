"""
A First Look at Object-Oriented Python - Defining a Class

Output as printed in the book:
    R1 40.0
    R2 100.0
"""

class Resistor:
    def __init__(self, name, resistance):
        self.name = name              # store the name on this object
        self.resistance = resistance  # store the value on this object

r1 = Resistor("R1", 40.0)
r2 = Resistor("R2", 100.0)

print(r1.name, r1.resistance)
print(r2.name, r2.resistance)
