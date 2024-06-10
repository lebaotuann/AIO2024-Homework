# Section 1, Q3
def count_word(file_path: str):
    """Count the number of times words appear in sentences that are read in the text file.

    Args:
        file_path (str): The data file path.

    Returns:
        dict: Dictionary of the number of words appearing in the sentences.
    """
    with open(file_path, "r") as f:
        # strip() -> remove the newline character (\n)
        resources = [line.strip() for line in f]
    counter = {}
    for line in resources:
        list_words = line.lower().split(" ")
        for word in list_words:
            if not word:
                continue
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    return counter
