import numpy as np

from cosine_similarity import compute_cosine
from eigenvector_eigenvalue import compute_eigenvalues_eigenvectors
from vector_matrix import (
    compute_vector_length,
    compute_dot_product,
    matrix_multi_vector,
    matrix_multi_matrix,
    inverse_matrix,
)

# Question 1
print("==== Question 1 ================================")
vector = np.array([-2, 4, 9, 21])
result = compute_vector_length([vector])
print(round(result, 2))

# Question 2
print("==== Question 2 ================================")
v1 = np.array([0, 1, -1, 2])
v2 = np.array([2, 5, 1, 0])
result = compute_dot_product(v1, v2)
print(round(result, 2))

# Question 3
print("==== Question 3 ================================")
x = np.array([[1, 2], [3, 4]])
k = np.array([1, 2])
print("result: \n", x.dot(k))

# Question 4
print("==== Question 4 ================================")
x = np.array([[-1, 2], [3, -4]])
k = np.array([1, 2])
print("result: \n", x @ k)

# Question 5
print("==== Question 5 ================================")
m = np.array([[-1, 1, 1], [0, -4, 9]])
v = np.array([0, 2, 1])
result = matrix_multi_vector(m, v)
print(result)

# Question 6
print("==== Question 6 ================================")
m1 = np.array([[0, 1, 2], [2, -3, 1]])
m2 = np.array([[1, -3], [6, 1], [0, -1]])
result = matrix_multi_matrix(m1, m2)
print(result)

# Question 7
print("==== Question 7 ================================")
m1 = np.eye(3)
m2 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result = m1 @ m2
print(result)

# Question 8
print("==== Question 8 ================================")
m1 = np.eye(2)
m1 = np.reshape(m1, (-1, 4))[0]
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1 @ m2
print(result)

# Question 9
print("==== Question 9 ================================")
m1 = np.array([[1, 2], [3, 4]])
m1 = np.reshape(m1, (-1, 4), "F")[0]
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1 @ m2
print(result)

# Question 10
print("==== Question 10 ================================")
m1 = np.array([[-2, 6], [8, -4]])
result = inverse_matrix(m1)
print(result)

# Question 11
print("==== Question 11 ================================")
matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
print(eigenvectors)

# Question 12
print("==== Question 12 ================================")
x = np.array([1, 2, 3, 4])
y = np.array([1, 0, 3, 0])
result = compute_cosine(x, y)
print(round(result, 3))

answer = """
Question 1: D
Question 2: B
Question 3: A
Question 4: B
Question 5: A
Question 6: C
Question 7: A
Question 8: D
Question 9: B
Question 10: A
Question 11: A
Question 12: C
"""
print(answer)
