"""
Engineering Statistics and Data Analysis - Data Analysis
Subsection: Predictive Analytics
Source: chapters/chapter14.tex, line 1275

Output as printed in the book:
    Predicted sales: [2693.00225734]
"""

from sklearn.linear_model import LinearRegression

X = [[26], [30], [35], [40]]   # temperature
y = [1000, 2500, 3500, 4500]   # sales

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[32]])
print("Predicted sales:", prediction)
