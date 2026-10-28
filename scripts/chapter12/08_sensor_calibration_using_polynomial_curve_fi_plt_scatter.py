"""
Interpolation, Curve Fitting and Calibration - Curve Fitting Using Polynomials
Subsection: Sensor Calibration
Example: Sensor Calibration Using Polynomial Curve Fitting
"""

# Plot the data and the fitted curve
plt.scatter(V, T, label='Collected Data', color='blue', marker='x')
plt.plot(V, s_t, label='Fitted Polynomial Curve', color='red')
plt.title('Sensor Calibration')
plt.xlabel('Sensor Reading (V)')
plt.ylabel('Temperature (\N{DEGREE SIGN}C)')
plt.legend()
plt.grid(True)
plt.show()
