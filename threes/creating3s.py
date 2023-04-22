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

    # Counts value will return as 0 if points made is not a 3
    if df.iloc[i, 3] != 3:
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

    # Counts value will return as 0 if points made is not a 3
    if df2.iloc[i, 3] != 3:
        df2.iloc[i, 7] = 0

        # Streak will reset if non-counted shot is a miss
        if df2.iloc[i, 1] == 0:
            streak = 0

    # Streak will reset is game day does not match or shot is a miss
    elif df2.iloc[i - 1, 0] != df2.iloc[i, 0] or df2.iloc[i, 1] == 0:
        streak = 0
    else:
        streak += 1

    if i % 10000 == 0:
        print("row: " + str(i))
    if streak > high:
        high = streak
        print("highest: " + str(high))

    # Shot streak will increase if all other test cases fail
    if streak not in counter:
        if df2.iloc[i, 7] != 0:
            counter[streak] = 1
    else:
        if df2.iloc[i, 7] != 0:
            counter[streak] += 1

# Prints counter ht of recorded shot attempts at each streak count
print(counter)

# Creates all of the shot streak data frames
threes0 = pd.DataFrame()
threes1 = pd.DataFrame()
threes2 = pd.DataFrame()
threes3 = pd.DataFrame()
threes4 = pd.DataFrame()
threes5 = pd.DataFrame()
threes6 = pd.DataFrame()
threes7 = pd.DataFrame()
threes8 = pd.DataFrame()
threes9 = pd.DataFrame()

print()
print("appending start")

# Appends all the values of 2018 shot streaks into the data frames
for i in range(len(df)):
    if df.iloc[i, 7] == 1:
        if df.iloc[i, 6] == 0:
            threes0 = threes0.append(df.iloc[i])
        if df.iloc[i, 6] == 1:
            threes1 = threes1.append(df.iloc[i])
        if df.iloc[i, 6] == 2:
            threes2 = threes2.append(df.iloc[i])
        if df.iloc[i, 6] == 3:
            threes3 = threes3.append(df.iloc[i])
        if df.iloc[i, 6] == 4:
            threes4 = threes4.append(df.iloc[i])
        if df.iloc[i, 6] == 5:
            threes5 = threes5.append(df.iloc[i])
        if df.iloc[i, 6] == 6:
            threes6 = threes6.append(df.iloc[i])
        if df.iloc[i, 6] == 7:
            threes7 = threes7.append(df.iloc[i])
        if df.iloc[i, 6] == 8:
            threes8 = threes8.append(df.iloc[i])
        if df.iloc[i, 6] == 9:
            threes9 = threes9.append(df.iloc[i])
    if i % 10000 == 0:
        print("row: " + str(i))

print()
print("appending2 start")

# Appends all the values of 2016 shot streaks into the data frames
for i in range(len(df2)):
    if df2.iloc[i, 7] == 1:
        if df2.iloc[i, 6] == 0:
            threes0 = threes0.append(df2.iloc[i])
        if df2.iloc[i, 6] == 1:
            threes1 = threes1.append(df2.iloc[i])
        if df2.iloc[i, 6] == 2:
            threes2 = threes2.append(df2.iloc[i])
        if df2.iloc[i, 6] == 3:
            threes3 = threes3.append(df2.iloc[i])
        if df2.iloc[i, 6] == 4:
            threes4 = threes4.append(df2.iloc[i])
        if df2.iloc[i, 6] == 5:
            threes5 = threes5.append(df2.iloc[i])
        if df2.iloc[i, 6] == 6:
            threes6 = threes6.append(df2.iloc[i])
        if df2.iloc[i, 6] == 7:
            threes7 = threes7.append(df2.iloc[i])
        if df2.iloc[i, 6] == 8:
            threes8 = threes8.append(df2.iloc[i])
        if df2.iloc[i, 6] == 9:
            threes9 = threes9.append(df2.iloc[i])
    if i % 10000 == 0:
        print("row: " + str(i))

# Appends all of the data frames into its individual csv files
threes0.to_csv("threes0.csv")
threes1.to_csv("threes1.csv")
threes2.to_csv("threes2.csv")
threes3.to_csv("threes3.csv")
threes4.to_csv("threes4.csv")
threes5.to_csv("threes5.csv")
threes6.to_csv("threes6.csv")
threes7.to_csv("threes7.csv")
threes8.to_csv("threes8.csv")
threes9.to_csv("threes9.csv")
