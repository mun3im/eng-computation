"""
Engineering Statistics and Data Analysis - Data Cleaning and Preprocessing
Subsection: Identifying and Handling Outliers with pandas
Example: Detecting Outliers
Source: chapters/chapter14.tex, line 1059

Output as printed in the book:
    DataFrame with Outlier Column:
         Node  Samples  Outlier
    0  ADC-01       10    False
    1  ADC-02       12    False
    2  ADC-03      100     True
    3  ADC-04       23    False
    4  ADC-05       18    False
    5  ADC-06       20    False
    6  ADC-07        2    False
"""

import pandas as pd

# Create the DataFrame
data = {'Node': ['ADC-01', 'ADC-02', 'ADC-03', 'ADC-04',
				 'ADC-05', 'ADC-06', 'ADC-07'],
        'Samples': [10, 12, 100, 23, 18, 20, 2]}
df = pd.DataFrame(data)

# Calculate the Interquartile Range (IQR)
Q1 = df['Samples'].quantile(0.25)
Q3 = df['Samples'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Detect outliers
df['Outlier'] = (df['Samples'] < lower_bound) | (df['Samples'] > upper_bound)

# Display the DataFrame with the outlier column
print("DataFrame with Outlier Column:")
print(df)
