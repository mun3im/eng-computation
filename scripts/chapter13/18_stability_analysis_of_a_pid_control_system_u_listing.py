"""
Numerical Calculus and System Models - Stability Analysis of a PID Control System Using Polynomial Roots

Output as printed in the book:
    Roots of the system:
    root1 = -1.00 +0.00j
    root2 = -1.00 +0.00j
    The system is stable
"""

# stability_demo.py
from stability_check import check_stability

# Example usage:
check_stability([4, 1, 0], [1], [1, -2])  	# Example system
check_stability([1, 1, 2], [1], [1, -2]) 	# Example system
check_stability([3, 3, 3], [1, 0], [1, 1])  # Example system
