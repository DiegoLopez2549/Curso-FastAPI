from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/rutas")
async def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name
    return full_name

@app.get("/rutas2")
async def get_name_whith_age(name: str, height: float):
    name_whith_age = name + " tiene " + str(height) 
    return name_whith_age

@app.get("/rutas3")
async def process_item(items: list[str]):
    for item in items:
        print (item.)