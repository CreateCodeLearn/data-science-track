## Solution Challenge 10
def data_url(country):
    '''
    Function to build url for data retrieval
    '''
    BASE_URL = "http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/"
    SUFFIX_URL = "-TAVG-Trend.txt"
    return(BASE_URL + country + SUFFIX_URL)