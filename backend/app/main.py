# app/main.py
from fastapi import FastAPI
from app.api import bug, auth, user

app = FastAPI(
    title="BugWise AI - Smart Bug Triage System",
    version="1.0.0"
)

# Include routers
app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/users")
app.include_router(bug.router, prefix="/bugs")
from app.routers import bug_routes
app.include_router(bug_routes.router)

@app.get("/")
def read_root():
    return {"message": "BugWise AI is running 🚀"}

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
