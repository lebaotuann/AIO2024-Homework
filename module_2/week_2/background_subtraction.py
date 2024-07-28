import cv2
import numpy as np


def compute_difference(bg_img, input_img):
    """Computes the absolute difference between two images.

    Args:
        bg_img: The background image.
        input_img: The input image.

    Returns:
        A numpy array representing the absolute difference image.
    """
    if bg_img.shape != input_img.shape:
        raise ValueError("Images must have the same dimensions")

    """
    # Another way.
    # Convert images to grayscale for simpler calculations (optional).
    gray_bg = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    gray_input = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    
    # Calculate absolute difference
    difference_single_channel = cv2.absdiff(gray_bg, gray_input)
    """

    difference_single_channel = cv2.absdiff(bg_img, input_img)
    return difference_single_channel


def compute_binary_mask(difference_single_channel):
    """Computes a binary mask from a difference image.

    Args:
        difference_single_channel: The absolute difference image.

    Returns:
        A binary mask.
    """
    _, mask = cv2.threshold(difference_single_channel, 0, 255, cv2.THRESH_BINARY)
    return mask


def replace_background(bg1_image, bg2_image, ob_image):
    """Replaces the background of an object image with a new background.

    Args:
        bg1_image: The original background image.
        bg2_image: The new background image.
        ob_image: The object image with the original background.

    Returns:
        The image with the replaced background.
    """
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)
    """
    # if binary_mask is gray image, we need to convert it to BGR image.
    binary_mask = cv2.cvtColor(binary_mask, cv2.COLOR_GRAY2BGR)
    """

    output = np.where(binary_mask == 255, ob_image, bg2_image)
    return output
