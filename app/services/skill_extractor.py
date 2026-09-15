SKILL_LIST = {
    "python",
    "java",
    "c++",
    "c#",
    "sql",
    "fastapi",
    "flask",
    "django",
    "machine learning",
    "deep learning",
    "nlp",
    "natural language processing",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "pandas",
    "numpy",
    "aws",
    "azure",
    "gcp",
    "docker",
    "kubernetes",
    "git",
    "github",
    "rest api",
    "mongodb",
    "mysql",
    "postgresql",
    "html",
    "css",
    "javascript",
    "react",
}


def extract_skills(text: str) -> set:
    text = text.lower()

    found_skills = set()

    for skill in SKILL_LIST:
        if skill in text:
            found_skills.add(skill)

    return found_skills


def find_skill_gaps(resume_text: str, job_description: str) -> tuple:
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = resume_skills.intersection(job_skills)
    missing_skills = job_skills.difference(resume_skills)

    return matched_skills, missing_skills

resume = """
Python developer with experience in FastAPI and SQL.
"""

job_description = """
Looking for a Python developer with FastAPI, SQL,
AWS and Docker experience.
"""

matched, missing = find_skill_gaps(
    resume,
    job_description
)

print("Matched skills:", matched)
print("Missing skills:", missing)