
def kelvin_to_celsius(temperature_K):
    '''
    Function to compute Celsius from Kelvin
    '''
    rv = temperature_K - 273.15
    return rv

def fahrenheit_to_celsius(temperature_F):
    '''
    Function to compite Celsius from Fahrenheit
    '''
    temp_K = fahrenheit_to_kelvin(temperature_F)
    temp_C = kelvin_to_celsius(temp_K)
    return temp_C
    
def fahrenheit_to_kelvin(a):
    """
    Function to compute Fahrenheit from Kelvin
    """
    kelvin = (a-32.0)*5/9 + 273.15
    return kelvin