from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# ✅ Load student marks from JSON file
with open("q-vercel-python.json", "r") as file:
    student_marks = {student["name"]: student["marks"] for student in json.load(file)}

@app.get("/api")
def get_marks(name: list[str] = Query(default=[])):
    if isinstance(name, str):  # Ensure name is always a list
        name = [name]
    return {"marks": [student_marks.get(n, 0) for n in name]}

@app.get("/")
def home():
    return {"message": "Hello, FastAPI on Vercel!"}
