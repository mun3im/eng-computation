"""
cheatsheet
Source: cheatsheet.tex, line 188
"""

import pandas as pd
df = pd.read_csv("d.csv")
df.head()
df.info()
df.describe()
df["c"]
df.loc[0]
df.iloc[0]
df.dropna()
df.fillna(0)
df.groupby("c").mean()
df["c"].mean()
df["c"].std()
	
