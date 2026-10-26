"""
Engineering Statistics and Data Analysis - Visualizing an Analysis
Source: chapters/chapter14.tex, line 1318
"""

import matplotlib.pyplot as plt

values = [10, 20, 30]
labels = ['A', 'B', 'C']

plt.bar(labels, values)
plt.title("Simple Bar Chart")
plt.show()
