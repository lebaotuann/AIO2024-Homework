import numpy as np
from play_tenis_classification import (
    create_train_data,
    compute_prior_probability,
    compute_conditional_probability,
    get_index_from_value,
    train_naive_bayes,
    prediction_play_tennis,
)

print("==== Question 1 ================================")
print('a) P("Play Tennis" = "Yes") = 6/10, P("Play Tennis" = "No") = 4/10')

print("==== Question 2 ================================")
print('b) P("Play Tennis" = "Yes"|X) ∝ 0.0028')

print("==== Question 3 ================================")
print('c) P("Play Tennis" = "No" | X) ∝ 0.0188')

print("==== Question 4 ================================")
print('b) "Play Tennis" = "No"')

print("==== Question 5 ================================")
print(
    '(A) P("Class" = "On Time") = 14/20, P("Class" = "Late") = 2/20, P("Class" = "Very Late") = 3/20, P("Class" = "Cancelled") = 1/20'
)

print("==== Question 6 ================================")
print('(C) P("Class" = "On Time" | X) ∝ 0.0026')

print("==== Question 7 ================================")
print('(D) P("Class" = "Late" | X) ∝ 0.0000')

print("==== Question 8 ================================")
print('(A) P("Class" = "Very Late" | X) ∝ 0.0222')

print("==== Question 9 ================================")
print('(D) P("Class" = "Cancelled" | X) ∝ 0.0000')

print("==== Question 10 ================================")
print('(C) "Very Late"')

print("==== Question 11 ================================")
print("a) mean = 1.566 và variance = 0.128")

print("==== Question 12 ================================")
print("b) mean = 3.733 và variance = 0.172")

print("==== Question 13 ================================")
print('a) P("Class" = "0" | X) = 1.09 ∗ 10^6 và P("Class" = "1" | X) = 0.3486')


train_data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(train_data)

print("==== Question 14 ================================")
print("P( play tennis = No)", prior_probability[0])
print("P( play tennis = Yes)", prior_probability[1])

print("==== Question 15 ================================")
print("x1 = ", list_x_name[0])
print("x2 = ", list_x_name[1])
print("x3 = ", list_x_name[2])
print("x4 = ", list_x_name[3])

print("==== Question 16 ================================")
outlook = list_x_name[0]
i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)
print(i1, i2, i3)

print("==== Question 17 ================================")
x1 = get_index_from_value("Sunny", list_x_name[0])
print(
    "P('Outlook'='Sunny'|'Play Tennis'='Yes') = ",
    np.round(conditional_probability[0][x1][1], 2),
)

print("==== Question 18 ================================")
x1 = get_index_from_value("Sunny", list_x_name[0])
print(
    "P('Outlook'='Sunny'|'Play Tennis'='No') = ",
    np.round(conditional_probability[0][x1][0], 2),
)

print("==== Question 19 ================================")
X = ["Sunny", "Cool", "High", "Strong"]
pred = prediction_play_tennis(
    X, list_x_name, prior_probability, conditional_probability
)
if pred:
    print("Ad should go!")
else:
    print("Ad should not go!")


answers = """
Question 1: A
Question 2: B
Question 3: C
Question 4: B
Question 5: A
Question 6: C
Question 7: D
Question 8: A
Question 9: D
Question 10: C
Question 11: A
Question 12: B
Question 13: A
Question 14: A
Question 15: B
Question 16: C
Question 17: D
Question 18: A
Question 19: A
"""
print(answers)
