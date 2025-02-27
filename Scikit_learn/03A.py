# Reshaping 1D to 2D
import numpy as np

arr1 = [1, 2, 3, 4, 5]

reshapedArr1 = np.array(arr1).reshape(-1, 1)

print(reshapedArr1)