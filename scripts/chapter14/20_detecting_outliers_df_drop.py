"""
Engineering Statistics and Data Analysis - Data Cleaning and Preprocessing
Subsection: Identifying and Handling Outliers with pandas
Example: Detecting Outliers
Source: chapters/chapter14.tex, line 1148

Output as printed in the book:
    Final DataFrame after replacing NaN with the median:
         Node  Samples
    0  ADC-01     10.0
    1  ADC-02     12.0
    2  ADC-03     15.0
    3  ADC-04     23.0
    4  ADC-05     18.0
    5  ADC-06     20.0
    6  ADC-07      2.0
"""

# Drop the 'Outlier' column
# Remove the 'Outlier' column from the DataFrame
df = df.drop(columns=['Outlier'])
# Display the final DataFrame
# Confirm all outliers are replaced and the 'Outlier' column is removed
print("\nFinal DataFrame after replacing NaN with the median:")
print(df)
