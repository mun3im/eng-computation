"""
Interpolation, Curve Fitting and Calibration - Air Pollutant Index (API) Calculation During a Haze Crisis
"""

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate API values using interpolation
def API_interpolation(km):

    # Given data points
    distances = np.array([0, 6, 15, 23, 30])    # Kilometres
    api_values = np.array([100, 180, 199, 280, 310])  # API values

    # Generate distances from 0 to 30 km at every 1 km
    full_distances = np.arange(0, 31, 1)

    # Interpolating API values linearly between the known points
    interpolated_api = np.interp(full_distances, distances, api_values)

    # Use np.atleast_1d to convert any input to a 1D array
    km = np.atleast_1d(km)

    # Outside the route, np.interp would silently return the end values
    if np.any((km < distances[0]) | (km > distances[-1])):
        raise ValueError('km must be between 0 and 30')

    # Extract API values for the requested km points
    result = {}
    for k in km:  # interpolate at the exact distance requested
        result[k] = round(float(np.interp(k, distances, api_values)), 2)
        print(f"API value at km {k:g} is {result[k]}")

    # Plotting the data
    plt.figure()
    # Known data points
    plt.plot(distances, api_values, 'o', label='Given API values')
    # Interpolated values
    plt.plot(full_distances, interpolated_api, 'x:', label='Interpolated API values')
    plt.xlabel('Distance (km)')
    plt.ylabel('API Value')
    plt.title('API Calculation from 5 Stations')
    plt.grid(True)
    plt.xticks(distances, ['Kulai', 'Senai', 'Skudai', 'Perling', 'Johor Bahru'], rotation=45)
    plt.legend()
    plt.show()
    return result
