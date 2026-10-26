"""
Measurements, Files and Spreadsheets - Importing and Exporting Data in Python
Subsection: Binary Data
Source: chapters/chapter10.tex, line 310
"""

import pickle

# Saving an object to a binary file
data = {'key': 'value'}
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Loading an object from a binary file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)  # Output: {'key': 'value'}
