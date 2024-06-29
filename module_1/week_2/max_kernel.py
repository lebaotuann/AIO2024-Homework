# Section 1, Q1
def max_kernel(num_list: list, k: int):
    """Calculates the maximum number of kernels in the integer list based on the sliding window.

    Args:
        num_list (list): A list of integers.
        k (int): The size of the sliding window.

    Returns:
        list: The max kernels
    """
    if not num_list:
        raise ValueError("num_list must be a list of integer elements")
    if k < 1:
        raise ValueError("k must be an integer greater than 0")
    result = []
    len_num_list = len(num_list)
    for i in range(len_num_list):
        result.append(max(num_list[i : i + k]))
        if i + k >= len_num_list:
            break
    return result
