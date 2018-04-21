## Solution Challenge 4

## convert int into string
data_ts.year.astype(str)

## concatenate string columns
date_string = data_ts.year.astype(str) + "-" + data_ts.month.astype(str)

## generate PeriodIndex object
idx = pd.to_datetime(date_string).dt.to_period('M')

## assign PeriodIndex to the DataFrame object
data_ts.set_index(idx, inplace=True) # use inplace=True to make change permanent

## review index
data_ts.index

## plot first rows of the data set
data_ts.head()