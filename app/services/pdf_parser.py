import fitz

def extract_text_from_pdf(pdf_file) -> str:
    document = fitz.open(stream=pdf_file, filetype="pdf")

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text()

    document.close()

    return extracted_text.strip()

# Flow:
# 1. FastAPI receives the uploaded PDF as an UploadFile.
# 2. file.read() reads the uploaded file's binary data (bytes).
# 3. The uploaded data is temporarily held in memory/disk by UploadFile.
# 4. fitz.open() takes these PDF bytes and parses them into a PyMuPDF
#    Document object that understands the PDF structure and its pages.
# 5. Document object → iterate through pages → get_text() extracts text
# → combine page text → return the complete resume text