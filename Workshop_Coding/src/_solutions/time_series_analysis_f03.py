def plot_anomalies(df, title):
    '''
    Function to create a time series plot
    '''
    
    ## compute window length 10 years --> 12 * 10 months
    w = 12*10
    
    ## compute 10-year-running mean for anomaly and add the result to the data frame
    df["10-year-anomaly"] = df.anomaly.rolling(window=w, center=True).mean()
    ## compute 10-year-running mean for uncertainty and add the result to the data frame
    df["10-year-uncertainty"] = df.uncertainty.rolling(window=w, center=True).mean()

    ## compute upper and lower bound of temperature anomaly
    upper_bound = df["10-year-anomaly"] + df["10-year-uncertainty"]
    lower_bound = df["10-year-anomaly"] - df["10-year-uncertainty"]
    
    ## Plotting ##
    ## Note that we make use to the matplotlib library as we have 
    ## even more controll over the aesthetics of the figure
    import matplotlib.pyplot as plt
    
    ## create figure and axis objects
    fig, ax = plt.subplots(figsize=(12,6))
    ## plot monthly anomaly
    df["anomaly"].plot(ax=ax, alpha=0.3, linewidth=0.5, color="blue")
    ## plot 10-year-anomaly
    df["10-year-anomaly"].plot(ax=ax, linewidth=2, color="red")
    ## fill area between upper and lower uncertainty bound
    ax.fill_between(df.index, lower_bound, upper_bound,color="gray", alpha=0.8)
    
    ## add line at y=0
    ax.axhline(y=0, linewidth=0.85, linestyle="--", color="black")

    ## set figure title
    ax.set_title(title, size=18)
    ## set label for y axis
    ax.set_ylabel("$^\circ$C")
    
    ## add legend
    plt.legend()
    
    return(fig, ax)