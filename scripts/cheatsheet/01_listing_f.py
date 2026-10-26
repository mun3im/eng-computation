"""
cheatsheet
Source: cheatsheet.tex, line 31
"""

x = 10          # var
a = [1, 2, 3]   # list
a[0]; a[-1]; a[1:3]
for x in a: ...
for i, v in enumerate(a): ...
for w, s in zip(w_lst, s_lst): ...
if x > 0: ...
elif x == 0: ...
else: ...
def f(x):
	return x**2
with open("f.txt") as fh:
	txt = fh.read()
try:
	1 / x
except ZeroDivisionError:
	print("error")
f"{x:.2f}"      # f-string
range(0, 10, 2)
	
