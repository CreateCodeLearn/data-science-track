## solution challenge 
def features_above_threshold(df, threshold=0.5):    
    cols2keep = df.notnull().sum()/df.shape[0] > threshold 
    rv = df.columns[cols2keep.values]
    return rv