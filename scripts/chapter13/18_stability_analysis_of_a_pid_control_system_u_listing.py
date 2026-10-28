"""
Numerical Calculus and System Models - Polynomials and System Models
Subsection: System Stability
Example: Stability Analysis of a PID Control System Using Polynomial Roots
"""

# example9.py
from stability_check import check_stability

# Example usage:
check_stability([4, 1, 0], [1], [1, -2])  	# Example system
check_stability([1, 1, 2], [1], [1, -2]) 	# Example system
check_stability([3, 3, 3], [1, 0], [1, 1])  # Example system
