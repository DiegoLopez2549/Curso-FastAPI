from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/rutas")
async def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name
    return full_name

print(get_full_name("Diego", "Lopez"))

@app.get("/rutas2")
async def get_name_whith_age(name: str, age: int):
    name_whith_age = name + " tiene " + str(age)
    return name_whith_age