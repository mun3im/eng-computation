"""
Measurements, Files and Spreadsheets - Case Study: Mesh Circuits
Subsection: Writing the Results Back to Excel
"""

# Create a DataFrame with only I1 and I2 to append to the original file
I_values_df = pd.DataFrame({'I1': I1_list, 'I2': I2_list})

# Load the existing sheet, keeping the other data intact and appending I1 and I2 correctly
with pd.ExcelWriter(file_path, mode='a', if_sheet_exists='overlay') as writer:
    # Adjusted startrow to 1
    I_values_df.to_excel(writer, startcol=6, startrow=1, index=False, header=False)

# Display confirmation message
print("I1 and I2 have been successfully appended to the Excel file starting from the correct row.")
