"""
Handling Imperfect Engineering Data - Missing Data and Outliers
Subsection: What Is an Outlier?
Example: Investigating a Suspicious Reading
"""

# Having concluded (from the steps above) that sample 18 is a sensor fault,
# flag it explicitly rather than silently overwriting it
is_suspect = np.zeros(t.size, dtype=bool)
is_suspect[18] = True

temp_flagged = temp.copy()
temp_flagged[is_suspect] = np.nan  # mark the flagged sample as missing

# Repair using the same interpolation tool used for missing data
temp_repaired = temp_flagged.copy()
temp_repaired[is_suspect] = np.interp(t[is_suspect], t[~is_suspect], temp_flagged[~is_suspect])
