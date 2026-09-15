from app.services.text_preprocessor import preprocess_text
from app.services.embeddings import generate_embedding
from app.services.similarity import calculate_similarity


def calculate_match_score(resume_text: str, job_description: str) -> float:
    # Step 1: Preprocess both texts
    cleaned_resume = preprocess_text(resume_text)
    cleaned_job_description = preprocess_text(job_description)

    # Step 2: Generate embeddings
    resume_embedding = generate_embedding(cleaned_resume)
    job_description_embedding = generate_embedding(cleaned_job_description)

    # Step 3: Calculate cosine similarity
    similarity_score = calculate_similarity(
        resume_embedding,
        job_description_embedding
    )

    return float(similarity_score)
