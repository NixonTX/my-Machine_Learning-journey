import numpy as np

arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# 2D Array aka Matirx
matrix = np.array([[1, 2, 3], [4, 5, 6]])
# print(matrix)

# 3D
matrix3 = np.array([[1, 1, 1],
                    [2, 2, 2],
                    [3, 3, 3]])
# print(matrix3)
# print(matrix3.shape) # (row, col)
# print(matrix.size) # no. of ele

arr1 = np.array([2, 3, 4, 5])
# print(arr1)

arr2 = np.array((10, 2, 22))
# print(arr2)

# zeros array: An array filled with zeros
zeros = np.zeros((2, 3))
# print(zeros)

ones = np.ones((3, 2))
# print(ones)

identity = np.eye(3)
# print(identity)

arr3 = np.arange(0, 10, 2)
# print(arr3)

arr4 = np.arange(0, 100, 11)
# print(arr4)

linespace_arr = np.linspace(0, 1, 5)
# print(linespace_arr)

linespace_arr2 = np.linspace(1, 10, 11)
# print(linespace_arr2)

# Random arrays - Generate random values between 0 and 1.
random_arr = np.random.rand(4, 3)
# print(random_arr)

# Random integers
random_ints = np.random.randint(1, 10, (3, 3))
# print(random_ints)

random_ints2 = np.random.randint(1, 5, (2, 3))
# print(random_ints2)

custome_arr = np.full((2, 3), 7)
# print(custome_arr)


## Array Operations ##
arr5 = np.array([1, 2, 3])
arr6 = np.array([4, 5, 6])

# element-wise operations
# print(arr5 + arr6)
# print(arr5 - arr6)
# print(arr5 * arr6)
# print(arr5 / arr6)

# Scalar operations
# scalar add & mul
# print(arr5 + 10)
# print(arr5 * 2)

# Universal fn (ufuncs)
arr7 = np.array([1, 4, 9, 16])
# print(np.sqrt(arr7))

# print(np.log(arr7))

arr8 = np.array([30, 90, 360])
# print(np.sin(arr8))

# Array aggregations
arr = np.array([1, 2, 3, 4, 5])
# print(arr.sum())
# print(arr.mean())
# print(arr.max())
# print(arr.min())
# print(arr.std()) # standard deviation: a statistical measurement that shows how spread out a set of data is from its mean

arr1 = np.array([1, 1, 2, 4])
# print(arr1.mean())
# print(arr1.std())

# Indexing
arr2 = np.array([10, 20, 30, 40, 50])
# print(arr2[1])

# Slicing
# print(arr2[1:4])
# print(arr2[2:4])
# print(arr2[4:5])
# print(arr2[:3])
# print(arr2[0:2])

# print(arr2[::2])
# print(arr2[::3])

# Boolean masking
arr3 = np.array([1, 2, 3, 4, 5])

mask = arr3 > 3
# print(mask)
# print(arr3[mask])

# Matrix operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# print(matrix1 + matrix2)

# print(np.dot(matrix1, matrix2)) # matrix multiplication

###

# Get Dimension
b = np.array([0])
a = np.array([[1, 1, 1], [2, 2, 3], [6, 5, 3]])
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
d = np.array([[[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]]])
# print(d.ndim)
# print(a.dtype)

e = np.array([1, 2, 3], dtype="int32")
# print(e.dtype)
# print(e.itemsize)
# print(a.nbytes) # total size

list = [1, 2]
# print(list.__sizeof__)

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# print(a)
# print(a.shape)

# get a specific ele [r, c]
# print(a[1, 5])
# print(a[1, -2])
# print(a[0, 0])

# print(a[0, :]) # specific row

# print(a[:, 2]) # specific col

# print(a[0, 1:6:2])
# print(a[0, 1:-1:2])
# a[0, 1] = 22
# print(a)

# a[:, 2] = 111
# print(a)

# a[0, :] = 333
# print(a)
z = np.array([3, 3, 3])
# print(np.full_like(a, 1))
# print(np.full_like(z, 0))

output = np.ones((5, 5))
# print(output)

z = np.zeros((3, 3))
z[1, 1] = 9
# print(z)

# output[1:4, 1:4] = z # from first row to 3rd(row 4 not included), same goes for col
output[1:-1, 1:-1] = z

# print(output)

# careful when copying arrays
a = np.array([1, 2, 3])
b = a
b[0] = 100
# print(b)
# print(a)

# copy
a = np.array([1, 2, 3])
b = a.copy()
b[0] = 100
# print(b)
# print(a)

# Linear Algebra
a = np.ones((2, 3))
# print(a)

b = np.full((3, 2), 2)
# print(b)

# print(np.matmul(a, b))

c = np.identity(3)
# print(np.linalg.det(c)) # determinant

# Statistics
s = np.array([[1, 2, 3], 
              [4, 5, 6]])
# print(np.min(s))
# print(np.max(s))
# print(np.min(s, axis=1))
# print(np.sum(s, axis=0)) # 0 =  Row, 1 = Col

# Reorganizing Arrays
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(before)

after = before.reshape(4, 2)
after = before.reshape(2, 2, 2)
# print(after)

# Miscellaneous - Load data from file (without Pandas)
