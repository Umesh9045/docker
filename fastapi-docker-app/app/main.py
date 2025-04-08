from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NameRequest(BaseModel):
    name: str

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/hello")
def say_hello(request: NameRequest):
    return {"message": f"Hello {request.name}"}
