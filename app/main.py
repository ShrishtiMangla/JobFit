from fastapi import FastAPI

app = FastAPI(title = "jobfit")

@app.get("/")
def home():
    return ( "Welcome to JobFit API!")