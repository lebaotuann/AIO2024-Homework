"""Section I, Question 2."""

import math

ALPHA = 0.01


def calc_sigmoid(x: float):
    """Calculates sigmoid function (or logistic function).

    Args:
        x (float): Number

    Returns:
        float: The Sigmoid value
    """
    return 1 / (1 + math.exp(-1 * x))


def calc_relu(x: float):
    """Calculates Rectified Linear Unit (ReLU).

    Args:
        x (float): Number

    Returns:
        float: The ReLU value.
    """
    return x if x > 0 else 0.0


def calc_elu(x: float):
    """Calculates Exponential Linear Unit (ELU).

    Args:
        x (float): Number.

    Returns:
        float: The ELU value.
    """
    return x if x > 0 else ALPHA * (math.exp(x) - 1)


def is_number(x: any):
    """Check if it is valid.

    Args:
        x (any): The input data

    Returns:
        bool: True if x is a number form after type-casting, otherwise is False
    """
    try:
        float(x)
    except ValueError:
        return False
    return True


def calc_activation_function(x: float, activation_name: str):
    """Calculates activation function given x value based on activation type.

    Args:
        x (float): Number.
        activation_name (str): The type of activation function such as sigmoid, relu, and elu.

    Returns:
        float: The result after going through activation function (sigmoid or relu or elu).
        Get None when activation_name is different sigmoid or relu or elu.

    """
    if activation_name == "sigmoid":
        output = calc_sigmoid(x)
    elif activation_name == "relu":
        output = calc_relu(x)
    elif activation_name == "elu":
        output = calc_elu(x)
    else:
        output = None
    return output


def run_activation_function():
    """Calculates activation function from input data."""
    str_x = input("Input x = ")
    if not is_number(str_x):
        print("x must be a number")
        return None
    activation_name = input("Input activation function (sigmoid | relu | elu): ")
    if activation_name not in ["sigmoid", "relu", "elu"]:
        print(f"{activation_name} is not supported")
        return None
    x = float(str_x)
    act_func_result = calc_activation_function(x, activation_name)
    print(f"{activation_name}: f({x}) = {act_func_result}")
