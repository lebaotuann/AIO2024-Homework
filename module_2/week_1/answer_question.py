# Basic NUMPY
import numpy as np
import matplotlib.image as mpimg
import pandas as pd
from constants import DATA_DIRECTORY_PATH

# region Basic Numpy

# Question 1
print("==== Question 1 ================================")
arr0 = np.arange(0, 10, 1)
print(arr0)

# Question 2
print("==== Question 2 ================================")
arr1 = np.ones((3, 3)) > 0
print("a: ", arr1)
arr2 = np.ones((3, 3), dtype=bool)
print("b: ", arr2)
arr3 = np.full((3, 3), fill_value=True, dtype=bool)
print("c", arr3)


# Question 3
print("==== Question 3 ================================")
arr5 = np.arange(0, 10)
print(arr5[arr5 % 2 == 1])

# Question 4
print("==== Question 4 ================================")
arr6 = np.arange(0, 10)
arr6[arr6 % 2 == 1] = -1
print(arr6)

# Question 5
print("==== Question 5 ================================")
arr7 = np.arange(10)
arr7_2d = arr7.reshape(2, -1)
print(arr7_2d)

# Question 6
print("==== Question 6 ================================")
arr8 = np.arange(10).reshape(2, -1)
arr9 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr8, arr9], axis=0)
print(c)

# Question 7
print("==== Question 7 ================================")
arr10 = np.arange(10).reshape(2, -1)
arr11 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr10, arr11], axis=1)
print(c)

# Question 8
print("==== Question 8 ================================")
arr12 = np.array([1, 2, 3])
print(np.repeat(arr12, 3))
print(np.tile(arr12, 3))

# Question 9
print("==== Question 9 ================================")
arr13 = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.where((arr13 >= 5) & (arr13 <= 10))
print(arr13[index])

# Question 10
print("==== Question 10 ================================")


def maxx(x, y):
    if x >= y:
        return x
    else:
        return y


arr_a = np.array([5, 7, 9, 8, 6, 4, 5])
arr_b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(arr_a, arr_b))

# Question 11
print("==== Question 11 ================================")
arr_a = np.array([5, 7, 9, 8, 6, 4, 5])
arr_b = np.array([6, 3, 4, 8, 9, 7, 1])
print(np.where(arr_a < arr_b, arr_b, arr_a))

# endregion Basic Numpy

# region Image with Numpy

img_path = DATA_DIRECTORY_PATH + "/data/module2_week1_dog.jpeg"
img = mpimg.imread(img_path)


# Question 12
print("==== Question 12 ================================")
gray_img_01 = (np.max(img, axis=-1) + np.min(img, axis=-1)) / 2
print(gray_img_01[0, 0])

# Question 13
print("==== Question 13 ================================")
gray_img_02 = np.average(img, axis=-1)
print(gray_img_02[0, 0])

# Question 14
print("==== Question 14 ================================")
gray_img_03 = np.dot(img, [0.21, 0.72, 0.07])
print(gray_img_03[0, 0])

# endregion Image with Numpy

# region Data analysis with Numpy
advertising_path = DATA_DIRECTORY_PATH + "/data/module2_week1_advertising.csv"
df = pd.read_csv(advertising_path)
data = df.to_numpy()

# Question 15
print("==== Question 15 ================================")
max_sale = np.max(data[:, 3])
index = np.where(data[:, 3] == np.max(data[:, 3]))
print(f"Max: {max_sale} - Index: {index[0][0]}")

# Question 16
print("==== Question 16 ================================")
average_tv1 = np.average(data[:, 0])
average_tv2 = np.mean(data, axis=0)[0]
print(average_tv1, average_tv2)

# Question 17
print("==== Question 17 ================================")
result = np.where(data[:, 3] >= 20)
print(len(result[0]))

# Question 18
print("==== Question 18 ================================")
filtered_data = data[data[:, 3] >= 15]
average_col1 = np.mean(filtered_data[:, 1])
print(average_col1)

# Question 19
print("==== Question 19 ================================")
average_newspaper = np.average(data, axis=0)[2]
filtered_data = data[data[:, 2] > average_newspaper]
print(np.sum(filtered_data, axis=0)[3])

# Question 20
print("==== Question 20 ================================")
average_sales = np.mean(data[:, 3])
scores = np.empty(0)
for i in range(len(data)):
    if data[i, 3] > average_sales:
        value = "Good"
    elif data[i, 3] < average_sales:
        value = "Bad"
    else:
        value = "Average"
    scores = np.append(scores, value)
print(scores[7:10])

# Question 21
print("==== Question 21 ================================")
average_sales = np.mean(data[:, 3])
closest_values = np.empty_like(data[:, 3], dtype=float)

for i in range(len(data)):
    differences = np.abs(data[i, 3] - average_sales)
    closest_values[i] = differences

index = np.where(closest_values == np.min(closest_values))
closest_average_sales = data[index][0][3]

scores = np.empty(0)
for i in range(len(data)):
    if data[i, 3] > closest_average_sales:
        value = "Good"
    elif data[i, 3] < closest_average_sales:
        value = "Bad"
    else:
        value = "Average"
    scores = np.append(scores, value)
print(scores[7:10])
# endregion Data analysis with Numpy


answers = """
Question 1: A
Question 2: D
Question 3: A
Question 4: B
Question 5: B
Question 6: A
Question 7: C
Question 8: A
Question 9: C
Question 10: D
Question 11: A
Question 12: A
Question 13: A
Question 14: C
Question 15: C
Question 16: B
Question 17: A
Question 18: B
Question 19: C
Question 20: C
Question 21: C
"""
print(answers)
