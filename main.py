from fastapi import FastAPI
from .schema import GetReport
app = FastAPI()

@app.get("/")
def hello():
    return {"Hello":"World"}

@app.get("/{teacher_name}")
def getreports(teachers_name: str, report : GetReport):
    return {"teachers_name": teachers_name, "report": report}