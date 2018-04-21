## Solution Challenge 11
URL = data_url("germany")
df = read_temp_data(URL)
df = monthly_index(df)
plot_anomalies(df, title="Germany")