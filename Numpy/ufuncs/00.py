import numpy as np
"""
Why Use ufuncs?
Faster than Python loops – Uses optimized C implementations.
Applies operations to entire arrays at once – No need for iteration.
Broadcasting support – Works on arrays of different shapes.
Supports mathematical and logical operations.
"""
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
# z = []

# for i, j in zip(x, y):
#     z.append(i + j)
# print(z)


z = np.add(x, y)
# print(z)

# Custom ufunc
def square(x):
    return x*x

ufunc_square = np.frompyfunc(square, 1, 1)
# print(ufunc_square(np.array([1, 2, 3, 4])))

def myadd(x, y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1) # no. of input args(2- x, y), no. of output args(1- x+y)

# print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

print(type(np.add))
print(type(np.concatenate))