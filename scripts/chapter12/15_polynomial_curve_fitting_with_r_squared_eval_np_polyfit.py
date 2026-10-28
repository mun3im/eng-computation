"""
Interpolation, Curve Fitting and Calibration - Curve Fitting Using Polynomials
Subsection: Data Modelling
Example: Polynomial Curve Fitting with R-Squared Evaluation for Water Usage Prediction
"""

plt.xlabel('Day')
plt.ylabel('Water Usage (Litre)')
plt.title('Water Usage for 1 Harvesting Cycle')
plt.legend(fontsize=8)  # Set legend font size to 8
plt.grid(True)
plt.show()

# Get and print coefficients for the 3rd-order polynomial
coeffs_order_3 = np.polyfit(day, water, 3)
print(f"Coefficients for 3rd-order polynomial: {coeffs_order_3}")
