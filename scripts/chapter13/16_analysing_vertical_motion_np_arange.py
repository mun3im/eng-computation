"""
Numerical Calculus and System Models - Analysing Vertical Motion
"""

# Generate time values from 0 to tground
t = np.arange(0, tground, 0.01)

# Calculate displacement values
d = np.polyval(p, t)

# Plot the vertical displacement
plt.plot(t, d)
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Vertical Displacement')
plt.show()
