"""
Data Visualization - Specialized Plots
Subsection: An Engineering Application: The Bode Plot
Example: Bode Plot of an RC Low-Pass Filter
Source: chapters/chapter7.tex, line 596

Output as printed in the book:
    Cutoff frequency: 72.1 Hz
"""

import numpy as np
import matplotlib.pyplot as plt

R, C = 4.7e3, 0.47e-6
fc = 1 / (2 * np.pi * R * C)          # cutoff frequency, about 72 Hz

# Evenly spaced in LOG frequency: 1 Hz to 10 kHz
f = np.logspace(0, 4, 500)

H = 1 / (1 + 1j * 2 * np.pi * f * R * C)

magnitude_db = 20 * np.log10(np.abs(H))
phase_deg = np.degrees(np.angle(H))

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.semilogx(f, magnitude_db)
ax1.set_ylabel('Magnitude (dB)')
ax1.grid(True, which='both')

ax2.semilogx(f, phase_deg)
ax2.set_ylabel('Phase (degrees)')
ax2.set_xlabel('Frequency (Hz)')
ax2.grid(True, which='both')

plt.tight_layout()
plt.show()

print(f"Cutoff frequency: {fc:.1f} Hz")
