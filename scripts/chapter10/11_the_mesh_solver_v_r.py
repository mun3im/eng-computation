"""
Measurements, Files and Spreadsheets - Case Study: Mesh Circuits
Subsection: The mesh\_solver(V, R)
"""

def mesh_solver(V, R):
    """
    Computes the current I on every loop of a mesh circuit.

    Parameters:
    V (np.ndarray): Column vector of voltage sources on each loop.
    R (np.ndarray): 2D array representing resistances and current indicators.

    Returns:
    np.ndarray: Column vector of the computed current on each loop.
    """
    i, r, M = separate_ir(R)
    Rmat = np.zeros((M, M))

    for m in range(M):
        for n in range(M):
            ind_i = np.logical_and(i[m, :], i[n, :])
            if n != m:
                Rmat[m, n] = -np.sum(r[ind_i])
            else:
                Rmat[m, n] = np.sum(r[ind_i])

    I = np.linalg.solve(Rmat, V)
    return I
