"""
Interpolation, Curve Fitting and Calibration - Predicting Internet Usage with Polynomial Curve Fitting

Output as printed in the book:
    Predicted internet usage (hours) for months 7, 8, 9 (1st Order Polynomial): [169.72       201.55428571 233.38857143]
    Predicted internet usage (hours) for months 7, 8, 9 (2nd Order Polynomial): [244.52       340.46857143 452.44571429]
    Predicted internet usage (hours) for months 7, 8, 9 (3rd Order Polynomial): [244.33333333 339.96190476 451.41904762]
"""

# Adjust title, labels, and grid
plt.title('Internet Usage and Polynomial Fits with Predictions')
plt.xlabel('Month')
plt.ylabel('Usage (hours)')

# Make the legend smaller with the fontsize argument
# Use 'small', 'x-small', or a specific size like 8
plt.legend(loc='upper left', fontsize='6')
plt.grid(True)
plt.show()
