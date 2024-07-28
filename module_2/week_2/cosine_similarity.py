import numpy as np


def compute_cosine(vector1, vector2):
    """Compute cosine similarity.

    Args:
        vector1 (numpy.ndarray): The first input vector.
        vector2 (numpy.ndarray): The second input vector.

    Returns:
        numpy.float64: The cosine similarity.
    """
    dot_product = np.dot(vector1, vector2)
    norm_vector1 = np.linalg.norm(vector1)
    norm_vector2 = np.linalg.norm(vector2)
    cos_sim = dot_product / (norm_vector1 * norm_vector2)
    return cos_sim
