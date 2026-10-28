"""
Engineering Statistics and Data Analysis - Data Analysis
Subsection: Descriptive Analytics (Bivariate)
"""

import matplotlib.pyplot as plt

temperature = [26, 30, 35, 40]
sales = [1000, 2500, 3500, 4500]

plt.scatter(temperature, sales)
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice-cream Sales")
plt.show()
