import numpy as np
from math import log

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

# newarr = np.add(arr1, arr2)
# newarr = np.subtract(arr1, arr2)
newarr = np.divide(arr1, arr2)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2) # quotient and mod

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr) # absolute value of a number is its distance from zero

# print(newarr)

## Rounding Decimals - truncation, fix, rounding, floor, ceil

# Truncation
# arr = np.trunc([-3.1666, 3.6667])
arr = np.fix([-3.1666, 3.6667])
arr = np.around(3.1666, 2)
arr = np.floor([-3.1666, 3.6667]) # nearest lower integer
arr = np.ceil([-3.1666, 3.6667]) # nearest upper integer

# print(arr)


## Logs - logarithmic functions(log, log2, log10 etc.)
arr = np.arange(1, 10)
arr = np.array([1, np.e, np.e**2, np.e**3])

# print(np.log(arr))

arr = np.array([1, 2, 4, 8, 16])
# print(np.log2(arr))
"""
log₂(1) = 0
log₂(2) = 1
log₂(4) = 2
log₂(8) = 3
log₂(16) = 4
"""

arr = np.array([1, 10, 100, 1000])

# print(np.log10(arr))
"""
log₁₀(1) = 0
log₁₀(10) = 1
log₁₀(100) = 2
log₁₀(1000) = 3
"""
