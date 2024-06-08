"""Section I, Question 1."""


def calculate_and_print_precision_recall_f1_score(tp: int, fp: int, fn: int):
    """Calculates and prints precision, recall, and F1-Score given True Positives, False Positives, and False Negatives.

    Args:
        tp (int): Number of the True Positives.
        fp (int): Number of the False Positives.
        fn (int): Number of the False Negatives.
    """
    if not isinstance(tp, int):
        print("tp is must be int")
        return None
    if not isinstance(fp, int):
        print("fp is must be int")
        return None
    if not isinstance(fn, int):
        print("fn is must be int")
        return None
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return None
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1-score is {f1_score}")
    return None


def calculate_f1_score(tp: int, fp: int, fn: int) -> float:
    """Calculates F1-Score given True Positives, False Positives, and False Negatives.

    Args:
        tp (int): Number of the True Positives.
        fp (int): Number of the False Positives.
        fn (int): Number of the False Negatives.

    Returns:
        float: F1-Score value.

    Raises:
        ValueError: If any input is non-positive.
    """
    if not isinstance(tp, int):
        raise ValueError("tp is must be int")
    if not isinstance(fp, int):
        raise ValueError("fp is must be int")
    if not isinstance(fn, int):
        raise ValueError("fn is must be int")
    if tp <= 0 or fp <= 0 or fn <= 0:
        raise ValueError("tp and fp and fn must be greater than zero")
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    return f1_score
