from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# x = random.chisquare(df=2, size=(2, 3))
# sns.kdeplot(random.chisquare(df=1, size=1000))
# print(x)

# Defective Bulbs Test
data = np.random.chisquare(df=4, size=1000) # df - degree of freedom
sns.kdeplot(data)
plt.xlabel("Chi-Square Value")
plt.ylabel("Density")
plt.title("Chi-Square Distribution (Quality Control Example)")
plt.show()