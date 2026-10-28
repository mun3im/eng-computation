"""
A First Look at Object-Oriented Python - Inheritance: Sharing Behaviour

Output as printed in the book:
    R: Z = 40.00+0.00j ohm, |Z| = 40.00 ohm
    L: Z = 0.00+75.40j ohm, |Z| = 75.40 ohm
    C: Z = -0.00-53.05j ohm, |Z| = 53.05 ohm
    
    Series total: Z = 40.00+22.35j ohm
    Magnitude:    45.82 ohm
    Phase angle:  29.2 deg
"""

f = 60.0
circuit = [Resistor("R", 40.0), Inductor("L", 0.2), Capacitor("C", 50e-6)]

for c in circuit:
    print(c.describe(f))

# Series impedances add (Chapter 8)
Z_total = sum(c.impedance(f) for c in circuit)

print(f"\nSeries total: Z = {Z_total:.2f} ohm")
print(f"Magnitude:    {abs(Z_total):.2f} ohm")
print(f"Phase angle:  {np.degrees(np.angle(Z_total)):.1f} deg")
