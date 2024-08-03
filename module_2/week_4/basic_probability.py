import numpy as np


def compute_mean(x):
    """Computes the mean of a given array

    Args:
        x: A numpy array.

    Returns:
        The mean of the array.
    """
    # Recommend return np.mean(x)
    sum_x = np.sum(x)
    return sum_x / len(x)


def compute_median(x):
    """Computes the median of a given array.

    Args:
        x: A numpy array.

    Returns:
        The median of the array.
    """
    # Recommend return np.median(x)

    size = len(x)
    x = np.sort(x)
    if size % 2 == 0:
        return (x[size // 2 - 1] + x[size // 2]) / 2
    else:
        return x[size // 2]


def compute_std(x):
    """Computes the Standard Deviation of a given array.

    Args:
        x: A numpy array.

    Returns:
        The Standard Deviation of the array.
    """
    mean = compute_mean(x)
    variance = np.mean((x - mean) ** 2)
    return np.sqrt(variance)


def compute_correlation_coefficient(x, y):
    """Computes the correlation coefficient between two arrays.

    Args:
        x: A numpy array.
        y: A numpy array of the same length as x.

    Returns:
        The correlation coefficient between x and y.
    """
    if len(x) != len(y):
        raise ValueError("X and Y must have the same length")
    # Recommend return np.corrcoef(x, y)

    n = len(x)
    numerator = n * np.sum(x * y) - np.sum(x) * np.sum(y)
    denominator = np.sqrt((n * np.sum(x ** 2) - np.sum(x) ** 2) * (n * np.sum(y ** 2) - np.sum(y) ** 2))

    return np.round(numerator / denominator, 2)
