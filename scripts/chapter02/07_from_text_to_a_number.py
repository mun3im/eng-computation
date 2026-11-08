"""
Your First Python Programs - From Text to a Number

Output as printed in the book:
    <class 'str'>
    <class 'float'> 4700.0
    R = 4700.0 ohms
"""

reading = "4.7"                # text, as input() would give it
print(type(reading))

R = float(reading) * 1000      # number, now in ohms
print(type(R), R)

label = "R = " + str(R) + " ohms"
print(label)
