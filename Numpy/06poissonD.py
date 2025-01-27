# Poisson distribution #
# Discrete distribution
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# x = random.poisson(lam=2, size=10)
# sns.histplot(x, kde=False)
# print(x)
# plt.show()

x = np.random.poisson(lam=3, size=1000)

sns.histplot(x, kde=True, bins=15, color="blue")
plt.title("Poisson Distribution (λ=3)")
plt.xlabel("No. of events")
plt.ylabel("Freq")
plt.show()