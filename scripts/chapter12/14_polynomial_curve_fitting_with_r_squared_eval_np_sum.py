"""
Interpolation, Curve Fitting and Calibration - Polynomial Curve Fitting with R-Squared Evaluation for Water Usage Prediction

Output as printed in the book:
    R-SQUARED VALUES:
    Polynomial Order 1 = 0.9743
    Polynomial Order 2 = 0.9750
    Polynomial Order 3 = 0.9947
    Polynomial Order 4 = 0.9947
    Polynomial Order 5 = 0.9961
"""

# Calculate and print R-squared values
R2 = [1 - np.sum((fit - water) ** 2) / np.sum((water - np.mean(water)) ** 2) for fit in water_fit]
print("R-SQUARED VALUES:")
for n, r2 in enumerate(R2, 1):
    print(f'Polynomial Order {n} = {r2:.4f}')

# Plot original data and fitted curves
plt.plot(day, water, 'x', label='Measured Data')
for fit, label in zip(water_fit, labels[1:]):
    plt.plot(day, fit, label=label)
