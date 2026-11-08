"""
Python Reference - Fun to Try: A Degree-to-Radian Table
"""

# Creates a table of degrees to radians
degree_start = int(input('Starting angle in whole degrees: '))
degree_final = int(input('Final angle in whole degrees: '))
incr = int(input('Table increment in whole degrees: '))

# Create the degree list from start to final with the given increment
degree = list(range(degree_start, degree_final + 1, incr))
radian = [deg / 180 for deg in degree]

# Display the header
print('A table of degrees to radians')
print('   deg°     π rad')

# Print each value formatted
for d, r in zip(degree, radian):
    print(f'{d:6.2f}°     {r:.4f}π')
