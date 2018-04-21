def read_temp_data(FILEPATH):
    '''
    Read temperature data provided by the open database of Berkeley Earth
    '''
    COLUMN_NAMES = ["year", "month", "anomaly", "uncertainty"]
    df = pd.read_csv(FILEPATH,
                     comment="%", 
                     delim_whitespace=True, 
                     header=None, 
                     usecols=[0, 1, 2, 3], 
                     names=COLUMN_NAMES)
    return(df)