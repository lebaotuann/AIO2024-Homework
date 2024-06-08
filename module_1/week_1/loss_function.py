"""Section I, Question 3 & 5"""

import math
import random


def calc_se(y: float, y_hat: float):
    """Calculates squared error.

    Args:
        y (float): The target number that the model is expected to predict correctly.
        y_hat (float): The predicted number comes from the model.

    Returns:
        float: The squared error value.
    """
    return (y - y_hat) ** 2


def calc_ae(y: float, y_hat: float):
    """Calculates absolute error.

    Args:
        y (float): The target number that the model is expected to predict correctly.
        y_hat (float): The predicted number comes from the model.

    Returns:
        float: The absolute error value.
    """
    return abs(y - y_hat)


def loss_function():
    """Calculates loss function from input data.
    Support loss functions:
        Mean Squared Error (MSE).
        Root Mean Squared Error (RMSE)
        Mean Absolute Error (MAE).
    """
    num_samples = input(
        "Input number of samples (integer number) which are generated: "
    )
    if not num_samples.isnumeric():
        print("Number of samples must be an integer number")
        return None
    loss_name = input("Input loss name (MSE | MAE | RMSE): ")
    if loss_name not in ["MSE", "MAE", "RMSE"]:
        print(f"{loss_name} is not supported")
        return None
    num_samples = int(num_samples)
    sum_error = 0.0
    for i in range(num_samples):
        target = random.uniform(0.0, 10.0)  # y
        predict = random.uniform(0.0, 10.0)  # y hat
        if loss_name in ["MSE", "RMSE"]:
            prediction_error = calc_se(y=target, y_hat=predict)
        else:
            # MAE
            prediction_error = calc_ae(y=target, y_hat=predict)
        sum_error += prediction_error
        loss_value = (
            math.sqrt((sum_error / (i + 1)))
            if loss_name == "RMSE"
            else sum_error / (i + 1)
        )
        print(
            f"loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss_value}"
        )
    return None


def md_nre_single_sample(y: float, y_hat: float, n: int, p: int):
    """Calculates the Mean Difference of nth Root Error for a sample

    Args:
        y (float): The target number (actual value).
        y_hat (float): The predicted number comes from the model.
        n (int): The nth root.
        p (int): The degree of the loss function.

    Returns:
        float: The Mean Difference of nth Root Error.
    """
    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / n)
    difference = y_root - y_hat_root
    loss = difference**p
    return loss
