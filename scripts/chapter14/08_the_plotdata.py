"""
Engineering Statistics and Data Analysis - Basic Statistical Analysis
Subsection: Choosing an Axis for Matrix Statistics
Example: Temperature Data Analysis with Python
Listing: The plotdata()
Source: chapters/chapter14.tex, line 343
"""

def plotdata(x, y, xlabel, ylabel):
    """
    Plot the x and y data with labels, legend, and title. The y-axis is adjusted to accommodate the legend.
    """
    plt.plot(x, y[:, 0], '-o', label='City A')
    plt.plot(x, y[:, 1], '-o', label='City B')
    plt.plot(x, y[:, 2], '-o', label='City C')

    # Set labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title('Temperature Reading over a Month for 3 Cities')

    # Adjust y-axis limit by adding an arbitrary increase to the max value
    plt.ylim([np.min(y) - 2, np.max(y) + 10])  # Adds extra space above and below

    # Place the legend in the top right corner
    plt.legend(loc='upper right')

    plt.grid(True)
    plt.show()
