import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# plt.barh(x, y)
# plt.bar(x, y, color="blue", alpha=0.5, width= 0.3)
plt.barh(x, y, color="hotpink", alpha=0.5, height= 0.3)

plt.show()