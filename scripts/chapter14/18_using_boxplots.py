"""
Engineering Statistics and Data Analysis - Data Cleaning and Preprocessing
Subsection: Using Boxplots
"""

import matplotlib.pyplot as plt

samples = [10, 12, 100, 23, 18, 20, 2]
plt.boxplot(samples, vert=False)
plt.title("Boxplot of Faulty-Sample Counts")
plt.xlabel("Samples")
plt.show()
