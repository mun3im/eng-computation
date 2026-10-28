"""
Engineering Statistics and Data Analysis - Understanding Engineering Measurements
Subsection: Measurement Error

Output as printed in the book:
    Absolute error: 0.243 ohms
    Relative error: 0.243 %
"""

measured = np.mean(readings)   # 100.24 ohms
true_value = 100.0             # from a calibrated reference

absolute_error = measured - true_value
relative_error = abs(absolute_error) / true_value * 100

print(f"Absolute error: {absolute_error:.3f} ohms")
print(f"Relative error: {relative_error:.3f} %")
