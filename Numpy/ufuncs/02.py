# Summations
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=0)
# axis=0 → Sum column-wise (downward)
# axis=1 → Sum row-wise (across)
# print(newarr)

# Cummulative Sum
arr = np.array([1, 2, 3])

newarr = np.cumsum(arr)
# print(newarr)


## Numpy Products
arr = np.array([1, 2, 3, 4])

x = np.prod(arr)
# print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2]) # product of the ele.s of two arrays
# print(x)

newarr = np.prod([arr1, arr2], axis=1)
# print(newarr)

newarr = np.cumprod(arr)
# print(newarr)


## NumPy Differences - subtracting two successive elements
arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)
# print(newarr)

newarr = np.diff(arr, n=2)  # doing it 2 times
# print(newarr)


## LCM
num1 = 4
num2 = 6

x = np.lcm(num1, num2)  # lowest common multiple of both numbers (4*3=12 and 6*2=12).
# print(x)

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)
# print(x)

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)
# print(x)

## GCD - Greatest Common Devisor

num1 = 6
num2 = 9

x = np.gcd(num1, num2)
# print(x)

arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr) # the highest number all values can be divided by.
# print(x)


## Trigonometric fn
x = np.sin(np.pi/2)
# print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)
# print(x)

# Convert Degrees Into Radians - radians values are pi/180 * degree_values.

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)
# print(x)

# Radians to Degrees
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)
# print(x)

# Find Angles
x = np.arcsin(1.0)
# print(x)

# Hypotenues

base = 3
perp = 4

x = np.hypot(base, perp)
# print(x)


## Hyperbolic Functions
x = np.sinh(np.pi/2)
# print(x)

x = np.array([0, 1, 2])
# print("sinh:", np.sinh(x))
# print("cosh:", np.cosh(x))
# print("tanh:", np.tanh(x))

# finding Angles
x = np.arcsinh(1.0)
# print(x)


## NumPy Set Operations
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)
# print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)
# print(newarr)

newarr = np.intersect1d(arr1, arr2, assume_unique=True)
# print(newarr)

newarr = np.setdiff1d(arr1, arr2, assume_unique=True)   #  finds the elements that are in arr1 but not in arr2 using np.setdiff1d()
# print(newarr)

newarr = np.setxor1d(arr1, arr2, assume_unique=True)    # values that are NOT present in BOTH sets
print(newarr)