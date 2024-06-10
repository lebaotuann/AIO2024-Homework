# Implement the code in the multiple choice


# Q1 max_kernel in max_kernel.py
# Q2 character_count in count_character.py
# Q3 count_word in count_word.py
# Q4 levenshtein_distance in levenshtein_distance.py
# Q5
def check_the_number(n):
    """Checks if a number exists in the list.

    Args:
        n (float): The number to check.

    Returns:
        bool: True if n appears in list, False if n does not appear in list.
    """
    list_of_numbers = []
    result = ""
    for i in range(1, 5):
        list_of_numbers.append(i)
    if n in list_of_numbers:
        result = "True"
    if n not in list_of_numbers:
        result = "False"
    return result


# Q6
def build_list_by_max_and_min(data: list, max_number: float, min_number: float):
    """Gives a list from the data based on max number and min number.

    Args:
        data (list): The list of the numbers.
        max_number (float): The max number.
        min_number (float): The min number.

    Returns:
        list: The expected list.
    """
    result = []
    for i in data:
        if i < min_number:
            result.append(min_number)
        elif i > max_number:
            result.append(max_number)
        else:
            result.append(i)
    return result


# Q7
def extend_list(destination: list, source: list):
    """Extends the destination list by the source list.

    Args:
        destination (list): The list is extended.
        source (list): The list to get resources.

    Returns:
        list: The list after extending.
    """
    destination.extend(source)
    return destination


# Q8
def min_list(numbers: list):
    """Finds the minimum of the number list.

    Args:
        numbers (list): The number list.

    Returns:
        float: The minimum of the number list.
    """
    # return min(numbers)  # Recommendation
    if (
        not numbers
        or not isinstance(numbers, list)
        or any(isinstance(n, str) for n in numbers)
    ):
        raise ValueError("numbers must be a list of numbers")
    mix_number = numbers[0]
    for number in numbers:
        if number < mix_number:
            mix_number = number
    return mix_number


# Q9
def max_list(numbers: list):
    """Finds the maximum of the number list.

    Args:
        numbers (list): The number list.

    Returns:
        float: The maximum of the number list.
    """
    # return max(numbers)  # Recommendation
    if (
        not numbers
        or not isinstance(numbers, list)
        or any(isinstance(n, str) for n in numbers)
    ):
        raise ValueError("numbers must be a list of numbers")
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


# Q10
def is_number_in_integer_list(integers: list, number: int = 1):
    """Check if a number exists in the integer list.

    Args:
        integers (list): The list of integers.
        number (int): The number to check.

    Returns:
        bool: True if number exists in list, otherwise is False.
    """
    return any(n == number for n in integers)


# Q11
def average(list_nums: list):
    """Calculates the average of the number list.

    Args:
        list_nums (list): The number list

    Returns:
        float: The average.
    """
    total_sum = 0
    for i in list_nums:
        total_sum += i
    # return sum(list_nums) / len(list_nums)
    return total_sum / len(list_nums)


# Q12
def list_numbers_divisible_by_3(data: list):
    """Find the number list divisible by 3 from the input number list.

    Args:
        data (list): The number list.

    Returns:
        list: The number list divisible by 3
    """
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var


# Q13
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
    temp_number = n
    while temp_number > 1:
        factorial_value *= temp_number
        temp_number -= 1
    return factorial_value


# Q14
def reverse_string(string: str):
    """Reverse the string.

    Args:
        string (str): The input string.

    Returns:
        str: The reversed string.
    """
    # return string[::-1]
    output = ""
    for s in string:
        output = s + output
    return output


# Q15
def is_number_greater_than_0(number: float):
    """Check if a number is greater than 0 or not.

    Args:
        number (float): The number to check.

    Returns:
        str: "T" if a number is greater than 0, otherwise is "N"
    """
    return "T" if number > 0 else "N"


def check_numbers(data: list):
    """Check whether the numbers in the list are greater than 0 or not.

    Args:
        data (list): The list of the numbers.

    Returns:
        list: The result after validating.
    """
    res = [is_number_greater_than_0(x) for x in data]
    return res


# Q16
def remove_duplicates(data: list):
    """Removes duplicate elements in the number list.

    Args:
        data (list): The number list from which to remove duplicates.

    Returns:
        list: A new list with duplicates removed
    """
    # return list(set(data))
    res = []
    for d in data:
        if d not in res:
            res.append(d)
    return res
