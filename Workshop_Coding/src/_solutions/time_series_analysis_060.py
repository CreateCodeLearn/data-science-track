## Solution Challenge 6
fig, ax = plt.subplots()
data_monthly.anomaly.plot.hist(bins=20, ax=ax)

fig, ax = plt.subplots()
data_monthly.anomaly.loc["1850":"1900"].hist(bins=20, alpha=0.4, ax=ax)
data_monthly.anomaly.loc["1950":"2000"].hist(bins=20, alpha=0.4, ax=ax)