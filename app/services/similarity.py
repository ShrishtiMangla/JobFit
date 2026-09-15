from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_embedding, job_description_embedding):
    similarity = cosine_similarity(
        [resume_embedding],
        [job_description_embedding]
    )

    return similarity[0][0]
