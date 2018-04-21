## Solution Challenge 3

FILEPATH = "../data/Complete_TAVG_complete.txt"

pd.read_csv(FILEPATH) # note this causes an ParserError, comment out that line
pd.read_csv(FILEPATH, comment="%")
pd.read_csv(FILEPATH, comment="%", delim_whitespace=True)
pd.read_csv(FILEPATH, comment="%", delim_whitespace=True, header=None)
pd.read_csv(FILEPATH, comment="%", delim_whitespace=True, header=None, usecols=[0, 1, 2, 3])

COLUMN_NAMES = ["year", "month", "anomaly", "uncertainty"]
pd.read_csv(FILEPATH, comment="%", delim_whitespace=True, header=None, usecols=[0, 1, 2, 3], names=COLUMN_NAMES)