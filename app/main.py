"""Minimal FastAPI app used for Git practice."""
from fastapi import FastAPI

from app.calculator import add

app = FastAPI(title="Git Practice Lab")


@app.get("/")
def root():
    return {"message": "hello git"}


@app.get("/add")
def add_endpoint(a: float, b: float):
    return {"result": add(a, b)}
