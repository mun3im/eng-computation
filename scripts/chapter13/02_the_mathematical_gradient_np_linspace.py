"""
Numerical Calculus and System Models - Numerical Calculus
Subsection: The Mathematical Gradient
Source: chapters/chapter13.tex, line 150
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Define our physical constants
C = 10e-6      # 10 microfarads (10 * 10^-6 Farads)
f = 50         # 50 Hz AC frequency

# 2. Set up our time array (2 full cycles of AC power = 40 milliseconds)
t = np.linspace(0, 0.04, 1000)  # 1000 data points

# 3. Define our Voltage signal: v(t) = 5 * sin(2 * pi * f * t)
v = 5 * np.sin(2 * np.pi * f * t)

# 4. Calculate the time step size (difference between consecutive time points)
dt = t[1] - t[0]

# 5. Use np.gradient to calculate the rate of change (dv/dt)
dv_dt = np.gradient(v, dt)

# 6. Apply the physical formula: i = C * (dv/dt)
i = C * dv_dt
i_mA = i * 1000  # Convert to milliamperes for easy reading

# --- Let's visualize the relationship! ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Top Plot: Voltage
ax1.plot(t * 1000, v, color='#007acc', linewidth=2.5, label='Voltage $v(t)$')
ax1.set_ylabel('Voltage (V)', color='#007acc', fontsize=11, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='#007acc')
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_title('Capacitor Voltage and Current Relationships', fontsize=12, fontweight='bold')
ax1.legend(loc='upper right')

# Bottom Plot: Current
ax2.plot(t * 1000, i_mA, color='#e05a47', linewidth=2.5, label='Calculated Current $i(t)$')
ax2.set_xlabel('Time (ms)', fontsize=11, fontweight='bold')
ax2.set_ylabel('Current (mA)', color='#e05a47', fontsize=11, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='#e05a47')
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()
