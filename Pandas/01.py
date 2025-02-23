import pandas as pd
import os

mydataset = {
    'rockets': ["Falcon-9", "Starship", "Vikas"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

# print(myvar)
# print(pd.__version__)

a = [1, 7, 2, 6, 8]
myvar = pd.Series(a, index = ["x", "y", "z", "a'", "b'"])

# print(myvar["a'"])

calories = {"d1": 420, "d2": 380, "d3": 390}
myvar = pd.Series(calories, index = ["d1", "d2"])

# print(myvar)

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
    # "time": ["second", "minute", "hour"]
}

df = pd.DataFrame(data)
# print(myvar)

# print(df.loc[[0, 1]])

# CSV Files - comma separated files
# os.chdir(r"C:\Users\nixon\Desktop\ML\L0\Pandas")
df = pd.read_csv("test-data/data.csv")

# print(df.to_string())

# print("Current Working Directory:", os.getcwd())

pd.options.display.max_rows = 9999
# print(df)
# print(pd.options.display.max_rows)

df = pd.read_json("test-data/data.json")
# print(df.to_string())

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

# df = pd.DataFrame(data)

# print(df)
print(df.info())