## Pandas - Cleaning Data - fixing bad data in your data set. ##
"""
Bad data could be:
    Empty cells
    Data in wrong format
    Wrong data
    Duplicates
"""

import pandas as pd

df = pd.read_csv("clean_data.csv")

# new_df = df.dropna()    # remove rows that contain empty cells - no change in the original

# print(new_df.to_string())

# df.dropna(inplace=True)   # does change the original
# df.fillna(130, inplace=True)    # fill null with value
# df["Calories"].fillna(130, inplace=True)

x = df["Calories"].mean()
# x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace=True)

"""
Median = the value in the middle, after you have sorted all values ascending.

Mode = the value that appears most frequently.
"""
print(df.to_string())