"""
Numerical Calculus and System Models - Stability Analysis of a PID Control System Using Polynomial Roots
"""

# stability_check.py
import numpy as np

def check_stability(C, Pn, Pd):
    # Construct the PID transfer function numerator and denominator
    Gn = [C[2], C[0], C[1]]  # PID constants (P, I, D)
    Gd = [1, 0]               # the PID's 1/s term

    # Polynomial multiplication
    # (replacing np.convolve with numpy.polymul)
    Hn = np.polymul(Gn, Pn)   	# Multiply the polynomials
    							# for numerator
    Hd = np.polymul(Gd, Pd)   	# Multiply the polynomials
    							# for denominator

    # Closed-loop denominator Gd*Pd + Gn*Pn. np.polyadd uses the same
    # highest-power-first order as polymul; the newer
    # np.polynomial.polynomial.polyadd uses the OPPOSITE order and would
    # misalign polynomials of different lengths.
    Hd = np.polyadd(Hd, Hn)

    # Calculate the roots of the final denominator polynomial
    roots = np.roots(Hd)
    print("Roots of the system:")
    for i, root in enumerate(roots):
        print(f"root{i + 1} = {root.real:.2f} {root.imag:+.2f}j")

    # Check stability: All roots should have negative real parts
    stable_roots = roots[roots.real >= 0]
    if len(stable_roots) == 0:
        print("The system is stable")
    else:
        print("The system is not stable")
