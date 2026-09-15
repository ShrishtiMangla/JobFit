from fastapi import FastAPI, UploadFile, File
from app.services.pdf_parser import extract_text_from_pdf
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
    try:
        return {
            "message": "Job description received successfully",
            "job_description": request.job_description
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to process job description"
        )