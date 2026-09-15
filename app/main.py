from fastapi import FastAPI, UploadFile, File , Form
from app.services.pdf_parser import extract_text_from_pdf
from app.services.matching import calculate_match_score
from app.models.job_description import JobDescriptionRequest
from app.services.text_preprocessor import preprocess_text


app = FastAPI(title="JobFit")


@app.get("/")
def home():
    return {"message": "Welcome to JobFit API!"}



@app.post("/extract-resume")
async def extract_resume(file: UploadFile = File(...)):
    pdf_file = await file.read()

    extracted_text = extract_text_from_pdf(pdf_file)

    return {
        "filename": file.filename,
        "text": extracted_text
    }


@app.post("/job-description")
def receive_job_description(request: JobDescriptionRequest):
    
    return {
        "message": "Job description received successfully",
        "job_description": request.job_description
    }

    

@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    # Read uploaded PDF
    pdf_file = await resume.read()

    # Extract text from PDF
    resume_text = extract_text_from_pdf(pdf_file)

    # Calculate similarity score
    similarity_score = calculate_match_score(
        resume_text,
        job_description
    )

    return {
        "filename": resume.filename,
        "match_score": round(similarity_score * 100, 2)
    }