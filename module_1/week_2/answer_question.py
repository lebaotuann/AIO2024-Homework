# from data import DATA_DIRECTORY_PATH
# from max_kernel import max_kernel
# from count_character import character_count
# from count_word import count_word
# from levenshtein_distance import levenshtein_distance
# from multiple_choice_section import (
#     check_the_number,
#     build_list_by_max_and_min,
#     extend_list,
#     min_list,
#     max_list,
#     is_number_in_integer_list,
#     average,
#     list_numbers_divisible_by_3,
#     factorial,
#     reverse_string,
#     check_numbers,
#     remove_duplicates,
# )
#
# # Section II
# # Q1
# assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
# assert max_kernel([3, 4, 5], 3) == [5]
# assert max_kernel([3, 4], 3) == [4]
# assert max_kernel([3], 3) == [3]
# assert max_kernel([3, 4, 5, 1, -44, 5, 10, 12, 33, 1], 3) == [
#     5,
#     5,
#     5,
#     5,
#     10,
#     12,
#     33,
#     33,
# ]
# num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
# k = 3
# print(f"Question 1: {max_kernel(num_list, k)}")
#
# # Q2
# assert character_count("Baby") == {"B": 1, "a": 1, "b": 1, "y": 1}
# assert character_count("smiles") == {"s": 2, "m": 1, "i": 1, "l": 1, "e": 1}
# print(f"Question 2: {character_count('smiles')}")
#
# # Q3
# file_path = DATA_DIRECTORY_PATH + "/module1_week1_P1_data.txt"
# result = count_word(file_path)
# assert result["who"] == 3
# print(f"Question 3: {result['man']}")
#
# # Q4
# assert levenshtein_distance("hi", "hello") == 4.0
# print(f"Question 4: {levenshtein_distance('hola', 'hello')}")
#
#
# # Q5
# assert check_the_number(n=7) == "False"
# print(f"Question 5: {check_the_number(n=2)}")
#
# # Q6
# assert build_list_by_max_and_min(data=[5, 2, 5, 0, 1], max_number=1, min_number=0) == [
#     1,
#     1,
#     1,
#     0,
#     1,
# ]
# assert build_list_by_max_and_min(data=[5, 2, 3, 0, 1], max_number=3, min_number=1) == [
#     3,
#     2,
#     3,
#     1,
#     1,
# ]
# print(
#     f"Question 6: {build_list_by_max_and_min(data=[10, 2, 5, 0, 1], max_number=2, min_number=1)}"
# )
#
# # Q7
#
# assert extend_list(["a", 2, 5], extend_list([1, 1], [0, 0])) == ["a", 2, 5, 1, 1, 0, 0]
# print(f"Question 7: {extend_list([1, 2], extend_list([3, 4], [0, 0]))}")
#
# # Q8
# assert min_list([1, 22, 93, -100]) == -100
# print(f"Question 8: {min_list([1, 2, 3, -1])}")
#
#
# # Q9
# assert max_list([1001, 9, 100, 0]) == 1001
# print(f"Question 9: {max_list([1, 9, 9, 0])}")
#
#
# # Q10
# assert is_number_in_integer_list([1, 3, 9, 4], -1) is False
# print(f"Question 10: {is_number_in_integer_list([1, 2, 3, 4], 2)}")
#
#
# # Q11
# assert average([4, 6, 8]) == 6
# print(f"Question 11: {average([0, 1, 2])}")
#
#
# # Q12
# assert list_numbers_divisible_by_3([3, 9, 4, 5]) == [3, 9]
# print(f"Question 12: {list_numbers_divisible_by_3([1, 2, 3, 5, 6])}")
#
# # Q13
# assert factorial(8) == 40320
# print(f"Question 13: {factorial(4)}")
#
#
# # Q14
# assert reverse_string("I can do it") == "ti od nac I"
# print(f"Question 14: {reverse_string('apricot')}")
#
#
# # Q15
# assert check_numbers([10, 0, -10, -1]) == ["T", "N", "N", "N"]
# print(f"Question 15: {check_numbers([2, 3, 4, -1])}")
#
# # Q16
# assert remove_duplicates([10, 10, 9, 7, 7]) == [10, 9, 7]
# print(f"Question 16: {remove_duplicates([9, 9, 8, 1, 1])}")
