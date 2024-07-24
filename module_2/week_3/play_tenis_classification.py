import numpy as np


def create_train_data():
    """Create data."""
    data = [
        ["Sunny", "Hot", "High", "Weak", "no"],
        ["Sunny", "Hot", "High", "Strong", "no"],
        ["Overcast", "Hot", "High", "Weak", "yes"],
        ["Rain", "Mild", "High", "Weak", "yes"],
        ["Rain", "Cool", "Normal", "Weak", "yes"],
        ["Rain", "Cool", "Normal", "Strong", "no"],
        ["Overcast", "Cool", "Normal", "Strong", "yes"],
        ["Overcast", "Mild", "High", "Weak", "no"],
        ["Sunny", "Cool", "Normal", "Weak", "yes"],
        ["Rain", "Mild", "Normal", "Weak", "yes"],
    ]
    return np.array(data)


def compute_prior_probability(train_data):
    y_unique = ["no", "yes"]
    prior_probability = np.zeros(len(y_unique))
    for idx, class_label in enumerate(y_unique):
        prior_probability[idx] = np.sum(train_data[:, -1] == class_label)
    prior_probability = prior_probability / len(train_data)

    return prior_probability


def compute_conditional_probability(train_data):
    y_unique = ["no", "yes"]
    conditional_probability = []
    list_x_name = []
    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

        x_conditional_probability = []
        for x in x_unique:
            probabilities = []
            for y in y_unique:
                count_x_and_y = np.sum(
                    (train_data[:, i] == x) & (train_data[:, -1] == y)
                )
                count_y = np.sum(train_data[:, -1] == y)
                if count_y == 0:
                    probabilities.append(0)
                else:
                    probabilities.append(count_x_and_y / count_y)
            x_conditional_probability.append(probabilities)
        conditional_probability.append(x_conditional_probability)
    return conditional_probability, list_x_name


def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]


def train_naive_bayes(train_data):
    prior_probability = compute_prior_probability(train_data)
    conditional_probability, list_x_name = compute_conditional_probability(train_data)
    return prior_probability, conditional_probability, list_x_name


def prediction_play_tennis(x, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(x[0], list_x_name[0])
    x2 = get_index_from_value(x[1], list_x_name[1])
    x3 = get_index_from_value(x[2], list_x_name[2])
    x4 = get_index_from_value(x[3], list_x_name[3])

    p0 = prior_probability[0]  # no
    p1 = prior_probability[1]  # yes

    # x1
    p0 *= conditional_probability[0][x1][0]
    p1 *= conditional_probability[0][x1][1]
    # x2
    p0 *= conditional_probability[1][x2][0]
    p1 *= conditional_probability[1][x2][1]
    # x3
    p0 *= conditional_probability[2][x3][0]
    p1 *= conditional_probability[2][x3][1]
    # x4
    p0 *= conditional_probability[3][x4][0]
    p1 *= conditional_probability[3][x4][1]

    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred
