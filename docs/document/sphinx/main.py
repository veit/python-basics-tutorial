from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/cusy.tasks/{task_id}")
def read_task(task_id: int, q: Optional[str] = None):
    return {"task_id": task_id, "q": q}


@app.put("/cusy.tasks/{task_id}")
def update_task(task_id: int, task: Task):
    return {"task_name": task.name, "task_id": task_id}
