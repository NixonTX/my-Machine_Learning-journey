# Binomial Distribution #
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

x = random.binomial(n=10, p=0.5, size=10)
y = random.binomial(n=10, p=0.5, size=1000)
# print(x)
# sns.histplot(y, kde=False)
# plt.show()

n = random.normal(loc=50, scale=5, size=1000)
b = random.binomial(n=100, p=0.5, size=1000)
sns.kdeplot(n, label='normal', linewidth=2)
sns.kdeplot(b, label='binomial', linewidth=2)

plt.legend()
plt.show()