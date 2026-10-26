"""
cheatsheet
Source: cheatsheet.tex, line 171
"""

import matplotlib.pyplot as plt
plt.plot(x, y, label="data")
plt.scatter(x, y)
plt.hist(y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.savefig("f.png")
plt.show()
	
