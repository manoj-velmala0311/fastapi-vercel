from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Correctly locate the JSON file
json_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")

if os.path.exists(json_path):
    with open(json_path, "r") as file:
        student_marks = json.load(file)
else:
    student_marks = {}  # Default to empty dictionary if file is missing

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    marks = [student_marks.get(n, 0) for n in name]
    return {"marks": marks}

@app.get("/")
def home():
    return {"message": "Hello, FastAPI on Vercel!"}
