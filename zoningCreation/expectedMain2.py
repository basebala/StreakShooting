import pandas as pd

df = pd.read_csv("streaksV2.csv")
df2 = pd.DataFrame(columns=list('ABCD'))

ht = {}

for row in range(len(df)):
    temp = []
    for col in range(3):
        temp.append(str(df.iloc[row, col]))
    temp.sort()
    string = "".join(temp)

    if string not in ht:
        ht[string] = []
    ht[string].append([df.iloc[row, col + 1], df.iloc[row, col + 2]])


def attempt(zone):
    if zone == 1:
        return 1
    if zone == 2:
        return 2
    return 3


count = 0
for x in ht:
    count += 1
print(count)

for x in sorted(ht):
    temp1 = [x, 1]
    temp2 = [x, 2]
    temp3 = [x, 3]

    made1 = 0
    made2 = 0
    made3 = 0
    attempt1 = 0
    attempt2 = 0
    attempt3 = 0

    for y in sorted(ht[x]):
        if attempt(y[0]) == 1:
            made1 += y[1]
            attempt1 += 1
        if attempt(y[0]) == 2:
            made2 += y[1]
            attempt2 += 1
        if attempt(y[0]) == 3:
            made3 += y[1]
            attempt3 += 1

    if attempt1 == 0:
        per1 = 0
    else:
        per1 = made1 / attempt1 * 100
    if attempt2 == 0:
        per2 = 0
    else:
        per2 = made2 / attempt2 * 100
    if attempt3 == 0:
        per3 = 0
    else:
        per3 = made3 / attempt3 * 100

    temp1 += [str(made1) + "/" + str(attempt1), per1]
    temp2 += [str(made2) + "/" + str(attempt2), per2]
    temp3 += [str(made3) + "/" + str(attempt3), per3]

    df3 = pd.DataFrame([temp1], columns=list('ABCD'))
    df2 = df2.append(df3, ignore_index=True)
    df3 = pd.DataFrame([temp2], columns=list('ABCD'))
    df2 = df2.append(df3, ignore_index=True)
    df3 = pd.DataFrame([temp3], columns=list('ABCD'))
    df2 = df2.append(df3, ignore_index=True)

df2.to_csv('streaksV3.csv', index=False, header=False)
