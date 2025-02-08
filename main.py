from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Student marks database
student_marks = {
    "Alice": 85, "Bob": 78, "Charlie": 92, "David": 65, "Eve": 88,
    "X": 10, "Y": 20  # Example values
}

@app.get("/api")
def get_marks(name: list[str] = []):
    print(f"Received names: {name}")  # Debugging print
    result = [student_marks.get(n, 0) for n in name]
    print(f"Returning marks: {result}")  # Debugging print
    return {"marks": result}

@app.get("/")
def home():
    return {"message": "Hello, FastAPI on Vercel!"}
