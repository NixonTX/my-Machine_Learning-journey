import pandas as pd

df = pd.read_csv('clean_data.csv')

# print(df.to_string())
h = df[df['Calories'] > 300]

# print(h)

df['Pulse'] = pd.to_numeric(df['Pulse'], errors= 'coerce')
df = df.dropna(subset=['Pulse'])

# print(df.columns)
# print(df.dtypes)

# i = df.groupby('Pulse').mean()

# print(i.head())

# print(df.isna().sum())
# print(df.duplicated().sum())
print(df.describe())