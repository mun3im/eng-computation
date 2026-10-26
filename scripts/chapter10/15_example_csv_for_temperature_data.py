"""
Measurements, Files and Spreadsheets - CSV Files
Subsection: Example: CSV for Temperature Data
Source: chapters/chapter10.tex, line 743
"""

import pandas as pd
import os

# Set the file path relative to the current script directory
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'tempData.csv')

# Read the data from the CSV file
# Assuming the first row contains labels and the second row has the temperature data
data = pd.read_csv(file_path, header=None)

# Example: use the second row, columns 2 onwards (like .iloc[1, 1:] in Excel)
temp_c = data.iloc[1, 1:]

# Convert Celsius to Fahrenheit
temp_f = temp_c * 9/5 + 32

# Display results
print("Celsius to Fahrenheit Conversion:")
for c, f in zip(temp_c, temp_f):
    print(f'{c:.0f}°C {f:10.2f}°F')

# Append the Fahrenheit data back to the CSV file
# This adds a new row of Fahrenheit values below existing data
output_data = pd.DataFrame([temp_f])
output_data.to_csv(file_path, mode='a', index=False, header=False)
