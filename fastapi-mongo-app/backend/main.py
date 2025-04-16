from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Task
import crud

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tasks")
def read_tasks():
    return crud.get_all_tasks()

@app.post("/tasks")
def add_task(task: Task):
    return crud.create_task(task.dict())

@app.put("/tasks/{name}")
def update_task(name: str, task: Task):
    result = crud.update_task(name, task.dict())
    if result["msg"] == "Task not found":
        raise HTTPException(status_code=404, detail=result["msg"])
    return result

@app.delete("/tasks/{name}")
def delete_task(name: str):
    result = crud.delete_task(name)
    if result["msg"] == "Task not found":
        raise HTTPException(status_code=404, detail=result["msg"])
    return result

@app.get("/summary")
def task_summary():
    return crud.get_priority_summary()
