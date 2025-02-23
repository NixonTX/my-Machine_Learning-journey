# Matplotlib Subplot
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x =np.array([0, 1, 2, 3])
y =np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)    # row, column, index of current plot
plt.subplot(2, 1, 1)
plt.title("Plot 1")
plt.plot(x, y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
plt.subplot(2, 1, 2)
plt.title("Plot 2")
plt.plot(x, y)

plt.suptitle("PLOTS")
plt.show()