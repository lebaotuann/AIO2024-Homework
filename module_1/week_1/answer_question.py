#
# from evaluation import calculate_f1_score
# from activation_function import is_number, calc_sigmoid, calc_elu, calc_activation_function
# from loss_function import calc_ae, calc_se
# from approximation import approx_cos, approx_sin, approx_sinh, approx_cosh
#
# # Section II
# # Q1
# assert round(calculate_f1_score(tp=2, fp=3, fn=5), 2) == 0.33
# print(f"Question 1: {round(calculate_f1_score(tp=2, fp=4, fn=5), 2)}")
#
# # Q2
# assert is_number(3) == 1.0
# assert is_number('-2a') == 0.0
# print(f"Question 2: {is_number(1)}, {is_number('n')}")
#
# # Q3
# print("Question 3: ReLU")
#
# # Q4
# assert round(calc_sigmoid(3), 2) == 0.95
# print(f"Question 4: {round(calc_sigmoid(2), 2)}")
#
# # Q5
# assert round(calc_elu(1)) == 1
# print(f"Question 5: {round(calc_elu(-1), 2)}")
#
# # Q6
# assert calc_activation_function(x=1, activation_name='relu') == 1
# print(f"Question 6: {round(calc_activation_function(x=3, activation_name='sigmoid'), 2)}")
#
# # Q7
# assert calc_ae(y=1, y_hat=6) == 5
# print(f"Question 7: {calc_ae(y=2, y_hat=9)}")
#
# # Q8
# assert calc_se(y=4, y_hat=2) == 4
# print(f"Question 8: {calc_se(y=2, y_hat=1)}")
#
# # Q9
# assert round(approx_cos(x=1, n=10), 2) == 0.54
# print(f"Question 9: {round(approx_cos(x=3.14, n=10), 2)}")
#
# # Q10
# assert round(approx_sin(x=1, n=10), 4) == 0.8415
# print(f"Question 10: {round(approx_sin(x=3.14, n=10), 4)}")
#
# # Q11
# assert round(approx_sinh(x=1, n=10), 2) == 1.18
# print(f"Question 11: {round(approx_sinh(x=3.14, n=10), 2)}")
#
# # Q12
# assert round(approx_cosh(x=1, n=10), 2) == 1.54
# print(f"Question 12: {round(approx_cosh(x=3.14, n=10), 2)}")
#
# # Q13
# print("Question 13: A")
