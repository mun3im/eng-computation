"""
Interpolation, Curve Fitting and Calibration - Curve Fitting Using Polynomials
Subsection: Data Trends
Example: Predicting Internet Usage with Polynomial Curve Fitting
Source: chapters/chapter12.tex, line 657
"""

# Plot the original data and the polynomial fits
# Transpose data to match months
plt.plot(months, data.T, 'o', label='Original Data')
plt.plot(months, average1, '--k', label='1st Degree Fit')
plt.plot(months, average2, '-.b', label='2nd Degree Fit')
plt.plot(months, average3, '-r', label='3rd Degree Fit')

# Plot the predictions for months 7, 8, and 9
plt.plot(np.concatenate([months, months_predict]),
          np.concatenate([average1, usage_predict_1st_order]),
          'k--', label='1st Degree Prediction', alpha=0.6)
plt.plot(np.concatenate([months, months_predict]),
          np.concatenate([average2, usage_predict_2nd_order]),
          'b-.', label='2nd Degree Prediction', alpha=0.6)
plt.plot(np.concatenate([months, months_predict]),
          np.concatenate([average3, usage_predict_3rd_order]),
          'r--', label='3rd Degree Prediction', alpha=0.6)
