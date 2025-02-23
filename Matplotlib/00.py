import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 500])

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])   # You can plot as many points as you like, just make sure you have the same number of points in both axis.

plt.plot(xpoints, ypoints)
# plt.plot(xpoints, ypoints, 'o')
plt.show()