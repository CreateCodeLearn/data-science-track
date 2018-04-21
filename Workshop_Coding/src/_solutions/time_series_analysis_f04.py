def plot_country_anomalies(AOI):
    '''
    Function to plot temperature anomaly data for any given country/region 
    of the open database of Earth Berkeley
    '''
    URL = data_url(AOI)
    df = read_temp_data(URL)
    df = monthly_index(df)
    plot_title = "Temperature anomaly relative to the period 1951-1980 for " + AOI.capitalize()
    return(plot_anomalies(df, title=plot_title))