"""
cheatsheet
Source: cheatsheet.tex, line 93
"""

import numpy as np
a = np.array([1, 2, 3])
A = np.array([[1, 2],
			  [3, 4]])
np.zeros(5)
np.ones(5)
np.arange(0, 10, 2)
np.linspace(0, 1, 5)
a.shape; A.shape; A.T
A[:, 0]
A[0, :]
A @ A           # matmul
np.dot(a, b)
np.cross(a, b)
np.linalg.solve(A, b)
np.linalg.inv(A)
np.linalg.det(A)
val, vec = np.linalg.eig(A)
a.mean()
a.std(ddof=1)
np.sqrt(a)
np.abs(a)
np.exp(a)
np.where(a > 0) # indices
a[a > 0]   # boolean mask
np.isnan(a)
np.argmin(a)
	
