from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionLocal, engine
from .models import Base  # Make sure this import is correct
from . import schemas, crud
from .routers import items, users

# This should now work correctly
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Project",
    description="A sample FastAPI project with users and items",
    version="0.1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Project"}