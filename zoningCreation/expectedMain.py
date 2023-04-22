import pandas as pd

df = (pd.read_csv("2016New.csv"))
df2 = (pd.read_csv("2018Original.csv"))
df3 = pd.DataFrame()

streak = df.iloc[0, 3]
game = df.iloc[0, 0]

for x in range(1, len(df)):
    if x % 1000 == 0:
        print(x)
    if streak == 3:
        for z in range(-3, 1):
            df3 = df3.append(df.iloc[x+z])
    if df.iloc[x, 0] == game and df.iloc[x, 3] == 1:
        streak += 1
    else:
        streak = df.iloc[x, 3]
    game = df.iloc[x, 0]


streak = df2.iloc[0, 3]
game = df2.iloc[0, 0]
for x in range(1, len(df2)):
    if x % 1000 == 0:
        print(x)
    if streak == 3:
        for z in range(-3, 1):
            df3 = df3.append(df2.iloc[x+z])
    if df2.iloc[x, 0] == game and df2.iloc[x, 3] == 1:
        streak += 1
    else:
        streak = df2.iloc[x, 3]
    game = df2.iloc[x, 0]

print(df3.head())
df3["C_QUARTER"] = df3["C_QUARTER"].astype(int)
df3["D_SHOT_MADE"] = df3["D_SHOT_MADE"].astype(int)
df3["H_LOCY"] = df3["H_LOCY"].astype(int)
df3["F_SHOT_SCORE"] = df3["F_SHOT_SCORE"].astype(int)
df3["G_LOCX"] = df3["G_LOCX"].astype(int)

df3.to_csv("streaks.csv")
