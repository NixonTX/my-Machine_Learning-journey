from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x = random.exponential(scale=2, size=(2, 3))

# print(x)

# sns.kdeplot(random.exponential(size=1000))

# plt.show()
# Waiting time for 100 bus
waiting_times = np.random.exponential(scale=10, size=100)

sns.kdeplot(waiting_times)
plt.xlabel("Waiting Time (minutes)")
plt.ylabel("Density")
plt.title("Exponential Distribution of Bus Waiting Time")
plt.show()