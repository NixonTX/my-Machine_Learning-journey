from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.uniform(size=(2, 3))
# print(x)

# sns.distplot(random.uniform(size=1000), hist = False)
sns.kdeplot(random.uniform(size=1000), bw_adjust=1)
plt.show()