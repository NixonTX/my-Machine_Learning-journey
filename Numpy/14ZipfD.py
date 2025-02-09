# a few items are extremely common, while most items are rare
"""
The most common words appear very frequently.
As we move to less common words, their frequency drops drastically.
This also applies to city populations (few large cities, many small ones) and website traffic (few popular sites, many niche sites).
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = 2
samples = np.random.zipf(a, 1000)

sns.histplot(samples, bins=50, kde=False, color="blue")
plt.title("Zipf Distribution - Word freq ex")
plt.xlabel("Word Rank")
plt.ylabel("Freqency")
plt.yscale("log")
plt.show()