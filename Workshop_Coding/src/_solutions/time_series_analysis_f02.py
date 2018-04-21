def monthly_index(df):
    '''
    Provide a time based index to a data frame
    '''    
    ## concatenate string columns
    date_string = df.year.astype(str) + "-" + df.month.astype(str)
    
    ## generate PeriodIndex object
    idx = pd.to_datetime(date_string).dt.to_period('M')

    ## assign PeriodIndex to the DataFrame object
    df.set_index(idx, inplace=True) # use inplace=True to make change permanent
    return(df)    