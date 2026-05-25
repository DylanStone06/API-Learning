from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
app = FastAPI()

tasks = []

class Task(BaseModel):
    title: str
    done: bool = False

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.get("/tasks/{id}")
def get_task_ID(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    return {"error": "task not found"}

@app.post("/tasks")
def create_task(task: Task):
    new_task = {"id": len(tasks) + 1, "title": task.title, "done": task.done}
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{id}")
def complete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            task["done"] = True
            return task
    return {"error": "task not found"}

@app.delete("/tasks/{id}")
def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return task
    return {"error": "task not found"}

@app.get("/test-db")
def test_db():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": "connected"}