"""Section I, Question 4."""

import math

N_GREATER_THAN_ZERO_MESSAGE = "n must be an integer greater than zero"


def factorial(n: int):
    """Calculates the factorial of a non-negative integer n

    Args:
        n (int): The non-negative integer n.

    Returns:
        int: The factorial of n.
    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    factorial_value = 1
    for i in range(n):
        factorial_value *= i + 1
    return factorial_value


def approx_sin(x: float, n: int):
    """Approximates the sine of the number.

    Args:
        x (float): The angle in radians.
        n (int): Number of terms (n > 0).

    Returns:
        float: The approximate sine of x.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError(N_GREATER_THAN_ZERO_MESSAGE)
    approx_value = 0.0
    for i in range(n):
        approx_value += math.pow(-1, i) * math.pow(x, 2 * i + 1) / factorial(2 * i + 1)
    return approx_value


def approx_cos(x: float, n: int):
    """Approximates the cosine of the number.

    Args:
        x (float): The angle in radians.
        n (int): Number of terms (n > 0).

    Returns:
        float: The approximate cosine of x.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError(N_GREATER_THAN_ZERO_MESSAGE)
    approx_value = 0.0
    for i in range(n):
        approx_value += math.pow(-1, i) * math.pow(x, 2 * i) / factorial(2 * i)
    return approx_value


def approx_sinh(x: float, n: int):
    """Approximates the sinh of the number.

    Args:
        x (float): The angle in radians.
        n (int): Number of terms (n > 0).

    Returns:
        float: The approximate sinh of x.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError(N_GREATER_THAN_ZERO_MESSAGE)
    approx_value = 0.0
    for i in range(n):
        approx_value += math.pow(x, 2 * i + 1) / factorial(2 * i + 1)
    return approx_value


def approx_cosh(x: float, n: int):
    """Approximates the cosh of the number.

    Args:
        x (float): The angle in radians.
        n (int): Number of terms (n > 0).

    Returns:
        float: The approximate cosh of x.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError(N_GREATER_THAN_ZERO_MESSAGE)
    approx_value = 0.0
    for i in range(n):
        approx_value += math.pow(x, 2 * i) / factorial(2 * i)
    return approx_value
