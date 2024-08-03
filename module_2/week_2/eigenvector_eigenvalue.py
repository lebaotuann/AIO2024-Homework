import numpy as np


def compute_eigenvalues_eigenvectors(matrix):
    """Compute eigenvalues and eigenvectors.

    - Eigenvalues are scalar values associated with a linear transformation.
    - Eigenvectors are non-zero vectors that, when multiplied by the matrix, result in a scalar multiple of themselves.

    Args:
        matrix (numpy.ndarray): The input matrix.

    Returns:
        tuple: The eigenvalues and the eigenvectors.
    """
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors
