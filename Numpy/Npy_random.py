import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.randint(1, 100)
# print(x)
x = random.rand(3)
# print(x)

x = random.randint(1, 10, size=(5))

x = random.choice([3, 5, 7, 9], size=(2, 2))

# Data distribution #
x = random.choice([3, 5, 7, 9], p=[0.2, 0.3, 0.5, 0.0], size=(2, 3)) # p - probability :: the sum of all prob no.s should be 1

# Random permutations #
# Shuffling - shuffle the array
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
# print(arr)

# Permutation - re-arranged array (and leaves the original array un-changed)
arr = np.array([1, 2, 3, 4, 5])
# print(random.permutation(arr))
# print(arr)

# # Seaborn #
# sns.displot([0, 1, 2, 3, 4, 5])
# # plt.show()

# sns.displot([0, 1, 2, 3, 4, 5], hist=False)
# plt.show()


x = random.binomial(n=10, p=0.5, size=10)
# print(x)
# print(np.random.rand(5))
# print(np.random.rand(2, 3))
# print(np.random.randint(1, 10, size=5))
# print(np.random.normal(loc=0, scale=1, size=5))
# print(np.random.choice([1, 2, 3, 4], size=3))
arr = np.array([1, 2, 3, 4])
np.random.shuffle(arr)
# print(arr)

# print(np.random.uniform(low=0.0, high=10.0, size=5))

# Seed
np.random.seed(42) # this value
# print(np.random.rand(3))