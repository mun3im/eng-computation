"""
Engineering Statistics and Data Analysis - Data Cleaning and Preprocessing
Subsection: Data Inspection: Missing Values
Example: Testing df.isnull()

Output as printed in the book:
    Original DataFrame:
         Node  Samples  Voltage
    0  ADC-01     10.0      2.5
    1  ADC-02      NaN      3.0
    2  ADC-03     16.0      NaN
    3  ADC-04     23.0      2.8
    4    None     18.0      3.2
    5  ADC-06     20.0      2.9
"""

import pandas as pd

# Create a sample DataFrame with missing values
data = {
    'Node': ['ADC-01', 'ADC-02', 'ADC-03', 'ADC-04', None, 'ADC-06'],
    'Samples': [10, None, 16, 23, 18, 20],
    'Voltage': [2.5, 3.0, None, 2.8, 3.2, 2.9]
}
df = pd.DataFrame(data)

# Check for missing values using isnull()
missing_values = df.isnull()

# Display the original DataFrame
print("Original DataFrame:")
print(df)
