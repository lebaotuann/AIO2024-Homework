# Section 1, Q2
def character_count(word: str):
    """Counts characters of the word.

    Args:
        word (str): The input word.

    Returns:
        dict: Dictionary of the number of characters appearing in the word.
    """
    character_statistic = {}
    for c in word:
        if not c.isalpha():
            continue
        if c in character_statistic:
            character_statistic[c] += 1
        else:
            character_statistic[c] = 1
    return character_statistic
