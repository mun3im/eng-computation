"""
Engineering Statistics and Data Analysis - Introduction to Machine Learning
Subsection: Simple Decision Tree Classifier
Source: chapters/chapter14.tex, line 1415

Output as printed in the book:
    'high'
"""

from sklearn.tree import DecisionTreeClassifier

X = [[1], [2], [3], [4]]
y = ['low', 'low', 'high', 'high']

model = DecisionTreeClassifier()
model.fit(X, y)
print(model.predict([[3]]))
