from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""

df = pd.read_csv("2018Original.csv")
player = "hi"
count=0
sum=0
dict = {'Name': [], 'Made': [], 'Taken': [], 'Percent': []}
df3 = pd.DataFrame(dict)
for x in range(0, len(df)):
    shotType = df.iloc[x, 4]
    if df.iloc[x,1]==player:
        if "layup" in shotType.lower() or "dunk" in shotType.lower():
            count+=1
            sum+=df.iloc[x, 3]
    else:
        if count>200:
            print(player)
            print(sum/count)
            df2 = {'Name': player, 'Made': sum, 'Taken': count, 'Percent': sum/count}
            df3 = df3.append(df2, ignore_index=True)
        player = df.iloc[x, 1]
        sum = 0
        count = 0
        if "layup" in shotType.lower() or "dunk" in shotType.lower():
            count+=1
            sum+=df.iloc[x, 3]


sum=0
count=0
df3 = df3.sort_values('Percent', ascending=False)
f = int(len(df3)/2)
for x in range(0, f):
    sum+=df3.iloc[x, 1]
    count+=df3.iloc[x, 2]

print(sum/count)
print(sum)
print(count)
print(df3.head())
"""

people_in_branch = 50

# Control is Alpaca, Experiment is Bear
control, experiment = np.random.rand(2, people_in_branch)

c_successes = sum(control < 0.8)

# Bears are about 10% better relative to Alpacas
e_successes = sum(experiment < 0.8)

c_failures = people_in_branch - c_successes
e_failures = people_in_branch - e_successes

# Our Priors
prior_successes = 20
prior_failures = 5

fig, ax = plt.subplots(1, 1)

# Control
c_alpha, c_beta = c_successes + prior_successes, c_failures + prior_failures
# Experiment
e_alpha, e_beta = e_successes + prior_successes, e_failures + prior_failures

x = np.linspace(.6, .8, 1000)

# Generate and plot the distributions!
c_distribution = beta(16421, 8102)
e_distribution = beta(592, 235)

ax.plot(x, c_distribution.pdf(x))
ax.plot(x, e_distribution.pdf(x))


ax.set(xlabel='Shot Probability(Blue=Top 50%, Orange=Streak of 4)', ylabel='Density')
ax.set(title='Binomial Distribution of Shot Probability for Layups/Dunks')


plt.show()
sum = 0
count = 0
df = pd.read_csv("attemped3L.csv")
for x in range(len(df)):
    if df.iloc[x, 2] == 1:
        sum += 1
    count += 1

print(sum/count)
print(sum)
print(count-sum)
