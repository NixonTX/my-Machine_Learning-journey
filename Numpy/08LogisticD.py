# to describe growth. Used extensively in machine learning in logistic regression, neural networks etc.
# The logistic distribution has a higher kurtosis (heavier tails), meaning it predicts extreme values with a higher probability than the normal distribution. This makes it useful when extreme variations are relevant.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.logistic(loc=1, scale=2, size=(2, 3))
# kdeplot - designed to work with 1D data, so we need to flatter the array
sns.kdeplot(x.flatten(), label="Logistic Distribution")
print(x)
plt.show()

# sns.kdeplot(random.logistic(size=1000))
# plt.show()