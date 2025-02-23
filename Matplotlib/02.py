import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([1, 3, 1, 3])

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

# plt.plot(ypoints, ls='dotted')     # linestyle 
# plt.plot(ypoints, c='hotpink', ls='-.', lw='20')

# plt.plot(y1)    # x-axis: default values(0, 1, 2, 3)
# plt.plot(y2)
# plt.plot(y3)

plt.plot(x1, y1, x2, y2)
plt.show()