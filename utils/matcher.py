from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(resume_text, job_text):
    """
    Calculate similarity score between resume and job description
    """
    documents = [resume_text, job_text]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return round(similarity[0][0] * 100, 2)


if __name__ == "__main__":
    resume = "I have experience in Python, Flask, SQL and Machine Learning."
    job = "Looking for a Python developer with Flask and SQL experience."

    print(calculate_match_score(resume, job))
