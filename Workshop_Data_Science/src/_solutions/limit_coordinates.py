## solution challenge 
print(df_clean.loc[((df_clean['Target Longitude'] > 180) |
                    (df_clean['Target Longitude'] < -180) | 
                    (df_clean['Target Latitude'] > 90 )| 
                    (df_clean['Target Latitude'] < -90)), 
                   ['Target Longitude', 'Target Latitude']].count())

df_clean.loc[((df_clean['Target Longitude'] > 180) |
                    (df_clean['Target Longitude'] < -180) | 
                    (df_clean['Target Latitude'] > 90 )| 
                    (df_clean['Target Latitude'] < -90)), 
                   ['Target Longitude', 'Target Latitude']] = np.nan