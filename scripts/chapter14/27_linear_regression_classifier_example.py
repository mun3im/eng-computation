"""
Engineering Statistics and Data Analysis - Introduction to Machine Learning
Subsection: Linear Regression Classifier Example

Output as printed in the book:
    Predicted sales for temperature 45°C: 5847.63
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Data Definition
temperature = [26, 30, 35, 40]
sales = [1000, 2500, 3500, 4500]

# 2. Machine Learning Model Training
X = np.array(temperature).reshape(-1, 1)
y = np.array(sales)

model = LinearRegression()
model.fit(X, y)

# 3. Prediction
temperature_to_predict = np.array([[45]])
predicted_sales = model.predict(temperature_to_predict)
print(f"Predicted sales for temperature 45°C: {predicted_sales[0]:.2f}")

# 4. Plotting
plt.figure(figsize=(8, 6))
sns.scatterplot(x=temperature, y=sales, color='blue',
				label='Original Data', s=70)

# Plot the predicted point
plt.scatter(temperature_to_predict[0], predicted_sales[0],
			color='red', marker='X', s=100,
			label=f'Predicted Sales at {temperature_to_predict[0][0]}°C')

# Plot the regression line
x_reg = np.array([min(temperature),
				 temperature_to_predict[0][0]]).reshape(-1, 1)
y_reg = model.predict(x_reg)
plt.plot(x_reg, y_reg, color='green', linestyle='--', label='Regression Line')
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice-cream Sales")
plt.title("Ice-cream Sales vs. Temperature with Linear Regression Prediction")
plt.legend()
plt.grid(True)
plt.show()
