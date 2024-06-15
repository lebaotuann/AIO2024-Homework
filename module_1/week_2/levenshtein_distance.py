# Section 1, Q4 - Levenshtein Distance


def levenshtein_distance(source: str, target: str):
    """Calculates the Levenshtein distance between two strings.
    The minimum edits to transform the source string to the target string (bottom right corner).
    Args:
        source (str): The source string.
        target (str): The target string.

    Returns:
        int: The Levenshtein distance.
    """
    row = len(source) + 1  # m
    column = len(target) + 1  # n
    # Create a storage matrix
    storage_matrix = [[0 for _ in range(column)] for _ in range(row)]
    # Initialize first row and column.
    for i in range(row):
        storage_matrix[i][0] = i
    for j in range(column):
        storage_matrix[0][j] = j
    # Calculate edits
    for i in range(1, row):
        for j in range(1, column):
            if source[i - 1] == target[j - 1]:
                sub_cost = 0  # Substitution cost is 0 because characters are the same.
            else:
                sub_cost = 1  # Substitution cost is 1
            # min(Deletion from source string, Insertion into source string, Substitution cost)
            storage_matrix[i][j] = min(
                storage_matrix[i - 1][j] + 1,
                storage_matrix[i][j - 1] + 1,
                storage_matrix[i - 1][j - 1] + sub_cost,
            )

    return storage_matrix[row - 1][column - 1]
