import pandas as pd
import math

df = pd.read_csv("streaks.csv")
df2 = pd.DataFrame(columns=list('ABCDE'))


def getRadius(locX, locY):
    return int(math.sqrt(locX ** 2 + locY ** 2))


def getAngle(locX, locY):
    if locX == 0:
        return 90
    if math.atan(locY / locX) * 180 / math.pi > 0:
        return math.atan(locY / locX) * 180 / math.pi
    else:
        return math.atan(locY / locX) * 180 / math.pi + 180


def getZone(radius, angle, shotType):
    if "layup" in shotType.lower() or "dunk" in shotType.lower():
        return 1
    elif angle < 55 and radius <= 220:
        return 4
    elif angle < 55:
        return 7
    elif angle <= 125 and radius <= 220:
        return 3
    elif angle <= 125:
        return 6
    elif radius <= 220:
        return 2
    else:
        return 5


def getZone2(shotScore, shotType):
    if "layup" in shotType.lower() or "dunk" in shotType.lower():
        return 1
    elif shotScore == 3:
        return 3
    return 2


for i in range(0, len(df), 4):
    temp = []
    for j in range(4):
        zone = getZone2(df.iloc[i + j, 6], df.iloc[i + j, 5])
        temp.append(zone)
        temp.append(df.iloc[(i + j), 4])
    df3 = pd.DataFrame([temp], columns=list('ABCDE'))
    df2 = df2.append(df3, ignore_index=True)

sum = 0
sum2 = 0
for i in range(573):
    if df2.iloc[i, 3] > 4:
        sum += 1
    else:
        sum2 += 1
print(sum / 573)
print(sum2 / 573)

df2.to_csv('streaksV2.csv', index=False, header=False)
