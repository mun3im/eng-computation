"""
Handling Imperfect Engineering Data - Missing Data and Outliers
Subsection: Handling Missing Data
Example: Handling Missing Data and Interpolation
"""

# Create subplots (top: original data with NaN values, bottom: data after filling NaN values)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# Plot the original data with NaN values
ax1.scatter(x, A, label='Original Data with Missing Values', color='blue')
ax1.set_title("Original Data with Missing Values (NaN)")
ax1.legend()

# Plot the data after filling NaN values with interpolation
ax2.scatter(x, A, label='Data After Filling Missing Values', color='blue')
ax2.scatter(x[nans], F[nans], label='Filled Data (Missing Values Replaced)', color='red')
ax2.set_title("Data After Filling Missing Values (Interpolation)")
ax2.legend()

# Display the plots
plt.tight_layout()
plt.show()
