## solution challenge 
# replace values with np.nan
df_clean.loc[df_clean["Altitude (meters)"] > max_height, "Altitude (meters)"] = np.nan