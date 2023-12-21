from fastapi import FastAPI
from typing import List, Tuple, Set, Dict

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
        print (item)

#Sets y tuplas
@app.get("/rutas4")
async def process_items(items_t: Tuple[int, int, str], Items_s: Set[bytes]):
    return items_t, Items_s

#Diccionarios en FastAPI
@app.get("/rutas5")
async def process_items(items: dict[str, float]):
    for item_name, item_price in items.items():
        print(item_name, item_price)