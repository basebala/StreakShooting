import pandas as pd
from matplotlib import pyplot as plt
import math
import numpy as np

df = pd.read_csv("attempted0.csv")
df1 = pd.read_csv("attempted1.csv")
df2 = pd.read_csv("attempted2.csv")
df3 = pd.read_csv("attempted3.csv")
df4 = pd.read_csv("attempted4.csv")
df5 = pd.read_csv("attempted5.csv")
# df6 = pd.read_csv("attempted6.csv")
# df7 = pd.read_csv("attempted7.csv")
# df8 = pd.read_csv("attempted8.csv")
# df9 = pd.read_csv("attempted9.csv")

y = []
sum0 = 0
count = 0
for x in range(len(df)):
    sum0 += math.sqrt(df.iloc[x, 5]**2+df.iloc[x, 6]**2)
    count += 1
print("attempted 0:  " + str(sum0/count))
y.append(sum0/count)

sum1 = 0
count = 0
for x in range(len(df1)):
    sum += math.sqrt(df1.iloc[x, 5] ** 2 + df1.iloc[x, 6] ** 2)
    count += 1
print("attempted 1:  " + str(sum1/count))
y.append(sum1/count)

sum2 = 0
count = 0
for x in range(len(df2)):
    sum2 += math.sqrt(df2.iloc[x, 5] ** 2 + df2.iloc[x, 6] ** 2)
    count += 1
print("attempted 2:  " + str(sum2/count))
y.append(sum2/count)

sum3 = 0
count = 0
for x in range(len(df3)):
    sum3 += math.sqrt(df3.iloc[x, 5] ** 2 + df3.iloc[x, 6] ** 2)
    count += 1
print("attempted 3:  " + str(sum3/count))
y.append(sum3/count)

sum4 = 0
count = 0
for x in range(len(df4)):
    sum4 += math.sqrt(df4.iloc[x, 5] ** 2 + df4.iloc[x, 6] ** 2)
    count += 1
print("attempted 4:  " + str(sum4/count))
y.append(sum4/count)

sum5 = 0
count = 0
for x in range(len(df5)):
    sum5 += math.sqrt(df5.iloc[x, 5] ** 2 + df5.iloc[x, 6] ** 2)
    count += 1
print("attempted 5:  " + str(sum5/count))
y.append(sum5/count)

"""
sum6 = 0
count = 0
for x in range(len(df6)):
    sum6 += math.sqrt(df6.iloc[x, 5] ** 2 + df6.iloc[x, 6] ** 2)
    count += 1
print("attempted 6:  " + str(sum6/count))
y.append(sum6/count)

sum7 = 0
count = 0
for x in range(len(df7)):
    sum7 += math.sqrt(df7.iloc[x, 5] ** 2 + df7.iloc[x, 6] ** 2)
    count += 1
print("attempted 7:  " + str(sum7/count))
y.append(sum7/count)

sum8 = 0
count = 0
for x in range(len(df8)):
    sum8 += math.sqrt(df8.iloc[x, 5] ** 2 + df8.iloc[x, 6] ** 2)
    count += 1
print("attempted 8:  " + str(sum8/count))
y.append(sum8/count)

sum9 = 0
count = 0
for x in range(len(df9)):
    sum9 += math.sqrt(df9.iloc[x, 5] ** 2 + df9.iloc[x, 6] ** 2)
    count += 1
print("attempted 9:  " + str(sum9/count))
y.append(sum9/count)
"""


xx = [0, 1, 2, 3, 4, 5]

print(np.corrcoef(xx, y))
yy = np.array([y[0], y[1], y[2], y[3], y[4], y[5]])
x = np.array([0, 1, 2, 3, 4, 5])
m, b = np.polyfit(x, yy, 1)

plt.plot(x, m*x + b)


plt.scatter(x, y)
plt.title('Shot Distance vs Attempted Streak Length')
plt.xlabel('Attempted Streak Length')
plt.ylabel('Shot Distance')
plt.show()
