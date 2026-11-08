"""
Numbers, Variables and Units - Collecting Readings in a List

Output as printed in the book:
    [11.8, 12.1, 11.9, 12.4]
    Number of readings: 4
    Highest: 12.4 Lowest: 11.8
    Average: 12.05
"""

readings = []              # an empty list
readings.append(11.8)
readings.append(12.1)
readings.append(11.9)
readings.append(12.4)

print(readings)
print("Number of readings:", len(readings))
print("Highest:", max(readings), "Lowest:", min(readings))
print("Average:", round(sum(readings) / len(readings), 2))
