"""
Python Reference - Special Characters
Subsection: Fun to Try: A Degree-to-Radian Table
Source: appendices/appendixA.tex, line 415
"""

# Creates a table of degrees to radians
degree_start = float(input('What starting value of degree would you like? '))
degree_final = float(input('What final value of degree would you like? '))
incr = float(input('What table increment would you like? '))

# Create the degree list from start to final with the given increment
degree = list(range(int(degree_start), int(degree_final) + 1, int(incr)))
radian = [deg / 180 for deg in degree]

# Display the header
print('A table of degrees to radians')
print(f' deg°       π rad')

# Print each value formatted
for d, r in zip(degree, radian):
    print(f'{d:6.2f}°     {r:10.4f}π')
