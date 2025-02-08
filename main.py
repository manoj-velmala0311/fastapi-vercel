from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
  
app = FastAPI() 
  
# Enable CORS to allow requests from any origin 
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]) 
  
# Imaginary student marks database
student_marks = {
    "Alice": 85, 
    "Bob": 78, 
    "Charlie": 92, 
    "David": 65, 
    "Eve": 88,
    "X": 10, 
    "Y": 20  # Example values
}

  
@app.get("/api") 
def get_marks(name: list[str] = []): 
    return {"marks": [student_marks.get(n, 0) for n in name]} 
  
@app.get("/") 
def home(): 
    return {"message": "Hello, FastAPI on Vercel!"}
