# Pareto Principle
# Simulating wealth Distribution
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

alpha = 2
wealth = np.random.pareto(alpha, 1000)* 10000

sns.histplot(wealth, bins=50, kde=True, color="purple")
plt.title("Pareto Distribution - Wealth Distribution ex")
plt.xlabel("Wealth")
plt.ylabel("No of People")
plt.xlim(0, 50000)
plt.show()