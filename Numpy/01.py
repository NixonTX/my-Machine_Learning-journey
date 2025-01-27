import numpy as np

## Advanced NumPy Features ##
# Broadcasting - to perform ele wise operations on arrays of diff. shapes
# Rules: 1] dimensions must be the same or one of them must be 1.
    # 2] smaller arrays are "stretched" to match the shape of the larger array

# Scalar broadcasting
arr = np.array([1, 2, 3])
# print(arr + 10)

# Array broadcasting
matrix = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
# print(matrix + row)

# Reshaping Arrays
arr = np.arange(1, 7)
# print(arr)

reshaped = arr.reshape(2, 3)
# print(reshaped)

# print(reshaped.flatten()) # flattening an array

# Transpose
matrix = np.array([[1, 2], [3, 4], [5, 6]])
# print(matrix)
# print(matrix.T)

# Stacking and Splitting
# stacking - combine arrays vertically or horizontally

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Vertical stack
# print(np.vstack((a, b)))

# Horizontal stack
# print(np.hstack((a, b)))

# Splitting
arr = np.array([1, 2, 3, 4, 5, 6])
# print(np.split(arr, 3))

# Advanced Indexing
arr = np.array([10, 20, 30, 40, 50])

# fancy indexing
indices = [0, 2, 4]
# print(arr[indices])

# Boolean masking
mask = arr > 25
# print(arr[mask])
# print(mask)

# multidimensional arrays
multi_arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# print(multi_arr.shape)
# print(multi_arr.size)

# accessing ele.s
# print(multi_arr[1, 0, 1]) # out: 6 (1st block, 0th row, 1st column)

# Common NumPy fun.s
# sorting
arr = np.array([4, 1, 3, 2])
# print(np.sort(arr))

# unique vals
arr = np.array([1, 2, 2, 3, 4, 4, 4])
# print(np.unique(arr))

# concatenation
a = np.array([1, 2])
b = np.array([3, 4])
print(np.concatenate((a, b)))