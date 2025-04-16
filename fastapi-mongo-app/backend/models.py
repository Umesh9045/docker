from pydantic import BaseModel

class Task(BaseModel):
    name: str
    priority: int
