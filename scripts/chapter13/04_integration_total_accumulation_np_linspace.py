"""
Numerical Calculus and System Models - Numerical Calculus
Subsection: Integration (Total Accumulation)
Source: chapters/chapter13.tex, line 255
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Setup constants
C = 10e-6         # 10 microfarads
t = np.linspace(0, 0.05, 1000)  # 50 milliseconds
dt = t[1] - t[0]

# 2. Constant current of 2 mA (0.002 Amps)
i = np.ones_like(t) * 0.002

# 3. Calculate accumulated current over time
# We multiply the cumulative sum of current by our time step size (dt)
# to represent the area under the current curve.
accumulated_current = np.cumsum(i) * dt

# 4. Apply physical formula: v = (1/C) * accumulated_current
v = (1 / C) * accumulated_current

# --- Let's visualize the charging capacitor ---
fig, ax1 = plt.subplots(figsize=(7, 4))

ax1.plot(t * 1000, v, color='#007acc', linewidth=2.5, label='Capacitor Voltage')
ax1.set_xlabel('Time (ms)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Voltage (V)', color='#007acc', fontsize=11, fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_title('Charging a Capacitor with Constant Current (Numerical Integration)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()
