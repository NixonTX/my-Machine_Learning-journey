# Default X-Points

import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([3, 8, 1, 10, 5, 7])
# ypoints = np.array([10, 11, 1, 2])
ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints)
# plt.plot(ypoints, marker = 'X')
# plt.plot(ypoints, 'P--k')
# plt.plot(ypoints, 'H:y', ms=15, mec='k')
# plt.plot(ypoints, 'P:m', ms=15, mec='r', mfc='y')
# plt.plot(ypoints, marker = 'P', ms = 10, mec = '#4CAF50', mfc = '#4CAF50')
plt.plot(ypoints, marker = 'o', ms = 11, mec = 'hotpink', mfc = 'hotpink')

plt.show()