"""
Measurements, Files and Spreadsheets - Case Study: Mesh Circuits
Subsection: Reading the Spreadsheet and Setting Up
"""

import pandas as pd
import numpy as np
import os
# Import the mesh_solver function from mesh_solver.py
from mesh_solver import mesh_solver

# Get the current script directory
current_dir = os.path.dirname(__file__)
# Ensure the Excel file is in the same directory
file_path = os.path.join(current_dir, 'circuit_analysis.xlsx')

# Load the Excel file
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Initialize lists to store the computed currents
I1_list = []
I2_list = []

# Convert DataFrame to NumPy array for easier iteration
data = df.to_numpy()
