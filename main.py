from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

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
        "title": "Thor",
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

# Parametro de ruta
@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
    try:
        movie = next((m for m in movies if m["id"] == id), None)
        if movie is not None:
            return movie
        else:
            return {"Error": "No hay películas para mostrar"}
    except Exception as e:
        return {"Error": f"Error interno del servidor: {str(e)}"}


# Parametro de consulta con subrutas
@app.get("/items/{item_id}/sub/{item_id2}")
def read_item(item_id: int, item_id2: str):
    return {"item_id": item_id, "item_id2": item_id2}

# Parametro de query
# Si el parametro no está especificado en la ruta, fastapi tomara este como parametro query
@app.get("/movies/", tags=["movies"])
def get_movies_by_category(category: str, year: int):
    return category

@app.post("/movies/", tags=["movies"])
def create_movie(movie: dict):
    return movie

class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str