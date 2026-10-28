"""
Numerical Calculus and System Models - Polynomials and System Models
Subsection: Frequency Response
Example: Polynomial Evaluation for Frequency Response
"""

import numpy as np
import matplotlib.pyplot as plt

# Given Q_n and Q_d from previous calculation
Q_n = [2, 4, 1]     # Numerator: 2s^2 + 4s + 1
Q_d = [1, -2, 0]    # Denominator: s^2 - 2s

# Define frequency range (1 mHz to 10 kHz) with logarithmic spacing
# 1000 points from 1e-3 Hz to 1e4 Hz
frequencies = np.logspace(-3, 4, 1000)
# Convert frequency to angular frequency (rad/s)
omega = 2 * np.pi * frequencies
s = 1j * omega                          # s = j*omega

# Evaluate the transfer function
# Q(s) = Q_n / Q_d over the frequency range
numerator = np.polyval(Q_n, s)
denominator = np.polyval(Q_d, s)

# Directly compute Q_s = Q_n / Q_d without handling zero-division
Q_s = numerator / denominator
