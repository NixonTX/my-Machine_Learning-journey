# stock price analysis #
import numpy as np

prices = np.array([752.25, 741.55, 754.95, 757.05, 773.10]) # stock prices(high) over 5 days of SBI

daily_change = (prices[1:] - prices[:-1]) / prices[:-1] * 100
# print(daily_change)


# Image Processing # - Normalize pixel values in an image matrix
image = np.array([
    [0, 128, 255],
    [64, 192, 32],
    [255, 128, 64]
])

# Normalize to range 0-1
normalized_image = image / 255.0
# print(normalized_image)


# Statistical Analysis #
scores = np.array([85, 90, 78, 92, 88, 76, 95])

mean = np.mean(scores)
median = np.median(scores)
std_dev = np.std(scores)

# print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")


# Financial Data #
# monthly loan payments for diff. interest rates
loan = 10000
rates = np.array([0.05, 0.06, 0.07]) # Interest rates for 3 banks
years = 5

# Formuls: Payment = (P * r * (1 + r)^n) / ((1 + r)^n - 1)

n = years * 12
monthly_rates = rates / 12
payments = (loan * monthly_rates * (1 + monthly_rates) **n) / ((1 + monthly_rates)**n -1)

# print(payments)