## Pandas - Cleaning Data of Wrong Format ##

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('clean_data.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')

df.dropna(subset=['Date'], inplace=True)

# print(df.to_string())
# print(df[df['Date'].isna()])


## Pandas - Fixing Wrong Data ##

# df.loc[7, 'Duration'] = 45

# for x in df.index:
#     if df.loc[x, "Duration"] > 120:
#         df.loc[x, "Duration"] = 120

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)

# print(df.to_string())


## Pandas - Removing Duplicates ##
# print(df.duplicated())
df.drop_duplicates(inplace=True)
# print(df.to_string())


## Pandas - Data Correlations ##
# print(df.corr())


## Pandas - Plotting ##
df = pd.read_csv("clean_data.csv")

# df.plot(kind = 'scatter', x = 'Duration', y= 'Calories')
# df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

df["Duration"].plot(kind = 'hist')

# df.plot()
plt.show()