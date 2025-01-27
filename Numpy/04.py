# Normal distribution #

import matplotlib.pyplot as plt
import numpy as np

# samples = np.random.normal(loc=0, scale=1, size=1000) # location- where the center of distribution is. 

# plt.hist(samples, bins=30, density=True, alpha=0.3, color='g')
# plt.title("Normal distribution (mean=0, std=1)")
# plt.show()

samples = np.random.normal(loc=170, scale=10, size=1000)

plt.hist(samples, bins=30, density=True, alpha=0.6, color='b')
plt.title("Normal Distribution: Adult Heights (mean=170 cm, std=10 cm)")
plt.xlabel("Height (cm)")
plt.ylabel("Density")
plt.show()