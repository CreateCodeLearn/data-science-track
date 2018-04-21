## Solution Challenge 8

# create Figure and Axes objetcs
fig, ax = plt.subplots(figsize=(12,6))

## compute window length 10 years --> 12 * 10 months
w = 12*10

## compute 10-year-running mean for anomaly and plot the result
data_monthly.anomaly.rolling(window=w, center=True).mean().plot(ax=ax)

## compute 10-year-running mean for anomaly and add the result to the data frame
data_monthly["10-year-anomaly"] = data_monthly.anomaly.rolling(window=w, center=True).mean()

## compute 10-year-running mean for uncertainty and add the result to the data frame
data_monthly["10-year-uncertainty"] = data_monthly.uncertainty.rolling(window=w, center=True).mean()

## check data set
data_monthly.sample(10)

## plot anomaly
data_monthly.anomaly.plot(ax=ax)

## plot 10-year running mean
data_monthly["10-year-anomaly"].plot(ax=ax)

## compute upper and lower bound of temperature anomaly
upper_bound = data_monthly["10-year-anomaly"] + data_monthly["10-year-uncertainty"]
lower_bound = data_monthly["10-year-anomaly"] - data_monthly["10-year-uncertainty"]

## plot upper and lower bound of temperature anomaly
upper_bound.plot(ax=ax)
lower_bound.plot(ax=ax)