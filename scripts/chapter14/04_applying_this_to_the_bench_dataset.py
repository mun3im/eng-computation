"""
Engineering Statistics and Data Analysis - Understanding Engineering Measurements
Subsection: Applying This to the Bench Dataset
Source: chapters/chapter14.tex, line 160

Output as printed in the book:
    Mean:   28.28 C
    Median: 27.71 C
    Max:    98.40 C
    Std:    7.06 C
"""

import pandas as pd

data = pd.read_csv('bench_rc.csv')
temp = data['temperature_C']

print(f"Mean:   {temp.mean():.2f} C")
print(f"Median: {temp.median():.2f} C")
print(f"Max:    {temp.max():.2f} C")
print(f"Std:    {temp.std():.2f} C")
