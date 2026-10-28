"""
Interpolation, Curve Fitting and Calibration - Increasing Signal Detail
Example: Comparison of Interpolation Methods for Signal Processing (Digital-to-Analog Converter)
"""

# Create subplots for stem plots using plt.subplot
plt.figure(figsize=(12, 8))

# Linear interpolation subplot
plt.subplot(2, 2, 1)
plt.stem(time_interp, amplitude_linear, linefmt='-', markerfmt='o', basefmt='k')
plt.title('Linear Interpolation')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')

# Nearest interpolation subplot
plt.subplot(2, 2, 2)
plt.stem(time_interp, amplitude_nearest, linefmt='-', markerfmt='o', basefmt='k')
plt.title('Nearest Interpolation')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')

# PCHIP interpolation subplot
plt.subplot(2, 2, 3)
plt.stem(time_interp, amplitude_pchip, linefmt='-', markerfmt='o', basefmt='k')
plt.title('PCHIP Interpolation')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')

# Spline interpolation subplot
plt.subplot(2, 2, 4)
plt.stem(time_interp, amplitude_spline, linefmt='-', markerfmt='o', basefmt='k')
plt.title('Spline Interpolation')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')

# Adjust layout and show plot
plt.tight_layout()
plt.show()
