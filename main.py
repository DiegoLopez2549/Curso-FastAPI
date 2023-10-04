from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="App con FastAPI", version="0.0.1", description="Una API para aprender"
)
movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
]


@app.get("/", tags=["home"], response_class=HTMLResponse)
def message():
    return """
        <html
            <head>
                <title>Web App con FastAPI</title>
                </head>
                <body>
                    <h1>¡Hola a todos!</h1>
                    <p>Este es un mensaje de ejemplo</p>
                </body>
        </html>
"""


@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
    try:
        return [movie for movie in movies if movie["id"] == id][0]
    except IndentationError:
        return {"Error": "No hay pelicalas para mostrar"}


@app.get("/items/{item_id}/sub/{item_id2}")
def read_item(item_id: int, item_id2: str):
    return {"item_id": item_id, "item_id2": item_id2}


# Porque las operaciones de path son evaluadas en orden,
# tienes que asegurarte de que el path para /users/me
# sea declarado antes que el path para /users/{user_id}:
# De otra manera el path para /users/{user_id}
# coincidiría también con /users/me "pensando"
# que está recibiendo el parámetro user_id con el valor "me".


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
