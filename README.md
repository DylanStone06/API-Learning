# Backend Fundamentals

Learning REST API development with Python and FastAPI.

## Progress

### Week 1 — API Foundations
- Understood what a REST API is and how HTTP requests work
- Built first endpoint returning JSON
- Implemented full CRUD API for a task list
  - GET /tasks — retrieve all tasks
  - POST /tasks — create a task with request body validation
  - PUT /tasks/{id} — mark a task as complete
  - DELETE /tasks/{id} — remove a task
- Learned Pydantic models for request body validation
- Understood HTTP methods, status codes, and JSON formatting rules

## Tech Stack
- Python 3.11
- FastAPI
- Uvicorn
- Pydantic

## What's Next
- Proper status codes (201 for resource creation)
- PostgreSQL database for persistent storage
- Authentication with JWT

## Known Limitations
- Data is stored in memory — restarting the server wipes all tasks
- No database connected yet
