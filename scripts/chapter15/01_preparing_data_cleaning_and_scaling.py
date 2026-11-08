"""
A First Look at Machine Learning - Preparing Data: Cleaning and Scaling
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.DataFrame({'height': [157, 163, 176, 152, None]})

# 1. Cleaning: Fill missing values with the mean
df['height'] = df['height'].fillna(df['height'].mean())

# 2. Transformation: Standardization (Mean=0, StdDev=1)
scaler = StandardScaler()
df['height_scaled'] = scaler.fit_transform(df[['height']])
print(df)
