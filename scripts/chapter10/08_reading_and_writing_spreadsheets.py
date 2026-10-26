"""
Measurements, Files and Spreadsheets - Reading and Writing Spreadsheets
Source: chapters/chapter10.tex, line 408
"""

# Reading data from a spreadsheet
# Import data
data = pd.read_excel(filename, sheet_name='Sheet1', usecols='B:Z', header=None)

# Selecting specific rows and columns with iloc
# Select data from the second row and from the second column onwards
selected_data = data.iloc[1, 1:]

# Writing data to a spreadsheet
# Export data
output_data.to_excel(filename, sheet_name='Sheet1', startcol=1, startrow=2, index=False, header=False)
