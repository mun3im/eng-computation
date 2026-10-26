"""
Engineering Statistics and Data Analysis - pandas for Data Analytics
Subsection: DataFrames
Example: Creating a DataFrame
Source: chapters/chapter14.tex, line 789

Output as printed in the book:
        Sensor  Readings
    0   TMP-01        10
    1   TMP-02        12
    2   TMP-03        16
    3   TMP-04        23
    4   TMP-05        18
    5   TMP-06        20
    6   TMP-07        25
    7   TMP-08        30
    8   TMP-09         8
    9   TMP-10        14
    10  TMP-11         5
    11  TMP-12        11
    Mean of Readings: 16.0
"""

import pandas as pd

# Faulty-sample counts logged by twelve temperature sensors
Sensor = ['TMP-01', 'TMP-02', 'TMP-03', 'TMP-04', 'TMP-05', 'TMP-06',
          'TMP-07', 'TMP-08', 'TMP-09', 'TMP-10', 'TMP-11', 'TMP-12']
Readings = [10, 12, 16, 23, 18, 20,
            25, 30, 8, 14, 5, 11]

# Create the DataFrame
df = pd.DataFrame({'Sensor': Sensor, 'Readings': Readings})

# Display the DataFrame
print(df)

# Calculate and display the mean of the Readings column
mean_readings = df['Readings'].mean()
print("Mean of Readings:", mean_readings)
