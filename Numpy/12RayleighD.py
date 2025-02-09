# used in signal processing
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# x = random.rayleigh(scale=2, size=(2, 3))
# sns.kdeplot(x)
# print(x)
# plt.show()

# y = sns.kdeplot(random.rayleigh(size=1000))
# print(y)
# plt.show()

# signal_strength = np.random.rayleigh(scale=5, size=1000)

# sns.histplot(signal_strength, bins=30, kde=True, color="orange")
# plt.title("Rayleigh Distribution - Wireless Signal Strength Example")
# plt.xlabel("Signal Strength")
# plt.ylabel("Frequency")
# plt.show()

# Simulating Wind Speed
sigma = 3 # Scale para
num_samples = 1000 # no. of data points

# Generate random wind component(east-west and north-south)
x = np.random.normal(0, sigma, num_samples) # east-west component
y = np.random.normal(0, sigma, num_samples) # north-south component

wind_speed = np.sqrt(x**2 + y**2) # magnitude of x & y

plt.hist(wind_speed, bins=30, density=True, alpha=0.6, label="Simulated Wind Speed") # bins = no. of bars; alpha=0.6 for transparency

x_vals = np.linspace(0, 15, 1000)
rayleigh_pdf = (x_vals / sigma**2) * np.exp(-x_vals**2 / (2 * sigma**2))

plt.plot(x_vals, rayleigh_pdf, 'r', linewidth=2, label="Rayleigh PDF (σ=3)")

plt.xlabel("Wind Speed")
plt.ylabel("Probability Density")
plt.title("Rayleigh Distribution Example: Wind Speed")
plt.legend()
plt.show()  

# PDF : probability density function