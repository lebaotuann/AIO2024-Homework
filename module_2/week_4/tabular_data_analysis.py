def correlation(x, y):
    """Calculate the Pearson correlation coefficient between two lists or arrays.

    Args:
        x: A numpy array.
        y: A numpy array of the same length as x.

    Returns:
        float: The correlation coefficient between `x` and `y`
    """
    if len(x) != len(y):
        raise ValueError("The lists x and y must have the same length")
    n = len(x)

    prod = [xi * yi for xi, yi in zip(x, y)]
    sum_prod_xy = sum(prod)

    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x ** 2
    squared_sum_y = sum_y ** 2

    squared_x = [xi ** 2 for xi in x]
    squared_y = [yi ** 2 for yi in y]
    sum_squared_x = sum(squared_x)
    sum_squared_y = sum(squared_y)

    # Use formula to calculate correlation
    numerator = n * sum_prod_xy - sum_x * sum_y
    denominator_x = n * sum_squared_x - squared_sum_x
    denominator_y = n * sum_squared_y - squared_sum_y
    denominator = (denominator_x * denominator_y) ** 0.5

    return numerator / denominator
