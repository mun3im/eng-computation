"""
Numerical Calculus and System Models - Polynomials and System Models
Subsection: Frequency Response
Example: Polynomial Evaluation for Frequency Response
Source: chapters/chapter13.tex, line 678
"""

# Plot frequency vs magnitude (|Q(s)|) with frequency
# on a logarithmic scale
plt.figure()
# Use semilogx for log frequency axis
plt.semilogx(frequencies, np.abs(Q_s))
plt.title("Frequency Response of Q(s)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude |Q(s)|")
plt.grid(True, which="both")  # Add grid lines for both major and minor
