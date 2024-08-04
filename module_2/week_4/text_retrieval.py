import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def tfidf_search(question, tfidf_vectorizer, context_embedded, top_d=5):
    """Perform a TF-IDF based search to find the most similar documents to a given query.

    This function takes a query, transforms it using the provided TF-IDF vectorizer,
    computes the cosine similarity scores between the query and a set of pre-embedded
    documents, and returns the top-k most similar documents based on these scores.
    Args:
        question (str): The search query string.
        tfidf_vectorizer (TfidfVectorizer): The fitted TF-IDF vectorizer.
        context_embedded (scipy.sparse.csr_matrix): The TF-IDF matrix of the pre-embedded documents.
        top_d (int, optional): The number of top documents to return. Default is 5.

    Returns:
        list: A list of dictionaries, each containing the ID and cosine score of the top-k most similar documents.
    """
    # lowercasing before encoding
    # encoding the query using the same TF-IDF vectorizer
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    # calculating cosine similarity scores
    cosine_scores = cosine_similarity(query_embedded, context_embedded).flatten()
    # Get top k cosine score and index its
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {"id": idx, "cosine_score": cosine_scores[idx]}
        results.append(doc_score)
    return results


def corr_search(question, tfidf_vectorizer, context_embedded, top_d=5):
    """Perform a TF-IDF based search to find the most correlated documents to a given query.

    This function takes a query, transforms it using the provided TF-IDF vectorizer,
    computes the correlation scores between the query and a set of pre-embedded
    documents, and returns the top-k most correlated documents based on these scores.

    Args:
        question (str): The search query string.
        tfidf_vectorizer (TfidfVectorizer): The fitted TF-IDF vectorizer.
        context_embedded (scipy.sparse.csr_matrix): The TF-IDF matrix of the pre-embedded documents.
        top_d (int, optional): The number of top documents to return. Default is 5.

    Returns:
        list: A list of dictionaries, each containing the ID and correlation score of the top-k most correlated documents.
    """
    # lowercasing before encoding
    # encoding the query using the same TF-IDF vectorizer
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    # Calculating correlation scores
    corr_scores = np.corrcoef(query_embedded.toarray()[0], context_embedded.toarray())
    corr_scores = corr_scores[0][1:]
    # Get top k cosine score and index its
    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc_score = {"id": idx, "corr_score": corr_scores[idx]}
        results.append(doc_score)
    return results
