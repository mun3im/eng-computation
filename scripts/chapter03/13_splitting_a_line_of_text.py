"""
Numbers, Variables and Units - Splitting a Line of Text

Output as printed in the book:
    ['time_s', 'voltage_V', 'current_mA']
    3 columns; the second is voltage_V
    11463.0 mV
"""

line = "time_s,voltage_V,current_mA"    # first line of bench_rc.csv
names = line.split(",")
print(names)
print(len(names), "columns; the second is", names[1])

row = "0.02,11.4630,2.4486"
values = row.split(",")
voltage = float(values[1])                # text -> number
print(f"{voltage * 1000:.1f} mV")
