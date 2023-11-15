from fastapi import FastAPI, Body
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

#Metodo POST
# Creamos una clase BaseModel para definir el formato de los datos que recibimos
class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str

@app.post("/movies", tags=['Movies'])
def create_movie(movie: Movie = Body(...)):
    movies.append(movie)
    return movie


# Modificar una pelicula por su ID
@app.put("/movies/{id}", tags=['Movies'])
def update_movie(id: int, movie: Movie = Body(...)):
    for m in movies:
        if m["id"] == id:
            m.update(movie)
            return m
    return {"Error": "Pelicula no encontrada"}

# Eliminar una pelicula por su ID
@app.delete("/movies/{id}", tags=['Movies'])
def delete_movie(id: int):
    for m in movies:
        if m["id"] == id:
            movies.remove(m)
            return {"message": "Pelicula eliminada correctamente"}
    return {"Error": "Pelicula no encontrada"}
