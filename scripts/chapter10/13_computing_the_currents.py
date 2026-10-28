"""
Measurements, Files and Spreadsheets - Case Study: Mesh Circuits
Subsection: Computing the Currents
"""

# Iterate over each row in the NumPy array to compute currents
for row in data:
    try:
        # Extract R1, R2, R3 and V1, V2 values
        R1, R2, R3 = row[1:4]  # R1, R2, R3 are in columns B, C, D
        V1, V2 = row[4:6]      # V1, V2 are in columns E, F

        # Prepare the R matrix
        R = np.array([
            [R1, R2, R3],
            [1, 0, 1],  # Assuming similar indicator for current flows in all sets
            [0, 1, 1]
        ])

        # Prepare the voltage vector
        V = np.array([V1, V2])

        # Compute currents using mesh_solver function
        I = mesh_solver(V, R)

        # Append the computed currents to the lists
        I1_list.append(I[0])
        I2_list.append(I[1])
    except Exception as e:
        print(f"An error occurred while processing row {row}: {e}")
