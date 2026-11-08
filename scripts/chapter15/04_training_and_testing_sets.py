"""
A First Look at Machine Learning - Training and Testing Sets

Output as printed in the book:
    R^2 on training data:    0.992
    R^2 on unseen test data: 0.975
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Ten (temperature, sales) records
X = [[22], [24], [26], [28], [30], [32], [34], [36], [38], [40]]
y = [450, 700, 1000, 1700, 2500, 2800, 3300, 3700, 4100, 4500]

# Hold back 20% of the records; random_state makes the split repeatable
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

model = LinearRegression().fit(X_train, y_train)
print(f"R^2 on training data:    {model.score(X_train, y_train):.3f}")
print(f"R^2 on unseen test data: {model.score(X_test, y_test):.3f}")
