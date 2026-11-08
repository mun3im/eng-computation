"""
Interpolation, Curve Fitting and Calibration - Sensor Calibration Using Polynomial Curve Fitting

Output as printed in the book:
    T(V) = 14.74V + -9.33
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
