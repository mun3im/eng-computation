"""
A First Look at Machine Learning - Classification with a Decision Tree

Output as printed in the book:
    high
"""

from sklearn.tree import DecisionTreeClassifier

X = [[1], [2], [3], [4]]
y = ['low', 'low', 'high', 'high']

model = DecisionTreeClassifier()
model.fit(X, y)
print(model.predict([[3]])[0])
