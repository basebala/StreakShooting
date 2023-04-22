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

    # Counts value will return as 0 if shot is layup/dunk or is a three
    if "dunk" in (df.iloc[i, 2]).lower() or "layup" in (df.iloc[i, 2]).lower() or df.iloc[i, 3] == 3:
        df.iloc[i, 7] = 0

        # Streak will reset if non-counted shot is a miss
        if df.iloc[i, 1] == 0:
            streak = 0

    # Streak will reset is game day does not match or shot is a miss
    elif df.iloc[i - 1, 0] != df.iloc[i, 0] or df.iloc[i, 1] == 0:
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

    # Counts value will return as 0 if shot is layup/dunk or is a three
    if "dunk" in (df2.iloc[i, 2]).lower() or "layup" in (df2.iloc[i, 2]).lower() or df2.iloc[i, 3] == 3:
        df2.iloc[i, 7] = 0

        # Streak will reset if non-counted shot is a miss
        if df2.iloc[i, 1] == 0:
            streak = 0

    # Streak will reset is game day does not match or shot is a miss
    elif df2.iloc[i - 1, 0] != df2.iloc[i, 0] or df2.iloc[i, 1] == 0:
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
twos0 = pd.DataFrame()
twos1 = pd.DataFrame()
twos2 = pd.DataFrame()
twos3 = pd.DataFrame()
twos4 = pd.DataFrame()
twos5 = pd.DataFrame()
twos6 = pd.DataFrame()
twos7 = pd.DataFrame()
twos8 = pd.DataFrame()
twos9 = pd.DataFrame()

print()
print("appending start")

# Appends all the values of 2018 shot streaks into the data frames
for i in range(len(df)):
    if df.iloc[i, 7] == 1:
        if df.iloc[i, 6] == 0:
            twos0 = twos0.append(df.iloc[i])
        if df.iloc[i, 6] == 1:
            twos1 = twos1.append(df.iloc[i])
        if df.iloc[i, 6] == 2:
            twos2 = twos2.append(df.iloc[i])
        if df.iloc[i, 6] == 3:
            twos3 = twos3.append(df.iloc[i])
        if df.iloc[i, 6] == 4:
            twos4 = twos4.append(df.iloc[i])
        if df.iloc[i, 6] == 5:
            twos5 = twos5.append(df.iloc[i])
        if df.iloc[i, 6] == 6:
            twos6 = twos6.append(df.iloc[i])
        if df.iloc[i, 6] == 7:
            twos7 = twos7.append(df.iloc[i])
        if df.iloc[i, 6] == 8:
            twos8 = twos8.append(df.iloc[i])
        if df.iloc[i, 6] == 9:
            twos9 = twos9.append(df.iloc[i])
    if i % 10000 == 0:
        print("row: " + str(i))

print()
print("appending2 start")

# Appends all the values of 2016 shot streaks into the data frames
for i in range(len(df2)):
    if df2.iloc[i, 7] == 1:
        if df2.iloc[i, 6] == 0:
            twos0 = twos0.append(df2.iloc[i])
        if df2.iloc[i, 6] == 1:
            twos1 = twos1.append(df2.iloc[i])
        if df2.iloc[i, 6] == 2:
            twos2 = twos2.append(df2.iloc[i])
        if df2.iloc[i, 6] == 3:
            twos3 = twos3.append(df2.iloc[i])
        if df2.iloc[i, 6] == 4:
            twos4 = twos4.append(df2.iloc[i])
        if df2.iloc[i, 6] == 5:
            twos5 = twos5.append(df2.iloc[i])
        if df2.iloc[i, 6] == 6:
            twos6 = twos6.append(df2.iloc[i])
        if df2.iloc[i, 6] == 7:
            twos7 = twos7.append(df2.iloc[i])
        if df2.iloc[i, 6] == 8:
            twos8 = twos8.append(df2.iloc[i])
        if df2.iloc[i, 6] == 9:
            twos9 = twos9.append(df2.iloc[i])
    if i % 10000 == 0:
        print("row: " + str(i))

# Appends all of the data frames into its individual csv files
twos0.to_csv("twos0.csv")
twos1.to_csv("twos1.csv")
twos2.to_csv("twos2.csv")
twos3.to_csv("twos3.csv")
twos4.to_csv("twos4.csv")
twos5.to_csv("twos5.csv")
twos6.to_csv("twos6.csv")
twos7.to_csv("twos7.csv")

# When ran, there where recorded twos streaks of higher than 7
