"""
Interpolation, Curve Fitting and Calibration - Curve Fitting Using Polynomials
Subsection: Data Trends
Example: Predicting Internet Usage with Polynomial Curve Fitting
Source: chapters/chapter12.tex, line 639
"""

# Evaluate the average using the polynomial coefficients for months 1 to 6
average1 = np.polyval(p1, months)
average2 = np.polyval(p2, months)
average3 = np.polyval(p3, months)

# Predicting internet usage for months 7, 8, and 9
months_predict = np.array([7, 8, 9])
usage_predict_1st_order = np.polyval(p1, months_predict)
usage_predict_2nd_order = np.polyval(p2, months_predict)
usage_predict_3rd_order = np.polyval(p3, months_predict)

# Display the predictions for months 7, 8, and 9
print(f"Predicted internet usage (hours) for months 7, 8, 9 (1st Order Polynomial): {usage_predict_1st_order}")
print(f"Predicted internet usage (hours) for months 7, 8, 9 (2nd Order Polynomial): {usage_predict_2nd_order}")
print(f"Predicted internet usage (hours) for months 7, 8, 9 (3rd Order Polynomial): {usage_predict_3rd_order}")
