"""
A First Look at Object-Oriented Python - Adding Methods
Source: chapters/chapter15.tex, line 188

Output as printed in the book:
    (40+0j)
"""

class Resistor:
    def __init__(self, name, resistance):
        self.name = name
        self.resistance = resistance

    def impedance(self, f):
        # A resistor's impedance is purely real and independent of frequency
        return complex(self.resistance, 0)

r1 = Resistor("R1", 40.0)
print(r1.impedance(1000))
