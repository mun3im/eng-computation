"""
Data Visualization - Plotting the Bench Experiment
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the bench recording (see Chapter 10 for what read_csv does)
data = pd.read_csv('bench_rc.csv')
t = data['time_s']
v = data['voltage_V']

plt.plot(t, v, 'o-', markersize=3, linewidth=1.4, label='Measured $v(t)$')
plt.xlabel('Time (s)')
plt.ylabel('Capacitor voltage (V)')
plt.title('RC Discharge: Measured Capacitor Voltage')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()
