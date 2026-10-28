"""
Measurements, Files and Spreadsheets - Case Study: Mesh Circuits
Subsection: The separate\_ir(R)
"""

# mesh_solver.py
import numpy as np

def separate_ir(R):
    """
    Separates resistances and current indicators.

    Parameters:
    R (np.ndarray): 2D array with resistances and current flow indicators.

    Returns:
    Tuple: (i, r, total_loops) - current flow indicators, resistor values, and number of loops.
    """
    r = R[0, :]
    i = R[1:, :].astype(bool)
    total_loops = R.shape[0] - 1
    return i, r, total_loops
