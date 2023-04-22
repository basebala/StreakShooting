"""
WARNING:
Will not run correctly because 2016 & 2018 shot csv files
are not in this current folder. These files are located
in the "shot attempt files" folder
"""

import pandas as pd

# Reads shot files
df = pd.read_csv("2018Original.csv")
df2 = pd.read_csv("2016New.csv")

# Modifies shot files
df2.drop(['B_PLAYER_NAME', 'C_QUARTER', "A"], axis=1, inplace=True)
df.drop(['B_PLAYER_NAME', 'C_QUARTER'], axis=1, inplace=True)
df.insert(6, "I_Streak", 0)
df2.insert(6, "I_Streak", 0)
df.insert(7, "J_Count", 1)
df2.insert(7, "J_Count", 1)

# Counter ht is created to keep track of shots attempted at each streak count
counter = {}

print("df1 start")

# Streak count starts at 0
streak = 0
high = 0

# Iterates through each row from 2018 data frame depending on its values
for i in range(len(df)):

    # Modifies row's streak count to the current streak count
    df.iloc[i, 6] = streak

    # Counts value will return as 0 if shot is layup/dunk
    if "dunk" in (df.iloc[i, 2]).lower() or "layup" in (df.iloc[i, 2]).lower():
        df.iloc[i, 7] = 0

        # Streak will reset if non-counted shot is a miss
        if df.iloc[i, 1] == 0:
            streak = 0

    # Streak will reset is game day does not match or shot is a miss
    elif df.iloc[i-1, 0] != df.iloc[i, 0] or df.iloc[i, 1] == 0:
        streak = 0

    # Shot streak will increase if all other test cases fail
    else:
        streak += 1

    if i % 10000 == 0:
        print("row: " + str(i))
    if streak > high:
        high = streak
        print("highest: " + str(high))

    # Modified counter ht to show how many shots were attempted at each streak count
    if streak not in counter:
        if df.iloc[i, 7] != 0:
            counter[streak] = 1
    else:
        if df.iloc[i, 7] != 0:
            counter[streak] += 1

print()
print("df2 start")

# Resets streak count
streak = 0

# Iterates through each row from 2016 data frame depending on its values
for i in range(len(df2)):

    # Modifies row's streak count to the current streak count
    df2.iloc[i, 6] = streak

    # Counts value will return as 0 if shot is layup/dunk
    if "dunk" in (df2.iloc[i, 2]).lower() or "layup" in (df2.iloc[i, 2]).lower():
        df2.iloc[i, 7] = 0

        # Streak will reset if non-counted shot is a miss
        if df2.iloc[i, 1] == 0:
            streak = 0

    # Streak will reset is game day does not match or shot is a miss
    elif df2.iloc[i-1, 0] != df2.iloc[i, 0] or df2.iloc[i, 1] == 0:
        streak = 0

    # Shot streak will increase if all other test cases fail
    else:
        streak += 1

    if i % 10000 == 0:
        print("row: " + str(i))
    if streak > high:
        high = streak
        print("highest: " + str(high))

    # Modified counter ht to show how many shots were attempted at each streak count
    if streak not in counter:
        if df2.iloc[i, 7] != 0:
            counter[streak] = 1
    else:
        if df2.iloc[i, 7] != 0:
            counter[streak] += 1

# Prints counter ht of recorded shot attempts at each streak count
print(counter)

# Creates all of the shot streak data frames
attempted0 = pd.DataFrame()
attempted1 = pd.DataFrame()
attempted2 = pd.DataFrame()
attempted3 = pd.DataFrame()
attempted4 = pd.DataFrame()
attempted5 = pd.DataFrame()
attempted6 = pd.DataFrame()
attempted7 = pd.DataFrame()
attempted8 = pd.DataFrame()
attempted9 = pd.DataFrame()

print()
print("appending start")

# Appends all the values of 2018 shot streaks into the data frames
for i in range(len(df)):
    if df.iloc[i, 7] == 1:
        if df.iloc[i, 6] == 0:
            attempted0 = attempted0.append(df.iloc[i])
        if df.iloc[i, 6] == 1:
            attempted1 = attempted1.append(df.iloc[i])
        if df.iloc[i, 6] == 2:
            attempted2 = attempted2.append(df.iloc[i])
        if df.iloc[i, 6] == 3:
            attempted3 = attempted3.append(df.iloc[i])
        if df.iloc[i, 6] == 4:
            attempted4 = attempted4.append(df.iloc[i])
        if df.iloc[i, 6] == 5:
            attempted5 = attempted5.append(df.iloc[i])
        if df.iloc[i, 6] == 6:
            attempted6 = attempted6.append(df.iloc[i])
        if df.iloc[i, 6] == 7:
            attempted7 = attempted7.append(df.iloc[i])
        if df.iloc[i, 6] == 8:
            attempted8 = attempted8.append(df.iloc[i])
        if df.iloc[i, 6] == 9:
            attempted9 = attempted9.append(df.iloc[i])
    if i % 10000 == 0:
        print("row: " + str(i))

print()
print("appending2 start")

# Appends all the values of 2016 shot streaks into the data frames
for i in range(len(df2)):
    if df2.iloc[i, 7] == 1:
        if df2.iloc[i, 6] == 0:
            attempted0 = attempted0.append(df2.iloc[i])
        if df2.iloc[i, 6] == 1:
            attempted1 = attempted1.append(df2.iloc[i])
        if df2.iloc[i, 6] == 2:
            attempted2 = attempted2.append(df2.iloc[i])
        if df2.iloc[i, 6] == 3:
            attempted3 = attempted3.append(df2.iloc[i])
        if df2.iloc[i, 6] == 4:
            attempted4 = attempted4.append(df2.iloc[i])
        if df2.iloc[i, 6] == 5:
            attempted5 = attempted5.append(df2.iloc[i])
        if df2.iloc[i, 6] == 6:
            attempted6 = attempted6.append(df2.iloc[i])
        if df2.iloc[i, 6] == 7:
            attempted7 = attempted7.append(df2.iloc[i])
        if df2.iloc[i, 6] == 8:
            attempted8 = attempted8.append(df2.iloc[i])
        if df2.iloc[i, 6] == 9:
            attempted9 = attempted9.append(df2.iloc[i])
    if i % 10000 == 0:
        print("row: " + str(i))

# Appends all of the data frames into its individual csv files
attempted0.to_csv("attempted0.csv")
attempted1.to_csv("attempted1.csv")
attempted2.to_csv("attempted2.csv")
attempted3.to_csv("attempted3.csv")
attempted4.to_csv("attempted4.csv")
attempted5.to_csv("attempted5.csv")
attempted6.to_csv("attempted6.csv")
attempted7.to_csv("attempted7.csv")
attempted8.to_csv("attempted8.csv")
attempted9.to_csv("attempted9.csv")
