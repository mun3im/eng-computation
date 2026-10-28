"""
Engineering Statistics and Data Analysis - Data Aggregation with groupby

Output as printed in the book:
               mean  sum
    component
    Capacitor  1.65  3.3
    Inductor   3.40  6.8
    Resistor   2.25  4.5
"""

import pandas as pd

data = {
    'component':   ['Resistor', 'Resistor', 'Capacitor',
    				'Capacitor', 'Inductor', 'Inductor'],
    'time_of_day': ['Morning', 'Evening', 'Morning',
    				'Evening', 'Morning', 'Evening'],
    'power_watts': [2.1, 2.4, 1.5, 1.8, 3.2, 3.6],
}
df = pd.DataFrame(data)

# Group by component type,
# then compute mean and total power for each group
summary = df.groupby('component')['power_watts'].agg(['mean', 'sum'])
print(summary)
