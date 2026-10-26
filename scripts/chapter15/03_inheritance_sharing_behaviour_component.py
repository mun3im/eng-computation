"""
A First Look at Object-Oriented Python - Inheritance: Sharing Behaviour
Source: chapters/chapter15.tex, line 212
"""

import numpy as np

class Component:
    """Shared behaviour for any two-terminal component."""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def impedance(self, f):
        # Each specific component type must supply its own version
        raise NotImplementedError("Each component type defines its own impedance")

    def describe(self, f):
        Z = self.impedance(f)
        return f"{self.name}: Z = {Z:.2f} ohm, |Z| = {abs(Z):.2f} ohm"


class Resistor(Component):
    def impedance(self, f):
        return complex(self.value, 0)          # Z = R

class Inductor(Component):
    def impedance(self, f):
        return 1j * 2 * np.pi * f * self.value  # Z = +j*w*L

class Capacitor(Component):
    def impedance(self, f):
        return -1j / (2 * np.pi * f * self.value)  # Z = -j/(w*C)
