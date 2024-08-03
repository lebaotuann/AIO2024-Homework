import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer

from basic_probability import compute_mean, compute_median, compute_std, compute_correlation_coefficient
from constants import DATA_DIRECTORY_PATH
from tabular_data_analysis import correlation
from text_retrieval import tfidf_search, corr_search

# Question 1
print("==== Question 1 ================================")
X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
print("Mean: ", compute_mean(X))

print("==== Question 2 ================================")
X = [1, 5, 4, 4, 9, 13]
print("Median: ", compute_median(X))

print("==== Question 3 ================================")
X = [171, 176, 155, 167, 169, 182]
print("STD: ", compute_std(X))

print("==== Question 4 ================================")
X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print("Correlation: ", compute_correlation_coefficient(X, Y))

advertising_path = DATA_DIRECTORY_PATH + "/data/module2_week4_advertising.csv"
data = pd.read_csv(advertising_path)

print("==== Question 5 ================================")
x = data["TV"]
y = data["Radio"]
corr_xy = correlation(x, y)
print(f"Correlation between TV and Sales: {round(corr_xy, 2)}")

print("==== Question 6 ================================")
features = ["TV", "Radio", "Newspaper"]
for feature_1 in features:
    for feature_2 in features:
        correlation_value = correlation(data[feature_1], data[feature_2])
        print(f"Correlation between {feature_1} and {feature_2}: {round(correlation_value, 2)}")

print("==== Question 7 ================================")
x = data["Radio"]
y = data["Newspaper"]
result = np.corrcoef(x, y)
print(result)

print("==== Question 8 ================================")
correlation_matrix = data.corr()
print(correlation_matrix)

print("==== Question 9 ================================")
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", linewidth=.5)
plt.title('Correlation Matrix')
plt.show()

vi_text_retrieval_path = DATA_DIRECTORY_PATH + "/data/module2_week4_vi_text_retrieval.csv"
vi_data_df = pd.read_csv(vi_text_retrieval_path)

print("==== Question 10 ================================")
context = vi_data_df["text"]
context = [doc.lower() for doc in context]
tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)
element = context_embedded.toarray()[7][0]
print(round(element, 2))

print("==== Question 11 ================================")
question = vi_data_df.iloc[0]["question"]
results = tfidf_search(question, tfidf_vectorizer, context_embedded, top_d=5)
print(round(results[0]["cosine_score"], 2))

print("==== Question 12 ================================")
question = vi_data_df.iloc[0]["question"]
results = corr_search(question, tfidf_vectorizer, context_embedded, top_d=5)
print(round(results[1]["corr_score"], 2))

answers = """
Question 1: A
Question 2: B
Question 3: C
Question 4: D
Question 5: B
Question 6: D
Question 7: C
Question 8: D
Question 9: B
Question 10: B
Question 11: D
Question 12: B
"""
print(answers)
