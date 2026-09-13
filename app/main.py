from fastapi import FastAPI, UploadFile, File
from app.services.pdf_parser import extract_text_from_pdf


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