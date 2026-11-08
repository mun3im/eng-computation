"""
Handling Imperfect Engineering Data - Investigating a Suspicious Reading
"""

import numpy as np
import matplotlib.pyplot as plt

# Bench temperature log (deg C), sampled once per second, with one suspicious sample
t = np.arange(0, 30, 1.0)
rng = np.random.default_rng(1)   # fixed seed: same 'noise' every run
temp = 25 + 1.5 * np.sin(0.2 * t) + rng.normal(0, 0.1, t.size)
temp[18] = 45.8  # a single sample looks far too high

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, temp, 'o-', label='Logged temperature')
ax.axhline(temp.mean(), color='gray', linestyle=':', label='Mean (for reference)')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Temperature (deg C)')
ax.set_title('Bench temperature log: is sample 18 a fault or a real event?')
ax.legend()
plt.tight_layout()
plt.show()
