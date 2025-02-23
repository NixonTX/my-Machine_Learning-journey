# Histogram
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

# print(x)

# plt.hist(x)
# plt.show()


## Pie Chart ##
y = np.array([48, 25, 17, 10])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0, 0, 0.1, 0]

plt.pie(y, labels= mylabels, startangle=90, explode=myexplode)
plt.legend(title = "Four Fruits:")
plt.show()