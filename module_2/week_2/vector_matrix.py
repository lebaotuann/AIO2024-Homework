import numpy as np


def compute_vector_length(vector):
    """Computes vector length using the Euclidean norm.

    Args:
        vector: The input vector.

    Returns:
        numpy.float64: The vector length.
    """
    return np.linalg.norm(vector)


def compute_dot_product(vector1, vector2):
    """Compute dot product of two vectors.

    Args:
        vector1 (numpy.ndarray): The first input vector.
        vector2 (numpy.ndarray): The second input vector.

    Returns:
        any: The dot product
    """
    return np.dot(vector1, vector2)


def matrix_multi_vector(matrix, vector):
    """Multiply matrix and vector.

    Args:
        matrix (numpy.ndarray): The input matrix.
        vector (numpy.ndarray): The input vector.

    Returns:
        numpy.ndarray: The result array.
    """
    return np.dot(matrix, vector)


def matrix_multi_matrix(matrix1, matrix2):
    """Multiply two matrices.

    Args:
        matrix1 (numpy.ndarray): The first input matrix.
        matrix2 (numpy.ndarray): The second input matrix.

    Returns:
        numpy.ndarray: The result.
    """
    return np.dot(matrix1, matrix2)


def inverse_matrix(matrix):
    """Calculate the inverse of a matrix.

    Args:
        matrix (numpy.ndarray): The input matrix.

    Returns:
        numpy.ndarray: The result.
    """
    determinant = np.linalg.det(matrix)
    if determinant == 0:
        raise ValueError("Singular matrix")
    return np.linalg.inv(matrix)
