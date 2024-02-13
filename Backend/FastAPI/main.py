from fastapi import FastAPI, Body
from typing import List, Tuple, Set, Dict
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/rutas")
async def url():
    return {"url": "http://127.0.0.1:8000/rutas"}