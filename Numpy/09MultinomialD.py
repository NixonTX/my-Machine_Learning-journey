from numpy import random
import numpy as np
import matplotlib.pyplot as plt

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

# print(x)

outcomes = np.random.multinomial(n=10, pvals=[0.0, 0.0, 1.0])

# print(outcomes)

# Ex: Marketing & A/B Testing: Evaluating customer preferences across multiple product categories.

# 3 products. A, B, C
n_customers = 100

pvals = [0.4, 0.35, 0.25]

results = np.random.multinomial(n_customers, pvals)

labels = ['A', 'B', 'C']

plt.bar(labels, results, color=['blue', 'green', 'red'])
plt.xlabel("Packaging Type")
plt.ylabel("NO. of customers")
plt.title("Customer Preferences for Packaging (Multinomial Distribution)")
plt.show()

print("Survey Results:", results)

"""
so the product A stays on top.
ChatGPT said:
ChatGPT
Not always. Since the multinomial distribution introduces randomness, A is expected to be on top most of the time, but not always.

If you run the simulation multiple times, sometimes B or C might get more votes due to natural variations. However, over many trials, A will have the highest count on average because it has the highest probability (40% chance per customer)."""