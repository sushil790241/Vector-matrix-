import numpy as np

# Vector example
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("Vector 1:", v1)
print("Vector 2:", v2)

# Vector operations
print("Vector Addition:", v1 + v2)
print("Dot Product:", np.dot(v1, v2))

# Matrix example
m1 = np.array([[1, 2],
               [3, 4]])

m2 = np.array([[5, 6],
               [7, 8]])

print("\nMatrix 1:\n", m1)
print("Matrix 2:\n", m2)

# Matrix operations
print("Matrix Addition:\n", m1 + m2)
print("Matrix Multiplication:\n", np.matmul(m1, m2))

# Transpose of matrix
print("Transpose of Matrix 1:\n", m1.T)
