import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"], index=["x", "y", "z"])

# print(df.head(1))
# print(df.tail(2))
# print(df.index)
# print(df.info())

# print(df.describe())

# print(df["A"].unique())
# print(df.shape)

results = pd.read_parquet('test-data/mine.parquet', engine='fastparquet')

print(results.head())