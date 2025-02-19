import numpy as np

#  Boolean Indexing
arr = np.array([10, 20, 30, 40, 50])
mask = arr > 25
# print(arr[mask])

# Integer Indexing
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 3, 4]
# print(arr[indices])

matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# print(matrix[[0, 2], [1, 2]]) # The first list [0, 2] refers to row indices → Picks row 0 and row 2
# The second list [1, 2] refers to column indices → Picks column 1 and column 2


## Linear algebra operations
# Dot product
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product = np.dot(a, b)  # dot product of two 1D vectors is the sum of the element-wise products.
# print(dot_product)

# Matrix Multiplication
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

matrix_product = np.matmul(A, B)
# print(matrix_product)

# Identity Matrix
I = np.eye(3)
# print(I)

# Matrix Inversion
A = np.array([[2, 3],
              [1, 4]])

A_inv = np.linalg.inv(A)
# print(A_inv)

# Determinant
A = np.array([[2, 3],
              [1, 4]])

det_A = np.linalg.det(A)
# print(det_A)


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = A * B
# print(result)


# Solving Linear Systems
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)   # Solving Ax = b

# print(x)

# Eigenvalues and Eigenvectors
M = np.array([[1, 2],
              [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(M)

# print("Eigenvalues:", eigenvalues)
# print("Eigenvectors:\n", eigenvectors)


# Norms (Vector/Matrix)
# L2 Norm (Euclidean Norm)
v1 = np.array([1, 2, 3])
norm_v = np.linalg.norm(v1)     # Measures the length (magnitude) of a vector.

# print(norm_v)

# Frobenius Norm (For Matrices) - Measures the magnitude of a matrix.
M = np.array([[1, 2], 
              [3, 4]])
norm_M = np.linalg.norm(M, 'fro')
# print(norm_M)


# Singular Value Decomposition (SVD)
U, S, Vt = np.linalg.svd(M)

# print("U:\n", U)    # Left singular vectors
# print("S:\n", S)    # Singular values (not a full matrix, just diagonal entries)
# print("Vt:\n", Vt)  # Right singular vectors (transposed)


# Trace - sum of diagonal ele.s
trace = np.trace(M)
# print(trace)

# Reshaping and Flattening
# print(M)

M_reshaped = M.reshape(4, 1)
# print(M_reshaped)

M_flattened = M.flatten()
# print(M_flattened)

# Diagonal Operations
diag = np.diag(M)
# print(diag)

diag_matrix = np.diag([1, 2, 3, 6])
# print(diag_matrix)


## Scenario: Portfolio Risk Analysis
cov_matrix = np.array([
    [0.04, 0.02, 0.01],  # Stock A
    [0.02, 0.05, 0.03],  # Stock B
    [0.01, 0.03, 0.06]   # Stock C
])

# Extract diagonal (variances of stocks)
variances = np.diag(cov_matrix)     # [0.04, 0.05, 0.06]

print("Variances of stocks:", variances)
"""
0.04, 0.05, 0.06 are the variances of Stock A, B, and C.
Higher variance means higher risk, lower variance means more stable returns.
Investors use this to balance risk in a portfolio.
"""