"""
Preformed minor changes from 2016Edited.csv file
and put them into 2016New.csv
"""

import pandas as pd

df = pd.read_csv("2016Edited.csv")

for x in range(len(df)):
    if x % 1000 == 0:
        print(x)
    df.iloc[x, 7] -= 41


df["G_LOCX"] = df["G_LOCX"].astype(int)
df["H_LOCY"] = df["H_LOCY"].astype(int)

df.to_csv("2016New.csv")
