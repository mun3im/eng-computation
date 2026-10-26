"""
cheatsheet
Source: cheatsheet.tex, line 127
"""

np.diff(y)       # diffs
np.gradient(y, x)
np.cumsum(y)     # runsum
np.trapezoid(y, x) # np.trapz
np.interp(x_new, x, y)
p = np.polyfit(x, y, deg=2)
np.polyval(p, x)
np.roots(p)
	
