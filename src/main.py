"""Simple FastAPI application."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    """Return welcome message."""
    return {"message": "Hello FastAPI"}


@app.get("/add")
def add(a: int, b: int):
    """Return addition of two numbers."""
    return {"result": a + b}