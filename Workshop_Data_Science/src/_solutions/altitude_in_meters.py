## solution challenge 
df_clean["Altitude (meters)"] = df_clean["Altitude (Hundreds of Feet)"].apply(lambda x: x*100*0.3048)