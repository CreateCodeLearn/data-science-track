## solution challenge 
df_clean["Mission Date"] = pd.to_datetime(df_clean["Mission Date"], infer_datetime_format=True)